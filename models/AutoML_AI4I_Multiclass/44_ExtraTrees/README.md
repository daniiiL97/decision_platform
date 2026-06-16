# Summary of 44_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
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

13.7 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                          0 |     0.969416 |                    0 |        0.818182 |                   0 |      0.969 |    0.35752  |       0.944891 |   0.10948 |
| recall    |                          0 |     0.999741 |                    0 |        0.246575 |                   0 |      0.969 |    0.249263 |       0.969    |   0.10948 |
| f1-score  |                          0 |     0.984345 |                    0 |        0.378947 |                   0 |      0.969 |    0.272659 |       0.95532  |   0.10948 |
| support   |                         92 |  7736        |                   62 |       73        |                  37 |      0.969 | 8000        |    8000        |   0.10948 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                       0 |                        90 |                                 0 |                            2 |                                0 |
| Labeled as No_Failure               |                                       0 |                      7734 |                                 0 |                            2 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        62 |                                 0 |                            0 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        55 |                                 0 |                           18 |                                0 |
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
