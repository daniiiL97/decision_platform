# Summary of 36_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 1.0
- **min_samples_split**: 30
- **max_depth**: 3
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

22.2 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                          0 |     0.974146 |            0.428571  |        0.734375 |                   0 |    0.97175 |    0.427418 |       0.952021 |  0.108333 |
| recall    |                          0 |     0.998449 |            0.0483871 |        0.643836 |                   0 |    0.97175 |    0.338134 |       0.97175  |  0.108333 |
| f1-score  |                          0 |     0.986147 |            0.0869565 |        0.686131 |                   0 |    0.97175 |    0.351847 |       0.960539 |  0.108333 |
| support   |                         92 |  7736        |           62         |       73        |                  37 |    0.97175 | 8000        |    8000        |  0.108333 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                       0 |                        88 |                                 2 |                            2 |                                0 |
| Labeled as No_Failure               |                                       0 |                      7724 |                                 0 |                           12 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        57 |                                 3 |                            2 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        24 |                                 2 |                           47 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        36 |                                 0 |                            1 |                                0 |

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
