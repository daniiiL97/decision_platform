# Summary of 17_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 15
- **learning_rate**: 0.1
- **feature_fraction**: 0.8
- **bagging_fraction**: 0.5
- **min_data_in_leaf**: 5
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

7.0 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.933333 |     0.989344 |             0.85     |        0.78125  |           0.117647  |     0.9845 |    0.734315 |       0.981689 | 0.0675181 |
| recall    |                   0.913043 |     0.996122 |             0.548387 |        0.684932 |           0.0540541 |     0.9845 |    0.639308 |       0.9845   | 0.0675181 |
| f1-score  |                   0.923077 |     0.992721 |             0.666667 |        0.729927 |           0.0740741 |     0.9845 |    0.677293 |       0.982747 | 0.0675181 |
| support   |                  92        |  7736        |            62        |       73        |          37         |     0.9845 | 8000        |    8000        | 0.0675181 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      84 |                         7 |                                 1 |                            0 |                                0 |
| Labeled as No_Failure               |                                       4 |                      7706 |                                 2 |                           11 |                               13 |
| Labeled as Overstrain_Failure       |                                       2 |                        24 |                                34 |                            2 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        19 |                                 2 |                           50 |                                2 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        33 |                                 1 |                            1 |                                2 |

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
