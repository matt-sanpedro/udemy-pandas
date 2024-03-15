import pandas as pd

titanic = pd.read_csv("titanic.csv")

# select specific rows
pd_series = titanic["age"]
print(pd_series) # output -> pandas series
print(type(pd_series)) # output: class 'pandas.core.series.Series'

# select multiple columns (create a list)
# most methods are available for both series and dataframes
print(type(titanic["age"]))             # datatype: series
print(type(titanic[["age", "sex"]]))    # datatype: dataframe
print(titanic[["age", "sex", "fare"]])

# alternative method select one column with dot notation
print(titanic.age)

# equals test whether to objects have same elements
# some people think should NOT use dot notation but can perform with less code
print(titanic.age.equals(titanic["age"]))
print(titanic.embarked)
