# Summary of 23_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 95
- **learning_rate**: 0.1
- **feature_fraction**: 1.0
- **bagging_fraction**: 0.5
- **min_data_in_leaf**: 10
- **metric**: multi_logloss
- **custom_eval_metric_name**: None
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

12.5 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.923913 |     0.990611 |             0.766667 |        0.78125  |           0.111111  |     0.9855 |    0.71471  |        0.98213 | 0.0606426 |
| recall    |                   0.923913 |     0.995605 |             0.741935 |        0.684932 |           0.027027  |     0.9855 |    0.674682 |        0.9855  | 0.0606426 |
| f1-score  |                   0.923913 |     0.993102 |             0.754098 |        0.729927 |           0.0434783 |     0.9855 |    0.688904 |        0.98366 | 0.0606426 |
| support   |                  92        |  7736        |            62        |       73        |          37         |     0.9855 | 8000        |     8000       | 0.0606426 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      85 |                         7 |                                 0 |                            0 |                                0 |
| Labeled as No_Failure               |                                       6 |                      7702 |                                10 |                           11 |                                7 |
| Labeled as Overstrain_Failure       |                                       1 |                        13 |                                46 |                            2 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        19 |                                 3 |                           50 |                                1 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        34 |                                 1 |                            1 |                                1 |

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
