import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

# 1. Load the trained model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('fashion_model.h5')

model = load_model()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

st.title("👕 AI Fashion Classifier")
st.write("Upload an image of a piece of clothing, and the AI will predict what it is.")

file = st.file_uploader("Please upload an image", type=["jpg", "png"])

def import_and_predict(image_data, model):
    size = (28, 28)
    image = ImageOps.fit(image_data, size, Image.Resampling.LANCZOS)
    image = image.convert("L")
    image = ImageOps.invert(image)
    img = np.asarray(image) / 255.0
    img_reshape = img[np.newaxis, ...]
    prediction = model.predict(img_reshape)
    return prediction

if file is not None:
    image = Image.open(file)
    st.image(image, caption="Uploaded Image", width=300)
    
    if st.button("Classify Image"):
        predictions = import_and_predict(image, model)
        score = tf.nn.softmax(predictions[0])
        st.write(f"### Prediction: {class_names[np.argmax(score)]}")
        st.write(f"Confidence: {100 * np.max(score):.2f}%")
