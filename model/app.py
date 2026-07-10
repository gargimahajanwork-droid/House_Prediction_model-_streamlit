# Import Libraries
import streamlit as st
import pandas as pd
import requests
# Title
st.title("🏠 House Price Prediction")

st.write("Enter the house details below.")


# User Inputs

housing_median_age = st.number_input("Housing Median Age", value=25)

total_rooms = st.number_input("Total Rooms", value=5)

total_bedrooms = st.number_input("Total Bedrooms", value=5)

population = st.number_input("Population", value=1200)

households = st.number_input("Households", value=5)

median_income = st.number_input("Median Income", value=4.5)

ocean_proximity = st.selectbox(
    "Ocean Proximity",
    [
        "<1H OCEAN",
        "INLAND",
        "ISLAND",
        "NEAR BAY",
        "NEAR OCEAN"
    ]
)


# Prediction

# Prediction

if st.button("Predict House Price"):

    response = requests.post(
        "https://house-prediction-model-streamlit-1.onrender.com/predict",
        json={
            "housing_median_age": housing_median_age,
            "total_rooms": total_rooms,
            "total_bedrooms": total_bedrooms,
            "population": population,
            "households": households,
            "median_income": median_income,
            "ocean_proximity": ocean_proximity
        }
    )

    if response.status_code == 200:
        prediction = response.json()["predicted_price"]
        st.success(f"Estimated House Price: ${prediction:,.2f}")
    else:
        st.write(response.json())
        st.error("Prediction failed!")

