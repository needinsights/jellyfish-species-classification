"""
Nama: Fernaldy Aristo Wirjowerdojo

// eda.py //
This programme was created to serve as the interface for the exploratory data analysis result.
"""

import streamlit as st

def run():
    st.title('Exploratory Data Analysis')

    # Example of jellyfish species
    st.header('Some examples of the jellyfishes')
    st.image('some_jellyfish.png', caption='Jellyfish examples')

    # Augmented Jellyfish
    st.header('Augmented images of jellyfishes')
    st.write('To produce a better model, the images of the jellyfish were augmented by applying\
             a few techniques such as horizontal / vertical flips, rotation, shearing and zooming.')
    with st.expander('Some examples of the augmented images'):
        st.image('augmented_jellyfish.png', caption='Augmented images')

    # Image size consistency
    st.header('Before the model can be trained, the image it takes in has to be considered first.')
    with st.expander('The chart of the image size (Height and Width)'):
        st.image('height_and_width.png', caption='Height and width of the original images')
        st.caption("The original images weren't consistent, so the image had to be resized first.")