# Summary of 20_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: multiclass
- **num_leaves**: 63
- **learning_rate**: 0.2
- **feature_fraction**: 0.5
- **bagging_fraction**: 0.8
- **min_data_in_leaf**: 30
- **metric**: multi_logloss
- **custom_eval_metric_name**: None
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

8.9 seconds

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.923077 |     0.978926 |             0.666667 |        0.642857 |           0.222222  |    0.97425 |    0.68675  |       0.969297 | 0.0876446 |
| recall    |                   0.26087  |     0.996768 |             0.193548 |        0.616438 |           0.0540541 |    0.97425 |    0.424336 |       0.97425  | 0.0876446 |
| f1-score  |                   0.40678  |     0.987767 |             0.3      |        0.629371 |           0.0869565 |    0.97425 |    0.482175 |       0.968318 | 0.0876446 |
| support   |                  92        |  7736        |            62        |       73        |          37         |    0.97425 | 8000        |    8000        | 0.0876446 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      24 |                        64 |                                 0 |                            3 |                                1 |
| Labeled as No_Failure               |                                       2 |                      7711 |                                 4 |                           16 |                                3 |
| Labeled as Overstrain_Failure       |                                       0 |                        42 |                                12 |                            6 |                                2 |
| Labeled as Power_Failure            |                                       0 |                        26 |                                 1 |                           45 |                                1 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        34 |                                 1 |                            0 |                                2 |

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
