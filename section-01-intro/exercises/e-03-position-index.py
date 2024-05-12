import pandas as pd
df = pd.read_csv("titanic.csv")
"""
Select and save the last 10 rows (and only the first two columns)
in the variable last_rows
"""

# print(df.iloc[2, 3])

last_rows = df.iloc[-10:,:2]
print(last_rows)

# investigate syntax
print("--- INVESTIGATE ---")
print(df.iloc[-10:,:5])
