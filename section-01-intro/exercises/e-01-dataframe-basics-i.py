import pandas as pd

# import cars dataset
cars = pd.read_csv("cars.csv")

# inspect first 10 rows of the dataframe cars
print(cars.head(10))

# inspect last 5 rows
print(cars.tail(5))

# inspect entire dataframe
pd.options.display.max_rows = 400
print(cars)

# get meta information on dataframe
cars.info()

# get summary statistics on dataframe
print(cars.describe())
