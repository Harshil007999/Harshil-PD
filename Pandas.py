import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Alice", "Alex", "Bob", "Charlie"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}) 
print(df1)

df2 = pd.DataFrame({
    "Name": ["Alex", "Bob", "David"],
    "Age": [30, 35, 45]
})
print(df2)

df3 = pd.merge(df1, df2, on = "Age")
print(df3)