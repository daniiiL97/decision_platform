# Summary of 19_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 95
- **learning_rate**: 0.05
- **feature_fraction**: 0.9
- **bagging_fraction**: 0.8
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

22.2 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.956522 |     0.986706 |             0.76     |        0.754386 |                   0 |    0.98325 |    0.691523 |       0.977918 |  0.062554 |
| recall    |                   0.717391 |     0.997802 |             0.612903 |        0.589041 |                   0 |    0.98325 |    0.583428 |       0.98325  |  0.062554 |
| f1-score  |                   0.819876 |     0.992223 |             0.678571 |        0.661538 |                   0 |    0.98325 |    0.630442 |       0.980204 |  0.062554 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |    0.98325 | 8000        |    8000        |  0.062554 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      66 |                        23 |                                 3 |                            0 |                                0 |
| Labeled as No_Failure               |                                       2 |                      7719 |                                 4 |                           10 |                                1 |
| Labeled as Overstrain_Failure       |                                       1 |                        20 |                                38 |                            3 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        26 |                                 4 |                           43 |                                0 |
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
