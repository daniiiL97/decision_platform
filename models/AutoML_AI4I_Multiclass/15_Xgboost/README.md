# Summary of 15_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.05
- **max_depth**: 6
- **min_child_weight**: 10
- **subsample**: 0.6
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

25.7 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.923077 |     0.983665 |             0.647059 |        0.577778 |                   0 |   0.978375 |    0.626316 |       0.972106 | 0.0601525 |
| recall    |                   0.652174 |     0.996381 |             0.532258 |        0.356164 |                   0 |   0.978375 |    0.507395 |       0.978375 | 0.0601525 |
| f1-score  |                   0.764331 |     0.989982 |             0.584071 |        0.440678 |                   0 |   0.978375 |    0.555812 |       0.97465  | 0.0601525 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.978375 | 8000        |    8000        | 0.0601525 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      60 |                        28 |                                 4 |                            0 |                                0 |
| Labeled as No_Failure               |                                       4 |                      7708 |                                 6 |                           15 |                                3 |
| Labeled as Overstrain_Failure       |                                       1 |                        24 |                                33 |                            4 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        41 |                                 6 |                           26 |                                0 |
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
