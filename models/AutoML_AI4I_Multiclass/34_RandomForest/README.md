# Summary of 34_RandomForest

[<< Go back](../README.md)


## Random Forest
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

17.6 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.958333 |     0.981686 |             0.692308 |        0.746032 |                   0 |    0.97875 |    0.675672 |       0.972484 | 0.0606453 |
| recall    |                   0.5      |     0.997802 |             0.290323 |        0.643836 |                   0 |    0.97875 |    0.486392 |       0.97875  | 0.0606453 |
| f1-score  |                   0.657143 |     0.989679 |             0.409091 |        0.691176 |                   0 |    0.97875 |    0.549418 |       0.974054 | 0.0606453 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |    0.97875 | 8000        |    8000        | 0.0606453 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      46 |                        41 |                                 3 |                            2 |                                0 |
| Labeled as No_Failure               |                                       2 |                      7719 |                                 2 |                           13 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        43 |                                18 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        25 |                                 1 |                           47 |                                0 |
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
