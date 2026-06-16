# Summary of 11_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.05
- **max_depth**: 6
- **min_child_weight**: 50
- **subsample**: 0.5
- **colsample_bytree**: 0.7
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

24.8 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                  0.380952  |     0.96942  |                    0 |               0 |                   0 |   0.967875 |    0.270074 |       0.94181  |  0.131659 |
| recall    |                  0.0869565 |     0.999871 |                    0 |               0 |                   0 |   0.967875 |    0.217365 |       0.967875 |  0.131659 |
| f1-score  |                  0.141593  |     0.98441  |                    0 |               0 |                   0 |   0.967875 |    0.225201 |       0.953553 |  0.131659 |
| support   |                 92         |  7736        |                   62 |              73 |                  37 |   0.967875 | 8000        |    8000        |  0.131659 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                       8 |                        84 |                                 0 |                            0 |                                0 |
| Labeled as No_Failure               |                                       1 |                      7735 |                                 0 |                            0 |                                0 |
| Labeled as Overstrain_Failure       |                                       9 |                        53 |                                 0 |                            0 |                                0 |
| Labeled as Power_Failure            |                                       2 |                        71 |                                 0 |                            0 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       1 |                        36 |                                 0 |                            0 |                                0 |

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
