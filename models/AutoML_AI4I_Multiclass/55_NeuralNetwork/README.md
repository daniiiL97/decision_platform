# Summary of 55_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 16
- **dense_2_size**: 8
- **learning_rate**: 0.01
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

15.7 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.723404 |     0.988563 |             0.681818 |        0.824561 |                   0 |   0.981625 |    0.643669 |       0.977068 | 0.0656175 |
| recall    |                   0.73913  |     0.994442 |             0.725806 |        0.643836 |                   0 |   0.981625 |    0.620643 |       0.981625 | 0.0656175 |
| f1-score  |                   0.731183 |     0.991494 |             0.703125 |        0.723077 |                   0 |   0.981625 |    0.629776 |       0.97923  | 0.0656175 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.981625 | 8000        |    8000        | 0.0656175 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      68 |                        20 |                                 4 |                            0 |                                0 |
| Labeled as No_Failure               |                                      22 |                      7693 |                                11 |                           10 |                                0 |
| Labeled as Overstrain_Failure       |                                       3 |                        13 |                                45 |                            0 |                                1 |
| Labeled as Power_Failure            |                                       1 |                        20 |                                 5 |                           47 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        36 |                                 1 |                            0 |                                0 |

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
