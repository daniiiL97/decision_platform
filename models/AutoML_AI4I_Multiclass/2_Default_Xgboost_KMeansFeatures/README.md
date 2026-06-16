# Summary of 2_Default_Xgboost_KMeansFeatures

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

18.6 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.954545 |     0.989996 |             0.796296 |        0.827586 |            0.333333 |   0.986875 |    0.780351 |       0.983568 | 0.0493753 |
| recall    |                   0.913043 |     0.997802 |             0.693548 |        0.657534 |            0.027027 |   0.986875 |    0.657791 |       0.986875 | 0.0493753 |
| f1-score  |                   0.933333 |     0.993884 |             0.741379 |        0.732824 |            0.05     |   0.986875 |    0.690284 |       0.984483 | 0.0493753 |
| support   |                  92        |  7736        |            62        |       73        |           37        |   0.986875 | 8000        |    8000        | 0.0493753 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      84 |                         7 |                                 0 |                            1 |                                0 |
| Labeled as No_Failure               |                                       4 |                      7719 |                                 4 |                            7 |                                2 |
| Labeled as Overstrain_Failure       |                                       0 |                        17 |                                43 |                            2 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        20 |                                 5 |                           48 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        34 |                                 2 |                            0 |                                1 |

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
