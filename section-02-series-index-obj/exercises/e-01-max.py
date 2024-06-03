import pandas as pd

df = pd.read_csv("titanic.csv")

# print highest value in fare column
print(df.fare.max())

# most common/frequent ticket price
print(df.fare.value_counts().index[0])