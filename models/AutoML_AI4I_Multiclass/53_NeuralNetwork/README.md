# Summary of 53_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 64
- **dense_2_size**: 4
- **learning_rate**: 0.05
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

16.2 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.682353 |     0.987532 |             0.568966 |        0.649351 |                   0 |      0.978 |    0.57764  |       0.973125 | 0.0731885 |
| recall    |                   0.630435 |     0.993149 |             0.532258 |        0.684932 |                   0 |      0.978 |    0.568155 |       0.978    | 0.0731885 |
| f1-score  |                   0.655367 |     0.990333 |             0.55     |        0.666667 |                   0 |      0.978 |    0.572473 |       0.975534 | 0.0731885 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |      0.978 | 8000        |    8000        | 0.0731885 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      58 |                        27 |                                 0 |                            7 |                                0 |
| Labeled as No_Failure               |                                      22 |                      7683 |                                18 |                           13 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        22 |                                33 |                            7 |                                0 |
| Labeled as Power_Failure            |                                       5 |                        13 |                                 5 |                           50 |                                0 |
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
