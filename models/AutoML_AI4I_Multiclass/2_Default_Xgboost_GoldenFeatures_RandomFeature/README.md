# Summary of 2_Default_Xgboost_GoldenFeatures_RandomFeature

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
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True
 - **random_seed**: 42

## Optimized metric
logloss

## Training time

20.3 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.977273 |     0.991387 |             0.87234  |        0.783133 |                   0 |      0.988 |    0.724827 |       0.983817 | 0.0448882 |
| recall    |                   0.934783 |     0.996898 |             0.66129  |        0.890411 |                   0 |      0.988 |    0.696676 |       0.988    | 0.0448882 |
| f1-score  |                   0.955556 |     0.994135 |             0.752294 |        0.833333 |                   0 |      0.988 |    0.707063 |       0.985752 | 0.0448882 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |      0.988 | 8000        |    8000        | 0.0448882 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      86 |                         5 |                                 0 |                            1 |                                0 |
| Labeled as No_Failure               |                                       1 |                      7712 |                                 5 |                           16 |                                2 |
| Labeled as Overstrain_Failure       |                                       1 |                        19 |                                41 |                            0 |                                1 |
| Labeled as Power_Failure            |                                       0 |                         8 |                                 0 |                           65 |                                0 |
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
