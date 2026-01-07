from pydantic import BaseModel
from typing import List

# Task 3 - Create a Schema for the Base User
class BaseUser(BaseModel):
    email: str
    username: str 
    first_name: str 
    last_name: str 
    gender: str 
    country: str 
    isActive: bool


# Task 4 - Create a Schema for the User Class
class User(BaseUser):
    id: int
    # The Config class inside the User model makes it compatible with SQLAlchemy ORM.
    class Config:
        orm_mode = True 


class UserCreate(BaseUser):
    password: str
