"""
Контур принятия решений для предиктивного обслуживания фрезерного станка.
Реализация 8 шагов архитектуры контура из лекций.
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from supervised.automl import AutoML


MODEL_DIR = Path('models/AutoML_AI4I_Multiclass')
CONFIG_PATH = Path('models/config.json')
LOG_PATH = Path('logs/decisions.jsonl')
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

LOG_RETENTION_HOURS = 24


CLASS_INFO = {
    'No_Failure': {
        'rus': 'Нет отказа',
        'auto_action': 'Продолжать работу. Параметры станка в норме',
        'review_action': 'Проверить станок: отказ не обнаружен, но уверенность модели невысокая',
        'manual_action': 'Проверить станок вручную: модель недостаточно уверена',
        'color': '#2ECC71',
    },
    'Heat_Dissipation_Failure': {
        'rus': 'Перегрев',
        'auto_action': 'Остановить станок, проверить теплоотвод',
        'review_action': 'Проверить систему охлаждения и теплоотвод',
        'manual_action': 'Вручную проверить возможный перегрев',
        'color': '#E74C3C',
    },
    'Power_Failure': {
        'rus': 'Отказ по мощности',
        'auto_action': 'Проверить режим мощности и нагрузку станка',
        'review_action': 'Проверить параметры мощности',
        'manual_action': 'Вручную проверить возможный отказ по мощности',
        'color': '#F39C12',
    },
    'Overstrain_Failure': {
        'rus': 'Перегрузка по моменту',
        'auto_action': 'Снизить нагрузку и проверить режим резания',
        'review_action': 'Проверить возможную перегрузку по моменту',
        'manual_action': 'Вручную проверить перегрузку по моменту',
        'color': '#9B59B6',
    },
    'Tool_Wear_Failure': {
        'rus': 'Износ инструмента',
        'auto_action': 'Проверить состояние инструмента',
        'review_action': 'Проверить возможный износ',
        'manual_action': 'Вручную проверить износ инструмента',
        'color': '#3498DB',
    },
    'Random_Failures': {
        'rus': 'Случайный отказ',
        'auto_action': 'Зафиксировать случайный отказ, осмотреть станок',
        'review_action': 'Проверить станок: возможен случайный отказ',
        'manual_action': 'Вручную осмотреть станок на случайный отказ',
        'color': '#95A5A6',
    },
}


FEATURE_INFO = {
    'Type': {
        'rus': 'Тип детали',
        'help': 'Категория детали: L, M или H.',
    },
    'Air_Temperature': {
        'rus': 'Температура воздуха, K',
        'help': 'Температура воздуха рядом со станком.',
    },
    'Process_Temperature': {
        'rus': 'Температура процесса, K',
        'help': 'Температура в зоне обработки.',
    },
    'Rotational_Speed': {
        'rus': 'Скорость вращения, об/мин',
        'help': 'Обороты шпинделя.',
    },
    'Torque': {
        'rus': 'Крутящий момент, Н·м',
        'help': 'Нагрузка на инструмент.',
    },
    'Tool_Wear': {
        'rus': 'Износ инструмента, мин',
        'help': 'Сколько минут работает инструмент.',
    },
}


def format_number(value):
    if abs(value) >= 100:
        return f'{value:.0f}'
    return f'{value:.2f}'


def generate_no_failure(rng):
    """Безопасные параметры, ни одно физическое правило отказа не сработает."""
    air = float(rng.uniform(297, 302))
    process = float(min(air + rng.uniform(11, 13), 313.5))

    return {
        'Type': str(rng.choice(['L', 'M', 'H'])),
        'Air_Temperature': air,
        'Process_Temperature': process,
        'Rotational_Speed': float(rng.uniform(1550, 1800)),
        'Torque': float(rng.uniform(28, 42)),
        'Tool_Wear': float(rng.uniform(20, 150)),
    }


def generate_heat_dissipation(rng):
    """Перегрев: разница температур < 10 K, обороты < 1500, тип L."""
    air = float(rng.uniform(300, 302))
    process = float(max(air + rng.uniform(3, 5), 306.0))

    return {
        'Type': 'L',
        'Air_Temperature': air,
        'Process_Temperature': process,
        'Rotational_Speed': float(rng.uniform(1200, 1300)),
        'Torque': float(rng.uniform(40, 55)),
        'Tool_Wear': float(rng.uniform(20, 100)),
    }


def generate_power_failure(rng):
    """Отказ по мощности: power = 0.10472 * RPM * Torque вне диапазона 4000–8500 Вт."""
    if rng.random() < 0.5:
        rpm = float(rng.uniform(1200, 1400))
        torque = float(rng.uniform(8, 18))
    else:
        rpm = float(rng.uniform(2600, 2880))
        torque = float(rng.uniform(45, 65))

    air = float(rng.uniform(297, 302))

    return {
        'Type': str(rng.choice(['L', 'M', 'H'])),
        'Air_Temperature': air,
        'Process_Temperature': float(air + rng.uniform(11, 13)),
        'Rotational_Speed': rpm,
        'Torque': torque,
        'Tool_Wear': float(rng.uniform(20, 150)),
    }


def generate_overstrain(rng):
    """Перегрузка: Torque * Tool_Wear > 10000 для типа L."""
    air = float(rng.uniform(297, 302))

    return {
        'Type': 'L',
        'Air_Temperature': air,
        'Process_Temperature': float(air + rng.uniform(11, 13)),
        'Rotational_Speed': float(rng.uniform(1550, 1700)),
        'Torque': float(rng.uniform(63, 70)),
        'Tool_Wear': float(rng.uniform(170, 185)),
    }


def generate_tool_wear(rng):
    """Износ: Tool_Wear в зоне 200–235 минут."""
    air = float(rng.uniform(297, 302))

    return {
        'Type': str(rng.choice(['M', 'H'])),
        'Air_Temperature': air,
        'Process_Temperature': float(air + rng.uniform(11, 13)),
        'Rotational_Speed': float(rng.uniform(1550, 1700)),
        'Torque': float(rng.uniform(35, 50)),
        'Tool_Wear': float(rng.uniform(200, 235)),
    }


CLASS_GENERATORS = {
    'Нет отказа': generate_no_failure,
    'Перегрев': generate_heat_dissipation,
    'Отказ по мощности': generate_power_failure,
    'Перегрузка по моменту': generate_overstrain,
    'Износ инструмента': generate_tool_wear,
}


CLASS_LABEL_TO_INTERNAL = {
    'Нет отказа': 'No_Failure',
    'Перегрев': 'Heat_Dissipation_Failure',
    'Отказ по мощности': 'Power_Failure',
    'Перегрузка по моменту': 'Overstrain_Failure',
    'Износ инструмента': 'Tool_Wear_Failure',
}


@st.cache_resource(show_spinner='Загрузка модели')
def load_model():
    return AutoML(results_path=str(MODEL_DIR))


@st.cache_data
def load_config():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def clear_last_result():
    if 'last_result' in st.session_state:
        del st.session_state.last_result


def set_machine_inputs(new_inputs, expected_class=None, clear_result=True):
    st.session_state.inputs = new_inputs.copy()

    for feature, value in new_inputs.items():
        st.session_state[f'in_{feature}'] = value

    if expected_class is not None:
        st.session_state.expected_class = expected_class

    if clear_result:
        clear_last_result()


def ensure_input_state(feature_columns):
    if 'expected_class' not in st.session_state:
        st.session_state.expected_class = 'Нет отказа'

    if 'inputs' not in st.session_state:
        rng = np.random.default_rng()
        initial_inputs = generate_no_failure(rng)
        set_machine_inputs(
            initial_inputs,
            expected_class='Нет отказа',
            clear_result=False,
        )
        return

    for feature in feature_columns:
        widget_key = f'in_{feature}'

        if feature in st.session_state.inputs and widget_key not in st.session_state:
            st.session_state[widget_key] = st.session_state.inputs[feature]


def sync_inputs_from_widgets(feature_columns):
    for feature in feature_columns:
        widget_key = f'in_{feature}'

        if widget_key in st.session_state:
            st.session_state.inputs[feature] = st.session_state[widget_key]


def step1_validate(inputs, config):
    """Шаг 1. Валидация по типу, диапазону, полноте."""
    errors = []

    for feature in config['feature_columns']:
        if feature not in inputs:
            errors.append(f'{feature}: отсутствует')
            continue

        value = inputs[feature]
        stats = config['feature_stats'][feature]

        if stats['dtype'] == 'numeric':
            if value is None or (isinstance(value, float) and np.isnan(value)):
                errors.append(f'{feature}: пропуск значения')
            elif value < stats['min']:
                errors.append(f'{feature}: ниже допустимого ({value:.2f} < {stats["min"]:.2f})')
            elif value > stats['max']:
                errors.append(f'{feature}: выше допустимого ({value:.2f} > {stats["max"]:.2f})')

        elif stats['dtype'] == 'categorical':
            if value not in stats['values']:
                errors.append(f'{feature}: значение {value} не в справочнике')

    return {
        'ok': len(errors) == 0,
        'errors': errors,
    }


def step2_early_rules(inputs):
    """Шаг 2. Ранние жёсткие правила до модели."""
    triggered = []

    if inputs.get('Tool_Wear', 0) >= 190:
        triggered.append({
            'name': 'critical_tool_wear',
            'message': f'Износ инструмента {inputs["Tool_Wear"]:.0f} мин в зоне риска — '
                       f'нужна проверка оператора',
        })

    if inputs.get('Torque', 0) < 3:
        triggered.append({
            'name': 'low_torque',
            'message': f'Крутящий момент {inputs["Torque"]:.2f} Н·м слишком низкий — '
                       f'нужна проверка датчика',
        })

    return triggered


def step4_predict(model, inputs, feature_columns, classes):
    """Шаг 4. Оценка модели."""
    x = pd.DataFrame([{c: inputs[c] for c in feature_columns}])
    proba_arr = model.predict_proba(x)[0]
    proba = dict(zip(classes, proba_arr.tolist()))
    pred = max(proba, key=proba.get)
    confidence = float(proba[pred])

    return pred, proba, confidence


def step5_apply_thresholds(confidence, t_low, t_high):
    """Шаг 5а. Пороги в зоны решений."""
    if confidence >= t_high:
        return 'auto_decision'

    if confidence >= t_low:
        return 'recommendation'

    return 'manual_review'


def step5_late_rules(prediction, probabilities, zone):
    """Шаг 5б. Поздние правила после модели."""
    triggered = []

    sorted_probs = sorted(probabilities.values(), reverse=True)
    top1 = sorted_probs[0]
    top2 = sorted_probs[1] if len(sorted_probs) > 1 else 0

    if top1 - top2 < 0.15:
        triggered.append({
            'name': 'close_probabilities',
            'message': f'Модель сомневается: разница между двумя главными вариантами '
                       f'только {top1 - top2:.1%}. Нужна проверка оператора',
        })
        return 'manual_review', triggered

    tool_wear_prob = probabilities.get('Tool_Wear_Failure', 0)

    if prediction != 'Tool_Wear_Failure' and tool_wear_prob > 0.05:
        triggered.append({
            'name': 'tool_wear_suspicion',
            'message': f'Есть риск износа инструмента: {tool_wear_prob:.1%}. '
                       f'Нужна проверка оператора',
        })
        return 'manual_review', triggered

    if prediction == 'No_Failure':
        failure_prob_sum = sum(
            p for c, p in probabilities.items() if c != 'No_Failure'
        )

        if failure_prob_sum > 0.05:
            triggered.append({
                'name': 'failure_suspicion',
                'message': f'Модель выбрала норму, но общий риск отказов {failure_prob_sum:.1%}. '
                           f'Нужна проверка оператора',
            })
            return 'manual_review', triggered

    if prediction == 'Tool_Wear_Failure' and zone == 'auto_decision':
        triggered.append({
            'name': 'tool_wear_forced_review',
            'message': 'Предсказан износ инструмента. Нужна проверка оператора',
        })
        return 'recommendation', triggered

    return zone, triggered


def step5_physics_rules(inputs, prediction):
    """Шаг 5в. Физические правила противоречий."""
    triggered = []

    air = inputs.get('Air_Temperature', 0)
    process = inputs.get('Process_Temperature', 0)
    rpm = inputs.get('Rotational_Speed', 0)
    torque = inputs.get('Torque', 0)
    tool_wear = inputs.get('Tool_Wear', 0)
    machine_type = inputs.get('Type', 'L')

    temp_diff = process - air

    if temp_diff < 10 and rpm < 1500 and machine_type == 'L':
        if prediction != 'Heat_Dissipation_Failure':
            triggered.append({
                'name': 'physics_heat_risk',
                'message': 'Параметры похожи на перегрев. Нужна проверка оператора',
            })

    if rpm > 0 and torque > 0:
        power = 0.10472 * rpm * torque

        if power < 4000 or power > 8500:
            if prediction != 'Power_Failure':
                triggered.append({
                    'name': 'physics_power_risk',
                    'message': 'Мощность вне безопасной зоны. Нужна проверка оператора',
                })

    overstrain_limit = {
        'L': 10000,
        'M': 11000,
        'H': 12000,
    }.get(machine_type, 10000)

    if tool_wear * torque > overstrain_limit:
        if prediction != 'Overstrain_Failure':
            triggered.append({
                'name': 'physics_overstrain_risk',
                'message': 'Нагрузка на инструмент слишком высокая. Нужна проверка оператора',
            })

    if tool_wear >= 180 and prediction != 'Tool_Wear_Failure':
        triggered.append({
            'name': 'physics_tool_wear_zone',
            'message': 'Износ инструмента близок к опасной зоне. Нужна проверка оператора',
        })

    if triggered:
        return 'manual_review', triggered

    return None, triggered


def has_risk_signals(inputs):
    """Финальная страховка: есть ли в параметрах хоть один признак риска."""
    air = inputs.get('Air_Temperature', 0)
    process = inputs.get('Process_Temperature', 0)
    rpm = inputs.get('Rotational_Speed', 0)
    torque = inputs.get('Torque', 0)
    tool_wear = inputs.get('Tool_Wear', 0)
    machine_type = inputs.get('Type', 'L')

    if tool_wear >= 180:
        return True, 'износ инструмента близок к опасной зоне'

    if process - air < 10 and rpm < 1500 and machine_type == 'L':
        return True, 'параметры похожи на перегрев'

    if rpm > 0 and torque > 0:
        power = 0.10472 * rpm * torque

        if power < 4000 or power > 8500:
            return True, 'мощность вне безопасной зоны'

    overstrain_limit = {'L': 10000, 'M': 11000, 'H': 12000}.get(machine_type, 10000)

    if tool_wear * torque > overstrain_limit:
        return True, 'нагрузка на инструмент слишком высокая'

    return False, None


def step6_business_logic(zone, prediction):
    """Шаг 6. Зона задаёт срочность, класс задаёт действие."""
    info = CLASS_INFO[prediction]

    zone_prefix = {
        'auto_decision': 'Авто-решение',
        'recommendation': 'Рекомендация оператору',
        'manual_review': 'Ручная проверка',
    }

    action_map = {
        'auto_decision': info['auto_action'],
        'recommendation': info['review_action'],
        'manual_review': info['manual_action'],
    }

    if zone == 'auto_decision' and prediction == 'No_Failure':
        severity = 'low'
    elif zone == 'manual_review':
        severity = 'high'
    else:
        severity = 'medium'

    if zone == 'manual_review' and prediction == 'No_Failure':
        action_text = 'Осмотреть станок, модель сомневается в норме'
    else:
        action_text = action_map[zone]

    label = f'{zone_prefix[zone]}: {action_text}'

    return {
        'execution_type': zone,
        'label': label,
        'severity': severity,
        'class_rus': info['rus'],
        'class_color': info['color'],
    }


def step8_log(record):
    """Шаг 8. Логирование решения."""
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(json.dumps(record, ensure_ascii=False, default=str) + '\n')


def _parse_ts(value):
    """Безопасно парсит timestamp в datetime, возвращает None при ошибке."""
    if not value:
        return None
    try:
        return datetime.fromisoformat(value)
    except (ValueError, TypeError):
        return None


def cleanup_old_records():
    """Удаляет из журнала записи старше LOG_RETENTION_HOURS.

    Вызывается при каждом чтении журнала. Перезаписывает файл
    только если что-то реально устарело — чтобы не дёргать диск зря.
    """
    if not LOG_PATH.exists():
        return 0

    cutoff = datetime.now() - timedelta(hours=LOG_RETENTION_HOURS)
    fresh_records = []
    removed = 0

    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                removed += 1
                continue

            ts = _parse_ts(record.get('timestamp'))

            if ts is None or ts >= cutoff:
                fresh_records.append(record)
            else:
                removed += 1

    if removed > 0:
        with open(LOG_PATH, 'w', encoding='utf-8') as f:
            for record in fresh_records:
                f.write(json.dumps(record, ensure_ascii=False, default=str) + '\n')

    return removed


def read_log():
    cleanup_old_records()

    if not LOG_PATH.exists():
        return []

    records = []

    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if line:
                records.append(json.loads(line))

    return records


def update_feedback(timestamp, feedback):
    records = read_log()

    for record in records:
        if record.get('timestamp') == timestamp:
            record['feedback'] = feedback

    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False, default=str) + '\n')


def run_pipeline(inputs, config, model, t_low, t_high, expected_class=None):
    """Полный прогон контура."""
    timestamp = datetime.now().isoformat(timespec='seconds')

    validation = step1_validate(inputs, config)

    if not validation['ok']:
        record = {
            'timestamp': timestamp,
            'expected_class': expected_class,
            'input': inputs,
            'validation': validation,
            'action': {
                'execution_type': 'safe_default',
                'label': 'Данные не прошли валидацию, модель не вызывалась',
                'severity': 'high',
            },
            'feedback': None,
        }

        step8_log(record)
        return record

    early = step2_early_rules(inputs)

    if early:
        action_label = 'Ранняя проверка: ' + early[0]['message']

        record = {
            'timestamp': timestamp,
            'expected_class': expected_class,
            'input': inputs,
            'validation': validation,
            'early_rules': early,
            'action': {
                'execution_type': 'early_rule',
                'label': action_label,
                'severity': 'high',
            },
            'feedback': None,
        }

        step8_log(record)
        return record

    pred, proba, conf = step4_predict(
        model,
        inputs,
        config['feature_columns'],
        config['classes'],
    )

    zone = step5_apply_thresholds(conf, t_low, t_high)
    zone_after, late = step5_late_rules(pred, proba, zone)

    physics_zone, physics_rules = step5_physics_rules(inputs, pred)

    if physics_zone is not None:
        zone_after = physics_zone
        late = late + physics_rules

    risk_present, risk_reason = has_risk_signals(inputs)

    if risk_present and zone_after == 'auto_decision' and pred == 'No_Failure':
        zone_after = 'manual_review'
        late = late + [{
            'name': 'risk_signal_block',
            'message': f'Есть признак риска: {risk_reason}. Авто-решение заблокировано',
        }]

    action = step6_business_logic(zone_after, pred)

    record = {
        'timestamp': timestamp,
        'expected_class': expected_class,
        'input': inputs,
        'validation': validation,
        'early_rules': early,
        'prediction': pred,
        'probabilities': proba,
        'confidence': conf,
        'zone_initial': zone,
        'late_rules': late,
        'zone_final': zone_after,
        'action': action,
        'thresholds': {
            't_low': t_low,
            't_high': t_high,
        },
        'feedback': None,
    }

    step8_log(record)
    return record


st.set_page_config(
    page_title='Контур решений',
    layout='wide',
    initial_sidebar_state='expanded',
)


config = load_config()

try:
    model = load_model()
except Exception as e:
    st.error(f'Не удалось загрузить модель из {MODEL_DIR}: {e}')
    st.info('Распакуйте архив с моделью в папку `models/`.')
    st.stop()


with st.sidebar:
    st.header('Настройки')

    t_low = st.slider('Порог ручной проверки', 0.0, 1.0, 0.60, 0.05)
    t_high = st.slider('Порог авто-решения', 0.0, 1.0, 0.90, 0.05)

    st.caption(
        'Ниже первого порога — ручная проверка. '
        'Выше второго — авто-решение, если нет признаков риска.'
    )

    if t_low > t_high:
        st.warning('Порог ручной проверки не должен быть выше порога авто-решения')

    st.divider()

    st.subheader('Стоимость ошибок')

    st.caption(
        'Эти два числа отвечают на простой вопрос: '
        '**что для нас дороже — пропустить отказ или зря отвлечь оператора?** '
        'От ответа зависит, какие пороги выставить.'
    )

    cost_auto = st.number_input(
        'Если станок сломался, а контур этого не заметил',
        min_value=1,
        value=20,
        help='Сколько мы условно теряем: простой линии, ремонт, брак деталей. '
             'Обычно это сильно дороже, чем лишняя проверка.',
    )
    cost_manual = st.number_input(
        'Если оператор зря проверил станок',
        min_value=1,
        value=3,
        help='Сколько мы условно теряем: время оператора, остановка на проверку.',
    )

    ratio = cost_auto / cost_manual

    if ratio >= 10:
        rec = 'Ошибка очень дорогая → нужны **строгие** значения (t_high около 0.90–0.95)'
        rec_color = '#EF4444'
    elif ratio >= 4:
        rec = 'Ошибка заметно дороже проверки → **умеренные** значения (t_high около 0.85–0.90)'
        rec_color = '#F59E0B'
    else:
        rec = 'Стоимости близки → можно сделать **мягче** (t_high около 0.75–0.85)'
        rec_color = '#22C55E'

    st.markdown(
        f"""
<div style="
    background: {rec_color}15;
    border-left: 3px solid {rec_color};
    padding: 10px 12px;
    border-radius: 6px;
    font-size: 12px;
    color: #D1D1D6;
    margin-top: 8px;
    line-height: 1.5;
">
    <div style="color: {rec_color}; font-weight: 600; margin-bottom: 4px;">
        Соотношение 1 : {ratio:.0f}
    </div>
    {rec}
</div>
        """,
        unsafe_allow_html=True,
    )


st.title('Контур принятия решений для предиктивного обслуживания')

st.caption(
    'Система оценивает параметры станка, определяет возможный отказ '
    'и выбирает действие для оператора.'
)


tab_pipeline, tab_thresholds, tab_monitoring, tab_about = st.tabs([
    'Контур решения',
    'Пороги и зоны',
    'Мониторинг',
    'О системе',
])


with tab_pipeline:
    st.subheader('Параметры станка')

    st.caption(
        'Выберите готовый пример или измените значения вручную. '
        'Под каждым полем указан допустимый диапазон.'
    )

    feature_columns = config['feature_columns']
    ensure_input_state(feature_columns)

    btn_cols = st.columns(5)

    for i, (label, gen_fn) in enumerate(CLASS_GENERATORS.items()):
        with btn_cols[i]:
            button_type = 'primary' if st.session_state.expected_class == label else 'secondary'

            if st.button(label, width='stretch', key=f'gen_{i}', type=button_type):
                rng = np.random.default_rng()
                new_inputs = gen_fn(rng)

                set_machine_inputs(
                    new_inputs,
                    expected_class=label,
                    clear_result=True,
                )

                st.rerun()

    st.info(f'Ожидаемый класс: {st.session_state.expected_class}')

    st.markdown('')

    cols = st.columns(3)

    for i, feature in enumerate(feature_columns):
        stats = config['feature_stats'][feature]
        info = FEATURE_INFO.get(feature, {'rus': feature, 'help': ''})
        widget_key = f'in_{feature}'

        with cols[i % 3]:
            if stats['dtype'] == 'numeric':
                min_v = float(stats['min'])
                max_v = float(stats['max'])
                step = max((max_v - min_v) / 1000, 0.01)

                current_value = float(st.session_state.inputs.get(feature, stats['mean']))
                current_value = min(max(current_value, min_v), max_v)

                if widget_key not in st.session_state:
                    st.session_state[widget_key] = current_value
                else:
                    st.session_state[widget_key] = min(
                        max(float(st.session_state[widget_key]), min_v),
                        max_v,
                    )

                value = st.number_input(
                    info['rus'],
                    min_value=min_v,
                    max_value=max_v,
                    step=step,
                    format='%.2f',
                    help=info['help'],
                    key=widget_key,
                    on_change=clear_last_result,
                )

                st.caption(
                    f'Можно ввести: от {format_number(min_v)} до {format_number(max_v)}'
                )

                st.session_state.inputs[feature] = float(value)

            else:
                values = stats['values']

                if widget_key not in st.session_state:
                    current = st.session_state.inputs.get(feature, values[0])

                    if current not in values:
                        current = values[0]

                    st.session_state[widget_key] = current

                if st.session_state[widget_key] not in values:
                    st.session_state[widget_key] = values[0]

                value = st.selectbox(
                    info['rus'],
                    values,
                    help=info['help'],
                    key=widget_key,
                    on_change=clear_last_result,
                )

                st.caption('Можно выбрать: ' + ', '.join(values))

                st.session_state.inputs[feature] = value

    sync_inputs_from_widgets(feature_columns)

    st.divider()

    if st.button('Запустить контур на текущих параметрах', type='primary'):
        st.session_state.last_result = run_pipeline(
            st.session_state.inputs.copy(),
            config,
            model,
            t_low,
            t_high,
            expected_class=st.session_state.expected_class,
        )

    if 'last_result' in st.session_state:
        result = st.session_state.last_result

        st.subheader('Прохождение контура')

        if result.get('expected_class'):
            st.info(f'Ожидаемый класс: {result["expected_class"]}')

        c1, c2 = st.columns(2)

        with c1:
            with st.container(border=True):
                st.markdown('**Шаг 1. Проверка данных**')
                st.caption('Проверяем, что значения заполнены и входят в допустимые диапазоны.')

                if result['validation']['ok']:
                    st.success('Все значения корректны')
                else:
                    st.error('Есть ошибки:')

                    for err in result['validation']['errors']:
                        st.write('•', err)

        with c2:
            with st.container(border=True):
                st.markdown('**Шаг 2. Быстрые правила**')
                st.caption('Если риск очевиден, модель не вызывается.')

                if result.get('early_rules'):
                    for rule in result['early_rules']:
                        st.warning(rule['message'])
                else:
                    st.info('Явного риска нет, переходим к модели')

        if 'prediction' in result:
            with st.container(border=True):
                st.markdown('**Шаг 3. Подготовка признаков**')
                st.caption(
                    'Используются входные признаки, подготовленные для модели. '
                    'На этапе запуска контура дополнительные признаки не создаются.'
                )
                st.info('Набор признаков передан модели в том же составе, что использовался при обучении')

            with st.container(border=True):
                st.markdown('**Шаг 4. Оценка модели**')
                st.caption(
                    'Модель выбирает наиболее вероятный класс. Затем результат проверяется правилами.'
                )

                expected_internal = CLASS_LABEL_TO_INTERNAL.get(result.get('expected_class'))
                prediction = result['prediction']
                prediction_rus = CLASS_INFO[prediction]['rus']

                if expected_internal == prediction:
                    st.success(f'Модель выбрала ожидаемый класс: {prediction_rus}')
                else:
                    st.warning(
                        f'Ожидали: {result.get("expected_class")}. '
                        f'Модель выбрала: {prediction_rus}.'
                    )

                m1, m2 = st.columns([1, 2])

                with m1:
                    info = CLASS_INFO[result['prediction']]
                    st.metric(info['rus'], f"{result['confidence']:.1%}")
                    st.caption(f"Внутреннее имя класса: `{result['prediction']}`")

                with m2:
                    proba_df = pd.DataFrame({
                        'Класс': [
                            CLASS_INFO[class_name]['rus']
                            for class_name in result['probabilities']
                        ],
                        'Вероятность': list(result['probabilities'].values()),
                    }).sort_values('Вероятность', ascending=True)

                    color_map = {
                        CLASS_INFO[class_name]['rus']: CLASS_INFO[class_name]['color']
                        for class_name in result['probabilities']
                    }

                    fig = px.bar(
                        proba_df,
                        x='Вероятность',
                        y='Класс',
                        orientation='h',
                        range_x=[0, 1],
                        color='Класс',
                        color_discrete_map=color_map,
                    )

                    fig.update_layout(
                        height=220,
                        margin=dict(l=0, r=0, t=0, b=0),
                        showlegend=False,
                    )

                    st.plotly_chart(fig, width='stretch')

            with st.container(border=True):
                st.markdown('**Шаг 5. Проверка решения**')
                st.caption(
                    'Смотрим на уверенность модели и признаки риска в параметрах.'
                )

                zone_text = {
                    'auto_decision': f"уверенность {result['confidence']:.1%} ≥ {t_high:.0%}",
                    'recommendation': f"{t_low:.0%} ≤ уверенность {result['confidence']:.1%} < {t_high:.0%}",
                    'manual_review': f"уверенность {result['confidence']:.1%} < {t_low:.0%}",
                }

                st.write(
                    f"Начальная зона: `{result['zone_initial']}` "
                    f"({zone_text[result['zone_initial']]})"
                )

                if result.get('late_rules'):
                    for rule in result['late_rules']:
                        st.warning(rule['message'])

                    st.write(f"Итоговая зона: `{result['zone_final']}`")
                else:
                    st.info('Дополнительных рисков не найдено')

            with st.container(border=True):
                st.markdown('**Шаги 6–7. Финальное действие**')
                st.caption('Показываем, что нужно сделать дальше.')

                action = result['action']

                if action['severity'] == 'low':
                    st.success(action['label'])
                elif action['severity'] == 'medium':
                    st.warning(action['label'])
                else:
                    st.error(action['label'])

                st.caption(f"Тип исполнения: `{action['execution_type']}`")

        with st.container(border=True):
            st.markdown('**Шаг 8. Журнал и обратная связь**')
            st.caption(
                'Решение записано. Оценка от оператора поможет потом разбирать ошибки.'
            )

            st.caption(f"timestamp: {result['timestamp']}")

            fb1, fb2, _ = st.columns([1, 1, 4])

            with fb1:
                if st.button('Согласен', width='stretch'):
                    update_feedback(result['timestamp'], 'agree')
                    st.toast('Сохранено')

            with fb2:
                if st.button('Не согласен', width='stretch'):
                    update_feedback(result['timestamp'], 'disagree')
                    st.toast('Сохранено')


with tab_thresholds:
    st.subheader('Пороги простыми словами')

    st.write(
        'Контур работает просто: модель даёт уверенность, а правила проверяют, '
        'нет ли опасных параметров.'
    )

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.markdown('**Ручная проверка**')
            st.metric('Зона', f'ниже {t_low:.0%}')
            st.caption('Модель не уверена. Решение принимает оператор.')

    with c2:
        with st.container(border=True):
            st.markdown('**Рекомендация**')
            st.metric('Зона', f'{t_low:.0%}–{t_high:.0%}')
            st.caption('Модель предлагает действие, оператор подтверждает.')

    with c3:
        with st.container(border=True):
            st.markdown('**Авто-решение**')
            st.metric('Зона', f'выше {t_high:.0%}')
            st.caption('Можно принять автоматически, если нет признаков риска.')

    st.divider()

    st.subheader('Главное правило безопасности')

    st.info(
        'Если параметры похожи на отказ, система не разрешает авто-решение '
        '«продолжать работу». Случай уходит оператору.'
    )

    st.divider()

    st.subheader('Какие пороги использует контур')

    st.caption(
        'Пороги сгруппированы по этапам: '
        'сначала ранние правила, потом проверка по модели, потом физические правила.'
    )

    st.markdown('##### 1. Ранние правила — срабатывают до модели')
    st.caption('Очевидные риски: модель в этом случае не вызывается.')

    early_cols = st.columns(2)

    with early_cols[0]:
        with st.container(border=True):
            st.markdown('**Износ инструмента**')
            st.metric('Порог', 'от 190 мин')
            st.caption('Инструмент работает слишком долго — нужна проверка.')

    with early_cols[1]:
        with st.container(border=True):
            st.markdown('**Крутящий момент**')
            st.metric('Порог', '< 3 Н·м')
            st.caption('Очень низкое значение может означать ошибку датчика.')

    st.markdown('')

    st.markdown('##### 2. Правила по выходу модели — проверка вероятностей')
    st.caption('Анализ уверенности и распределения классов.')

    model_cols_1 = st.columns(2)

    with model_cols_1[0]:
        with st.container(border=True):
            st.markdown('**Авто-решение**')
            st.metric('Порог уверенности', f'от {t_high:.0%}')
            st.caption('Разрешено только если нет признаков риска.')

    with model_cols_1[1]:
        with st.container(border=True):
            st.markdown('**Сомнение модели**')
            st.metric('Порог', 'разница < 15%')
            st.caption('Если два главных класса слишком близки — решает оператор.')

    model_cols_2 = st.columns(2)

    with model_cols_2[0]:
        with st.container(border=True):
            st.markdown('**Риск износа по модели**')
            st.metric('Порог', '> 5%')
            st.caption('Даже небольшой риск износа отправляет случай на проверку.')

    with model_cols_2[1]:
        with st.container(border=True):
            st.markdown('**Скрытый риск отказа**')
            st.metric('Порог', '> 5%')
            st.caption('Модель выбрала «нет отказа», но сумма рисков отказов выше 5%.')

    st.markdown('')

    st.markdown('##### 3. Физические правила — сравнение с физикой процесса')
    st.caption('Параметры станка сравниваются с признаками отказов.')

    phys_cols_1 = st.columns(2)

    with phys_cols_1[0]:
        with st.container(border=True):
            st.markdown('**Перегрев**')
            st.metric('Условие', 'ΔT < 10 K, об/мин < 1500, тип L')
            st.caption('Малая разница температур при низких оборотах и типе L.')

    with phys_cols_1[1]:
        with st.container(border=True):
            st.markdown('**Мощность**')
            st.metric('Безопасная зона', '4000–8500 Вт')
            st.caption('P = 0.10472 · RPM · Torque. Выход из диапазона — проверка.')

    phys_cols_2 = st.columns(2)

    with phys_cols_2[0]:
        with st.container(border=True):
            st.markdown('**Перегрузка по моменту**')
            st.metric('Порог (L / M / H)', '10000 / 11000 / 12000')
            st.caption('Tool_Wear × Torque. Порог зависит от типа детали.')

    with phys_cols_2[1]:
        with st.container(border=True):
            st.markdown('**Износ — предупреждение**')
            st.metric('Порог', 'от 180 мин')
            st.caption('Если модель не выбрала износ, контур всё равно проверяет риск.')

    st.divider()

    st.subheader('Зачем нужны эти пороги')

    st.write(
        'Если сделать пороги строже, оператор будет проверять больше случаев. '
        'Если сделать мягче, автоматических решений станет больше, но риск ошибки вырастет.'
    )

    expected_cost_per_check = cost_manual
    expected_cost_per_miss = cost_auto

    st.markdown(
        f"""
**Как сейчас настроены стоимости (из боковой панели):**

- одна ошибка авто-решения «стоит» как **{expected_cost_per_miss / expected_cost_per_check:.0f} ручных проверок**
- значит, выгодно отправлять случай оператору, если **риск ошибки** модели выше, чем {1 / (expected_cost_per_miss / expected_cost_per_check):.1%}
- именно поэтому порог авто-решения стоит **высоким** — {t_high:.0%}: модель должна быть очень уверена, чтобы заменить оператора
        """
    )


with tab_monitoring:
    st.subheader('Состояние контура')

    st.caption(
        f'Здесь видно, сколько решений прошло через систему и как часто нужен оператор. '
        f'Журнал хранится последние {LOG_RETENTION_HOURS} часов — более старые записи '
        f'удаляются автоматически.'
    )

    records = read_log()

    if not records:
        st.info('Журнал пуст. Запустите контур.')
    else:
        df_log = pd.DataFrame([
            {
                'time': record.get('timestamp'),
                'expected_class': record.get('expected_class'),
                'prediction': record.get('prediction'),
                'confidence': record.get('confidence'),
                'zone': record.get('zone_final'),
                'feedback': record.get('feedback'),
            }
            for record in records
        ])

        total = len(df_log)
        with_fb = int(df_log['feedback'].notna().sum())
        avg_conf = df_log['confidence'].dropna().mean()
        zone_counts = df_log['zone'].value_counts()
        manual_share = zone_counts.get('manual_review', 0) / total

        c1, c2, c3, c4 = st.columns(4)

        c1.metric('Всего решений', total)
        c2.metric('С обратной связью', f'{with_fb} ({100 * with_fb / total:.0f}%)')
        c3.metric(
            'Средняя уверенность',
            f'{avg_conf:.3f}' if pd.notna(avg_conf) else '-',
        )
        c4.metric('Доля ручной проверки', f'{100 * manual_share:.0f}%')

        st.divider()

        st.markdown('**Health-check контура**')

        if manual_share > 0.3 and total >= 5:
            st.warning(
                f'Доля ручной проверки {100 * manual_share:.0f}% выше 30% — '
                f'оператор перегружен. Подумайте о пересмотре порогов или правил.'
            )
        else:
            st.success(
                'Нагрузка на оператора в норме: менее 30% решений требуют ручной проверки.'
            )

        if total >= 5 and with_fb / total < 0.5:
            st.warning(
                f'Только {100 * with_fb / total:.0f}% решений получили обратную связь. '
                f'Без неё сложнее понять, где модель ошибается.'
            )
        elif total >= 5:
            st.success(
                f'Обратная связь поступает по {100 * with_fb / total:.0f}% решений.'
            )

        st.divider()

        st.subheader('Последние решения')

        st.dataframe(
            df_log.tail(20).iloc[::-1],
            width='stretch',
            height=300,
            hide_index=True,
        )

        st.download_button(
            'Скачать журнал',
            data=LOG_PATH.read_bytes(),
            file_name='decisions.jsonl',
            mime='application/x-ndjson',
        )


with tab_about:
    st.subheader('Кейс')

    st.write(
        'Фрезерный станок работает на производственной линии. '
        'Система получает параметры процесса и выбирает безопасное действие.'
    )

    st.divider()

    st.subheader('Датасет AI4I 2020 Predictive Maintenance')

    st.write(
        'Модель обучена на открытом датасете **AI4I 2020 Predictive Maintenance Dataset** '
        '(UCI Machine Learning Repository). Это синтетический набор данных, '
        'который моделирует работу промышленного фрезерного станка и используется '
        'как стандартный бенчмарк в задачах предиктивного обслуживания.'
    )

    st.markdown('##### Что в датасете')

    ds1, ds2, ds3 = st.columns(3)

    ds1.metric('Наблюдений', '10 000')
    ds2.metric('Признаков', '6 рабочих + 8 служебных')
    ds3.metric('Классов отказа', '5 + норма')

    st.markdown('##### Признаки станка')

    st.markdown('''
| Признак | Что означает | Типичный диапазон |
| --- | --- | --- |
| **Type** | Качество детали: L (Low, 50%), M (Medium, 30%), H (High, 20%) | L / M / H |
| **Air temperature** | Температура воздуха в цеху | ~295–305 K (≈22–32 °C) |
| **Process temperature** | Температура в зоне обработки | ~305–315 K (≈32–42 °C) |
| **Rotational speed** | Обороты шпинделя | ~1100–2900 об/мин |
| **Torque** | Крутящий момент на инструменте | ~3–77 Н·м |
| **Tool wear** | Время работы инструмента с момента замены | 0–253 мин |
    ''')

    st.markdown('##### Типы отказов и физические правила, по которым они генерируются')

    st.markdown('''
| Класс | Доля в данных | Условие возникновения |
| --- | --- | --- |
| **No Failure** — нет отказа | ~96.5 % | Все параметры в норме |
| **Heat Dissipation Failure** (HDF) — отказ теплоотвода | ~1.2 % | Разница температур < 8.6 K **и** обороты < 1380 об/мин |
| **Power Failure** (PWF) — отказ по мощности | ~0.95 % | Мощность вне диапазона 3500–9000 Вт (P = 2π·RPM·Torque / 60) |
| **Overstrain Failure** (OSF) — перегрузка по моменту | ~0.78 % | Tool_Wear × Torque превышает порог: 11000 для L, 12000 для M, 13000 для H |
| **Tool Wear Failure** (TWF) — износ инструмента | ~0.46 % | Износ достиг случайной точки в диапазоне 200–240 мин |
| **Random Failures** (RNF) — случайный отказ | ~0.19 % | Случайный отказ с вероятностью 0.1% на любом наблюдении |
    ''')

    st.info(
        '**Важно:** классы сильно несбалансированы. Из 10 000 наблюдений только '
        '~339 содержат отказы — модель должна научиться ловить редкие события, '
        'не выдавая много ложных срабатываний на 96.5 % нормальных наблюдений.'
    )

    st.markdown('##### Почему пороги в контуре близки, но не равны порогам датасета')

    st.write(
        'В контуре физические правила (вкладка «Пороги и зоны») немного жёстче, '
        'чем в исходном датасете: ΔT < 10 K вместо 8.6 K, мощность 4000–8500 Вт вместо '
        '3500–9000 Вт. Это сделано **намеренно** — чтобы создать «зону подозрения» '
        'до того, как наступит реальный отказ. Если ждать точного совпадения с физикой '
        'отказа, у оператора уже не будет времени среагировать.'
    )

    st.markdown('##### Откуда взять датасет')

    st.markdown(
        '- **UCI ML Repository:** [archive.ics.uci.edu/dataset/601](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset)  \n'
        '- **Авторы:** Stephan Matzka, School of Engineering — Technology and Life, '
        'Hochschule für Technik und Wirtschaft Berlin, 2020  \n'
        '- **Лицензия:** Creative Commons Attribution 4.0 International (CC BY 4.0)'
    )

    st.divider()

    st.subheader('Архитектура контура')

    st.markdown('''
| Шаг | Что делает | Функция в коде |
| --- | --- | --- |
| 1 | Проверяет входные данные | `step1_validate` |
| 2 | Проверяет очевидные риски | `step2_early_rules` |
| 3 | Использует признаки, подготовленные при обучении | выполняется при обучении модели |
| 4 | Получает прогноз модели | `step4_predict` |
| 5 | Проверяет уверенность и риски | `step5_apply_thresholds`, `step5_late_rules`, `step5_physics_rules` |
| 6 | Выбирает действие | `step6_business_logic`, `has_risk_signals` |
| 7 | Показывает итог оператору | поле `action` в результате |
| 8 | Сохраняет решение | `step8_log`, вкладка «Мониторинг» |
    ''')

    st.subheader('Модель')

    if 'test_metrics' in config:
        metrics = config['test_metrics']

        c1, c2, c3, c4 = st.columns(4)

        c1.metric('F1-macro', f"{metrics.get('f1_macro', 0):.4f}")
        c2.metric('Balanced acc', f"{metrics.get('balanced_accuracy', 0):.4f}")
        c3.metric('Log loss', f"{metrics.get('log_loss', 0):.4f}")
        c4.metric('ROC-AUC OvR', f"{metrics.get('roc_auc_ovr_macro', 0):.4f}")

    st.write(
        'Модель обучена через mljar-supervised. Лучший вариант — `Ensemble_Stacked`.'
    )

    st.subheader('Почему нужен контур')

    st.write(
        'Одна модель может ошибиться, особенно на редких отказах. '
        'Поэтому поверх модели добавлены правила безопасности.'
    )

    st.markdown('''
- до модели проверяются очевидные опасные значения
- после модели проверяется уверенность прогноза
- затем параметры сравниваются с физическими признаками риска
- если риск есть, авто-решение блокируется
    ''')

    st.write(
        'Главная идея: станок продолжает работу автоматически только тогда, '
        'когда модель уверена и параметры выглядят безопасно.'
    )

    st.subheader('Ограничения')

    st.markdown('''
- данные синтетические
- на реальном станке распределения могут отличаться
- пороги нужно настраивать под реальную цену ошибок
    ''')

    st.subheader('Защита от ошибок модели')

    st.write(
        'Даже если модель ошибается, контур проверяет результат несколькими способами. '
        'Это снижает риск пропустить отказ.'
    )