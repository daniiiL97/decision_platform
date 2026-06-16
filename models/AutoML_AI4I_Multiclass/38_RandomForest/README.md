# Summary of 38_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.7
- **min_samples_split**: 50
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

16.8 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                          0 |     0.9739   |                    0 |        0.710145 |                   0 |   0.971625 |    0.336809 |       0.948241 | 0.0999993 |
| recall    |                          0 |     0.998449 |                    0 |        0.671233 |                   0 |   0.971625 |    0.333936 |       0.971625 | 0.0999993 |
| f1-score  |                          0 |     0.986022 |                    0 |        0.690141 |                   0 |   0.971625 |    0.335232 |       0.95978  | 0.0999993 |
| support   |                         92 |  7736        |                   62 |       73        |                  37 |   0.971625 | 8000        |    8000        | 0.0999993 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                       0 |                        88 |                                 0 |                            4 |                                0 |
| Labeled as No_Failure               |                                       0 |                      7724 |                                 0 |                           12 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        59 |                                 0 |                            3 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        24 |                                 0 |                           49 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        36 |                                 0 |                            1 |                                0 |

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
