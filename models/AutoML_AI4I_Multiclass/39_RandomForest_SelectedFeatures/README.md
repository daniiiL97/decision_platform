# Summary of 39_RandomForest_SelectedFeatures

[<< Go back](../README.md)


## Random Forest
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

21.0 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.909091 |     0.982188 |             0.8      |        0.770492 |                   0 |   0.979375 |    0.692354 |       0.973461 | 0.0598693 |
| recall    |                   0.434783 |     0.997932 |             0.451613 |        0.643836 |                   0 |   0.979375 |    0.505633 |       0.979375 | 0.0598693 |
| f1-score  |                   0.588235 |     0.989997 |             0.57732  |        0.701493 |                   0 |   0.979375 |    0.571409 |       0.974968 | 0.0598693 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.979375 | 8000        |    8000        | 0.0598693 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      40 |                        50 |                                 1 |                            1 |                                0 |
| Labeled as No_Failure               |                                       3 |                      7720 |                                 1 |                           12 |                                0 |
| Labeled as Overstrain_Failure       |                                       1 |                        32 |                                28 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        23 |                                 3 |                           47 |                                0 |
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
