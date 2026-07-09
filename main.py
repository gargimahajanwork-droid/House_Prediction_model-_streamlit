from fastapi import FastAPI,Depends
from database import engine , get_db
from models import Base , HousePrediction
from schemas import HousePredictionRequest,HousePredictResponse

from sqlalchemy.orm import Session
import joblib
import pandas as pd 


# Load ML files only once
model = joblib.load("model/model.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to House Price Prediction API"
    }




@app.post("/predict", response_model=HousePredictResponse)
def predict_house_price(
    request: HousePredictionRequest,
    db: Session = Depends(get_db)
):
    # Convert the selected ocean proximity category into its encoded value
    ocean = label_encoder.transform([request.ocean_proximity])[0]

    # Create a DataFrame because the ML model expects the input in tabular format
    input_data = pd.DataFrame({
        "housing_median_age": [request.housing_median_age],
        "total_rooms": [request.total_rooms],
        "total_bedrooms": [request.total_bedrooms],
        "population": [request.population],
        "households": [request.households],
        "median_income": [request.median_income],
        "ocean_proximity": [ocean]
    })

    # Predict the house price
    predicted_price = float(model.predict(input_data)[0])

    # Create a new database object to store the user inputs and prediction
    prediction = HousePrediction(
        housing_median_age=request.housing_median_age,
        total_rooms=request.total_rooms,
        total_bedrooms=request.total_bedrooms,
        population=request.population,
        households=request.households,
        median_income=request.median_income,
        ocean_proximity=request.ocean_proximity,
        predicted_price=predicted_price
    )

    # Save the prediction into the database
    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    # Return the predicted house price to the client
    return HousePredictResponse(
        predicted_price=predicted_price
    )