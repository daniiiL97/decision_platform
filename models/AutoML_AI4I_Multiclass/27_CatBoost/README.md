# Summary of 27_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 5
- **rsm**: 0.7
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

44.5 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.933333 |     0.988347 |             0.759259 |        0.79661  |                   0 |     0.9845 |    0.69551  |       0.979618 | 0.0505848 |
| recall    |                   0.76087  |     0.997673 |             0.66129  |        0.643836 |                   0 |     0.9845 |    0.612734 |       0.9845   | 0.0505848 |
| f1-score  |                   0.838323 |     0.992988 |             0.706897 |        0.712121 |                   0 |     0.9845 |    0.650066 |       0.981837 | 0.0505848 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |     0.9845 | 8000        |    8000        | 0.0505848 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      70 |                        17 |                                 3 |                            2 |                                0 |
| Labeled as No_Failure               |                                       3 |                      7718 |                                 3 |                            9 |                                3 |
| Labeled as Overstrain_Failure       |                                       1 |                        19 |                                41 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       1 |                        20 |                                 5 |                           47 |                                0 |
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
