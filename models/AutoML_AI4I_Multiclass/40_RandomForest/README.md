# Summary of 40_RandomForest

[<< Go back](../README.md)


## Random Forest
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

19.2 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.918367 |     0.982682 |             0.741935 |        0.716418 |                   0 |   0.979125 |    0.671881 |       0.973102 | 0.0617893 |
| recall    |                   0.48913  |     0.997544 |             0.370968 |        0.657534 |                   0 |   0.979125 |    0.503035 |       0.979125 | 0.0617893 |
| f1-score  |                   0.638298 |     0.990057 |             0.494624 |        0.685714 |                   0 |   0.979125 |    0.561739 |       0.974816 | 0.0617893 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.979125 | 8000        |    8000        | 0.0617893 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      45 |                        41 |                                 3 |                            3 |                                0 |
| Labeled as No_Failure               |                                       3 |                      7717 |                                 2 |                           14 |                                0 |
| Labeled as Overstrain_Failure       |                                       1 |                        36 |                                23 |                            2 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        24 |                                 1 |                           48 |                                0 |
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
