import streamlit as st
import pandas as pd
import joblib

model = joblib.load('/content/drive/MyDrive/car_price_model.pkl')

st.title("Car Price Predictor")
st.write("Enter car details to predict the price")

car_age = st.slider("Car Age (years)", 0, 15, 5)
mileage = st.number_input("Mileage (km)", min_value=0, max_value=200000, value=50000)
engine_size = st.number_input("Engine Size (L)", min_value=1.0, max_value=3.0, value=1.6, step=0.1)
fuel_type = st.selectbox("Fuel Type", ["Diesel", "Petrol"])
transmission = st.selectbox("Transmission", ["Automatic", "Manual"])
city = st.selectbox("City", ["Islamabad", "Karachi", "Lahore", "Peshawar"])

input_data = pd.DataFrame({
    'Car_Age': [car_age],
    'Mileage_km': [mileage],
    'Engine_Size_L': [engine_size],
    'Fuel_Type_Petrol': [1 if fuel_type == "Petrol" else 0],
    'Transmission_Manual': [1 if transmission == "Manual" else 0],
    'City_Karachi': [1 if city == "Karachi" else 0],
    'City_Lahore': [1 if city == "Lahore" else 0],
    'City_Peshawar': [1 if city == "Peshawar" else 0],
})

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Price: PKR {prediction[0]:,.0f}")
