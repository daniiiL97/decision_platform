# Summary of 61_Xgboost_GoldenFeatures_SelectedFeatures

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

23.2 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.965517 |     0.991265 |             0.918367 |        0.794872 |                   0 |     0.9885 |    0.734004 |       0.984028 | 0.0442686 |
| recall    |                   0.913043 |     0.997544 |             0.725806 |        0.849315 |                   0 |     0.9885 |    0.697142 |       0.9885   | 0.0442686 |
| f1-score  |                   0.938547 |     0.994395 |             0.810811 |        0.821192 |                   0 |     0.9885 |    0.712989 |       0.98615  | 0.0442686 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |     0.9885 | 8000        |    8000        | 0.0442686 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      84 |                         6 |                                 0 |                            2 |                                0 |
| Labeled as No_Failure               |                                       2 |                      7717 |                                 3 |                           13 |                                1 |
| Labeled as Overstrain_Failure       |                                       1 |                        16 |                                45 |                            0 |                                0 |
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
