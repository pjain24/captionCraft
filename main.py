import streamlit as st
from PIL import Image
from utils import getSummary, generateCaption
# from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
# import numpy as np

st.header('CaptionCraft : Your AI caption generator')

additional_info = ""

with st.form(key='my_form_to_submit'):
    # Display an image uploader widget
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    additional_info = st.text_input('Tell me something more about this image ?', '...')

    submit_button = st.form_submit_button(label='Submit')


if submit_button:

    # Check if an image has been uploaded
    if uploaded_file is not None:
        # Use the uploaded image for further processing
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image')

        summary = getSummary(image)

        st.subheader('Image summary :')
        st.text(summary)

        caption = generateCaption(summary, additional_info)
        st.subheader('Caption :')
        st.text(caption)
    else:
        st.text("Please submit a valid image to start")


    
