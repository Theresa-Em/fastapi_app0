from sqlalchemy.orm import Session
from sqlalchemy import update
import models, schemas

# Task 6 - Get Users
def get_users(db: Session, skip:int=0, limit:int=0):
    return db.query(models.User).offset(skip).limit(limit).all()
# ------------------------------
# Task 7 - Get Users by ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
# ------------------------------
# Task 8 - Get User by Email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# ------------------------------
# Task 9 - Add a User
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = hash(user.password)
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password, \
        username=user.username, first_name=user.first_name, last_name=user.last_name, \
        gender=user.gender, country=user.country, isActive=user.isActive)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ------------------------------
# Task 10 - Update a User
def update_user(db: Session, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    for field in user.__dict__:
        setattr(db_user, field, getattr(user, field))
    db.commit()
    db.refresh(db_user)
    return db_user

# ------------------------------
# Task 11 - Delete a User
def delete_user(db: Session, user_id: int):
    record_obj = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(record_obj)
    db.commit()
    return record_obj

# ------------------------------