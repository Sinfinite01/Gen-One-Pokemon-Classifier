import pandas
import os
from torchvision import transforms
import time

start_time = time.time()

# Using the inbuilt pandas function to read a dataframe from a pkl file
pokemon_df = pandas.read_pickle(os.path.join('Data', 'pkl_data', 'pokemon100_1.pkl'))

end_time = time.time()

# Calculate the elapsed time
elapsed_time_seconds = end_time - start_time

elapsed_minutes = int(elapsed_time_seconds // 60)
elapsed_seconds = elapsed_time_seconds % 60

print("Elapsed Time to read the file:", elapsed_minutes, "minutes", "{:.2f}".format(elapsed_seconds), "seconds")


start_time = time.time()

# Output the first image in the Abra column
pil_image = None
for image in pokemon_df['Dratini']:
    # Print out first row of the image to get a sense of how the image is formatted
    print(image[0])
    print(type(image))
    to_pil = transforms.ToPILImage()
    pil_image = to_pil(image)
    break
pil_image.show()
pil_image.save('output_image.png')

end_time = time.time()

# Calculate the elapsed time
elapsed_time_seconds = end_time - start_time

elapsed_minutes = int(elapsed_time_seconds // 60)
elapsed_seconds = elapsed_time_seconds % 60

print("Elapsed Time to output the image:", elapsed_minutes, "minutes", "{:.2f}".format(elapsed_seconds), "seconds")

# I'm going to run this visualizer that reads this pickle file of the dataframe of tensors and then output the first image, lets see how long that takes
# I'm visualizing my dataset rn. I converted it to a dataframe of pytorch tensors
