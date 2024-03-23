**Training a PyTorch CNN Classifier on a Keras Pokemon Dataset**

Welcome to our repository where we delve into the world of Pokémon classification using deep learning techniques! Here, you'll find scripts to train a convolutional neural network (CNN) classifier using PyTorch on the popular Keras Pokemon dataset. The dataset can be accessed on Kaggle: [Keras Pokemon Dataset](https://www.kaggle.com/datasets/lantian773030/pokemonclassification/data).

**Resources:**

- [Google Slides Presentation](https://docs.google.com/presentation/d/15xClN4Mg3g_DBQwHsOMu5rcFlWVArflWNzJ8UfOtcME/edit?usp=sharing)

**Files:**

- `data_cleaner.py`: This script efficiently handles dataset cleaning tasks, ensuring all images are standardized to RGB format and resized uniformly. It then organizes the data into a Pandas DataFrame saved as a pickle (pkl) file.
- `pokemon_cnn.ipynb`: Dive into this Jupyter Notebook to create and train a powerful CNN on the preprocessed dataset.
- `pokedex.ipynb`: Embark on a fun journey with this notebook, where you can test your trained model on Pokémon starters and explore their Gen One Pokedex descriptions.
- `model_tester.ipynb`: Experiment with different models using this notebook. The default model achieves an impressive 88% accuracy on a test set trained on 10 Pokémon.
- `Models`: This directory contains saved .pth files of trained CNNs, each named in the format x_ypercent_z.pth:

    - `x`: Represents the number of Pokémon the model was trained on or is designed to classify.
    - `y`: Indicates the percent accuracy achieved on the test set.
    - `z`: Iterates upward if a .pth model with the same `x` and `y` already exists.

Feel free to explore the provided resources and scripts to gain insights into the Pokémon classification process and experiment with the trained models!