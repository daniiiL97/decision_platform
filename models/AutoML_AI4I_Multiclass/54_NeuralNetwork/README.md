# Summary of 54_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 16
- **dense_2_size**: 16
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

14.6 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.797468 |     0.988563 |             0.774194 |        0.753425 |                   0 |   0.982375 |    0.66273  |       0.977987 | 0.0605875 |
| recall    |                   0.684783 |     0.994442 |             0.774194 |        0.753425 |                   0 |   0.982375 |    0.641368 |       0.982375 | 0.0605875 |
| f1-score  |                   0.736842 |     0.991494 |             0.774194 |        0.753425 |                   0 |   0.982375 |    0.651191 |       0.980123 | 0.0605875 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.982375 | 8000        |    8000        | 0.0605875 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      63 |                        25 |                                 3 |                            1 |                                0 |
| Labeled as No_Failure               |                                      15 |                      7693 |                                10 |                           15 |                                3 |
| Labeled as Overstrain_Failure       |                                       0 |                        11 |                                48 |                            2 |                                1 |
| Labeled as Power_Failure            |                                       1 |                        16 |                                 1 |                           55 |                                0 |
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
