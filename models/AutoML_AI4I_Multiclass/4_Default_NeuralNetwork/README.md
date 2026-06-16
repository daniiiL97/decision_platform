# Summary of 4_Default_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
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

13.8 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.953846 |     0.987692 |             0.745763 |        0.671053 |                   0 |   0.982625 |    0.671671 |       0.977971 | 0.0713669 |
| recall    |                   0.673913 |     0.995863 |             0.709677 |        0.69863  |                   0 |   0.982625 |    0.615617 |       0.982625 | 0.0713669 |
| f1-score  |                   0.789809 |     0.991761 |             0.727273 |        0.684564 |                   0 |   0.982625 |    0.638681 |       0.979999 | 0.0713669 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.982625 | 8000        |    8000        | 0.0713669 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      62 |                        25 |                                 3 |                            2 |                                0 |
| Labeled as No_Failure               |                                       2 |                      7704 |                                 7 |                           23 |                                0 |
| Labeled as Overstrain_Failure       |                                       1 |                        17 |                                44 |                            0 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        19 |                                 3 |                           51 |                                0 |
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
