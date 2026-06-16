# Summary of 21_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 63
- **learning_rate**: 0.1
- **feature_fraction**: 0.8
- **bagging_fraction**: 0.8
- **min_data_in_leaf**: 15
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

11.4 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.961538 |     0.988459 |             0.785714 |        0.725806 |                   0 |      0.984 |    0.692304 |       0.979609 | 0.0613145 |
| recall    |                   0.815217 |     0.996381 |             0.709677 |        0.616438 |                   0 |      0.984 |    0.627543 |       0.984    | 0.0613145 |
| f1-score  |                   0.882353 |     0.992404 |             0.745763 |        0.666667 |                   0 |      0.984 |    0.657437 |       0.981664 | 0.0613145 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |      0.984 | 8000        |    8000        | 0.0613145 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      75 |                        16 |                                 1 |                            0 |                                0 |
| Labeled as No_Failure               |                                       2 |                      7708 |                                 7 |                           14 |                                5 |
| Labeled as Overstrain_Failure       |                                       0 |                        16 |                                44 |                            2 |                                0 |
| Labeled as Power_Failure            |                                       1 |                        23 |                                 3 |                           45 |                                1 |
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
