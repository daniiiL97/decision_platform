"""
Контур принятия решений для предиктивного обслуживания фрезерного станка.
Реализация 8 шагов архитектуры контура из лекций.
"""

import json
from datetime import datetime
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


CLASS_INFO = {
    'No_Failure': {
        'rus': 'Нет отказа',
        'auto_action': 'Продолжать работу. Параметры станка в норме',
        'review_action': 'Оператор проверяет станок: отказ не обнаружен, но уверенность модели невысокая',
        'manual_action': 'Оператор проверяет станок вручную: модель недостаточно уверена',
        'color': '#2ECC71',
    },
    'Heat_Dissipation_Failure': {
        'rus': 'Перегрев',
        'auto_action': 'Оператор останавливает станок и проверяет теплоотвод',
        'review_action': 'Оператор проверяет систему охлаждения и теплоотвод',
        'manual_action': 'Оператор вручную проверяет возможный перегрев',
        'color': '#E74C3C',
    },
    'Power_Failure': {
        'rus': 'Отказ по мощности',
        'auto_action': 'Оператор проверяет режим мощности и нагрузку станка',
        'review_action': 'Оператор проверяет параметры мощности',
        'manual_action': 'Оператор вручную проверяет возможный отказ по мощности',
        'color': '#F39C12',
    },
    'Overstrain_Failure': {
        'rus': 'Перегрузка по моменту',
        'auto_action': 'Оператор снижает нагрузку и проверяет режим резания',
        'review_action': 'Оператор проверяет возможную перегрузку по моменту',
        'manual_action': 'Оператор вручную проверяет перегрузку по моменту',
        'color': '#9B59B6',
    },
    'Tool_Wear_Failure': {
        'rus': 'Износ инструмента',
        'auto_action': 'Оператор проверяет состояние инструмента',
        'review_action': 'Оператор проверяет возможный износ инструмента',
        'manual_action': 'Оператор вручную проверяет износ инструмента',
        'color': '#3498DB',
    },
    'Random_Failures': {
        'rus': 'Случайный отказ',
        'auto_action': 'Оператор фиксирует случайный отказ и осматривает станок',
        'review_action': 'Оператор проверяет станок: возможен случайный отказ',
        'manual_action': 'Оператор вручную осматривает станок на случайный отказ',
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


def read_log():
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

    cost_auto = st.number_input('Ошибка авто-решения', min_value=1, value=20)
    cost_manual = st.number_input('Ручная проверка', min_value=1, value=3)

    st.caption('Используется только для пояснения логики порогов.')


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
                'Решение сохраняется в журнал. Обратная связь помогает потом анализировать ошибки.'
            )

            st.caption(f"timestamp: {result['timestamp']}")

            fb1, fb2, _ = st.columns([1, 1, 4])

            with fb1:
                if st.button('Согласен с решением', width='stretch'):
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

    st.subheader('Что считается риском')

    risk_cols = st.columns(2)

    with risk_cols[0]:
        st.markdown('''
- высокий износ инструмента
- слишком большая нагрузка
- подозрение на перегрев
        ''')

    with risk_cols[1]:
        st.markdown('''
- мощность вне безопасной зоны
- модель сомневается между классами
- есть небольшой риск отказа при ответе «нет отказа»
        ''')

    st.divider()

    st.subheader('Зачем нужны эти пороги')

    st.write(
        'Если сделать пороги строже, оператор будет проверять больше случаев. '
        'Если сделать мягче, автоматических решений станет больше, но риск ошибки вырастет.'
    )

    st.caption(
        f'В этой версии цена ошибки авто-решения: {cost_auto}, '
        f'цена ручной проверки: {cost_manual}.'
    )


with tab_monitoring:
    st.subheader('Состояние контура')

    st.caption(
        'Здесь видно, сколько решений прошло через систему и как часто нужен оператор.'
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