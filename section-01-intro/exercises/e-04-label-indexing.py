import pandas as pd

df = pd.read_csv("summer.csv", index_col="Athlete")

# problem 1
print(df.loc["UNDA, Maider", "Event"])
print(df.loc["OCHAL, Glenn", "Event"])

# problem 2
sliced = df.loc[["PAVIA, Automne", "OCHAL, Glenn"], ["Country", "Sport"]]
print(sliced)
