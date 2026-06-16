# Summary of 64_Xgboost_GoldenFeatures

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.1
- **max_depth**: 6
- **min_child_weight**: 1
- **subsample**: 1.0
- **colsample_bytree**: 1.0
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

18.7 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.965116 |     0.991138 |             0.9      |        0.815789 |                   0 |   0.988375 |    0.734409 |       0.983948 | 0.0455716 |
| recall    |                   0.902174 |     0.997544 |             0.725806 |        0.849315 |                   0 |   0.988375 |    0.694968 |       0.988375 | 0.0455716 |
| f1-score  |                   0.932584 |     0.994331 |             0.803571 |        0.832215 |                   0 |   0.988375 |    0.71254  |       0.986064 | 0.0455716 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.988375 | 8000        |    8000        | 0.0455716 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      83 |                         7 |                                 1 |                            1 |                                0 |
| Labeled as No_Failure               |                                       2 |                      7717 |                                 3 |                           12 |                                2 |
| Labeled as Overstrain_Failure       |                                       1 |                        16 |                                45 |                            0 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        11 |                                 0 |                           62 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        35 |                                 1 |                            1 |                                0 |

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
