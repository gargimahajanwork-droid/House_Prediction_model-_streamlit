from sqlalchemy import Column, Integer, Float, String
from database import Base


class HousePrediction(Base):
    __tablename__ = "house_predictions"

    id = Column(Integer, primary_key=True, index=True)

    housing_median_age = Column(Integer)

    total_rooms = Column(Integer)

    total_bedrooms = Column(Integer)

    population = Column(Integer)

    households = Column(Integer)

    median_income = Column(Float)

    ocean_proximity = Column(String)

    predicted_price = Column(Float)