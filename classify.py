import pandas as pd
import os
from PIL import Image
import numpy as np

print(os.getcwd())
print(os.listdir())
print(os.path.join('Data', 'archive', 'dataset'))
print(os.listdir(os.path.join('Data', 'archive', 'dataset')))

# for pokemon_folder in os.listdir(os.path.join('Data', 'archive', 'dataset')):
#     for jpeg in os.listdir(os.path.join('Data', 'archive', 'dataset', pokemon_folder)):
#         if jpeg[-4:] == '.jpg':
#             img = Image.open(os.path.join('Data', 'archive', 'dataset', pokemon_folder, jpeg))

#             # Print Image Info
#             print(img.format)
#             print(img.size)
#             print(img.mode)

#             np_img = np.array(img)
#             print(np_img)
#             print(type(np_img))
#             break
#     break

def photo_to_np(dir: str) -> np.ndarray:
    img = Image.open(dir)
    return np.array(img)

def pad_lists(lists):
    # Find the longest list
    max_length = max(len(li) for li in lists)

    # Pad lists to make them equal with None
    padded_lists = [li + [np.NaN] * (max_length - len(li)) for li in lists]

    return padded_lists

def set_of_file_types(ir: str) -> set:
    my_set = {}
    for pokemon_folder in os.listdir(dir):
        for image in os.listdir(os.path.join(dir, pokemon_folder)):
            my_set.add(image[-4:])
    return my_set

def pokemon_to_df(dir: str) -> pd.DataFrame:
    pokemon_dict = {}
    for pokemon_folder in os.listdir(dir):
        images = []
        for jpeg in os.listdir(os.path.join(dir, pokemon_folder)):
            # The if statement is to exclude the .svg in there
            if jpeg[-4:] == '.jpg':
                images.append(photo_to_np(os.path.join(dir, pokemon_folder, jpeg)))
        pokemon_dict[pokemon_folder] = images
    
    equal_len_lists = pad_lists(pokemon_dict.values())
    test_frame = pd.DataFrame(dict(zip(pokemon_dict.keys(), equal_len_lists)))
    return test_frame

pokemon_df = pokemon_to_df(os.path.join('Data', 'archive', 'dataset'))
print(pokemon_df)
print(set_of_file_types(os.path.join('Data', 'archive', 'dataset')))