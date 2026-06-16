# Summary of 62_Xgboost_GoldenFeatures_SelectedFeatures

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.1
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

15.7 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.965517 |     0.990755 |             0.88     |        0.810811 |                   0 |      0.988 |    0.729417 |       0.983382 | 0.0449278 |
| recall    |                   0.913043 |     0.997415 |             0.709677 |        0.821918 |                   0 |      0.988 |    0.688411 |       0.988    | 0.0449278 |
| f1-score  |                   0.938547 |     0.994074 |             0.785714 |        0.816327 |                   0 |      0.988 |    0.706932 |       0.985601 | 0.0449278 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |      0.988 | 8000        |    8000        | 0.0449278 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      84 |                         7 |                                 1 |                            0 |                                0 |
| Labeled as No_Failure               |                                       2 |                      7716 |                                 4 |                           13 |                                1 |
| Labeled as Overstrain_Failure       |                                       1 |                        17 |                                44 |                            0 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        13 |                                 0 |                           60 |                                0 |
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
