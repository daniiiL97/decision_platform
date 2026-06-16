# Summary of 63_Xgboost_GoldenFeatures

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

26.7 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.976471 |     0.99114  |             0.895833 |        0.807692 |                   0 |     0.9885 |    0.734227 |       0.983975 | 0.0453032 |
| recall    |                   0.902174 |     0.997802 |             0.693548 |        0.863014 |                   0 |     0.9885 |    0.691308 |       0.9885   | 0.0453032 |
| f1-score  |                   0.937853 |     0.99446  |             0.781818 |        0.834437 |                   0 |     0.9885 |    0.709714 |       0.986102 | 0.0453032 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |     0.9885 | 8000        |    8000        | 0.0453032 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      83 |                         6 |                                 1 |                            2 |                                0 |
| Labeled as No_Failure               |                                       1 |                      7719 |                                 3 |                           12 |                                1 |
| Labeled as Overstrain_Failure       |                                       1 |                        18 |                                43 |                            0 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        10 |                                 0 |                           63 |                                0 |
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
