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

# ATTRIBUTES (stored in the object)
print(titanic.shape) # (rows, cols)
print(titanic.size) # all elements in dataframe (rows * cols)
print(titanic.index)
print(titanic.columns)

# DATAFRAME METHODS
print(titanic.head(n = 2))
titanic.info()
print(titanic.min(numeric_only=True))

# METHOD CHAINING
print(titanic.mean(numeric_only=True).sort_values())

# SORTING COLUMNS
print(titanic.sort_values(by="age"))
