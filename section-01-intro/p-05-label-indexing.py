import pandas as pd
summer = pd.read_csv("summer.csv", index_col="Athlete")

print(summer.iloc[2])
print(summer.loc["DRIVAS, Dimitrios"])
print(summer.iloc[2].equals(summer.loc["DRIVAS, Dimitrios"])) # True

# pandas can have duplicates with same key
print(summer.loc["PHELPS, Michael"])

# slicing with rows and columns
print(summer.loc[["PHELPS, Michael", "LEWIS, Carl"], ["Medal", "Event"]])

# select all rows and specific columns
# print(summer.loc[:, ["Medal", "Event"]])

print(summer.head(10))

# both left and right boundaries are included
print(summer.loc[:"CHASAPIS, Spiridon"])

# phelps will throw error since non-unique label (duplicate entries)
# print(summer.loc["PHELPS, Michael":])

print(summer.loc["DRIVAS, Dimitrios":"BLAKE, Arthur", "City":"Discipline"])

# will throw error since ther is no "Age" column
print(summer.loc["PHELPS, Michael", ["Year", "Age"]])
