import json
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from supervised.automl import AutoML

MODEL_DIR = Path("models/AutoML_Concrete_Strength")
CONFIG_PATH = Path("models/config.json")
LOG_PATH = Path("logs/decisions.jsonl")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

LOG_RETENTION_HOURS = 24

BASE_INPUT_COLUMNS = [
    "CEMENT",
    "BLAST_FURNACE_SLAG",
    "FLY_ASH",
    "WATER",
    "SUPERPLASTICIZER",
    "COARSE_AGGREGATE",
    "FINE_AGGREGATE",
    "AGE",
]

FEATURE_INFO = {
    "CEMENT": {
        "label": "Цемент, кг/м³",
        "short": "Цемент",
        "help": "Основное вяжущее вещество в бетонной смеси.",
        "step": 5.0,
    },
    "BLAST_FURNACE_SLAG": {
        "label": "Доменный шлак, кг/м³",
        "short": "Шлак",
        "help": "Минеральная добавка. Может заменять часть цемента.",
        "step": 5.0,
    },
    "FLY_ASH": {
        "label": "Зола-уноса, кг/м³",
        "short": "Зола-уноса",
        "help": "Минеральная добавка. В составе может отсутствовать.",
        "step": 5.0,
    },
    "WATER": {
        "label": "Вода, кг/м³",
        "short": "Вода",
        "help": "Количество воды для затворения смеси.",
        "step": 2.0,
    },
    "SUPERPLASTICIZER": {
        "label": "Суперпластификатор, кг/м³",
        "short": "Суперпластификатор",
        "help": "Химическая добавка для регулирования подвижности смеси.",
        "step": 0.5,
    },
    "COARSE_AGGREGATE": {
        "label": "Щебень, кг/м³",
        "short": "Щебень",
        "help": "Крупный заполнитель бетонной смеси.",
        "step": 5.0,
    },
    "FINE_AGGREGATE": {
        "label": "Песок, кг/м³",
        "short": "Песок",
        "help": "Мелкий заполнитель бетонной смеси.",
        "step": 5.0,
    },
    "AGE": {
        "label": "Возраст образца, дней",
        "short": "Возраст",
        "help": "Возраст бетона к моменту оценки прочности.",
        "step": 1.0,
    },
}

COMPOSITION_PROFILES = {
    "Типовая смесь для 28 дней": {
        "description": (
            "Базовый состав для первой оценки. Подходит для демонстрации "
            "расчёта при сроке твердения 28 дней."
        ),
        "ranges": {
            "CEMENT": (300, 380),
            "BLAST_FURNACE_SLAG": (0, 80),
            "FLY_ASH": (0, 40),
            "WATER": (170, 195),
            "SUPERPLASTICIZER": (3, 8),
            "COARSE_AGGREGATE": (950, 1050),
            "FINE_AGGREGATE": (740, 830),
            "AGE": (28, 28),
        },
    },
    "Смесь с повышенной прочностью": {
        "description": (
            "Вариант с большим количеством вяжущего, меньшим расходом воды "
            "и суперпластификатором. Решение зависит от результата расчёта."
        ),
        "ranges": {
            "CEMENT": (430, 520),
            "BLAST_FURNACE_SLAG": (40, 140),
            "FLY_ASH": (0, 30),
            "WATER": (140, 165),
            "SUPERPLASTICIZER": (8, 16),
            "COARSE_AGGREGATE": (900, 1020),
            "FINE_AGGREGATE": (680, 790),
            "AGE": (28, 56),
        },
    },
    "Состав с минеральными добавками": {
        "description": (
            "Вариант с умеренным количеством цемента, доменным шлаком "
            "и золой-уносом. Его удобно сравнивать с базовым составом."
        ),
        "ranges": {
            "CEMENT": (230, 310),
            "BLAST_FURNACE_SLAG": (40, 120),
            "FLY_ASH": (30, 100),
            "WATER": (180, 205),
            "SUPERPLASTICIZER": (1, 6),
            "COARSE_AGGREGATE": (940, 1050),
            "FINE_AGGREGATE": (740, 850),
            "AGE": (28, 28),
        },
    },
    "Контроль через 7 дней": {
        "description": (
            "Пример для оценки прочности на раннем сроке твердения. "
            "По нему удобно увидеть, как возраст влияет на результат."
        ),
        "ranges": {
            "CEMENT": (300, 390),
            "BLAST_FURNACE_SLAG": (0, 60),
            "FLY_ASH": (0, 30),
            "WATER": (165, 190),
            "SUPERPLASTICIZER": (3, 9),
            "COARSE_AGGREGATE": (950, 1050),
            "FINE_AGGREGATE": (740, 830),
            "AGE": (7, 7),
        },
    },
}


# Загружает сохранённую модель AutoML.
@st.cache_resource(show_spinner="Загрузка модели")
def load_model():
    return AutoML(results_path=str(MODEL_DIR))


# Загружает конфигурацию модели из файла.
@st.cache_data
def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


# Ищет таблицу с важностью признаков в папке модели.
@st.cache_data(show_spinner=False)
def load_global_feature_importance(model_dir_text):
    model_dir = Path(model_dir_text)

    if not model_dir.exists():
        return pd.DataFrame(columns=["feature", "importance"])

    candidates = []
    csv_paths = sorted(model_dir.rglob("*.csv"))

    for csv_path in csv_paths:
        if "importance" not in csv_path.name.lower():
            continue

        try:
            table = pd.read_csv(csv_path)
        except Exception:
            continue

        if table.empty or len(table.columns) < 2:
            continue

        normalized = {str(column).strip().lower(): column for column in table.columns}

        feature_column = next(
            (
                normalized[name]
                for name in [
                    "feature",
                    "feature_name",
                    "variable",
                    "column",
                    "name",
                ]
                if name in normalized
            ),
            None,
        )

        importance_column = next(
            (
                normalized[name]
                for name in [
                    "importance",
                    "mean_importance",
                    "permutation_importance",
                    "weight",
                    "value",
                ]
                if name in normalized
            ),
            None,
        )

        if feature_column is None or importance_column is None:
            feature_column = table.columns[0]
            importance_column = table.columns[1]

        parsed = pd.DataFrame({
            "feature": table[feature_column].astype(str).str.strip().str.upper(),
            "importance": pd.to_numeric(
                table[importance_column],
                errors="coerce",
            ),
        }).dropna()

        parsed = parsed.loc[parsed["feature"].isin(BASE_INPUT_COLUMNS)].copy()

        if parsed.empty:
            continue

        parsed["importance"] = parsed["importance"].abs()
        parsed = (
            parsed.groupby("feature", as_index=False)["importance"]
            .mean()
            .sort_values("importance", ascending=False)
        )

        candidates.append(parsed)

    if not candidates:
        return pd.DataFrame(columns=["feature", "importance"])

    best_candidate = max(
        candidates,
        key=lambda table: (len(table), float(table["importance"].sum())),
    )
    return best_candidate.reset_index(drop=True)


# Проверяет, подходит ли конфигурация для приложения.
def validate_config(config):
    required_keys = {
        "feature_columns",
        "feature_stats",
        "prediction_interval",
        "test_metrics",
    }
    missing_keys = required_keys.difference(config)

    if missing_keys:
        raise ValueError(
            "В config.json отсутствуют поля " + ", ".join(sorted(missing_keys))
        )

    if list(config["feature_columns"]) != BASE_INPUT_COLUMNS:
        raise ValueError(
            "Список признаков в config.json не совпадает с приложением. "
            "Проверьте, что используется модель Concrete Strength."
        )

    missing_stats = set(BASE_INPUT_COLUMNS).difference(config["feature_stats"])

    if missing_stats:
        raise ValueError(
            "В config.json отсутствуют диапазоны " + ", ".join(sorted(missing_stats))
        )

    radius = float(config["prediction_interval"].get("radius", 0))

    if not np.isfinite(radius) or radius <= 0:
        raise ValueError("В config.json указан некорректный радиус интервала.")


# Удаляет текущий результат расчёта.
def clear_last_result():
    st.session_state.pop("last_result", None)


# Создаёт состав по выбранному профилю.
def composition_from_profile(profile_name):
    rng = np.random.default_rng()
    composition = {}

    for feature, (low, high) in COMPOSITION_PROFILES[profile_name]["ranges"].items():
        value = low if low == high else rng.uniform(low, high)
        step = FEATURE_INFO[feature]["step"]
        composition[feature] = float(np.round(value / step) * step)

    return composition


# Создаёт случайный состав в пределах обучающих данных.
def composition_from_training_ranges(config):
    rng = np.random.default_rng()
    composition = {}

    for feature in BASE_INPUT_COLUMNS:
        stats = config["feature_stats"][feature]
        low = float(stats["min"])
        high = float(stats["max"])
        step = FEATURE_INFO[feature]["step"]

        value = rng.uniform(low, high)
        composition[feature] = float(np.round(value / step) * step)

    return composition


# Сохраняет состав в состоянии приложения.
def set_composition(composition):
    for feature, value in composition.items():
        st.session_state[f"input_{feature}"] = float(value)

    clear_last_result()


# Создаёт начальные значения формы.
def initialise_state():
    if "composition_profile" not in st.session_state:
        st.session_state.composition_profile = next(iter(COMPOSITION_PROFILES))

    first_input_key = f"input_{BASE_INPUT_COLUMNS[0]}"

    if first_input_key not in st.session_state:
        set_composition(composition_from_profile(st.session_state.composition_profile))

    if "required_strength_input" not in st.session_state:
        st.session_state.required_strength_input = 40.0

    if "safety_margin_input" not in st.session_state:
        st.session_state.safety_margin_input = 2.0


# Возвращает форму к исходным значениям.
def reset_application_state():
    keys_to_reset = [
        "composition_profile",
        "required_strength_input",
        "safety_margin_input",
        "cost_miss_input",
        "cost_test_input",
        "last_result",
    ]

    keys_to_reset.extend(f"input_{feature}" for feature in BASE_INPUT_COLUMNS)

    for key in keys_to_reset:
        st.session_state.pop(key, None)

    st.session_state["hide_result_after_reset"] = True
    initialise_state()


# Собирает значения состава из состояния.
def get_inputs_from_state():
    return {
        feature: float(st.session_state[f"input_{feature}"])
        for feature in BASE_INPUT_COLUMNS
    }


# Форматирует число для интерфейса.
def format_number(value):
    return f"{value:.0f}" if abs(value) >= 100 else f"{value:.1f}"


# Определяет допустимые границы ползунка.
def slider_bounds(feature, config):
    stats = config["feature_stats"][feature]
    max_train = float(stats["max"])
    max_input = max(max_train * 1.2, max_train + 10)

    if feature == "AGE":
        max_input = max(max_input, 365.0)

    return 0.0, float(max_input)


# Проверяет корректность введённых значений.
def step1_validate(inputs):
    errors = []

    for feature in BASE_INPUT_COLUMNS:
        value = inputs.get(feature)

        if value is None:
            errors.append(f"Не заполнено поле «{FEATURE_INFO[feature]['label']}».")
        elif not np.isfinite(value):
            errors.append(
                f"Поле «{FEATURE_INFO[feature]['label']}» содержит некорректное число."
            )
        elif value < 0:
            errors.append(
                f"Поле «{FEATURE_INFO[feature]['label']}» не может быть отрицательным."
            )

    return {"ok": not errors, "errors": errors}


# Проверяет физические ограничения и диапазоны обучения.
def step2_checks(inputs, config):
    hard_rules = []
    range_warnings = []

    if inputs["WATER"] < 1:
        hard_rules.append("В составе нет воды. Проверьте дозирование или ввод данных.")

    if inputs["CEMENT"] < 100:
        hard_rules.append(
            "Цемента меньше 100 кг/м³. Такой состав не подходит для расчёта прочности."
        )

    if inputs["AGE"] < 1:
        hard_rules.append(
            "Возраст образца меньше суток. Оценка прочности в этот момент некорректна."
        )

    for feature in BASE_INPUT_COLUMNS:
        stats = config["feature_stats"][feature]
        value = float(inputs[feature])
        low = float(stats["min"])
        high = float(stats["max"])

        if value < low or value > high:
            range_warnings.append(
                f"«{FEATURE_INFO[feature]['label']}» равно {value:.1f} и находится вне "
                f"диапазона обучения от {format_number(low)} до {format_number(high)}."
            )

    return hard_rules, range_warnings


# Рассчитывает прогноз прочности модели.
def step4_predict(model, inputs, feature_columns):
    model_input = pd.DataFrame([
        {feature: inputs[feature] for feature in feature_columns}
    ])
    return float(model.predict(model_input)[0])


# Сравнивает прогноз с технологическими границами.
def step5_compare_with_policy(prediction, interval_radius, required_strength, safety_margin):
    lower = prediction - interval_radius
    upper = prediction + interval_radius
    automatic_threshold = required_strength + safety_margin

    if upper < required_strength:
        status = "confident_fail"
        reason = (
            f"Даже максимальное ожидаемое значение {upper:.1f} МПа ниже "
            f"требования {required_strength:.1f} МПа. Состав не обеспечивает "
            "нужную прочность при заданных условиях."
        )
    elif lower >= automatic_threshold:
        status = "confident_pass"
        reason = (
            f"Даже минимальное ожидаемое значение {lower:.1f} МПа выше границы "
            f"рекомендации {automatic_threshold:.1f} МПа. Расчёт подтверждает "
            "достаточный запас прочности."
        )
    else:
        status = "uncertain"
        reason = (
            f"Ожидаемая прочность находится в диапазоне от {lower:.1f} до "
            f"{upper:.1f} МПа. Диапазон пересекает технологическую границу, "
            "поэтому результат нужно подтвердить лабораторным испытанием."
        )

    return {
        "status": status,
        "lower": lower,
        "upper": upper,
        "automatic_threshold": automatic_threshold,
        "reason": reason,
    }


# Выбирает действие по результату оценки.
def step6_choose_action(assessment):
    if assessment["status"] == "confident_pass":
        return {
            "code": "recommend_composition",
            "title": "Направить состав на производство",
            "message": (
                "Весь расчётный диапазон выше границы рекомендации. "
                "Состав можно направить на производство и провести "
                "подтверждающее лабораторное испытание."
            ),
            "severity": "success",
        }

    if assessment["status"] == "confident_fail":
        return {
            "code": "adjust_composition",
            "title": "Скорректировать состав перед отправкой на производство",
            "message": (
                "Расчёт показывает недостаточную прочность. Необходимо изменить "
                "состав и повторить оценку до отправки на производство."
            ),
            "severity": "error",
        }

    return {
        "code": "laboratory_test",
        "title": "Назначить лабораторное испытание",
        "message": (
            "Прогноз находится в пограничной области. Для решения нужен "
            "контрольный образец и лабораторное испытание."
        ),
        "severity": "warning",
    }


# Добавляет запись в журнал решений.
def step8_log(record):
    with open(LOG_PATH, "a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")


# Выполняет полный расчёт состава.
def run_pipeline(inputs, config, model, required_strength, safety_margin, composition_profile):
    st.session_state["hide_result_after_reset"] = False
    timestamp = datetime.now().isoformat(timespec="seconds")
    validation = step1_validate(inputs)

    if not validation["ok"]:
        record = {
            "timestamp": timestamp,
            "composition_profile": composition_profile,
            "input": inputs,
            "validation": validation,
            "hard_rules": [],
            "range_warnings": [],
            "action": {
                "code": "input_error",
                "title": "Исправить входные данные",
                "message": "Расчёт не выполнен, потому что в форме есть ошибки.",
                "severity": "error",
            },
            "feedback": None,
        }
        step8_log(record)
        return record

    hard_rules, range_warnings = step2_checks(inputs, config)

    if hard_rules:
        record = {
            "timestamp": timestamp,
            "composition_profile": composition_profile,
            "input": inputs,
            "validation": validation,
            "hard_rules": hard_rules,
            "range_warnings": range_warnings,
            "action": {
                "code": "data_check",
                "title": "Проверить состав и входные параметры",
                "message": (
                    "Расчёт не выполнен, потому что в составе есть физически "
                    "некорректные значения."
                ),
                "severity": "warning",
            },
            "feedback": None,
        }
        step8_log(record)
        return record

    prediction = step4_predict(model, inputs, config["feature_columns"])
    interval_radius = float(config["prediction_interval"]["radius"])

    assessment = step5_compare_with_policy(
        prediction=prediction,
        interval_radius=interval_radius,
        required_strength=required_strength,
        safety_margin=safety_margin,
    )

    action = step6_choose_action(assessment)

    record = {
        "timestamp": timestamp,
        "composition_profile": composition_profile,
        "input": inputs,
        "validation": validation,
        "hard_rules": [],
        "range_warnings": range_warnings,
        "prediction": prediction,
        "interval_radius": interval_radius,
        "required_strength": required_strength,
        "safety_margin": safety_margin,
        "assessment": assessment,
        "action": action,
        "feedback": None,
    }

    step8_log(record)
    return record


# Создаёт один состав выбранного профиля.
def sample_composition(profile_name, rng):
    composition = {}

    for feature, (low, high) in COMPOSITION_PROFILES[profile_name]["ranges"].items():
        value = low if low == high else rng.uniform(low, high)
        step = FEATURE_INFO[feature]["step"]
        composition[feature] = float(np.round(value / step) * step)

    return composition


# Подбирает состав для выбранной зоны решения.
def find_scenario_composition(model, config, required_strength, safety_margin, target_status, max_attempts=120):
    profiles_by_status = {
        "confident_fail": [
            "Состав с минеральными добавками",
            "Контроль через 7 дней",
        ],
        "uncertain": [
            "Типовая смесь для 28 дней",
            "Состав с минеральными добавками",
        ],
        "confident_pass": [
            "Смесь с повышенной прочностью",
            "Типовая смесь для 28 дней",
        ],
    }

    rng = np.random.default_rng()
    candidate_profiles = profiles_by_status[target_status]

    for profile_name in candidate_profiles:
        for _ in range(max_attempts):
            composition = sample_composition(profile_name, rng)
            prediction = step4_predict(model, composition, config["feature_columns"])

            assessment = step5_compare_with_policy(
                prediction=prediction,
                interval_radius=float(config["prediction_interval"]["radius"]),
                required_strength=required_strength,
                safety_margin=safety_margin,
            )

            if assessment["status"] == target_status:
                return composition, profile_name

    return None, None


# Создаёт пример с нулевым количеством воды.
def build_no_water_scenario():
    return {
        "CEMENT": 340.0,
        "BLAST_FURNACE_SLAG": 0.0,
        "FLY_ASH": 0.0,
        "WATER": 0.0,
        "SUPERPLASTICIZER": 5.0,
        "COARSE_AGGREGATE": 980.0,
        "FINE_AGGREGATE": 790.0,
        "AGE": 28.0,
    }


# Применяет состав и запускает расчёт.
def apply_and_calculate_scenario(composition, profile_name, model, config, required_strength, safety_margin):
    set_composition(composition)

    st.session_state.last_result = run_pipeline(
        inputs=composition,
        config=config,
        model=model,
        required_strength=required_strength,
        safety_margin=safety_margin,
        composition_profile=profile_name,
    )


# Преобразует строку в дату и время.
def parse_timestamp(value):
    try:
        return datetime.fromisoformat(value)
    except (TypeError, ValueError):
        return None


# Читает актуальные записи журнала.
def read_log():
    if not LOG_PATH.exists():
        return []

    cutoff = datetime.now() - timedelta(hours=LOG_RETENTION_HOURS)
    records = []
    rewrite_file = False

    with open(LOG_PATH, "r", encoding="utf-8") as file:
        for line in file:
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                rewrite_file = True
                continue

            timestamp = parse_timestamp(record.get("timestamp"))

            if timestamp is not None and timestamp < cutoff:
                rewrite_file = True
                continue

            records.append(record)

    if rewrite_file:
        with open(LOG_PATH, "w", encoding="utf-8") as file:
            for record in records:
                file.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")

    return records


# Сохраняет обратную связь по расчёту.
def update_feedback(timestamp, feedback):
    records = read_log()

    for record in records:
        if record.get("timestamp") == timestamp:
            record["feedback"] = feedback

    with open(LOG_PATH, "w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")


# Показывает выбранное действие.
def render_action(action):
    if action["severity"] == "success":
        st.success(f"**{action['title']}**\n\n{action['message']}")
    elif action["severity"] == "warning":
        st.warning(f"**{action['title']}**\n\n{action['message']}")
    else:
        st.error(f"**{action['title']}**\n\n{action['message']}")


# Показывает прогноз на шкале зон решения.
def render_zone_visual(required_strength, automatic_threshold, prediction, lower, upper, active_status):
    scale_min = max(0.0, min(required_strength - 15.0, lower - 5.0, prediction - 5.0))
    scale_max = max(automatic_threshold + 15.0, upper + 5.0, prediction + 5.0)

    if scale_max - scale_min < 20:
        scale_max = scale_min + 20

    fig = go.Figure()
    zone_y0, zone_y1 = 0.40, 0.60

    zones = [
        (scale_min, required_strength, "#B42318"),
        (required_strength, automatic_threshold, "#B54708"),
        (automatic_threshold, scale_max, "#067647"),
    ]

    for x0, x1, color in zones:
        fig.add_shape(
            type="rect",
            x0=x0,
            x1=x1,
            y0=zone_y0,
            y1=zone_y1,
            fillcolor=color,
            opacity=0.95,
            line_width=0,
        )

    fig.add_trace(
        go.Scatter(
            x=[lower, upper],
            y=[0.5, 0.5],
            mode="lines+markers",
            line=dict(color="#FFFFFF", width=8),
            marker=dict(color="#FFFFFF", size=8),
            hovertemplate="90% интервал<br>%{x:.1f} МПа<extra></extra>",
            showlegend=False,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[prediction],
            y=[0.5],
            mode="markers",
            marker=dict(
                color="#111827",
                size=18,
                symbol="diamond",
                line=dict(color="#FFFFFF", width=2),
            ),
            hovertemplate=f"Прогноз модели<br>{prediction:.1f} МПа<extra></extra>",
            showlegend=False,
        )
    )

    fig.add_vline(x=required_strength, line_dash="dash", line_color="#FFFFFF", line_width=2)
    fig.add_vline(x=automatic_threshold, line_dash="dash", line_color="#FFFFFF", line_width=2)

    fig.add_annotation(
        x=prediction,
        y=0.84,
        text=f"Прогноз {prediction:.1f} МПа",
        showarrow=False,
        font=dict(color="#FFFFFF", size=13),
    )

    fig.update_layout(
        height=165,
        margin=dict(l=8, r=8, t=24, b=30),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        hovermode="x",
        font=dict(color="#D1D5DB"),
    )

    fig.update_xaxes(
        title="Прочность бетона, МПа",
        range=[scale_min, scale_max],
        showgrid=False,
        zeroline=False,
        tickfont=dict(color="#D1D5DB"),
        title_font=dict(color="#D1D5DB"),
    )

    fig.update_yaxes(range=[0, 1], visible=False, fixedrange=True)

    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})

    cards = [
        {
            "key": "confident_fail",
            "title": "Красная зона",
            "range": f"Ниже {required_strength:.1f} МПа",
            "action": "Скорректировать состав смеси",
            "background": "#3A1718",
            "border": "#EF4444",
        },
        {
            "key": "uncertain",
            "title": "Жёлтая зона",
            "range": f"От {required_strength:.1f} до {automatic_threshold:.1f} МПа",
            "action": "Назначить лабораторное испытание",
            "background": "#3A2A12",
            "border": "#F59E0B",
        },
        {
            "key": "confident_pass",
            "title": "Зелёная зона",
            "range": f"От {automatic_threshold:.1f} МПа",
            "action": "Направить состав на производство",
            "background": "#133326",
            "border": "#22C55E",
        },
    ]

    columns = st.columns(3)

    for column, card in zip(columns, cards):
        is_active = card["key"] == active_status
        outline = f"3px solid {card['border']}" if is_active else "1px solid #3F4654"
        state = "Текущий результат" if is_active else "Зона решения"

        with column:
            st.markdown(
                f"""
                    <div style="
                        min-height: 138px;
                        padding: 14px 15px;
                        border-radius: 9px;
                        border: {outline};
                        background: {card['background']};
                    ">
                        <div style="
                            font-size: 12px;
                            color: #C7CEDA;
                            margin-bottom: 7px;
                        ">{state}</div>
                        <div style="
                            font-size: 18px;
                            font-weight: 700;
                            margin-bottom: 7px;
                            color: {card['border']};
                        ">{card['title']}</div>
                        <div style="font-size: 14px; margin-bottom: 8px;">
                            {card['range']}
                        </div>
                        <div style="font-size: 13px; color: #E5E7EB;">
                            {card['action']}
                        </div>
                    </div>
                    """,
                unsafe_allow_html=True,
            )

    st.caption(
        "Белая линия показывает 90% интервал. Чёрный ромб показывает точечный прогноз. "
        "Пунктирные линии отмечают требуемую прочность и границу автоматической рекомендации."
    )


# Показывает важность основных признаков.
def render_global_feature_importance():
    importance = load_global_feature_importance(str(MODEL_DIR))

    if importance.empty:
        st.caption(
            "Файл с глобальной важностью признаков AutoML не найден. "
            "После повторного обучения с explain_level=1 он появится в папке модели."
        )
        return

    display = importance.copy()
    display["Параметр"] = display["feature"].map(
        lambda feature: FEATURE_INFO.get(feature, {"short": feature})["short"]
    )

    display = display[["Параметр", "importance"]].head(3)
    display = display.rename(columns={"importance": "Важность"})

    st.write("Три параметра, которые сильнее всего учитывает итоговая модель")
    st.dataframe(display, width="stretch", hide_index=True)


# Показывает этапы выполненного расчёта.
def render_pipeline_trace(result, config):
    with st.expander("Расчёты по 8 шагам системы", expanded=True):
        st.markdown("### Шаг 1. Проверка входных данных")
        st.write(
            "Проверяются заполненность полей, числовой формат и отсутствие "
            "отрицательных значений."
        )

        input_rows = pd.DataFrame([
            {
                "Параметр": FEATURE_INFO[feature]["label"],
                "Введено": f"{float(result['input'][feature]):.1f}",
                "Статус": "корректно" if float(result["input"][feature]) >= 0 else "ошибка",
            }
            for feature in BASE_INPUT_COLUMNS
        ])

        st.dataframe(input_rows, width="stretch", hide_index=True)

        if not result["validation"]["ok"]:
            st.error("Во входных данных есть ошибки.")

            for error in result["validation"]["errors"]:
                st.write(f"• {error}")

            st.markdown("### Шаг 8. Запись результата")
            st.code(
                f"timestamp = {result['timestamp']}\nstatus = input_error",
                language="text",
            )
            return

        st.success("Входные данные прошли проверку.")

        st.markdown("### Шаг 2. Физические ограничения и область обучения")
        st.write(
            "Сначала отсекаются физически невозможные значения. Затем каждый параметр "
            "сравнивается с диапазоном обучающего набора. Выход за обучающий диапазон "
            "не останавливает расчёт, но отмечается как предупреждение."
        )

        range_rows = []

        for feature in BASE_INPUT_COLUMNS:
            stats = config["feature_stats"][feature]
            value = float(result["input"][feature])
            train_min = float(stats["min"])
            train_max = float(stats["max"])
            is_within = train_min <= value <= train_max

            range_rows.append({
                "Параметр": FEATURE_INFO[feature]["short"],
                "Введено": f"{value:.1f}",
                "Диапазон обучения": f"от {train_min:.1f} до {train_max:.1f}",
                "Статус": "в диапазоне" if is_within else "вне диапазона",
            })

        st.dataframe(pd.DataFrame(range_rows), width="stretch", hide_index=True)

        if result.get("hard_rules"):
            st.warning("Расчёт модели остановлен.")

            for rule in result["hard_rules"]:
                st.write(f"• {rule}")

            st.markdown("### Шаг 8. Запись результата")
            st.code(
                f"timestamp = {result['timestamp']}\nstatus = data_check",
                language="text",
            )
            return

        if result.get("range_warnings"):
            st.warning(
                "Расчёт выполнен с предупреждением. Часть параметров выходит "
                "за диапазон обучающих данных."
            )

            for warning in result["range_warnings"]:
                st.write(f"• {warning}")
        else:
            st.success("Параметры находятся в диапазонах обучающих данных.")

        st.markdown("### Шаг 3. Формирование входного вектора")
        st.write(
            "Формируется одна строка из восьми исходных параметров. "
            "Новые признаки и скрытые правила не добавляются."
        )

        model_input = pd.DataFrame([{
            FEATURE_INFO[feature]["short"]: result["input"][feature]
            for feature in BASE_INPUT_COLUMNS
        }])

        st.dataframe(model_input, width="stretch", hide_index=True)

        st.markdown("### Шаг 4. Расчёт прогнозной прочности")
        st.write(
            "AutoML-модель получает входной вектор и возвращает оценку прочности "
            "на сжатие к заданному возрасту образца."
        )

        prediction = float(result["prediction"])
        st.code(f"ŷ = model(X) = {prediction:.1f} МПа", language="text")
        st.success(f"Прогнозная прочность составляет {prediction:.1f} МПа.")

        st.markdown("### Шаг 5. Интервал и технологические границы")
        st.write(
            "К прогнозу добавляется радиус 90% интервала. Затем нижняя и верхняя "
            "границы сравниваются с требуемой прочностью и запасом."
        )

        radius = float(result["interval_radius"])
        lower = float(result["assessment"]["lower"])
        upper = float(result["assessment"]["upper"])
        required = float(result["required_strength"])
        margin = float(result["safety_margin"])
        automatic = float(result["assessment"]["automatic_threshold"])

        calculations = pd.DataFrame([
            {
                "Расчёт": "Нижняя граница интервала",
                "Подстановка": f"{prediction:.1f} - {radius:.1f}",
                "Результат": f"{lower:.1f} МПа",
            },
            {
                "Расчёт": "Верхняя граница интервала",
                "Подстановка": f"{prediction:.1f} + {radius:.1f}",
                "Результат": f"{upper:.1f} МПа",
            },
            {
                "Расчёт": "Граница рекомендации",
                "Подстановка": f"{required:.1f} + {margin:.1f}",
                "Результат": f"{automatic:.1f} МПа",
            },
        ])

        st.dataframe(calculations, width="stretch", hide_index=True)

        upper_below_required = upper < required
        lower_above_automatic = lower >= automatic

        checks = pd.DataFrame([
            {
                "Условие": f"{upper:.1f} < {required:.1f}",
                "Смысл": "Верхняя граница ниже требования",
                "Результат": "да" if upper_below_required else "нет",
            },
            {
                "Условие": f"{lower:.1f} ≥ {automatic:.1f}",
                "Смысл": "Нижняя граница выше границы рекомендации",
                "Результат": "да" if lower_above_automatic else "нет",
            },
        ])

        st.dataframe(checks, width="stretch", hide_index=True)
        st.success(f"Итог. {result['assessment']['reason']}")

        st.markdown("### Шаг 6. Выбор действия")
        st.write(
            "Если верхняя граница ниже требования, состав корректируется. "
            "Если нижняя граница выше требования с запасом, состав направляется "
            "на производство. В остальных случаях нужен лабораторный контроль."
        )

        if upper_below_required:
            applied_rule = "Выбрано правило. Весь расчётный диапазон ниже требования."
        elif lower_above_automatic:
            applied_rule = "Выбрано правило. Весь расчётный диапазон выше границы рекомендации."
        else:
            applied_rule = "Выбрано правило. Расчётный диапазон пересекает технологическую границу."

        st.code(applied_rule, language="text")
        st.success(f"Выбранное действие. {result['action']['title']}.")

        st.markdown("### Шаг 7. Представление результата")
        st.write(
            "На основной странице показываются прогноз, интервал, зоны решения "
            "и краткое основание для выбранного действия."
        )
        st.success("Рекомендация показана на основной странице.")

        st.markdown("### Шаг 8. Журналирование и обратная связь")
        st.write(
            "В журнал сохраняются состав смеси, прогноз, технологические границы, "
            "действие и оценка пользователя."
        )

        st.code(
            f"timestamp = {result['timestamp']}\n"
            f"action = {result['action']['code']}\n"
            f"prediction = {prediction:.1f} МПа\n"
            f"required_strength = {required:.1f} МПа",
            language="text",
        )

        st.success("Запись сохранена в журнале.")


st.set_page_config(
    page_title="Система контроля качества бетонной смеси",
    layout="wide",
    initial_sidebar_state="expanded",
)

config = load_config()

try:
    validate_config(config)
except ValueError as error:
    st.error(f"Конфигурация модели не подходит для приложения. {error}")
    st.stop()

try:
    model = load_model()
except Exception as error:
    st.error(f"Не удалось загрузить модель из {MODEL_DIR}. {error}")
    st.info("Распакуйте архив модели в папку models/.")
    st.stop()

initialise_state()

st.title("Система контроля качества бетонной смеси")
st.caption("Учебная демонстрация контура принятия решений")

st.write(
    "Технолог задаёт состав бетонной смеси и возраст образца. Модель рассчитывает "
    "ожидаемую прочность на сжатие к указанному сроку твердения. Затем приложение "
    "предлагает одно из трёх действий. Скорректировать состав, назначить "
    "лабораторное испытание или направить состав на производство."
)

with st.sidebar:
    st.header("Параметры оценки")

    st.selectbox(
        "Типовой состав",
        options=list(COMPOSITION_PROFILES),
        key="composition_profile",
        help="Типовой состав задаёт стартовые значения компонентов.",
    )

    st.caption(COMPOSITION_PROFILES[st.session_state.composition_profile]["description"])

    if st.button("Сформировать состав", width="stretch"):
        set_composition(composition_from_profile(st.session_state.composition_profile))
        st.rerun()

    if st.button("Сформировать допустимый состав", width="stretch"):
        set_composition(composition_from_training_ranges(config))
        st.rerun()

    if st.button("Сбросить все параметры", width="stretch"):
        reset_application_state()
        st.rerun()

    st.caption(
        "Сброс возвращает стартовые значения и убирает текущий результат с шагами расчёта. "
        "Журнал решений сохраняется."
    )

    st.divider()
    st.subheader("Границы решения")

    st.slider(
        "Требуемая прочность, МПа",
        min_value=10.0,
        max_value=80.0,
        step=0.5,
        key="required_strength_input",
        help="Минимальная прочность, которую состав должен обеспечить к заданному возрасту.",
        on_change=clear_last_result,
    )

    st.slider(
        "Запас для автоматической рекомендации, МПа",
        min_value=0.0,
        max_value=10.0,
        step=0.5,
        key="safety_margin_input",
        help=(
            "Чем больше запас, тем осторожнее система и тем чаще предлагает "
            "лабораторный контроль."
        ),
        on_change=clear_last_result,
    )

    required_strength_sidebar = float(st.session_state.required_strength_input)
    safety_margin_sidebar = float(st.session_state.safety_margin_input)

    st.caption(
        f"Граница автоматической рекомендации составляет "
        f"**{required_strength_sidebar + safety_margin_sidebar:.1f} МПа**."
    )

    with st.expander("Стоимость ошибок", expanded=False):
        cost_miss = st.number_input(
            "Одобрить слабую партию",
            min_value=1,
            value=50,
            step=1,
            key="cost_miss_input",
            help="Условная стоимость пропуска недостаточной прочности.",
        )

        cost_test = st.number_input(
            "Лишнее лабораторное испытание",
            min_value=1,
            value=5,
            step=1,
            key="cost_test_input",
            help="Условная стоимость дополнительной проверки нормального состава.",
        )

        ratio = cost_miss / cost_test

        st.caption(
            f"Соотношение равно 1 к {ratio:.0f}. Чем оно больше, тем разумнее "
            "увеличивать запас для автоматической рекомендации."
        )

main_tab, about_tab, journal_tab = st.tabs([
    "Оценка состава смеси",
    "Как работает система",
    "Журнал решений",
])

with main_tab:
    required_strength = float(st.session_state.required_strength_input)
    safety_margin = float(st.session_state.safety_margin_input)

    st.subheader("Учебные сценарии")
    st.write(
        "Кнопки ниже подбирают примеры по текущей модели и заданным границам. "
        "Поэтому красный, пограничный и зелёный сценарии проверяются расчётом, "
        "а не назначаются заранее."
    )

    scenario_1, scenario_2, scenario_3, scenario_4 = st.columns(4)

    # Подбирает и применяет учебный сценарий.
    def apply_target_scenario(target_status, title):
        with st.spinner("Подбираем пример по текущей модели и границам решения..."):
            composition, profile_name = find_scenario_composition(
                model=model,
                config=config,
                required_strength=required_strength,
                safety_margin=safety_margin,
                target_status=target_status,
            )

        if composition is None:
            st.warning(
                f"Не удалось подобрать пример для сценария «{title}» при текущих границах. "
                "Попробуйте изменить требуемую прочность или запас."
            )
            return

        apply_and_calculate_scenario(
            composition=composition,
            profile_name=profile_name,
            model=model,
            config=config,
            required_strength=required_strength,
            safety_margin=safety_margin,
        )

    with scenario_1:
        if st.button("Показать красную зону", width="stretch"):
            apply_target_scenario("confident_fail", "красная зона")

    with scenario_2:
        if st.button("Показать пограничный случай", width="stretch"):
            apply_target_scenario("uncertain", "пограничный случай")

    with scenario_3:
        if st.button("Показать зелёную зону", width="stretch"):
            apply_target_scenario("confident_pass", "зелёная зона")

    with scenario_4:
        if st.button("Показать ошибку ввода", width="stretch"):
            invalid_composition = build_no_water_scenario()

            apply_and_calculate_scenario(
                composition=invalid_composition,
                profile_name="Ошибка ввода, вода равна 0",
                model=model,
                config=config,
                required_strength=required_strength,
                safety_margin=safety_margin,
            )

    st.divider()
    st.subheader("Состав смеси")

    with st.expander("Изменить состав смеси вручную", expanded=False):
        left_column, right_column = st.columns(2)

        with left_column:
            st.markdown("**Вяжущие материалы и добавки**")

            for feature in ["CEMENT", "BLAST_FURNACE_SLAG", "FLY_ASH", "SUPERPLASTICIZER"]:
                min_value, max_value = slider_bounds(feature, config)

                st.slider(
                    FEATURE_INFO[feature]["label"],
                    min_value=float(min_value),
                    max_value=float(max_value),
                    step=float(FEATURE_INFO[feature]["step"]),
                    key=f"input_{feature}",
                    help=FEATURE_INFO[feature]["help"],
                    on_change=clear_last_result,
                )

        with right_column:
            st.markdown("**Вода, заполнители и срок твердения**")

            for feature in ["WATER", "COARSE_AGGREGATE", "FINE_AGGREGATE", "AGE"]:
                min_value, max_value = slider_bounds(feature, config)

                st.slider(
                    FEATURE_INFO[feature]["label"],
                    min_value=float(min_value),
                    max_value=float(max_value),
                    step=float(FEATURE_INFO[feature]["step"]),
                    key=f"input_{feature}",
                    help=FEATURE_INFO[feature]["help"],
                    on_change=clear_last_result,
                )

    current_inputs = get_inputs_from_state()

    preview_left, preview_right = st.columns([2, 1])

    with preview_left:
        composition_table = pd.DataFrame([
            {
                "Компонент": FEATURE_INFO[feature]["label"],
                "Значение": f"{current_inputs[feature]:.1f}",
            }
            for feature in BASE_INPUT_COLUMNS
        ])

        st.dataframe(composition_table, width="stretch", hide_index=True, height=280)

    with preview_right:
        st.metric("Требуемая прочность", f"{required_strength:.1f} МПа")
        st.metric("Граница рекомендации", f"{required_strength + safety_margin:.1f} МПа")

        st.caption(
            "При пересечении границы прогнозным интервалом выбирается "
            "лабораторное испытание."
        )

    if st.button("Рассчитать прогноз прочности", type="primary", width="stretch"):
        st.session_state.last_result = run_pipeline(
            inputs=current_inputs,
            config=config,
            model=model,
            required_strength=required_strength,
            safety_margin=safety_margin,
            composition_profile=st.session_state.composition_profile,
        )
        st.rerun()

    result = st.session_state.get("last_result")

    if result is not None:
        st.divider()
        st.subheader("Результат оценки")

        if "prediction" in result:
            metric_1, metric_2, metric_3, metric_4 = st.columns(4)

            metric_1.metric("Прогнозная прочность", f"{result['prediction']:.1f} МПа")

            metric_2.metric(
                "90% интервал",
                f"{result['assessment']['lower']:.1f}–{result['assessment']['upper']:.1f} МПа",
            )

            metric_3.metric("Требование", f"{result['required_strength']:.1f} МПа")

            metric_4.metric(
                "Граница рекомендации",
                f"{result['assessment']['automatic_threshold']:.1f} МПа",
            )

            render_zone_visual(
                required_strength=float(result["required_strength"]),
                automatic_threshold=float(result["assessment"]["automatic_threshold"]),
                prediction=float(result["prediction"]),
                lower=float(result["assessment"]["lower"]),
                upper=float(result["assessment"]["upper"]),
                active_status=result["assessment"]["status"],
            )

            if result.get("range_warnings"):
                st.warning(
                    "Часть параметров выходит за диапазон обучения. Прогноз рассчитан, "
                    "но его следует трактовать осторожнее."
                )

        render_action(result["action"])

        if "prediction" in result:
            with st.expander("Основание для решения", expanded=True):
                st.write(result["assessment"]["reason"])

                st.caption(
                    "Модель рассчитывает прочность, а технологические границы "
                    "переводят этот расчёт в действие."
                )

        render_pipeline_trace(result, config)

        feedback_left, feedback_right, _ = st.columns([1, 1, 4])

        with feedback_left:
            if st.button("Рекомендация полезна", key="feedback_yes", width="stretch"):
                update_feedback(result["timestamp"], "useful")
                st.toast("Оценка сохранена в журнале")

        with feedback_right:
            if st.button("Нужна корректировка", key="feedback_no", width="stretch"):
                update_feedback(result["timestamp"], "needs_review")
                st.toast("Оценка сохранена в журнале")

with about_tab:
    st.subheader("Как работает система")

    st.write(
        "Технолог задаёт состав бетонной смеси и возраст образца. Модель оценивает "
        "ожидаемую прочность на сжатие к выбранному сроку твердения. Затем результат "
        "сравнивается с требованием проекта, и приложение предлагает дальнейшее действие."
    )

    st.caption(
        "Это задача регрессии. Модель выдаёт числовой прогноз в МПа, "
        "а не только ответ о соответствии состава требованию."
    )

    metrics = config.get("test_metrics", {})
    metric_1, metric_2, metric_3, metric_4 = st.columns(4)

    metric_1.metric("Средняя ошибка MAE", f"{metrics.get('mae', 0):.2f} МПа")
    metric_2.metric("Ошибка RMSE", f"{metrics.get('rmse', 0):.2f} МПа")
    metric_3.metric("Качество R²", f"{metrics.get('r2', 0):.3f}")
    metric_4.metric(
        "Попадание в 90% интервал",
        f"{100 * metrics.get('interval_coverage', 0):.1f}%",
    )

    st.caption(
        "MAE и RMSE показывают, насколько прогноз в среднем отличается от измерения. "
        "R² показывает, какую часть различий в прочности объясняет модель."
    )

    st.divider()
    st.subheader("Данные для обучения")

    st.write(
        "Для обучения использован открытый набор Concrete Compressive Strength "
        "из UCI Machine Learning Repository. В нём собраны результаты испытаний "
        "1 030 бетонных образцов. Для каждого образца известны компоненты смеси, "
        "возраст и измеренная прочность на сжатие."
    )

    data_left, data_right = st.columns(2)

    with data_left:
        st.metric("Образцов", "1 030")
        st.metric("Что прогнозируем", "Прочность в МПа")

    with data_right:
        st.metric("Параметров на входе", "8")
        st.metric("Тип задачи", "Регрессия")

    st.markdown(
        """
| Параметр | Простое объяснение |
| --- | --- |
| Цемент | Основное вяжущее вещество |
| Доменный шлак | Минеральная добавка, которая может заменить часть цемента |
| Зола уноса | Минеральная добавка |
| Вода | Вода для приготовления смеси |
| Суперпластификатор | Добавка для регулирования подвижности смеси |
| Щебень | Крупный заполнитель |
| Песок | Мелкий заполнитель |
| Возраст | Сколько дней твердел образец |
| Прочность на сжатие | Значение, которое нужно предсказать |
        """
    )

    st.caption(
        "Источник данных. UCI Machine Learning Repository, "
        "Concrete Compressive Strength Data Set, I-Cheng Yeh, 1998."
    )

    st.divider()
    st.subheader("Как получается прогноз")

    st.write(
        "Прочность зависит от сочетания всех компонентов и срока твердения. "
        "Например, одинаковое количество цемента может дать разную прочность "
        "при разном количестве воды или добавок. Модель рассматривает эти "
        "параметры вместе и оценивает ожидаемый результат."
    )

    with st.expander("Какие параметры важнее для модели", expanded=True):
        render_global_feature_importance()

    st.divider()
    st.subheader("Как понимать результат")

    st.write(
        "После расчёта показывается прогнозная прочность и диапазон возможных значений. "
        "Диапазон нужен потому, что модель не может предсказать результат без ошибки. "
        "Нижняя граница соответствует более осторожной оценке, верхняя показывает "
        "более благоприятный вариант."
    )

    with st.expander("Почему рядом с прогнозом есть интервал", expanded=False):
        coverage = 100 * float(metrics.get("interval_coverage", 0))

        st.write(
            "Ширина интервала рассчитана по ошибкам модели на проверочных данных. "
            f"На отдельной тестовой части фактическая прочность попадала в интервал "
            f"в {coverage:.1f}% случаев. Это близко к заявленному уровню 90%."
        )

    st.divider()
    st.subheader("Как выбирается действие")

    st.write(
        "При выборе действия учитывается весь диапазон возможной прочности. "
        "Центрального прогноза недостаточно, потому что он может находиться рядом "
        "с требуемым значением. Такой подход снижает риск принять решение только "
        "по одной числовой оценке."
    )

    st.markdown(
        """
| Положение расчётного диапазона | Что это означает | Дальнейшее действие |
| --- | --- | --- |
| Весь диапазон ниже требуемой прочности | Даже благоприятная оценка не подтверждает соответствие требованию | Скорректировать состав перед отправкой на производство |
| Весь диапазон выше требования и заданного запаса | Даже осторожная оценка подтверждает достаточный запас прочности | Направить состав на производство и провести лабораторное испытание |
| Диапазон пересекает требование или границу рекомендации | Результат находится рядом с технологической границей | Провести лабораторное испытание |
        """
    )

    st.caption(
        "Требуемую прочность и запас задают в левой панели. Модель оценивает "
        "прочность, а границы переводят расчёт в технологическое действие."
    )

    st.divider()
    st.subheader("Что нужно учитывать")

    with st.expander("Модель не видит фактическую прочность заранее", expanded=False):
        st.write(
            "До испытания известны только состав смеси и возраст образца. "
            "Измеренная прочность появляется после испытания и не передаётся в модель. "
            "Поэтому при расчёте не используется готовый ответ."
        )

    with st.expander("Когда результат менее надёжен", expanded=False):
        st.write(
            "Модель училась на 1 030 составах из набора данных. Если пользователь "
            "задаёт значение, которого среди обучающих примеров не было, расчёт "
            "выполняется с предупреждением. В такой ситуации модель работает "
            "за пределами знакомых ей данных, поэтому результат нужно трактовать осторожнее."
        )

    with st.expander("Почему цена ошибок имеет значение", expanded=False):
        cost_miss_value = int(st.session_state.get("cost_miss_input", 50))
        cost_test_value = int(st.session_state.get("cost_test_input", 5))
        ratio = cost_miss_value / cost_test_value

        st.write(
            f"Сейчас в левой панели соотношение равно 1 к {ratio:.0f}. "
            "Это означает, что пропуск недостаточной прочности считается дороже, "
            "чем дополнительное лабораторное испытание. Пока это соотношение "
            "служит учебной иллюстрацией и не меняет выбор действия автоматически."
        )

    with st.expander("Почему модель проверяют на новых данных", expanded=False):
        st.write(
            "На реальном производстве могут меняться материалы, дозировки, "
            "оборудование и условия твердения. Тогда новые составы отличаются "
            "от данных, на которых училась модель. Поэтому её нужно сверять "
            "со свежими результатами испытаний и при необходимости переобучать."
        )

    st.divider()
    st.subheader("Ограничения")

    st.write(
        "Набор данных небольшой, поэтому приложение подходит для учебной "
        "демонстрации и предварительной оценки. В расчёте не учитываются "
        "температура и влажность твердения, марка цемента, тонкость помола "
        "и особенности конкретного производства."
    )

    st.write(
        "Рекомендация не заменяет производственный контроль и подтверждающее "
        "лабораторное испытание. Границы решения задаёт пользователь. Они "
        "отражают выбранный подход к контролю качества, а не вывод самой модели."
    )

with journal_tab:
    st.subheader("Журнал решений за последние 24 часа")

    st.caption(
        "Это общий демонстрационный журнал для текущего запуска приложения. "
        "Записи могут исчезнуть после перезапуска или обновления хостинга. "
        "Не используйте его как персональное или постоянное хранилище."
    )

    st.caption(
        "В производственной системе к таким записям обычно добавляют номер партии, "
        "ответственного технолога и фактический результат испытания."
    )

    records = read_log()

    if not records:
        st.info("Журнал пока пуст.")
    else:
        log_rows = []

        for record in records:
            action = record.get("action", {})

            log_rows.append({
                "Время": record.get("timestamp"),
                "Типовой состав": record.get("composition_profile", "нет данных"),
                "Прогноз, МПа": record.get("prediction"),
                "Требование, МПа": record.get("required_strength"),
                "Запас, МПа": record.get("safety_margin"),
                "Действие": action.get("title", "нет данных"),
                "Обратная связь": record.get("feedback"),
            })

        log_df = pd.DataFrame(log_rows)
        total = len(log_df)

        lab_count = int(
            (log_df["Действие"] == "Назначить лабораторное испытание").sum()
        )

        adjust_count = int(
            (log_df["Действие"] == "Скорректировать состав перед отправкой на производство").sum()
        )

        feedback_count = int(log_df["Обратная связь"].notna().sum())

        stat_1, stat_2, stat_3, stat_4 = st.columns(4)

        stat_1.metric("Всего расчётов", total)
        stat_2.metric("Лабораторный контроль", lab_count)
        stat_3.metric("Корректировка состава", adjust_count)
        stat_4.metric("Есть обратная связь", f"{feedback_count} из {total}")

        st.dataframe(log_df.iloc[::-1], width="stretch", hide_index=True, height=360)

        st.download_button(
            "Скачать журнал",
            data=LOG_PATH.read_bytes(),
            file_name="concrete_decisions.jsonl",
            mime="application/x-ndjson",
        )