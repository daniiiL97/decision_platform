# Summary of 68_LightGBM_GoldenFeatures_SelectedFeatures

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 95
- **learning_rate**: 0.1
- **feature_fraction**: 1.0
- **bagging_fraction**: 1.0
- **min_data_in_leaf**: 50
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

27.8 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.897727 |     0.990621 |             0.816327 |        0.842105 |           0.25      |    0.98675 |    0.759356 |       0.983421 | 0.0471802 |
| recall    |                   0.858696 |     0.996639 |             0.645161 |        0.876712 |           0.027027  |    0.98675 |    0.680847 |       0.98675  | 0.0471802 |
| f1-score  |                   0.877778 |     0.993621 |             0.720721 |        0.85906  |           0.0487805 |    0.98675 |    0.699992 |       0.984576 | 0.0471802 |
| support   |                  92        |  7736        |            62        |       73        |          37         |    0.98675 | 8000        |    8000        | 0.0471802 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      79 |                        11 |                                 1 |                            1 |                                0 |
| Labeled as No_Failure               |                                       8 |                      7710 |                                 5 |                           10 |                                3 |
| Labeled as Overstrain_Failure       |                                       1 |                        20 |                                40 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                         8 |                                 1 |                           64 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        34 |                                 2 |                            0 |                                1 |

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
