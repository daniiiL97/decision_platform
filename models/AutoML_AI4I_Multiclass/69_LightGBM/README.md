# Summary of 69_LightGBM

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

18.8 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.977273 |     0.989986 |             0.807692 |        0.727273 |                   0 |   0.985875 |    0.700445 |       0.981451 | 0.0477602 |
| recall    |                   0.934783 |     0.996768 |             0.677419 |        0.657534 |                   0 |   0.985875 |    0.653301 |       0.985875 | 0.0477602 |
| f1-score  |                   0.955556 |     0.993366 |             0.736842 |        0.690647 |                   0 |   0.985875 |    0.675282 |       0.983586 | 0.0477602 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.985875 | 8000        |    8000        | 0.0477602 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      86 |                         5 |                                 1 |                            0 |                                0 |
| Labeled as No_Failure               |                                       2 |                      7711 |                                 3 |                           15 |                                5 |
| Labeled as Overstrain_Failure       |                                       0 |                        17 |                                42 |                            3 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        21 |                                 4 |                           48 |                                0 |
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
