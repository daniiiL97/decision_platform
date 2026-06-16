# Summary of 52_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 4
- **learning_rate**: 0.1
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

13.6 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.634409 |     0.986758 |             0.757576 |        0.604167 |                   0 |   0.977125 |    0.596582 |       0.972874 | 0.0746119 |
| recall    |                   0.641304 |     0.992115 |             0.403226 |        0.794521 |                   0 |   0.977125 |    0.566233 |       0.977125 | 0.0746119 |
| f1-score  |                   0.637838 |     0.989429 |             0.526316 |        0.686391 |                   0 |   0.977125 |    0.567995 |       0.974455 | 0.0746119 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.977125 | 8000        |    8000        | 0.0746119 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      59 |                        32 |                                 0 |                            1 |                                0 |
| Labeled as No_Failure               |                                      32 |                      7675 |                                 6 |                           23 |                                0 |
| Labeled as Overstrain_Failure       |                                       1 |                        23 |                                25 |                           13 |                                0 |
| Labeled as Power_Failure            |                                       1 |                        13 |                                 1 |                           58 |                                0 |
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
