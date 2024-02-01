import pandas
from PIL import Image
import matplotlib.pyplot as plt
import os
import numpy as np

def show_image(image_array):
    img = Image.fromarray(image_array)
    img.show()

pokemon_df = pandas.read_csv(os.path.join('Data', 'csv_data', 'pokemon.csv'))

print(pokemon_df)

for image in pokemon_df['Abra']:
    print(type(np.fromstring(image)))
    break


