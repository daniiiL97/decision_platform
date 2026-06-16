# Summary of 33_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 5
- **rsm**: 0.9
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

44.8 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.953846 |     0.987216 |             0.764706 |        0.806452 |                   0 |   0.984125 |    0.702444 |       0.978892 | 0.0509305 |
| recall    |                   0.673913 |     0.99819  |             0.629032 |        0.684932 |                   0 |   0.984125 |    0.597213 |       0.984125 | 0.0509305 |
| f1-score  |                   0.789809 |     0.992673 |             0.690265 |        0.740741 |                   0 |   0.984125 |    0.642698 |       0.981106 | 0.0509305 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.984125 | 8000        |    8000        | 0.0509305 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      62 |                        24 |                                 4 |                            2 |                                0 |
| Labeled as No_Failure               |                                       3 |                      7722 |                                 2 |                            9 |                                0 |
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
