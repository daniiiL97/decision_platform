# Summary of 59_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
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

16.8 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.692982 |     0.988929 |             0.69697  |        0.826923 |                   0 |    0.98125 |    0.641161 |       0.977211 | 0.0727786 |
| recall    |                   0.858696 |     0.99302  |             0.741935 |        0.589041 |                   0 |    0.98125 |    0.636538 |       0.98125  | 0.0727786 |
| f1-score  |                   0.76699  |     0.99097  |             0.71875  |        0.688    |                   0 |    0.98125 |    0.632942 |       0.978937 | 0.0727786 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |    0.98125 | 8000        |    8000        | 0.0727786 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      79 |                        12 |                                 0 |                            1 |                                0 |
| Labeled as No_Failure               |                                      34 |                      7682 |                                14 |                            6 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        15 |                                46 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       1 |                        24 |                                 5 |                           43 |                                0 |
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
