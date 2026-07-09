from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
import os 
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

# dependency injection , this function provides a database session whenever an API requires database access 
def get_db():
    db = SessionLocal()

    try: 
        yield db 

    finally:
        db.close()

