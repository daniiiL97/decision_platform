# Summary of 42_RandomForest

[<< Go back](../README.md)


## Random Forest
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

22.4 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   1        |     0.976735 |             0.555556 |        0.769231 |                   0 |     0.9745 |    0.660304 |       0.967328 | 0.0686693 |
| recall    |                   0.228261 |     0.998578 |             0.16129  |        0.547945 |                   0 |     0.9745 |    0.387215 |       0.9745   | 0.0686693 |
| f1-score  |                   0.371681 |     0.987536 |             0.25     |        0.64     |                   0 |     0.9745 |    0.449843 |       0.966999 | 0.0686693 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |     0.9745 | 8000        |    8000        | 0.0686693 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      21 |                        68 |                                 2 |                            1 |                                0 |
| Labeled as No_Failure               |                                       0 |                      7725 |                                 1 |                           10 |                                0 |
| Labeled as Overstrain_Failure       |                                       0 |                        51 |                                10 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        30 |                                 3 |                           40 |                                0 |
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
