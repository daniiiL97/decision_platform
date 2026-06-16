# Summary of 12_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.1
- **max_depth**: 5
- **min_child_weight**: 5
- **subsample**: 0.7
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

14.6 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.96     |     0.986187 |             0.76087  |        0.696429 |                   0 |   0.982125 |    0.680697 |       0.976935 | 0.0547842 |
| recall    |                   0.782609 |     0.996768 |             0.564516 |        0.534247 |                   0 |   0.982125 |    0.575628 |       0.982125 | 0.0547842 |
| f1-score  |                   0.862275 |     0.99145  |             0.648148 |        0.604651 |                   0 |   0.982125 |    0.621305 |       0.979189 | 0.0547842 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.982125 | 8000        |    8000        | 0.0547842 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      72 |                        17 |                                 2 |                            1 |                                0 |
| Labeled as No_Failure               |                                       3 |                      7711 |                                 3 |                           15 |                                4 |
| Labeled as Overstrain_Failure       |                                       0 |                        26 |                                35 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        30 |                                 4 |                           39 |                                0 |
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
