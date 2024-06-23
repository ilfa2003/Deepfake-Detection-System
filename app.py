import streamlit as st
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Inception model
model = load_model('DENSENET.h5')

# Function to preprocess the uploaded image
def preprocess_image(image_data):
    img = image.load_img(image_data, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize pixel values to between 0 and 1
    return img_array

# Function to make prediction
def predict(image_data):
    img_array = preprocess_image(image_data)
    prediction = model.predict(img_array)
    return prediction[0][0]  # Assuming binary classification, return the probability of being fake


# Streamlit app
def main():
    st.set_page_config(page_title="Deepfake Detection System", layout="wide")
    #st.title("Deepfake Detection App")
   
    st.markdown(
                f"""
                <style>
                .stApp {{
                    background: url("https://c02.purpledshub.com/uploads/sites/41/2022/08/deepfakes-small-78221c8.jpg");
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
    st.markdown(
        """<style>
    div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 50px;
    }
    </style>
    """, unsafe_allow_html=True)
    # Customize title style
    st.markdown(
        """
        <style>
        /* Center the title */
        .title-wrapper {
            display: flex;
            justify-content: center;
        }
        /* Increase the font size of the title */
        .title-wrapper .stTitle {
            font-size: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Apply CSS to increase the font size of success and error messages
    st.markdown(
        """
        <style>
        /* Increase font size of success message */
        .stAlert.success div[data-baseweb="toast"] > div > div {
            font-size: 24px !important;
        }
        
        /* Increase font size of error message */
        .stAlert.error div[data-baseweb="toast"] > div > div {
            font-size: 24px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the title
    st.markdown("<div class='title-wrapper'><h1 class='stTitle'>Deepfake Detection App</h1></div>", unsafe_allow_html=True)

    # Upload image
    st.subheader("Upload Image:")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

        # Make prediction
        if st.button("Predict"):
            prediction = predict(uploaded_file)
            if prediction > 0.5:
                st.success("The image is classified as REAL.")
            else:
                st.error("The image is classified as FAKE.")

if __name__ == "__main__":
    main()
