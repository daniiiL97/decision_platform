# Summary of 74_Xgboost_GoldenFeatures

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.05
- **max_depth**: 6
- **min_child_weight**: 1
- **subsample**: 0.9
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

38.3 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.954023 |     0.991518 |             0.914894 |        0.790123 |                   0 |   0.988125 |    0.730112 |       0.984069 | 0.0445679 |
| recall    |                   0.902174 |     0.997285 |             0.693548 |        0.876712 |                   0 |   0.988125 |    0.693944 |       0.988125 | 0.0445679 |
| f1-score  |                   0.927374 |     0.994393 |             0.788991 |        0.831169 |                   0 |   0.988125 |    0.708385 |       0.985942 | 0.0445679 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.988125 | 8000        |    8000        | 0.0445679 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      83 |                         6 |                                 1 |                            2 |                                0 |
| Labeled as No_Failure               |                                       3 |                      7715 |                                 2 |                           13 |                                3 |
| Labeled as Overstrain_Failure       |                                       1 |                        16 |                                43 |                            1 |                                1 |
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
