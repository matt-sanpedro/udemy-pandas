import pandas as pd

my_dict = {
    "Name": ["Lionel Messi", "Cristiano Ronaldo", "Neymay Junior", "Kylian Mbappe", "Manuel Neuer"],
    "Nationality": ["Argentina", "Portugal", "Brasil", "France", "Germany"],
    "Club": ["FC Barcelona", "Juventus FC", "Paris SG", "Paris SG", "FC Bayern"],
    "World_Champion": [False, False, False, True, True],
    "Goals_2018": [45, 44, 28, 21, 0]
}
df = pd.DataFrame(data = my_dict)
print(df)

# similar to index_col when reading csv and convertikng to dataframe
df.set_index("Name", inplace=True)
print(df)
print(df.loc["Lionel Messi"])

animals = ["cat", "dog", "elephant"]
# change the sequence
animals.append("mouse")
print(animals)
animals.reverse()
print(animals)
animals.pop(-1)
print(animals)
