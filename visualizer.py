import pandas
from PIL import Image
import matplotlib.pyplot as plt
import os
import numpy as np
import pickle


# def is_pickle_file_corrupted(file_path):
#     # Check if the file exists
#     if not os.path.exists(file_path):
#         print(f"File '{file_path}' not found.")
#         return True  # File does not exist, consider it corrupted
    
#     # Check if the file is empty
#     if os.path.getsize(file_path) == 0:
#         print(f"File '{file_path}' is empty.")
#         return True  # File is empty, consider it corrupted
    
#     try:
#         # Open the file in binary mode
#         with open(file_path, 'rb') as f:
#             # Read the first 4 bytes (header) to verify if it starts with the expected bytes
#             header = f.read(4)
#             if header != b'\x80\x04':
#                 print(f"Invalid pickle file header in '{file_path}'.")
#                 return True  # Invalid header, consider it corrupted
            
#             # Read the remaining bytes to check if there is any unexpected content
#             remaining_data = f.read()
#             if len(remaining_data) == 0:
#                 print(f"No data found after the header in '{file_path}'.")
#                 return True  # No data after the header, consider it corrupted
            
#             # Check if the file ends abruptly (missing footer or unexpected data)
#             if remaining_data.endswith(b'\x87q.'):
#                 print(f"File '{file_path}' ends abruptly.")
#                 return True  # File ends abruptly, consider it corrupted
            
#             # No obvious signs of corruption found
#             return False
#     except Exception as e:
#         print(f"Error reading pickle file '{file_path}': {e}")
#         return True  # Exception occurred, consider it corrupted

# pickle_file_path = os.path.join('Data', 'pkl_data', 'pokemon1.pkl')

# # Check if the pickle file is corrupted
# if is_pickle_file_corrupted(pickle_file_path):
#     print("The pickle file is corrupted.")
# else:
#     print("The pickle file is not corrupted.")

# # Read DataFrame from the file
# with open(os.path.join('Data', 'pkl_data', 'pokemon1.pkl'), 'rb') as f:
#     pokemon_df = pickle.load(f)

pokemon_df = pandas.read_pickle(os.path.join('Data', 'pkl_data', 'pokemon2.pkl'))



print(pokemon_df)

pil_image = None
for image in pokemon_df['Abra']:
    print(image)
    print(type(image))
    to_pil = transforms.ToPILImage()
    pil_image = to_pil(image)
    break
pil_image.show()
pil_image.save('output_image.png')

