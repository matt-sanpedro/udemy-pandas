import pandas as pd

summer = pd.read_csv("summer.csv", index_col="Athlete")
# summer = pd.read_csv("summer.csv")

# print(summer.loc[[0, 5, 30000], ["Athlete", "Medal"]])

# print(summer.reindex(index = [0, 5, 30000, 40000], columns = ["Athlete", "Medal", "Age"]))

# cannot use reindex method with duplicate indices
print(summer.reindex(["PHELPS, Michael"], columns = ["Medal", "Age"]))
