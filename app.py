import streamlit as st
from streamlit_drawable_canvas  import st_canvas
from tensorflow.keras.models import load_model
import numpy as np

# Load the pre-trained model
#@st.cache_resource()
def load_my_model():
    return load_model('my_model.keras')

model = load_my_model()
# Set up the page
st.title("MNIST Digit Predictor")
st.markdown("Draw a digit on the canvas below and click 'Predict'")

# create a canvas 
canvas_result = st_canvas(
    fill_color="white",  #background 
    stroke_width=10,
    stroke_color="#000000",
    background_color="#FFFFFF",
    update_streamlit=True,
    height=150,
    width=150,
    drawing_mode="freedraw",
    key="canvas",
)

# predicting
if st.button('Predict'):
    if canvas_result.image_data is not None:
        img = canvas_result.image_data.astype(np.uint8)
        img = np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])  # Convert to grayscale
        img = img / 255.0  # Normalize
        img = np.expand_dims(img, axis=(0, -1))  # Reshape for the model (1, 150, 150, 1)
        img = np.resize(img, (1,784))  # Resize to match model's expected input
        
        # Make the prediction
        prediction = model.predict(img)
        st.write(f'Predicted Digit: {np.argmax(prediction)}')
        st.bar_chart(prediction[0])
    else:
        st.write("Draw a digit")
