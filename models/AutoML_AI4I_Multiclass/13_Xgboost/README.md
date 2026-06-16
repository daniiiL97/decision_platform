# Summary of 13_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.15
- **max_depth**: 7
- **min_child_weight**: 25
- **subsample**: 0.6
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

14.7 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.745455 |     0.978462 |             0.756098 |        0.909091 |                   0 |   0.975625 |    0.677821 |       0.968901 | 0.0822874 |
| recall    |                   0.445652 |     0.99832  |             0.5      |        0.136986 |                   0 |   0.975625 |    0.416192 |       0.975625 | 0.0822874 |
| f1-score  |                   0.557823 |     0.988291 |             0.601942 |        0.238095 |                   0 |   0.975625 |    0.47723  |       0.96893  | 0.0822874 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.975625 | 8000        |    8000        | 0.0822874 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      41 |                        46 |                                 4 |                            1 |                                0 |
| Labeled as No_Failure               |                                      11 |                      7723 |                                 2 |                            0 |                                0 |
| Labeled as Overstrain_Failure       |                                       1 |                        30 |                                31 |                            0 |                                0 |
| Labeled as Power_Failure            |                                       2 |                        59 |                                 2 |                           10 |                                0 |
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
