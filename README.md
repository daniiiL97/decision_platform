# Decision Platform

Проект выполнен в рамках курса «Интеллектуальные платформы и автоматизация принятия решений».

Репозиторий содержит контур принятия решений для задачи предиктивного обслуживания фрезерного станка. Система получает параметры оборудования, проверяет входные значения, применяет правила, вызывает ML модель, определяет зону решения и сохраняет результат в журнал.

В качестве данных используется [AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset) из UCI Machine Learning Repository.

## Disclaimer

В проекте используются синтетические данные.

Пороги правил заданы вручную.

Модель обучена с помощью [mljar-supervised](https://supervised.mljar.com/).

Для запуска приложения требуется распакованная модель в папке `models`.

## Getting Started

Требования

* Python 3.10, 3.11 или 3.12
* pip
* распакованная модель в папке `models`

```bash id="r4vmk9"
git clone https://github.com/daniiiL97/decision_platform.git
cd decision_platform

python -m venv .venv
.venv\Scripts\activate
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

После запуска приложение доступно на локальном порте `8501`.

Если модель отсутствует, её нужно обучить в ноутбуке, скачать архив и распаковать в папку

```text id="1671or"
models/AutoML_AI4I_Multiclass/
```

## Usage

В приложении есть четыре раздела.

| Раздел         | Содержание                              |
| -------------- | --------------------------------------- |
| Контур решения | запуск pipeline и проверка сценариев    |
| Пороги и зоны  | правила, пороги и зоны решений          |
| Мониторинг     | журнал решений, feedback и health check |
| О системе      | архитектура, метрики и ограничения      |

В основном сценарии доступны генераторы входных параметров.

```text id="wteior"
Нет отказа
Перегрев
Отказ по мощности
Перегрузка по моменту
Износ инструмента
```

После генерации значения можно изменить вручную и повторно запустить контур.

## How It Works

Контур состоит из 8 шагов.

| Шаг | Описание                                              |
| --- | ----------------------------------------------------- |
| 1   | Проверка входных данных                               |
| 2   | Ранние правила до модели                              |
| 3   | Инженерия признаков                                   |
| 4   | Предсказание ML модели                                |
| 5   | Проверка порогов, поздних правил и физических условий |
| 6   | Применение бизнес логики                              |
| 7   | Выбор финального действия                             |
| 8   | Запись результата и обратной связи                    |

Модель возвращает класс отказа и вероятности по классам. После этого результат проходит через правила и пороги.

Зоны решений

| Зона           | Условие                                    |
| -------------- | ------------------------------------------ |
| auto           | уверенность модели выше верхнего порога    |
| recommendation | уверенность между нижним и верхним порогом |
| manual         | уверенность ниже нижнего порога            |

Если физические правила находят риск, автоматическое продолжение работы блокируется.

## Model

Используется датасет [AI4I 2020 Predictive Maintenance](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset).

Классы модели

* No Failure
* Heat Dissipation Failure
* Power Failure
* Overstrain Failure
* Tool Wear Failure
* Random Failure

Обучение выполнено через [mljar-supervised](https://github.com/mljar/mljar-supervised) в режиме `Compete`.

Лучшая модель

```text id="hfxwu1"
Ensemble_Stacked
```

Метрики на тестовой выборке

| Метрика           | Значение |
| ----------------- | -------- |
| F1 macro          | 0.7117   |
| Balanced accuracy | 0.7454   |
| Log loss          | 0.0373   |
| ROC AUC OvR macro | 0.9914   |

Для редких классов используются дополнительные проверки. Они учитывают износ инструмента, мощность, температуру, момент и противоречия между физическими признаками и результатом модели.

## Project Structure

```text id="6b0629"
decision_platform/
├── app.py
├── requirements.txt
├── models/
│   ├── AutoML_AI4I_Multiclass/
│   └── config.json
└── logs/
    └── decisions.jsonl
```

Основные функции в `app.py`

| Функция                  | Назначение                        |
| ------------------------ | --------------------------------- |
| `step1_validate`         | проверка входных данных           |
| `step2_early_rules`      | ранние правила                    |
| `step4_predict`          | вызов модели                      |
| `step5_apply_thresholds` | определение зоны решения          |
| `step5_late_rules`       | поздние правила                   |
| `step5_physics_rules`    | физические проверки               |
| `has_risk_signals`       | блокировка авто решения при риске |
| `step6_business_logic`   | выбор действия                    |
| `step8_log`              | запись в журнал                   |
| `update_feedback`        | сохранение обратной связи         |
| `run_pipeline`           | запуск контура                    |

## References

* [AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset)
* [mljar-supervised documentation](https://supervised.mljar.com/)
* [mljar-supervised GitHub](https://github.com/mljar/mljar-supervised)
* [Streamlit documentation](https://docs.streamlit.io/)

## License

MIT
