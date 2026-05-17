import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic-Dataset.csv')

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Titanic Data Analysis', fontsize=16)


survival_counts = df['Survived'].value_counts()
axes[0, 0].bar(['Died', 'Survived'], survival_counts.values, color=['red', 'green'])
axes[0, 0].set_title('Survived vs Died')
axes[0, 0].set_ylabel('Count')


gender_survival = df.groupby('Sex')['Survived'].mean() * 100
axes[0, 1].barh(['Female', 'Male'], gender_survival.values, color=['pink', 'blue'])
axes[0, 1].set_title('Survival Rate by Gender %')
axes[0, 1].set_xlabel('Survival Rate %')


axes[0, 2].hist(df['Age'].dropna(), bins=20, color='purple', edgecolor='black')
axes[0, 2].set_title('Age Distribution')
axes[0, 2].set_xlabel('Age')
axes[0, 2].set_ylabel('Count')


class_survival = df.groupby('Pclass')['Survived'].mean() * 100
axes[1, 0].bar(['1st Class', '2nd Class', '3rd Class'], class_survival.values, color=['gold', 'silver', 'brown'])
axes[1, 0].set_title('Survival Rate by Class %')
axes[1, 0].set_ylabel('Survival Rate %')


for pclass in [1, 2, 3]:
    axes[1, 1].hist(df[df['Pclass'] == pclass]['Fare'], bins=20, alpha=0.5, label=f'Class {pclass}')
axes[1, 1].set_title('Fare Distribution by Class')
axes[1, 1].set_xlabel('Fare')
axes[1, 1].set_ylabel('Count')
axes[1, 1].legend()


embarked_counts = df['Embarked'].value_counts()
axes[1, 2].bar(embarked_counts.index, embarked_counts.values, color=['orange', 'teal', 'cyan'])
axes[1, 2].set_title('Passengers by Embarkation Point')
axes[1, 2].set_ylabel('Count')

plt.tight_layout()
plt.show()
