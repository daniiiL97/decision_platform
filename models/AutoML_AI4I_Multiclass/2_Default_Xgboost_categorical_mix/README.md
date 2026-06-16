# Summary of 2_Default_Xgboost_categorical_mix

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

21.1 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.988506 |     0.990245 |             0.867925 |        0.727273 |            0.333333 |      0.987 |    0.781456 |       0.983839 | 0.0476678 |
| recall    |                   0.934783 |     0.997285 |             0.741935 |        0.657534 |            0.027027 |      0.987 |    0.671713 |       0.987    | 0.0476678 |
| f1-score  |                   0.960894 |     0.993753 |             0.8      |        0.690647 |            0.05     |      0.987 |    0.699059 |       0.984743 | 0.0476678 |
| support   |                  92        |  7736        |            62        |       73        |           37        |      0.987 | 8000        |    8000        | 0.0476678 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      86 |                         5 |                                 0 |                            1 |                                0 |
| Labeled as No_Failure               |                                       1 |                      7715 |                                 3 |                           15 |                                2 |
| Labeled as Overstrain_Failure       |                                       0 |                        15 |                                46 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        22 |                                 3 |                           48 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        34 |                                 1 |                            1 |                                1 |

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
