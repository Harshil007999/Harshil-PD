import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Titanic-Dataset.csv')

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Titanic Deep Analysis — Seaborn', fontsize=16)


sns.countplot(data=df, x='Sex', hue='Survived', ax=axes[0, 0], palette='Set1')
axes[0, 0].set_title('Survival Count by Gender')
axes[0, 0].legend(['Died', 'Survived'])


sns.countplot(data=df, x='Pclass', hue='Survived', ax=axes[0, 1], palette='Set2')
axes[0, 1].set_title('Survival Count by Class')
axes[0, 1].legend(['Died', 'Survived'])


sns.histplot(data=df, x='Age', hue='Survived', bins=20, kde=True, ax=axes[0, 2])
axes[0, 2].set_title('Age Distribution by Survival')


sns.boxplot(data=df, x='Pclass', y='Fare', hue='Survived', ax=axes[1, 0])
axes[1, 0].set_title('Fare by Class and Survival')


sns.barplot(data=df, x='Pclass', y='Fare', hue='Survived', ax=axes[1, 1])
axes[1, 1].set_title('Average Fare by Class and Survival')


numeric_df = df[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']]
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=axes[1, 2])
axes[1, 2].set_title('Correlation Heatmap')


plt.tight_layout()
plt.show()