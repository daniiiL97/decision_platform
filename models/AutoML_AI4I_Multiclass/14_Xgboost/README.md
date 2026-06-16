# Summary of 14_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.1
- **max_depth**: 8
- **min_child_weight**: 1
- **subsample**: 0.6
- **colsample_bytree**: 0.5
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

18.4 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.952381 |     0.984182 |             0.767442 |        0.679245 |           0.5       |   0.980625 |    0.77665  |       0.977114 | 0.0622356 |
| recall    |                   0.652174 |     0.997285 |             0.532258 |        0.493151 |           0.027027  |   0.980625 |    0.540379 |       0.980625 | 0.0622356 |
| f1-score  |                   0.774194 |     0.99069  |             0.628571 |        0.571429 |           0.0512821 |   0.980625 |    0.603233 |       0.977224 | 0.0622356 |
| support   |                  92        |  7736        |            62        |       73        |          37         |   0.980625 | 8000        |    8000        | 0.0622356 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      60 |                        28 |                                 3 |                            1 |                                0 |
| Labeled as No_Failure               |                                       3 |                      7715 |                                 2 |                           15 |                                1 |
| Labeled as Overstrain_Failure       |                                       0 |                        28 |                                33 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        33 |                                 4 |                           36 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        35 |                                 1 |                            0 |                                1 |

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
