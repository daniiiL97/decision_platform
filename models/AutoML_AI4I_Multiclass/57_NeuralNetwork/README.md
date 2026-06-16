# Summary of 57_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 64
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

16.6 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.74026  |     0.986797 |             0.854545 |        0.828125 |                   0 |   0.981875 |    0.681945 |       0.976925 | 0.0598021 |
| recall    |                   0.619565 |     0.995088 |             0.758065 |        0.726027 |                   0 |   0.981875 |    0.619749 |       0.981875 | 0.0598021 |
| f1-score  |                   0.674556 |     0.990925 |             0.803419 |        0.773723 |                   0 |   0.981875 |    0.648525 |       0.979268 | 0.0598021 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.981875 | 8000        |    8000        | 0.0598021 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      57 |                        33 |                                 1 |                            1 |                                0 |
| Labeled as No_Failure               |                                      20 |                      7698 |                                 6 |                            9 |                                3 |
| Labeled as Overstrain_Failure       |                                       0 |                        14 |                                47 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        19 |                                 1 |                           53 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        37 |                                 0 |                            0 |                                0 |

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
