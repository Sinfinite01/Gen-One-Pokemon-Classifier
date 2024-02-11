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
    for pokemon_folder in os.listdir(dir):
        images = []
        print(f"processing {pokemon_folder} images...")
        for image in os.listdir(os.path.join(dir, pokemon_folder)):
            images.append(photo_to_tensor(os.path.join(dir, pokemon_folder, image), resize=True, resize_num=resize_num))
        pokemon_dict[pokemon_folder] = images
    
    equal_len_lists = pad_lists(pokemon_dict.values())
    test_frame = pd.DataFrame(dict(zip(pokemon_dict.keys(), equal_len_lists)))
    return test_frame

# Choosing the dimension to resize the images to make them all uniform
image_size = 400

# Creating a dataframe of pytorch tensors of the pokemon images 
pokemon_df = pokemon_to_df(os.path.join('Data', 'archive', 'dataset'), resize_num = image_size)

counter = 1

# Create a Pickle file from the inbuilt dataframe.to_pickle() function
while True:
    file_name = 'pokemon' + str(image_size) + '_' + str(counter) + '.pkl'

    # Check to make sure the file name doesn't already exist
    if file_name not in os.listdir(os.path.join('Data', 'pkl_data')):
        # Create the file and dump to it
        pokemon_df.to_pickle(os.path.join('Data', 'pkl_data', file_name))
        break
    counter += 1