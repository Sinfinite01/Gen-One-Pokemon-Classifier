import pandas as pd
import os
from PIL import Image
import numpy as np
import cairosvg
import io



# print(os.getcwd())
# print(os.listdir())
# print(os.path.join('Data', 'archive', 'dataset'))
# print(os.listdir(os.path.join('Data', 'archive', 'dataset')))

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
    try:
        # Check if the file is an SVG
        if dir.lower().endswith('.svg'):
            # Convert SVG to PNG using cairosvg
            svg_data = open(dir, 'rb').read()
            png_data = cairosvg.svg2png(svg_data)
            img = Image.open(io.BytesIO(png_data))
        else:
            # Open other image formats with PIL
            img = Image.open(dir)
        img_array = np.array(img)
        return img_array
    except Exception as e:
        print(f"Error opening image: {e}")
        return None

def pad_lists(lists):
    # Find the longest list
    max_length = max(len(li) for li in lists)

    # Pad lists to make them equal with None
    padded_lists = [li + [np.NaN] * (max_length - len(li)) for li in lists]

    return padded_lists

def set_of_file_types(dir: str) -> set:
    my_set = set({})
    for pokemon_folder in os.listdir(dir):
        for image in os.listdir(os.path.join(dir, pokemon_folder)):
            if image[-4:] == "pg')":
                print("error is here", os.path.join(dir, pokemon_folder, image))
            my_set.add(image[-4:])
    return my_set

def pokemon_to_df(dir: str) -> pd.DataFrame:
    pokemon_dict = {}
    for pokemon_folder in os.listdir(dir):
        images = []
        for jpeg in os.listdir(os.path.join(dir, pokemon_folder)):
            images.append(photo_to_np(os.path.join(dir, pokemon_folder, jpeg)))
        pokemon_dict[pokemon_folder] = images
    
    equal_len_lists = pad_lists(pokemon_dict.values())
    test_frame = pd.DataFrame(dict(zip(pokemon_dict.keys(), equal_len_lists)))
    return test_frame

def df_to_csv(df: pd.DataFrame, dir: str, name: str):
    output_directory = dir

    output_filename = name + '.csv'

    output_path = output_directory + '/' + output_filename

    # Output the DataFrame to a CSV file in the specified directory
    df.to_csv(output_path, index=False)
    return None

pokemon_df = pokemon_to_df(os.path.join('Data', 'archive', 'dataset'))
print(pokemon_df)
print(set_of_file_types(os.path.join('Data', 'archive', 'dataset')))
df_to_csv(pokemon_df, os.path.join('Data', 'csv_data'), 'pokemon1')