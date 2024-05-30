import pandas as pd

summer = pd.read_csv("summer.csv")
print(summer)

# get first 5 rows and rows 354 and 765
rows = list(range(5)) + [354, 765]
print(rows)

print(summer.iloc[rows])

# get first three columns and the columns "Gender" and "Event"
# print(type(summer.columns[:3].to_list())) 
col = summer.columns[:3].to_list() + ["Gender", "Event"]
print(col)
print(summer.loc[:, col])

# combining position and label-based indexing
print(summer.loc[[200, 300], ["Athlete", "Medal"]])

# label based indexing with index column label
summer = pd.read_csv("summer.csv", index_col = "Athlete")
col = summer.columns[[4, 6]]
print(col)

print(summer.loc["PHELPS, Michael", col])
# print(summer.ix["PHELPS, Michael", [4, 6]]) # deprecated as of pandas 1.0
