# Summary of 78_CatBoost_SelectedFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.15
- **depth**: 5
- **rsm**: 0.8
- **loss_function**: MultiClass
- **eval_metric**: MultiClass
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

38.3 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.902778 |     0.987964 |             0.754386 |        0.813559 |                   0 |      0.984 |    0.691737 |       0.979013 | 0.0500926 |
| recall    |                   0.706522 |     0.997415 |             0.693548 |        0.657534 |                   0 |      0.984 |    0.611004 |       0.984    | 0.0500926 |
| f1-score  |                   0.792683 |     0.992667 |             0.722689 |        0.727273 |                   0 |      0.984 |    0.647062 |       0.981262 | 0.0500926 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |      0.984 | 8000        |    8000        | 0.0500926 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      65 |                        21 |                                 4 |                            2 |                                0 |
| Labeled as No_Failure               |                                       6 |                      7716 |                                 3 |                            9 |                                2 |
| Labeled as Overstrain_Failure       |                                       1 |                        18 |                                43 |                            0 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        20 |                                 5 |                           48 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        35 |                                 2 |                            0 |                                0 |

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
