import pandas as pd

df = pd.read_csv("titanic.csv")

fare = df.fare
print(fare)