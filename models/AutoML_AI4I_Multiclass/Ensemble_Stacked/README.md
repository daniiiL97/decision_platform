# Summary of Ensemble_Stacked

[<< Go back](../README.md)


## Ensemble structure
| Model                                                           |   Weight |
|:----------------------------------------------------------------|---------:|
| 17_LightGBM                                                     |        1 |
| 23_LightGBM                                                     |        3 |
| 2_Default_Xgboost_GoldenFeatures_SelectedFeatures_BoostOnErrors |        2 |
| 2_Default_Xgboost_GoldenFeatures_SelectedFeatures_Stacked       |       40 |
| 54_NeuralNetwork                                                |        1 |
| 58_NeuralNetwork                                                |        3 |
| 67_LightGBM_GoldenFeatures                                      |        1 |
| 68_LightGBM_GoldenFeatures_SelectedFeatures                     |        1 |
| Ensemble                                                        |       16 |

### Metric details
|           |   Heat_Dissipation_Failure |   No_Failure |   Overstrain_Failure |   Power_Failure |   Tool_Wear_Failure |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------------------------:|-------------:|---------------------:|----------------:|--------------------:|-----------:|------------:|---------------:|----------:|
| precision |                   0.965517 |     0.992416 |             0.927273 |        0.833333 |                   0 |   0.990125 |    0.743708 |       0.985561 | 0.0368944 |
| recall    |                   0.913043 |     0.998061 |             0.822581 |        0.890411 |                   0 |   0.990125 |    0.724819 |       0.990125 | 0.0368944 |
| f1-score  |                   0.938547 |     0.995231 |             0.871795 |        0.860927 |                   0 |   0.990125 |    0.7333   |       0.987794 | 0.0368944 |
| support   |                  92        |  7736        |            62        |       73        |                  37 |   0.990125 | 8000        |    8000        | 0.0368944 |


## Confusion matrix
|                                     |   Predicted as Heat_Dissipation_Failure |   Predicted as No_Failure |   Predicted as Overstrain_Failure |   Predicted as Power_Failure |   Predicted as Tool_Wear_Failure |
|:------------------------------------|----------------------------------------:|--------------------------:|----------------------------------:|-----------------------------:|---------------------------------:|
| Labeled as Heat_Dissipation_Failure |                                      84 |                         6 |                                 0 |                            2 |                                0 |
| Labeled as No_Failure               |                                       2 |                      7721 |                                 3 |                           10 |                                0 |
| Labeled as Overstrain_Failure       |                                       1 |                        10 |                                51 |                            0 |                                0 |
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
