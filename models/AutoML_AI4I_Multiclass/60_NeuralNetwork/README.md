# Summary of 60_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 16
- **dense_2_size**: 16
- **learning_rate**: 0.08
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

15.1 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.616162 |     0.987907 |             0.734375 |        0.84127  |                   0 |       0.98 |    0.635943 |       0.97576  | 0.0745422 |
| recall    |                   0.663043 |     0.992632 |             0.758065 |        0.726027 |                   0 |       0.98 |    0.627953 |       0.98     | 0.0745422 |
| f1-score  |                   0.638743 |     0.990264 |             0.746032 |        0.779412 |                   0 |       0.98 |    0.63089  |       0.977824 | 0.0745422 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |       0.98 | 8000        |    8000        | 0.0745422 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      61 |                        28 |                                 2 |                            1 |                                0 |
| Labeled as No_Failure               |                                      36 |                      7679 |                                13 |                            7 |                                1 |
| Labeled as Overstrain_Failure       |                                       1 |                        13 |                                47 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       1 |                        18 |                                 1 |                           53 |                                0 |
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
