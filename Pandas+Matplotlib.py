import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
# print(df)
# print(df.columns)
class_type = df["Pclass"].value_counts()

plt.title("Passenger Class Distribution", fontsize = 18.5, fontweight = 'bold')

plt.xlabel("Passenger Class")
plt.ylabel("# of Passengers")

plt.bar(class_type.index, class_type.values)

plt.show()