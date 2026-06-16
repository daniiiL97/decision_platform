# Summary of 41_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.7
- **min_samples_split**: 40
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

14.9 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                          0 |     0.970378 |            0.5       |        0.814815 |                   0 |     0.9695 |    0.457039 |       0.949666 | 0.0808077 |
| recall    |                          0 |     0.999354 |            0.0483871 |        0.30137  |                   0 |     0.9695 |    0.269822 |       0.9695   | 0.0808077 |
| f1-score  |                          0 |     0.984653 |            0.0882353 |        0.44     |                   0 |     0.9695 |    0.302578 |       0.956858 | 0.0808077 |
| support   |                         92 |  7736        |           62         |       73        |                  37 |     0.9695 | 8000        |    8000        | 0.0808077 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                       0 |                        90 |                                 2 |                            0 |                                0 |
| Labeled as No_Failure               |                                       0 |                      7731 |                                 0 |                            5 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        59 |                                 3 |                            0 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        51 |                                 0 |                           22 |                                0 |
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
