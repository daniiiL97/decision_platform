# Summary of 18_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 31
- **learning_rate**: 0.05
- **feature_fraction**: 0.9
- **bagging_fraction**: 0.9
- **min_data_in_leaf**: 20
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

12.8 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.962025 |     0.988728 |             0.804348 |        0.796875 |           0.25      |     0.9855 |    0.760395 |       0.981825 | 0.0537248 |
| recall    |                   0.826087 |     0.997802 |             0.596774 |        0.69863  |           0.027027  |     0.9855 |    0.629264 |       0.9855   | 0.0537248 |
| f1-score  |                   0.888889 |     0.993245 |             0.685185 |        0.744526 |           0.0487805 |     0.9855 |    0.672125 |       0.983019 | 0.0537248 |
| support   |                  92        |  7736        |            62        |       73        |          37         |     0.9855 | 8000        |    8000        | 0.0537248 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      76 |                        14 |                                 2 |                            0 |                                0 |
| Labeled as No_Failure               |                                       3 |                      7719 |                                 2 |                           10 |                                2 |
| Labeled as Overstrain_Failure       |                                       0 |                        22 |                                37 |                            3 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        18 |                                 3 |                           51 |                                1 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        34 |                                 2 |                            0 |                                1 |

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
