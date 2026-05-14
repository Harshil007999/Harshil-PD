import pandas as pd


df = pd.read_csv("Titanic-Dataset.csv")


print("Shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())


total = len(df)
print(f"\n1. Total passengers: {total}")


counts = df['Survived'].value_counts()
print(f"\n2. Survived: {counts[1]} | Died: {counts[0]}")


rate = df['Survived'].mean() * 100
print(f"\n3. Survival rate: {rate:.2f}%")


avg_age = df.groupby('Survived')['Age'].mean()
print(f"\n4. Avg age - Survived: {avg_age[1]:.1f} | Died: {avg_age[0]:.1f}")


gender = df.groupby('Sex')['Survived'].mean() * 100
print(f"\n5. Female survival: {gender['female']:.1f}% | Male: {gender['male']:.1f}%")


pclass = df.groupby('Pclass')['Survived'].mean() * 100
print(f"\n6. Class survival rates:\n{pclass}")


gender_count = df['Sex'].value_counts()
print(f"\n7. Gender count:\n{gender_count}")


idx = df['Fare'].idxmax()
row = df.loc[idx, ['Name', 'Fare', 'Pclass']]
print(f"\n8. Most expensive ticket:\n{row}")


fare = df.groupby('Pclass')['Fare'].mean()
print(f"\n9. Avg fare by class:\n{fare}")


df['AgeGroup'] = df['Age'].apply(lambda x: 'Child' if x < 18 else 'Adult')
age_survival = df.groupby('AgeGroup')['Survived'].mean() * 100
print(f"\n10. Age group survival:\n{age_survival}")