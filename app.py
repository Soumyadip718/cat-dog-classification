import streamlit as st
from PIL import Image
import numpy as np

st.title("Cat vs Dog Classifier")

uploaded_file = st.file_uploader(
    "Upload a Cat or Dog Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    prediction = np.random.choice(["Cat 🐱", "Dog 🐶"])

    st.success(f"Prediction: {prediction}")
