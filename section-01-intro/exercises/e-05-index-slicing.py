import pandas as pd

cars = pd.read_csv("cars.csv")

# inspect
print(cars)
print(cars.info())
print("INDEX: ", cars.index)

# selecting columns
print(cars.name[393])
print(cars["name"][393])

# select all columns on index 100 with iloc method
print(cars.iloc[100])

# select name column on index 200 with iloc method
print(cars.iloc[200, 8])
print(cars.iloc[200]["name"])

# test for equality
print(cars.tail(10))
print(cars.iloc[-10:])
print(cars.tail(10).equals(cars.iloc[-10:])) # True

# Select the last 10 rows and the columns mpg, horsepower, origin and name with the iloc operator
print(cars.iloc[-10:][["mpg", "horsepower", "origin", "name"]])
print(cars.iloc[-10:, [0, 3, 7, 8]])


# import dataset and set column name as index
cars = pd.read_csv("cars.csv", index_col="name")

# inspect
print(cars)
print(cars.info())
print("INDEX: ", cars.index)

# select the row with index label "ford ranger" with loc operator
print(cars.loc["ford ranger"])

# select the row with the index label "ford torino" and only the columns "model_year" and "origin"
print(cars.loc[["ford torino"], ["model_year", "origin"]])
print(cars.loc["ford torino", ["model_year", "origin"]])

# select the columns "mpg" and "weight" (all rows) with the loc operator!
print(cars.loc[:, ["mpg", "weight"]])
