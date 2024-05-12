import pandas as pd

# summer = pd.read_csv("summer.csv", index_col="Athlete")
# # cannot use reindex method with duplicate indices
# print(summer.reindex(["PHELPS, Michael"], columns = ["Medal", "Age"]))

# reindex method: conforms DataFrame to new index with optional filling logic
summer = pd.read_csv("summer.csv")
print(summer.loc[[0, 5, 30000], ["Athlete", "Medal"]])
new_df = summer.reindex(index = [0, 5, 30000, 40000], columns = ["Athlete", "Medal", "Age"])
print(new_df)

# can use rename method to rename columns
new_df.rename(columns={"Athlete": "AthleteName"}, inplace=True)
print(new_df)
