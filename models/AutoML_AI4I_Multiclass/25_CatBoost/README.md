# Summary of 25_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.15
- **depth**: 3
- **rsm**: 1.0
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

32.4 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.925373 |     0.987582 |             0.754386 |        0.761905 |                   0 |   0.983375 |    0.685849 |       0.978432 | 0.0519621 |
| recall    |                   0.673913 |     0.997156 |             0.693548 |        0.657534 |                   0 |   0.983375 |    0.60443  |       0.983375 | 0.0519621 |
| f1-score  |                   0.779874 |     0.992346 |             0.722689 |        0.705882 |                   0 |   0.983375 |    0.640158 |       0.980609 | 0.0519621 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.983375 | 8000        |    8000        | 0.0519621 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      62 |                        25 |                                 3 |                            2 |                                0 |
| Labeled as No_Failure               |                                       5 |                      7714 |                                 4 |                           11 |                                2 |
| Labeled as Overstrain_Failure       |                                       0 |                        18 |                                43 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        19 |                                 6 |                           48 |                                0 |
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
