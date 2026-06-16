# Summary of 37_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.8
- **min_samples_split**: 50
- **max_depth**: 4
- **eval_metric_name**: logloss
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

15.0 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                  1         |     0.975992 |            0.6       |        0.706667 |                   0 |      0.973 |    0.656532 |       0.966383 | 0.0798936 |
| recall    |                  0.0108696 |     0.998449 |            0.0967742 |        0.726027 |                   0 |      0.973 |    0.366424 |       0.973    | 0.0798936 |
| f1-score  |                  0.0215054 |     0.987093 |            0.166667  |        0.716216 |                   0 |      0.973 |    0.378296 |       0.962593 | 0.0798936 |
| support   |                 92         |  7736        |           62         |       73        |                  37 |      0.973 | 8000        |    8000        | 0.0798936 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                       1 |                        84 |                                 2 |                            5 |                                0 |
| Labeled as No_Failure               |                                       0 |                      7724 |                                 0 |                           12 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        52 |                                 6 |                            4 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        19 |                                 1 |                           53 |                                0 |
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
