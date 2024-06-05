import pandas as pd
import numpy as np

# import entire csv file as dataframe
summer = pd.read_csv("summer.csv")
print(summer.head())
print(summer["Athlete"].equals(summer.Athlete))
print(summer.iloc[0]) # series - first row of dataframe

# can import specific columns from csv and can convert to pandas series
athlete_df = pd.read_csv("summer.csv", usecols=["Athlete"], )
print(type(athlete_df)) # dataframe
print(type(athlete_df.squeeze())) # series
athlete_series = athlete_df.squeeze()
print(athlete_df.head())
print(athlete_series.head())
print(athlete_df.index)         # RangeIndex(start=0, stop=31165, step=1)
print(athlete_series.index)     # RangeIndex(start=0, stop=31165, step=1)

# create a pandas series from scratch
print(pd.Series([10, 25, 6, 36, 2]))
print(pd.Series([10, 25, 6, 36, 2], index=["Mon", "Tue", "Wed", "Thu", "Fri"]))
print(pd.Series([10, 25, 6, 36, 2], index=["Mon", "Tue", "Wed", "Thu", "Fri"], name="Sales"))

# create a pandas series using numpy
sales = np.array([10, 25, 6, 36, 2])
print(sales)
sales_series = pd.Series(sales)
print(sales_series)

# transform a dictionary to a pandas series
sales_dict = {"Mon": 10, "Tue": 25, "Wed": 6, "Thu": 36, "Fri": 2}
sales_dseries = pd.Series(sales_dict)
print(sales_dseries)
# new labels will not have values (ie. Sat and Sun)
print(pd.Series(sales_dict, index=["Fri", "Sat", "Sun", "Mon", "Tue", "Wed"]))
# passing all new indices will result in series with no value
print(pd.Series(sales_dict, index=[1,2,3,4,5]))
