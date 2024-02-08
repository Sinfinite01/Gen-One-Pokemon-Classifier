import pandas
from PIL import Image
import matplotlib.pyplot as plt
import os
from torchvision import transforms
import time

# Using the inbuilt pandas function to read a dataframe from a pkl file
pokemon_df = pandas.read_pickle(os.path.join('Data', 'pkl_data', 'pokemon2.pkl'))

# Output the first image in the Abra column
pil_image = None
for image in pokemon_df['Mewtwo']:
    print(image)
    print(type(image))
    to_pil = transforms.ToPILImage()
    pil_image = to_pil(image)
    break
pil_image.show()
pil_image.save('output_image.png')
