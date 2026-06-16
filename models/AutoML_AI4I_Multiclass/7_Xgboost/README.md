# Summary of 7_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.1
- **max_depth**: 7
- **min_child_weight**: 5
- **subsample**: 1.0
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

13.8 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.948718 |     0.986568 |             0.755556 |        0.694915 |                   0 |   0.982625 |    0.677151 |       0.977118 | 0.0541445 |
| recall    |                   0.804348 |     0.996898 |             0.548387 |        0.561644 |                   0 |   0.982625 |    0.582255 |       0.982625 | 0.0541445 |
| f1-score  |                   0.870588 |     0.991706 |             0.635514 |        0.621212 |                   0 |   0.982625 |    0.623804 |       0.979585 | 0.0541445 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.982625 | 8000        |    8000        | 0.0541445 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      74 |                        15 |                                 2 |                            1 |                                0 |
| Labeled as No_Failure               |                                       3 |                      7712 |                                 4 |                           16 |                                1 |
| Labeled as Overstrain_Failure       |                                       1 |                        26 |                                34 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        29 |                                 3 |                           41 |                                0 |
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
