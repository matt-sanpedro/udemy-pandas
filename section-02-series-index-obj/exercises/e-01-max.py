import pandas as pd

df = pd.read_csv("titanic.csv")
print(df)

# print highest value in fare column
print(df.fare.max())

# most common/frequent ticket price
print(df.fare.value_counts().index[0])

# number of unique fare costs
print(df.fare.unique())
print(len(df.fare.unique()))
print(df.fare.nunique())
print(df.fare.describe())
