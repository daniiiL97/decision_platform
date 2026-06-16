# Summary of 3_Default_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.15
- **depth**: 5
- **rsm**: 1
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

40.3 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.918919 |     0.987711 |             0.740741 |        0.79661  |                   0 |   0.983875 |    0.688796 |       0.978694 | 0.0512897 |
| recall    |                   0.73913  |     0.997415 |             0.645161 |        0.643836 |                   0 |   0.983875 |    0.605108 |       0.983875 | 0.0512897 |
| f1-score  |                   0.819277 |     0.992539 |             0.689655 |        0.712121 |                   0 |   0.983875 |    0.642719 |       0.98105  | 0.0512897 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.983875 | 8000        |    8000        | 0.0512897 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      68 |                        19 |                                 3 |                            2 |                                0 |
| Labeled as No_Failure               |                                       6 |                      7716 |                                 4 |                            9 |                                1 |
| Labeled as Overstrain_Failure       |                                       0 |                        21 |                                40 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        21 |                                 5 |                           47 |                                0 |
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
