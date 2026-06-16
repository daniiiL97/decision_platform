# Summary of 2_Default_Xgboost_GoldenFeatures_SelectedFeatures_BoostOnErrors

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

20.8 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.976744 |     0.99165  |             0.884615 |        0.842105 |                   0 |   0.989125 |    0.739023 |       0.984698 | 0.0434571 |
| recall    |                   0.913043 |     0.997802 |             0.741935 |        0.876712 |                   0 |   0.989125 |    0.705899 |       0.989125 | 0.0434571 |
| f1-score  |                   0.94382  |     0.994716 |             0.807018 |        0.85906  |                   0 |   0.989125 |    0.720923 |       0.986838 | 0.0434571 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.989125 | 8000        |    8000        | 0.0434571 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      84 |                         5 |                                 1 |                            2 |                                0 |
| Labeled as No_Failure               |                                       2 |                      7719 |                                 4 |                            9 |                                2 |
| Labeled as Overstrain_Failure       |                                       0 |                        16 |                                46 |                            0 |                                0 |
| Labeled as Power_Failure            |                                       0 |                         9 |                                 0 |                           64 |                                0 |
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
