# Summary of 75_LightGBM_GoldenFeatures

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 127
- **learning_rate**: 0.1
- **feature_fraction**: 1.0
- **bagging_fraction**: 0.9
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

32.8 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.910112 |     0.991261 |             0.847826 |        0.839506 |                   0 |   0.987625 |    0.717741 |       0.983247 | 0.0468815 |
| recall    |                   0.880435 |     0.997027 |             0.629032 |        0.931507 |                   0 |   0.987625 |    0.6876   |       0.987625 | 0.0468815 |
| f1-score  |                   0.895028 |     0.994135 |             0.722222 |        0.883117 |                   0 |   0.987625 |    0.6989   |       0.985277 | 0.0468815 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.987625 | 8000        |    8000        | 0.0468815 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      81 |                         9 |                                 1 |                            1 |                                0 |
| Labeled as No_Failure               |                                       7 |                      7713 |                                 3 |                           10 |                                3 |
| Labeled as Overstrain_Failure       |                                       1 |                        20 |                                39 |                            2 |                                0 |
| Labeled as Power_Failure            |                                       0 |                         4 |                                 1 |                           68 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        35 |                                 2 |                            0 |                                0 |

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
