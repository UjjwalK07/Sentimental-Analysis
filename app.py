import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.datasets import imdb

# Load the trained model
model = load_model('sentimental.keras')

# Load word index for preprocessing
word_index = imdb.get_word_index()

# Function to preprocess the text
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

# Streamlit app
import streamlit as st
st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as positive or negative.')

# User input
user_input = st.text_area('Movie Review')

if st.button('Classify'):
    preprocessed_text = preprocess_text(user_input)
    prediction = model.predict(preprocessed_text)

    sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'
    st.write(f'Sentiment: {sentiment}')
    st.write(f'Prediction Score: {prediction[0][0]:.4f}')
else:
    st.write('Please enter a movie review.')
