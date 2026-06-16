# Summary of 51_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.7
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

15.2 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                          0 |     0.968809 |                    0 |        0.882353 |                   0 |   0.968625 |    0.370232 |       0.94489  |  0.105369 |
| recall    |                          0 |     0.999741 |                    0 |        0.205479 |                   0 |   0.968625 |    0.241044 |       0.968625 |  0.105369 |
| f1-score  |                          0 |     0.984032 |                    0 |        0.333333 |                   0 |   0.968625 |    0.263473 |       0.954601 |  0.105369 |
| support   |                         92 |  7736        |                   62 |       73        |                  37 |   0.968625 | 8000        |    8000        |  0.105369 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                       0 |                        92 |                                 0 |                            0 |                                0 |
| Labeled as No_Failure               |                                       0 |                      7734 |                                 0 |                            2 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        62 |                                 0 |                            0 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        58 |                                 0 |                           15 |                                0 |
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
