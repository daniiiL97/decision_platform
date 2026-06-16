# Summary of 65_Xgboost_GoldenFeatures

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.05
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

38.2 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.976744 |     0.990885 |             0.952381 |        0.790123 |                   0 |    0.98825 |    0.742027 |       0.984009 | 0.0443125 |
| recall    |                   0.913043 |     0.997673 |             0.645161 |        0.876712 |                   0 |    0.98825 |    0.686518 |       0.98825  | 0.0443125 |
| f1-score  |                   0.94382  |     0.994267 |             0.769231 |        0.831169 |                   0 |    0.98825 |    0.707697 |       0.985856 | 0.0443125 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |    0.98825 | 8000        |    8000        | 0.0443125 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      84 |                         6 |                                 0 |                            2 |                                0 |
| Labeled as No_Failure               |                                       1 |                      7718 |                                 1 |                           14 |                                2 |
| Labeled as Overstrain_Failure       |                                       1 |                        21 |                                40 |                            0 |                                0 |
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
