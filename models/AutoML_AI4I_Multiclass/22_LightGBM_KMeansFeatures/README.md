# Summary of 22_LightGBM_KMeansFeatures

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 127
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

23.5 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.942529 |     0.98896  |             0.698113 |        0.742424 |                   0 |      0.984 |    0.674405 |       0.979349 | 0.0540784 |
| recall    |                   0.891304 |     0.995863 |             0.596774 |        0.671233 |                   0 |      0.984 |    0.631035 |       0.984    | 0.0540784 |
| f1-score  |                   0.916201 |     0.9924   |             0.643478 |        0.705036 |                   0 |      0.984 |    0.651423 |       0.981607 | 0.0540784 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |      0.984 | 8000        |    8000        | 0.0540784 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      82 |                         8 |                                 2 |                            0 |                                0 |
| Labeled as No_Failure               |                                       5 |                      7704 |                                 8 |                           16 |                                3 |
| Labeled as Overstrain_Failure       |                                       0 |                        23 |                                37 |                            1 |                                1 |
| Labeled as Power_Failure            |                                       0 |                        20 |                                 4 |                           49 |                                0 |
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
