# Summary of 56_NeuralNetwork

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

13.3 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.72     |     0.98341  |             0.787234 |        0.820896 |                   0 |    0.97925 |    0.662308 |       0.972829 | 0.0700581 |
| recall    |                   0.391304 |     0.996122 |             0.596774 |        0.753425 |                   0 |    0.97925 |    0.547525 |       0.97925  | 0.0700581 |
| f1-score  |                   0.507042 |     0.989725 |             0.678899 |        0.785714 |                   0 |    0.97925 |    0.592276 |       0.975326 | 0.0700581 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |    0.97925 | 8000        |    8000        | 0.0700581 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      36 |                        54 |                                 1 |                            1 |                                0 |
| Labeled as No_Failure               |                                      14 |                      7706 |                                 6 |                           10 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        24 |                                37 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        16 |                                 2 |                           55 |                                0 |
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
