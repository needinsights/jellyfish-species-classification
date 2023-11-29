"""
Nama: Fernaldy Aristo Wirjowerdojo

// model.py //
This programme was created to perform the prediction.
"""

from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.utils import get_file
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import os

def run():
    """
    Main function to predict the jellyfish species, runs by:
    - Asking the user for the url of the jellyfish
    - Runs the function load_and_preprocess_image
    - Shows the image from the url given
    - When the predict button is pressed, gives the prediction made by the model
    """
    url = st.text_input(label='Please input the link to the image:')
    image = load_and_preprocess_image(url)
    if st.button(label='Predict'):
        predict(image)

def load_and_preprocess_image(url, target_size=(224, 224)):
    """
    Loads and processes the image from the url given by the user, the process is as follows:
    - Grabs the file and saves it temporarily in the folder /tmp; The path is saved as image_path
    - The image is loaded using the function load_img and shown 
    - Converts the image into a numpy array
    - Normalise the pixel values
    - Adds a batch dimension to match the input of the model

    > Returns the image with a dimension of (1, 224, 224, 3)
    """
    try:
        # Download the image and save it as a temporary file
        image_path = get_file(origin=url, fname="temp_image.png", extract=False, cache_dir='./')

        # Load the image
        image = load_img(image_path)

        # Delete the image to conserve space
        os.remove(image_path)

        # Show the image
        st.image(image, caption='Jellyfish')

        # Resize the image
        image = image.resize(target_size)

        # Convert the image to a numpy array
        image = img_to_array(image)

        # Normalize the image
        image /= 255.0

        # Add a batch dimension
        image = np.expand_dims(image, axis=0)

        return image
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def predict(image):
    """
    Predicts the species of the jellyfish given by the user, the process is as follows:
    - Loads the model
    - Performs the prediction and prints out the prediction
    """
    model = load_model('model_4') 
    pred = model.predict(image, verbose=False) 
    class_labels = ['Barrel Jellyfish', 'Moon Jellyfish', 'Blue Jellyfish', 'Compass Jellyfish', 'Lions Mane Jellyfish', 'Mauve Stinger Jellyfish']
    pred = np.argmax(pred, axis=1)[0]

    st.write(f'This is a {class_labels[pred]}!')
