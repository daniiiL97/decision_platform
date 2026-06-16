# Summary of 16_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 95
- **learning_rate**: 0.1
- **feature_fraction**: 0.5
- **bagging_fraction**: 0.8
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

14.5 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.8125   |     0.980203 |             0.806452 |        0.815789 |            0.333333 |     0.9775 |    0.749655 |       0.972436 | 0.0680334 |
| recall    |                   0.423913 |     0.998449 |             0.403226 |        0.424658 |            0.027027 |     0.9775 |    0.455454 |       0.9775   | 0.0680334 |
| f1-score  |                   0.557143 |     0.989242 |             0.537634 |        0.558559 |            0.05     |     0.9775 |    0.538516 |       0.972499 | 0.0680334 |
| support   |                  92        |  7736        |            62        |       73        |           37        |     0.9775 | 8000        |    8000        | 0.0680334 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      39 |                        50 |                                 3 |                            0 |                                0 |
| Labeled as No_Failure               |                                       3 |                      7724 |                                 0 |                            7 |                                2 |
| Labeled as Overstrain_Failure       |                                       4 |                        33 |                                25 |                            0 |                                0 |
| Labeled as Power_Failure            |                                       2 |                        38 |                                 2 |                           31 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        35 |                                 1 |                            0 |                                1 |

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
