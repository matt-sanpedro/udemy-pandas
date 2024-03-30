import pandas as pd
df = pd.read_csv("titanic.csv")

# print(df.iloc[2, 3])

last_rows = df.iloc[-10:,:2]
print(last_rows)
