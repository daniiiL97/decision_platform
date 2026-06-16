# Summary of 71_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 6
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

51.9 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.958904 |     0.988222 |             0.740741 |        0.786885 |                   0 |   0.984625 |    0.69495  |       0.979559 |  0.050521 |
| recall    |                   0.76087  |     0.997802 |             0.645161 |        0.657534 |                   0 |   0.984625 |    0.612274 |       0.984625 |  0.050521 |
| f1-score  |                   0.848485 |     0.992989 |             0.689655 |        0.716418 |                   0 |   0.984625 |    0.649509 |       0.98186  |  0.050521 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.984625 | 8000        |    8000        |  0.050521 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      70 |                        16 |                                 4 |                            2 |                                0 |
| Labeled as No_Failure               |                                       3 |                      7719 |                                 3 |                           10 |                                1 |
| Labeled as Overstrain_Failure       |                                       0 |                        21 |                                40 |                            1 |                                0 |
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
