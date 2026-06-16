# Summary of 24_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 63
- **learning_rate**: 0.2
- **feature_fraction**: 1.0
- **bagging_fraction**: 0.9
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

7.5 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.836957 |     0.990181 |             0.619048 |        0.671233 |            0.125    |   0.979125 |    0.648484 |       0.978631 |  0.132849 |
| recall    |                   0.836957 |     0.990693 |             0.629032 |        0.671233 |            0.108108 |   0.979125 |    0.647205 |       0.979125 |  0.132849 |
| f1-score  |                   0.836957 |     0.990437 |             0.624    |        0.671233 |            0.115942 |   0.979125 |    0.647714 |       0.978875 |  0.132849 |
| support   |                  92        |  7736        |            62        |       73        |           37        |   0.979125 | 8000        |    8000        |  0.132849 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      77 |                        11 |                                 2 |                            2 |                                0 |
| Labeled as No_Failure               |                                      13 |                      7664 |                                15 |                           18 |                               26 |
| Labeled as Overstrain_Failure       |                                       1 |                        18 |                                39 |                            3 |                                1 |
| Labeled as Power_Failure            |                                       0 |                        18 |                                 5 |                           49 |                                1 |
| Labeled as Tool_Wear_Failure        |                                       1 |                        29 |                                 2 |                            1 |                                4 |

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
