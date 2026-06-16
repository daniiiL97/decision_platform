# Summary of 5_Default_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.9
- **min_samples_split**: 30
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

13.6 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                  1         |     0.975006 |            0.625     |        0.753623 |                   0 |    0.97275 |    0.670726 |       0.966052 | 0.0804628 |
| recall    |                  0.0108696 |     0.998449 |            0.0806452 |        0.712329 |                   0 |    0.97275 |    0.360458 |       0.97275  | 0.0804628 |
| f1-score  |                  0.0215054 |     0.986588 |            0.142857  |        0.732394 |                   0 |    0.97275 |    0.376669 |       0.962068 | 0.0804628 |
| support   |                 92         |  7736        |           62         |       73        |                  37 |    0.97275 | 8000        |    8000        | 0.0804628 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                       1 |                        86 |                                 2 |                            3 |                                0 |
| Labeled as No_Failure               |                                       0 |                      7724 |                                 0 |                           12 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        55 |                                 5 |                            2 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        20 |                                 1 |                           52 |                                0 |
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
