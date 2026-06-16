# Summary of 30_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.2
- **depth**: 5
- **rsm**: 0.8
- **loss_function**: MultiClass
- **eval_metric**: MultiClass
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

30.8 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.929577 |     0.988086 |             0.754386 |        0.777778 |                   0 |   0.983875 |    0.689965 |       0.979113 | 0.0514259 |
| recall    |                   0.717391 |     0.997027 |             0.693548 |        0.671233 |                   0 |   0.983875 |    0.61584  |       0.983875 | 0.0514259 |
| f1-score  |                   0.809816 |     0.992536 |             0.722689 |        0.720588 |                   0 |   0.983875 |    0.649126 |       0.981272 | 0.0514259 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.983875 | 8000        |    8000        | 0.0514259 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      66 |                        20 |                                 4 |                            2 |                                0 |
| Labeled as No_Failure               |                                       5 |                      7713 |                                 4 |                           11 |                                3 |
| Labeled as Overstrain_Failure       |                                       0 |                        18 |                                43 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        20 |                                 4 |                           49 |                                0 |
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
