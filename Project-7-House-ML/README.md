## Project 7 — House Price Prediction (ML)

### About
End-to-end regression ML project predicting house prices using 
Python and Scikit-learn. Follows a complete ML pipeline from 
raw data to evaluated model.

### Pipeline
1. Exploratory Data Analysis (6 charts)
2. Data cleaning (removed zero price outliers)
3. Train/Validation/Test split
4. Preprocessing (imputation and scaling)
5. Baseline model (mean prediction)
6. Model comparison (Linear Regression vs Random Forest)
7. Feature importance analysis
8. Final evaluation on unseen test data

### Results
| Model | Val RMSE |
|-------|----------|
| Baseline (mean) | $386,485 |
| Linear Regression | $237,512 |
| Random Forest (no limit) | $243,650 |
| Random Forest (max_depth=10) | $239,881 |
| Final Test RMSE | $248,834 |

### Tools Used
- Python, Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn

### Key Findings
- sqft_living is the strongest predictor of house price with 0.52 importance
- Linear Regression outperformed Random Forest on this dataset
- Removing zero price outliers was critical for accurate evaluation
- Model beats baseline by $137,000 RMSE