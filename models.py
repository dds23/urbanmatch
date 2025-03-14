from sqlalchemy import Column, Integer, String, ARRAY
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    gender_preference = Column(String)
    email = Column(String, unique=True, index=True)
    city = Column(String, index=True)
    interests = Column(ARRAY(String))

