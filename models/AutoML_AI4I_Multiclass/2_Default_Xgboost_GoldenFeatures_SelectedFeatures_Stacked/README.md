# Summary of 2_Default_Xgboost_GoldenFeatures_SelectedFeatures_Stacked

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

417.2 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.965909 |     0.992541 |             0.894737 |        0.822785 |                   0 |   0.989875 |    0.735194 |       0.985337 | 0.0396976 |
| recall    |                   0.923913 |     0.997673 |             0.822581 |        0.890411 |                   0 |   0.989875 |    0.726916 |       0.989875 | 0.0396976 |
| f1-score  |                   0.944444 |     0.995101 |             0.857143 |        0.855263 |                   0 |   0.989875 |    0.73039  |       0.98757  | 0.0396976 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.989875 | 8000        |    8000        | 0.0396976 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      85 |                         5 |                                 0 |                            2 |                                0 |
| Labeled as No_Failure               |                                       2 |                      7718 |                                 5 |                           11 |                                0 |
| Labeled as Overstrain_Failure       |                                       1 |                        10 |                                51 |                            0 |                                0 |
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
