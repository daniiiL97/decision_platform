# Summary of 73_Xgboost_GoldenFeatures_SelectedFeatures

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

24.0 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.942529 |     0.991006 |             0.895833 |        0.775    |                   0 |     0.9875 |    0.720874 |       0.983157 | 0.0445131 |
| recall    |                   0.891304 |     0.997027 |             0.693548 |        0.849315 |                   0 |     0.9875 |    0.686239 |       0.9875   | 0.0445131 |
| f1-score  |                   0.916201 |     0.994007 |             0.781818 |        0.810458 |                   0 |     0.9875 |    0.700497 |       0.985196 | 0.0445131 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |     0.9875 | 8000        |    8000        | 0.0445131 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      82 |                         7 |                                 1 |                            2 |                                0 |
| Labeled as No_Failure               |                                       4 |                      7713 |                                 3 |                           14 |                                2 |
| Labeled as Overstrain_Failure       |                                       1 |                        17 |                                43 |                            1 |                                0 |
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
