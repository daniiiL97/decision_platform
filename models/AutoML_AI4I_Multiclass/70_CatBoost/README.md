# Summary of 70_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 4
- **rsm**: 0.8
- **loss_function**: MultiClass
- **eval_metric**: MultiClass
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

45.8 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.944444 |     0.98733  |             0.75     |        0.779661 |                   0 |     0.9835 |    0.692287 |       0.978537 | 0.0511414 |
| recall    |                   0.73913  |     0.997285 |             0.629032 |        0.630137 |                   0 |     0.9835 |    0.599117 |       0.9835   | 0.0511414 |
| f1-score  |                   0.829268 |     0.992283 |             0.684211 |        0.69697  |                   0 |     0.9835 |    0.640546 |       0.980737 | 0.0511414 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |     0.9835 | 8000        |    8000        | 0.0511414 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      68 |                        19 |                                 3 |                            2 |                                0 |
| Labeled as No_Failure               |                                       4 |                      7715 |                                 4 |                           10 |                                3 |
| Labeled as Overstrain_Failure       |                                       0 |                        22 |                                39 |                            1 |                                0 |
| Labeled as Power_Failure            |                                       0 |                        23 |                                 4 |                           46 |                                0 |
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
