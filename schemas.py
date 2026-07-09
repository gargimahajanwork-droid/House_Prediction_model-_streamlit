from pydantic import BaseModel

class HousePredictionRequest(BaseModel):

    housing_median_age:int
    total_rooms: int 
    total_bedrooms:int 
    population: int 
    households: int 
    median_income: float 
    ocean_proximity: str 

class HousePredictResponse(BaseModel):

    predicted_price : float 
