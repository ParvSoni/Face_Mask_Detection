import streamlit as st
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import cv2

# loading model
model = tf.keras.models.load_model('trained_model.h5')

class_labels = ['Unmasked', 'Masked']

st.title('Face Mask Detection')
st.markdown('Upload an image')

uploaded_file = st.file_uploader("Attach Image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # pre-processing image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    test_img = cv2.imdecode(file_bytes, 1)
    
    test_img = cv2.resize(test_img, (128, 128))
    test_input = test_img.reshape((1, 128, 128, 3)) / 255.0
    
    # Predicting
    prediction = model.predict(test_input)
    predicted_class = class_labels[int(prediction[0][0] > 0.5)]
    
    st.image(test_img, caption=f'Uploaded Image: {predicted_class}', use_column_width=True)
    st.write(f'Prediction: {predicted_class}')
    
    # Previewing the image
    plt.imshow(cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB))
    plt.title(f'Prediction: {predicted_class}')
    plt.axis('off')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()