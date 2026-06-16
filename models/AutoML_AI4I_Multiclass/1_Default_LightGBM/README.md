# Summary of 1_Default_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 63
- **learning_rate**: 0.05
- **feature_fraction**: 0.9
- **bagging_fraction**: 0.9
- **min_data_in_leaf**: 10
- **metric**: multi_logloss
- **custom_eval_metric_name**: None
- **num_class**: 5
- **explain_level**: 2

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True
 - **random_seed**: 42

## Optimized metric
logloss

## Training time

40.4 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.95     |     0.985587 |             0.9      |        0.829787 |            0.333333 |    0.98375 |    0.799741 |       0.980076 | 0.0631967 |
| recall    |                   0.826087 |     0.998837 |             0.435484 |        0.534247 |            0.027027 |    0.98375 |    0.564336 |       0.98375  | 0.0631967 |
| f1-score  |                   0.883721 |     0.992167 |             0.586957 |        0.65     |            0.05     |    0.98375 |    0.632569 |       0.9803   | 0.0631967 |
| support   |                  92        |  7736        |            62        |       73        |           37        |    0.98375 | 8000        |    8000        | 0.0631967 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      76 |                        16 |                                 0 |                            0 |                                0 |
| Labeled as No_Failure               |                                       2 |                      7727 |                                 0 |                            6 |                                1 |
| Labeled as Overstrain_Failure       |                                       2 |                        32 |                                27 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        31 |                                 2 |                           39 |                                1 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        34 |                                 1 |                            1 |                                1 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Precision Recall Curve

![Precision Recall Curve](precision_recall_curve.png)



[<< Go back](../README.md)
