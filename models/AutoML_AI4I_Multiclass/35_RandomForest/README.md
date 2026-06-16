# Summary of 35_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 1.0
- **min_samples_split**: 20
- **max_depth**: 3
- **eval_metric_name**: logloss
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

15.3 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.914286 |     0.9738   |             0.5      |        0.875    |                   0 |   0.973125 |    0.652617 |       0.964038 | 0.0771608 |
| recall    |                   0.347826 |     0.999354 |             0.016129 |        0.287671 |                   0 |   0.973125 |    0.330196 |       0.973125 | 0.0771608 |
| f1-score  |                   0.503937 |     0.986411 |             0.03125  |        0.43299  |                   0 |   0.973125 |    0.390918 |       0.963848 | 0.0771608 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.973125 | 8000        |    8000        | 0.0771608 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      32 |                        60 |                                 0 |                            0 |                                0 |
| Labeled as No_Failure               |                                       2 |                      7731 |                                 0 |                            3 |                                0 |
| Labeled as Overstrain_Failure       |                                       1 |                        60 |                                 1 |                            0 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        52 |                                 0 |                           21 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        36 |                                 1 |                            0 |                                0 |

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
