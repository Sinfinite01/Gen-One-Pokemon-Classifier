import pandas
import os
from torchvision import transforms
import time

start_time = time.time()

# Using the inbuilt pandas function to read a dataframe from a pkl file
pokemon_df = pandas.read_pickle(os.path.join('Data', 'pkl_data', 'pokemon100_3.pkl'))

one_hot_pokemon = pandas.get_dummies(pokemon_df['pokemon'], prefix = 'pokemon')

print(one_hot_pokemon.head(5))