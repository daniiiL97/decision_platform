# Summary of 28_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 4
- **rsm**: 0.7
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

46.0 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.945946 |     0.988472 |             0.785714 |        0.790323 |                   0 |      0.985 |    0.702091 |       0.980032 | 0.0507812 |
| recall    |                   0.76087  |     0.997544 |             0.709677 |        0.671233 |                   0 |      0.985 |    0.627865 |       0.985    | 0.0507812 |
| f1-score  |                   0.843373 |     0.992987 |             0.745763 |        0.725926 |                   0 |      0.985 |    0.66161  |       0.982321 | 0.0507812 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |      0.985 | 8000        |    8000        | 0.0507812 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      70 |                        17 |                                 3 |                            2 |                                0 |
| Labeled as No_Failure               |                                       4 |                      7717 |                                 5 |                            9 |                                1 |
| Labeled as Overstrain_Failure       |                                       0 |                        17 |                                44 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        21 |                                 3 |                           49 |                                0 |
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
