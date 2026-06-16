# Summary of 29_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 5
- **rsm**: 0.9
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

47.8 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.942857 |     0.987457 |             0.732143 |        0.762712 |                   0 |   0.983375 |    0.685034 |       0.978347 | 0.0510823 |
| recall    |                   0.717391 |     0.997285 |             0.66129  |        0.616438 |                   0 |   0.983375 |    0.598481 |       0.983375 | 0.0510823 |
| f1-score  |                   0.814815 |     0.992347 |             0.694915 |        0.681818 |                   0 |   0.983375 |    0.636779 |       0.980577 | 0.0510823 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.983375 | 8000        |    8000        | 0.0510823 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      66 |                        20 |                                 4 |                            2 |                                0 |
| Labeled as No_Failure               |                                       4 |                      7715 |                                 4 |                           11 |                                2 |
| Labeled as Overstrain_Failure       |                                       0 |                        20 |                                41 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        23 |                                 5 |                           45 |                                0 |
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
