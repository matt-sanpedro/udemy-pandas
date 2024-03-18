"""
INDEXING
In Pandas, there are two ways of indexing:
[EXAMPLE]
nationality     club    world_champion  height  goals

[1] ZERO-BASED INDEXING
0               1       2               3       4

[2] NEGATIVE-BASED INDEXING
-5              -4      -3              -2      -1
"""
import pandas as pd

summer = pd.read_csv("summer.csv", index_col="Athlete")
print("\n---SUMMER PREVIEW---")
print(summer)

print("\n---SUMMER INFO---")
summer.info()

# selecting rows with iloc
print(summer.iloc[1])

# check data type
print(type(summer.iloc[1]))

# negative indexing
print(summer.iloc[-1])

# get 3 rows by passing a list or perform slicing
print(summer.iloc[:5])

# get last 5 rows
print(summer.iloc[-5:])

# get all the rows
print(summer.iloc[:])

# list with index position that are not neighbors
print(summer.iloc[[2, 45, 5469]])
