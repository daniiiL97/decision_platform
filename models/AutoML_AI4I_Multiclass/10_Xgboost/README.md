# Summary of 10_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.1
- **max_depth**: 4
- **min_child_weight**: 10
- **subsample**: 0.6
- **colsample_bytree**: 0.6
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
| precision |                   0.921875 |     0.983797 |             0.7      |        0.574468 |                   0 |      0.979 |    0.636028 |       0.9726   | 0.0596213 |
| recall    |                   0.641304 |     0.996768 |             0.564516 |        0.369863 |                   0 |      0.979 |    0.51449  |       0.979    | 0.0596213 |
| f1-score  |                   0.75641  |     0.99024  |             0.625    |        0.45     |                   0 |      0.979 |    0.56433  |       0.975211 | 0.0596213 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |      0.979 | 8000        |    8000        | 0.0596213 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      59 |                        30 |                                 3 |                            0 |                                0 |
| Labeled as No_Failure               |                                       4 |                      7711 |                                 4 |                           16 |                                1 |
| Labeled as Overstrain_Failure       |                                       1 |                        22 |                                35 |                            4 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        40 |                                 6 |                           27 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        35 |                                 2 |                            0 |                                0 |

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
