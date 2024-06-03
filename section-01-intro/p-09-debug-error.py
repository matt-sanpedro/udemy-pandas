# dataset: five most successful athletes in summer olympic games (medals)
my_dict = {
    "Phelps, Michael": 22,
    "Latynina, Larisa": 18,
    "Andrianov, Nikolay": 15,
    "Mangiarotti, Edoardo": 13,
    "Ono, Takashi": 13
}
print(my_dict)

# question 1: how many medlas did Michael Phelps win in his career
print(my_dict["Phelps, Michael"])

# question 2: how many medals did Micahel Phelps and Takashi Ono win together?
print(my_dict["Phelps, Michael"] + my_dict["Ono, Takashi"])

# question 3: how many medals did Michael Phelps win more than Larisa Latynina
print(my_dict["Phelps, Michael"] - my_dict["Latynina, Larisa"])

# question 4: store the dataset in a Pandas series
import pandas as pd
my_series = pd.Series(my_dict)
print(type(my_series))
print(my_series)
