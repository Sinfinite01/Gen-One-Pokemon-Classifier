import pandas as pd
import os
from PIL import Image
import numpy as np
import cairosvg
import io
import pickle
from torchvision import transforms
from torch import Tensor




# Takes in a photo and returns a PyTorch Tensor
def photo_to_tensor(dir: str, resize: bool = False, resize_num = int) -> Tensor:
    # Check if the file is an SVG
    if dir.lower().endswith('.svg'):
        # Convert SVG to PNG using cairosvg
        svg_data = open(dir, 'rb').read()
        png_data = cairosvg.svg2png(svg_data)
        img = Image.open(io.BytesIO(png_data))
    else:
        # Open other image formats with PIL
        img = Image.open(dir)

    # Convert image to RGB if it has an alpha channel (RGBA)
    if img.mode == 'P':
        img = img.convert('RGBA')
        img = img.convert('RGB')
    elif img.mode != 'RGB':
        img = img.convert('RGB')

    transform = None
    if resize:
        transform = transforms.Compose([
            transforms.Resize((resize_num, resize_num)),  # Resize the image
            transforms.ToTensor(),           # Convert the image to a PyTorch tensor
        ])
    else:
        transform = transforms.Compose([
            transforms.ToTensor(),           # Convert the image to a PyTorch tensor
        ])
            
    img_array = transform(img)
    return img_array

# Takes in a list of lists then pads them with np.NaN so that they are all the same length
def pad_lists(lists: list) -> list:
    # Find the longest list
    max_length = max(len(li) for li in lists)

    # Pad lists to make them equal with None
    padded_lists = [li + [np.NaN] * (max_length - len(li)) for li in lists]

    return padded_lists

# Function iterates through the original Pokemon data and creates a set 
# of the suffixes of the file types
def set_of_file_types(dir: str) -> set:
    my_set = set({})
    for pokemon_folder in os.listdir(dir):
        for image in os.listdir(os.path.join(dir, pokemon_folder)):
            if image[-4:] == "pg')":
                print("error is here", os.path.join(dir, pokemon_folder, image))
            my_set.add(image[-4:])
    return my_set

# Takes in a directory to the Pokemon dataset, outputs a dataframe
def pokemon_to_df(dir: str, resize_num: int=100) -> pd.DataFrame:
    pokemon_dict = {}
    pokemon = []
    images = []
    for pokemon_folder in os.listdir(dir):
        print(f"processing {pokemon_folder} images...")
        for image in os.listdir(os.path.join(dir, pokemon_folder)):
            images.append(photo_to_tensor(os.path.join(dir, pokemon_folder, image), resize=True, resize_num=resize_num))
            pokemon.append(pokemon_folder)
    pokemon_dict['pokemon'] = pokemon
    pokemon_dict['tensor'] = images
    
    print('Converting to a DataFrame...')
    equal_len_lists = pad_lists(pokemon_dict.values())
    pok_frame = pd.DataFrame(dict(zip(pokemon_dict.keys(), equal_len_lists)))
    one_hot_pok_frame = pd.get_dummies(pok_frame['pokemon'], prefix = 'pokemon')
    pok_frame.pop('pokemon')
    final_pok_frame = pd.concat([pok_frame, one_hot_pok_frame], axis=1)
    return final_pok_frame

# Choosing the dimension to resize the images to make them all uniform
image_size = 100

# Creating a dataframe of pytorch tensors of the pokemon images 
pokemon_df = pokemon_to_df(os.path.join('Data', 'archive', 'PokemonData'), resize_num = image_size)

counter = 1

# Create a Pickle file from the inbuilt dataframe.to_pickle() function
while True:
    file_name = 'pokemon' + str(image_size) + '_' + str(counter) + '.pkl'

    # Check to make sure the file name doesn't already exist
    if file_name not in os.listdir(os.path.join('Data', 'pkl_data')):
        # Create the file and dump to it
        print('Pickle-ing DataFrame...')
        pokemon_df.to_pickle(os.path.join('Data', 'pkl_data', file_name))
        break
    counter += 1