"""
Nama: Fernaldy Aristo Wirjowerdojo

// app.py //
This programme was created to serve as the main interface of the project.
"""

import streamlit as st
import eda
import model

page = st.sidebar.selectbox(label="Select Page:", options=["Home Page", "Exploratory Data Analysis", "Predict Data"])

if page == "Home Page":
    st.title("Home Page")
    st.write('')
    st.write("Name  : Fernaldy Aristo Wirjowerdojo")
    st.write("This programme was created using the library streamlit to visualise an interactive platform and huggingface to deploy the model online.\
              The primary use of this platform is to show the results of the exploratory data analysis and to predict a jellyfish's species\
              when given an image link by the user.")
    st.write('')
    st.caption("Please choose the page option in the sidebar on the left side of the screen!")
    st.write('')
    st.write('')

elif page == "Exploratory Data Analysis":
    eda.run()

else:
    model.run()