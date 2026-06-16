# Summary of 26_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.2
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

31.6 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.958333 |     0.988853 |             0.762712 |        0.809524 |                   0 |   0.985375 |    0.703884 |       0.98054  | 0.0513433 |
| recall    |                   0.75     |     0.997673 |             0.725806 |        0.69863  |                   0 |   0.985375 |    0.634422 |       0.985375 | 0.0513433 |
| f1-score  |                   0.841463 |     0.993244 |             0.743802 |        0.75     |                   0 |   0.985375 |    0.665702 |       0.982752 | 0.0513433 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.985375 | 8000        |    8000        | 0.0513433 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      69 |                        18 |                                 3 |                            2 |                                0 |
| Labeled as No_Failure               |                                       3 |                      7718 |                                 5 |                            9 |                                1 |
| Labeled as Overstrain_Failure       |                                       0 |                        16 |                                45 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        18 |                                 4 |                           51 |                                0 |
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
