from pydantic import BaseModel, EmailStr
from typing import List, Optional, Literal
from enum import Enum


class Gender(str, Enum):
    male = 'male'
    female = 'female'
    other = 'other'


class UserBase(BaseModel):
    name: str
    age: int
    email: EmailStr
    city: str
    interests: List[str]


class UserCreate(UserBase):
    pass


class User(UserBase):
    gender: str
    gender_preference: str
    id: int

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    city: Optional[str] = None
    interests: Optional[List[str]] = None

    class Config:
        from_attributes = True
