# Summary of 2_Default_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.075
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

10.0 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.988372 |     0.990243 |             0.824561 |        0.738462 |                   0 |   0.986625 |    0.708328 |       0.98206  | 0.0484147 |
| recall    |                   0.923913 |     0.997027 |             0.758065 |        0.657534 |                   0 |   0.986625 |    0.667308 |       0.986625 | 0.0484147 |
| f1-score  |                   0.955056 |     0.993623 |             0.789916 |        0.695652 |                   0 |   0.986625 |    0.68685  |       0.984286 | 0.0484147 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.986625 | 8000        |    8000        | 0.0484147 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      85 |                         6 |                                 0 |                            1 |                                0 |
| Labeled as No_Failure               |                                       1 |                      7713 |                                 4 |                           15 |                                3 |
| Labeled as Overstrain_Failure       |                                       0 |                        14 |                                47 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        21 |                                 4 |                           48 |                                0 |
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
