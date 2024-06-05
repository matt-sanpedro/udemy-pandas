# analyzing non-numerical pandas series with unique, nunique, value_counts
import pandas as pd
summer = pd.read_csv("summer.csv")

print(summer.head())
summer.info()
athlete = summer["Athlete"]
print(athlete.head())
print(athlete.tail())

print(athlete.equals(summer.Athlete)) # True

print(athlete.dtype)
print(athlete.shape)
print(athlete.describe())

print(athlete.size) # total size of series
print(athlete.count()) # total non-null values

print(athlete.min()) # returns alphabetically first athlete
print(athlete.unique())
print(len(athlete.unique())) # 22762 unique athletes
print(athlete.nunique(dropna=False))     # 22762 unique athletes

print(athlete.value_counts())
print(athlete.value_counts(sort=True, ascending=True))
print(athlete.value_counts(sort=True, ascending=False, normalize=True))
