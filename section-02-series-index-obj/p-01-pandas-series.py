import pandas as pd

titanic = pd.read_csv("titanic.csv")
print(titanic)

print(type(titanic["age"]))
print(titanic["age"])

# assigning the series to variable and calling methods
age = titanic["age"]
print(age.equals(titanic.age))
print(age.head())
print(age.tail())
print(age.dtype)
print(age.shape)
print(len(age))
print(age.index)
age.info()
print(age.to_frame())
print(age) # series dtype

# analyzing numerical series
print(age.describe()) # count: sum of elements with non-null values
print("COUNT: ", age.count())
print(age.size)
print(age.sum())
print(age.sum(skipna = False)) # returns -> nan (cannot resolve null values)
print(sum(age)) # returns -> nan (cannot handle missing values)
print(age.min())
print(age.max())
print(age.mean())
print(age.median()) # median calculates the 50 percentile
print(age.unique()) # returned in order of appearance in series
print(len(age.unique())) # returns -> 89
print((age.nunique(dropna = True))) # returns -> 88 (excludes NA values)
print(age.value_counts(sort = True, dropna = False)) # returns -> series of unique value counts
print(age.value_counts(ascending = True, normalize = True)) # normalize set to True returns frequency of occurence
print(age.value_counts(bins = 5)) # bins returns counts for each interval
