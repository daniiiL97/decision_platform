# Summary of 43_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.8
- **min_samples_split**: 50
- **max_depth**: 7
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

15.0 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                          0 |     0.971838 |             0.727273 |        0.771429 |                   0 |   0.970625 |    0.494108 |       0.952443 | 0.0826215 |
| recall    |                          0 |     0.999224 |             0.129032 |        0.369863 |                   0 |   0.970625 |    0.299624 |       0.970625 | 0.0826215 |
| f1-score  |                          0 |     0.985341 |             0.219178 |        0.5      |                   0 |   0.970625 |    0.340904 |       0.959086 | 0.0826215 |
| support   |                         92 |  7736        |            62        |       73        |                  37 |   0.970625 | 8000        |    8000        | 0.0826215 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                       0 |                        89 |                                 2 |                            1 |                                0 |
| Labeled as No_Failure               |                                       0 |                      7730 |                                 0 |                            6 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        53 |                                 8 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        45 |                                 1 |                           27 |                                0 |
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
