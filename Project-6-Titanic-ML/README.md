## Project 6 — Titanic Survival Prediction (ML)

### About
End-to-end machine learning project predicting Titanic survival 
using Python and Scikit-learn. Follows a complete ML pipeline 
from raw data to evaluated model.

### Pipeline
1. Exploratory Data Analysis
2. Feature Engineering (Title, FamilySize, IsAlone, AgeGroup)
3. Data Preprocessing (imputation, scaling, encoding)
4. Baseline models
5. Model comparison (LR vs Decision Tree vs Random Forest)
6. Feature importance analysis
7. Final evaluation on unseen test data

### Results
| Model | Validation Accuracy |
|-------|-------------------|
| Baseline (majority) | 59.3% |
| Logistic Regression | 86.4% |
| Decision Tree | 80.2% |
| Random Forest | 82.7% |
| Final Test Accuracy | 84.4% |

### Tools Used
- Python, Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn

### Key Findings
- Logistic Regression outperformed Random Forest on this dataset
- Model beats baseline by 27% showing genuine learning
- Title and Sex were most important features for survival prediction