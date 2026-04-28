import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("data.pkl", "rb"))

st.set_page_config(page_title="AI Predictor", layout="wide")

# Custom UI
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 AI Prediction App")
st.write("Enter values to get prediction")

# Example input fields (modify based on your model)
col1, col2 = st.columns(2)

with col1:
    val1 = st.number_input("Feature 1")
    val2 = st.number_input("Feature 2")

with col2:
    val3 = st.number_input("Feature 3")
    val4 = st.number_input("Feature 4")

# Predict button
if st.button("Predict"):
    try:
        input_data = np.array([[val1, val2, val3, val4]])
        prediction = model.predict(input_data)
        
        st.success(f"Prediction: {prediction[0]}")
    except Exception as e:
        st.error(f"Error: {e}")
      
