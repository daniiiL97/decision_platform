# Summary of 48_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.9
- **min_samples_split**: 20
- **max_depth**: 5
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

21.2 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                          0 |     0.970869 |            0.333333  |        0.878788 |                   0 |    0.97025 |    0.436598 |       0.949433 |  0.090096 |
| recall    |                          0 |     0.999483 |            0.016129  |        0.39726  |                   0 |    0.97025 |    0.282574 |       0.97025  |  0.090096 |
| f1-score  |                          0 |     0.984968 |            0.0307692 |        0.54717  |                   0 |    0.97025 |    0.312581 |       0.957696 |  0.090096 |
| support   |                         92 |  7736        |           62         |       73        |                  37 |    0.97025 | 8000        |    8000        |  0.090096 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                       0 |                        91 |                                 1 |                            0 |                                0 |
| Labeled as No_Failure               |                                       0 |                      7732 |                                 0 |                            4 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        61 |                                 1 |                            0 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        43 |                                 1 |                           29 |                                0 |
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
