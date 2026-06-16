# Summary of 72_Xgboost_GoldenFeatures_SelectedFeatures

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.075
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

20.1 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.942529 |     0.990879 |             0.875    |        0.7875   |                   0 |     0.9875 |    0.719181 |       0.982986 |  0.044755 |
| recall    |                   0.891304 |     0.997027 |             0.677419 |        0.863014 |                   0 |     0.9875 |    0.685753 |       0.9875   |  0.044755 |
| f1-score  |                   0.916201 |     0.993943 |             0.763636 |        0.823529 |                   0 |     0.9875 |    0.699462 |       0.985112 |  0.044755 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |     0.9875 | 8000        |    8000        |  0.044755 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      82 |                         7 |                                 1 |                            2 |                                0 |
| Labeled as No_Failure               |                                       4 |                      7713 |                                 4 |                           14 |                                1 |
| Labeled as Overstrain_Failure       |                                       1 |                        19 |                                42 |                            0 |                                0 |
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
