
import streamlit as st
import pickle
import numpy as np
import joblib


# Load the trained models
crop_model = joblib.load("Crops_Recommendation.pkl")
crop_encoder = joblib.load("crop_label_encoder.pkl")
fertilizer_model = joblib.load("fertilizer_recommendation_model.pkl")
fertilizer_encoder = joblib.load("label_encoders.pkl")

st.title("🌾 Crop & Fertilizer Recommendation System")

# User inputs
N = st.number_input("Nitrogen (N) Level", min_value=0)
P = st.number_input("Phosphorus (P) Level", min_value=0)
K = st.number_input("Potassium (K) Level", min_value=0)
temperature = st.number_input("Temperature (°C)", min_value=0.0)
humidity = st.number_input("Humidity (%)", min_value=0.0)
ph = st.number_input("pH Level", min_value=0.0)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0)

if st.button("Predict Crop & Fertilizer"):
    # Ensure correct input shape
    user_input = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    
    crop_prediction = crop_model.predict(user_input)[0]
    recommended_crop = crop_encoder.inverse_transform([crop_prediction])[0]

    fertilizer_prediction = fertilizer_model.predict([[N, P, K]])[0]
    recommended_fertilizer = fertilizer_encoder.inverse_transform([fertilizer_prediction])[0]

    st.success(f"🌱 Recommended Crop: {recommended_crop}")
    st.success(f"🌾 Recommended Fertilizer: {recommended_fertilizer}")
