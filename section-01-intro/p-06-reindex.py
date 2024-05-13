import pandas as pd

# summer = pd.read_csv("summer.csv", index_col="Athlete")
# # cannot use reindex method with duplicate indices
# print(summer.reindex(["PHELPS, Michael"], columns = ["Medal", "Age"]))

# reindex method: conforms DataFrame to new index with optional filling logic
summer = pd.read_csv("summer.csv")

# warning: loc method will throw error if index is out of range
print(summer.loc[[0, 5, 30000], ["Athlete", "Medal"]])

# best practice: if in doubt of index number, reindex will NOT throw error
# note: age values will return NaN since it was nonexistent before
new_df = summer.reindex(index = [0, 5, 30000, 40000], columns = ["Athlete", "Medal", "Age"])
print(new_df)

# can use rename method to rename columns
new_df.rename(columns={"Athlete": "AthleteName"}, inplace=True)
print(new_df)

# # warning: cannot index with duplicate axis, below will throw error
# summer_athlete_df = pd.read_csv("summer.csv", index_col="Athlete")
# summer_athlete_df.reindex(index=["PHELPS, Michael"], columns=["Medal", "Age"])
