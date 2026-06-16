# Summary of 32_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.15
- **depth**: 3
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

35.7 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.9375   |     0.98683  |             0.75     |        0.806452 |                   0 |   0.983375 |    0.696156 |       0.978218 | 0.0510686 |
| recall    |                   0.652174 |     0.997673 |             0.629032 |        0.684932 |                   0 |   0.983375 |    0.592762 |       0.983375 | 0.0510686 |
| f1-score  |                   0.769231 |     0.992222 |             0.684211 |        0.740741 |                   0 |   0.983375 |    0.637281 |       0.980387 | 0.0510686 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.983375 | 8000        |    8000        | 0.0510686 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      60 |                        27 |                                 3 |                            2 |                                0 |
| Labeled as No_Failure               |                                       4 |                      7718 |                                 4 |                            9 |                                1 |
| Labeled as Overstrain_Failure       |                                       0 |                        22 |                                39 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        19 |                                 4 |                           50 |                                0 |
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
