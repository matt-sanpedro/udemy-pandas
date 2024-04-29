import pandas as pd

# importing from CSV and first inspection
summer = pd.read_csv("summer.csv", index_col="Athlete")

print(summer)
print(summer.info())

# select one column
print(summer.Medal)
print(summer["Medal"])

# select multiple columns: best to use loc
print(summer[["Year", "Medal"]])
print(summer.loc[:, ["Year", "Medal"]])

# select positional rows
print(summer.iloc[10:21])

# select labeled rows
print(summer.loc["LEWIS, Carl"])

# putting it all together
# example 1: works but can cause problems (2 operations)
print(summer[["Year", "Event", "Medal"]].loc["LEWIS, Carl"])

# example 2: chained indexing can cause problems (2 operations)
print(summer.loc["LEWIS, Carl"][["Year", "Event", "Medal"]])

# example 3: best practice because only ONE indexing operation
print(summer.loc["LEWIS, Carl", ["Year", "Event", "Medal"]])

# outlook on pandas objects
print(type(summer)) # pandas dataframe
print(type(summer["Year"])) # pandas series
print(summer.index)
print(type(summer.index)) # pandas index
print(summer.columns)
print(type(summer.columns)) # pandas index
