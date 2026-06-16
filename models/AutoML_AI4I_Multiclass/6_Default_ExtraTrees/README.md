# Summary of 6_Default_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.9
- **min_samples_split**: 30
- **max_depth**: 4
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

10.1 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                          0 |     0.970751 |                    0 |        0.882353 |                   0 |   0.970375 |    0.370621 |       0.946767 |  0.100256 |
| recall    |                          0 |     0.999612 |                    0 |        0.410959 |                   0 |   0.970375 |    0.282114 |       0.970375 |  0.100256 |
| f1-score  |                          0 |     0.98497  |                    0 |        0.560748 |                   0 |   0.970375 |    0.309144 |       0.957583 |  0.100256 |
| support   |                         92 |  7736        |                   62 |       73        |                  37 |   0.970375 | 8000        |    8000        |  0.100256 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                       0 |                        92 |                                 0 |                            0 |                                0 |
| Labeled as No_Failure               |                                       0 |                      7733 |                                 0 |                            3 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        61 |                                 0 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        43 |                                 0 |                           30 |                                0 |
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
