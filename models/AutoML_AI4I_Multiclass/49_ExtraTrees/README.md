# Summary of 49_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.8
- **min_samples_split**: 40
- **max_depth**: 6
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

15.8 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                          0 |     0.970142 |             0.5      |        0.851852 |                   0 |   0.969625 |    0.464399 |       0.949775 | 0.0895803 |
| recall    |                          0 |     0.999612 |             0.016129 |        0.315068 |                   0 |   0.969625 |    0.266162 |       0.969625 | 0.0895803 |
| f1-score  |                          0 |     0.984657 |             0.03125  |        0.46     |                   0 |   0.969625 |    0.295181 |       0.956603 | 0.0895803 |
| support   |                         92 |  7736        |            62        |       73        |                  37 |   0.969625 | 8000        |    8000        | 0.0895803 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                       0 |                        91 |                                 1 |                            0 |                                0 |
| Labeled as No_Failure               |                                       0 |                      7733 |                                 0 |                            3 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        60 |                                 1 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        50 |                                 0 |                           23 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        37 |                                 0 |                            0 |                                0 |

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
