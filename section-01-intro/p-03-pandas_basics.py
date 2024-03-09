import pandas as pd

titanic = pd.read_csv("titanic.csv")

# select specific rows
pd_series = titanic["age"]
print(pd_series) # output -> pandas series
print(type(pd_series)) # output: class 'pandas.core.series.Series'

# select multiple columns
print(type(titanic["age"]))             # datatype: series
print(type(titanic[["age", "sex"]]))    # datatype: dataframe
print(titanic[["age", "sex", "fare"]])
