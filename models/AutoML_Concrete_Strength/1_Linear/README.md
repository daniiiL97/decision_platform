# Summary of 1_Linear

[<< Go back](../README.md)


## Linear Regression (Linear)
- **n_jobs**: -1
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **random_seed**: 42

## Optimized metric
rmse

## Training time

21.1 seconds

### Metric details:
| Metric   |      Score |
|:---------|-----------:|
| MAE      |   8.19209  |
| MSE      | 109.039    |
| RMSE     |  10.4422   |
| R2       |   0.598419 |
| MAPE     |   0.314062 |



## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature            |    Learner_1 |    Learner_2 |    Learner_3 |    Learner_4 |    Learner_5 |
|:-------------------|-------------:|-------------:|-------------:|-------------:|-------------:|
| CEMENT             |  0.762106    |  0.810355    |  0.83059     |  0.789949    |  0.805425    |
| BLAST_FURNACE_SLAG |  0.579271    |  0.648706    |  0.672024    |  0.593753    |  0.628763    |
| AGE                |  0.43299     |  0.438967    |  0.427602    |  0.469256    |  0.442021    |
| FLY_ASH            |  0.358069    |  0.373153    |  0.387484    |  0.351528    |  0.392963    |
| FINE_AGGREGATE     |  0.127979    |  0.174737    |  0.19386     |  0.155135    |  0.175141    |
| COARSE_AGGREGATE   |  0.0996894   |  0.160842    |  0.172112    |  0.10873     |  0.0965806   |
| SUPERPLASTICIZER   |  0.0999642   |  0.150705    |  0.110263    |  0.0852495   |  0.0581843   |
| intercept          | -1.66837e-16 |  1.68748e-16 | -2.69975e-18 |  4.08433e-16 | -2.15159e-16 |
| WATER              | -0.157976    | -0.0760112   | -0.111747    | -0.166324    | -0.180168    |


## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
