# Summary of 2_Default_Xgboost_GoldenFeatures_SelectedFeatures

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

18.5 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.965909 |     0.991265 |             0.918367 |        0.818182 |                   0 |    0.98875 |    0.738745 |       0.984245 | 0.0436463 |
| recall    |                   0.923913 |     0.997544 |             0.725806 |        0.863014 |                   0 |    0.98875 |    0.702055 |       0.98875  | 0.0436463 |
| f1-score  |                   0.944444 |     0.994395 |             0.810811 |        0.84     |                   0 |    0.98875 |    0.71793  |       0.98639  | 0.0436463 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |    0.98875 | 8000        |    8000        | 0.0436463 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      85 |                         7 |                                 0 |                            0 |                                0 |
| Labeled as No_Failure               |                                       2 |                      7717 |                                 3 |                           13 |                                1 |
| Labeled as Overstrain_Failure       |                                       1 |                        16 |                                45 |                            0 |                                0 |
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
