# Summary of 9_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.05
- **max_depth**: 9
- **min_child_weight**: 10
- **subsample**: 0.8
- **colsample_bytree**: 0.6
- **eval_metric**: mlogloss
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

23.0 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.918919 |     0.985422 |             0.708333 |        0.62963  |                   0 |    0.98025 |    0.648461 |       0.974706 | 0.0567511 |
| recall    |                   0.73913  |     0.996122 |             0.548387 |        0.465753 |                   0 |    0.98025 |    0.549879 |       0.98025  | 0.0567511 |
| f1-score  |                   0.819277 |     0.990743 |             0.618182 |        0.535433 |                   0 |    0.98025 |    0.592727 |       0.977147 | 0.0567511 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |    0.98025 | 8000        |    8000        | 0.0567511 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      68 |                        20 |                                 3 |                            1 |                                0 |
| Labeled as No_Failure               |                                       5 |                      7706 |                                 4 |                           17 |                                4 |
| Labeled as Overstrain_Failure       |                                       1 |                        25 |                                34 |                            2 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        34 |                                 5 |                           34 |                                0 |
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
