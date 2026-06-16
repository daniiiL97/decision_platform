# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                                                           |   Weight |
|:----------------------------------------------------------------|---------:|
| 17_LightGBM                                                     |        6 |
| 22_LightGBM                                                     |        4 |
| 23_LightGBM                                                     |        9 |
| 2_Default_Xgboost_GoldenFeatures_SelectedFeatures_BoostOnErrors |       42 |
| 2_Default_Xgboost_categorical_mix                               |        3 |
| 2_Default_Xgboost_categorical_mix_KMeansFeatures                |        1 |
| 53_NeuralNetwork                                                |        1 |
| 54_NeuralNetwork                                                |        4 |
| 57_NeuralNetwork                                                |        2 |
| 58_NeuralNetwork                                                |       11 |
| 67_LightGBM_GoldenFeatures                                      |        6 |
| 68_LightGBM_GoldenFeatures_SelectedFeatures                     |        3 |

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.965909 |     0.992036 |             0.903846 |        0.866667 |                   0 |       0.99 |    0.745692 |       0.98532  | 0.0390148 |
| recall    |                   0.923913 |     0.99832  |             0.758065 |        0.890411 |                   0 |       0.99 |    0.714142 |       0.99     | 0.0390148 |
| f1-score  |                   0.944444 |     0.995168 |             0.824561 |        0.878378 |                   0 |       0.99 |    0.72851  |       0.987594 | 0.0390148 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |       0.99 | 8000        |    8000        | 0.0390148 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      85 |                         5 |                                 1 |                            1 |                                0 |
| Labeled as No_Failure               |                                       2 |                      7723 |                                 3 |                            8 |                                0 |
| Labeled as Overstrain_Failure       |                                       1 |                        14 |                                47 |                            0 |                                0 |
| Labeled as Power_Failure            |                                       0 |                         8 |                                 0 |                           65 |                                0 |
| Labeled as Tool_Wear_Failure        |                                       0 |                        35 |                                 1 |                            1 |                                0 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Precision Recall Curve

![Precision Recall Curve](precision_recall_curve.png)



[<< Go back](../README.md)
