# Summary of 31_CatBoost_SelectedFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
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

50.4 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.946667 |     0.988098 |             0.759259 |        0.807018 |                   0 |   0.984875 |    0.700208 |       0.979626 | 0.0502476 |
| recall    |                   0.771739 |     0.998061 |             0.66129  |        0.630137 |                   0 |   0.984875 |    0.612245 |       0.984875 | 0.0502476 |
| f1-score  |                   0.850299 |     0.993055 |             0.706897 |        0.707692 |                   0 |   0.984875 |    0.651589 |       0.981998 | 0.0502476 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.984875 | 8000        |    8000        | 0.0502476 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      71 |                        16 |                                 3 |                            2 |                                0 |
| Labeled as No_Failure               |                                       4 |                      7721 |                                 3 |                            8 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        20 |                                41 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        22 |                                 5 |                           46 |                                0 |
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
