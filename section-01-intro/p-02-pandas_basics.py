import pandas as pd

titanic = pd.read_csv("titanic.csv")

# object is an instance of the pandas class dataframe
print(type(titanic)) 

# can use the len function
print(len(titanic)) # 891 -> amount of rows

# round function for int and float values
print(round(titanic))

# min function will return column name at alphabetical pov
print(min(titanic)) # age
