# Summary of 8_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.15
- **max_depth**: 6
- **min_child_weight**: 25
- **subsample**: 0.5
- **colsample_bytree**: 0.5
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

13.6 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.666667 |     0.975246 |             0.8125   |       0.5       |                   0 |   0.972125 |    0.590883 |       0.961589 | 0.0954358 |
| recall    |                   0.391304 |     0.99819  |             0.209677 |       0.0821918 |                   0 |   0.972125 |    0.336273 |       0.972125 | 0.0954358 |
| f1-score  |                   0.493151 |     0.986585 |             0.333333 |       0.141176  |                   0 |   0.972125 |    0.390849 |       0.96357  | 0.0954358 |
| support   |                  92        |  7736        |            62        |      73         |                  37 |   0.972125 | 8000        |    8000        | 0.0954358 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      36 |                        55 |                                 0 |                            1 |                                0 |
| Labeled as No_Failure               |                                      13 |                      7722 |                                 0 |                            1 |                                0 |
| Labeled as Overstrain_Failure       |                                       3 |                        42 |                                13 |                            4 |                                0 |
| Labeled as Power_Failure            |                                       2 |                        64 |                                 1 |                            6 |                                0 |
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
