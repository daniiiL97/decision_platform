# Summary of 58_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 16
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

13.7 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.737705 |     0.986918 |             0.774194 |        0.746835 |                   0 |   0.980875 |    0.64913  |       0.975648 | 0.0624713 |
| recall    |                   0.48913  |     0.9947   |             0.774194 |        0.808219 |                   0 |   0.980875 |    0.613249 |       0.980875 | 0.0624713 |
| f1-score  |                   0.588235 |     0.990794 |             0.774194 |        0.776316 |                   0 |   0.980875 |    0.625908 |       0.977946 | 0.0624713 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.980875 | 8000        |    8000        | 0.0624713 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      45 |                        42 |                                 1 |                            4 |                                0 |
| Labeled as No_Failure               |                                      14 |                      7695 |                                12 |                           15 |                                0 |
| Labeled as Overstrain_Failure       |                                       1 |                        12 |                                48 |                            0 |                                1 |
| Labeled as Power_Failure            |                                       1 |                        13 |                                 0 |                           59 |                                0 |
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
