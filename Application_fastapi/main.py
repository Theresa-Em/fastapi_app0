from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud
import models
import schemas

# Task 5 - Import Here
from database import SessionLocal, engine
# ------------------------------

app = FastAPI()

@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def docs_redirect():
    response = RedirectResponse(url='/docs')
    return response

# Task 5 - Fetch the Session to the Main Application
# creates a new SQLAlchemy session session using SessionLocal() method and yields this session for use. 
# Once the operation is complete, the session is closed in the finally block to ensure proper resource cleanup.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------------
# Task 6 - Create an Endpoint to Get Users
@app.get("/users/", response_model=List[schemas.User])
def read_users(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
    
# ------------------------------
# Task 7 - Create an Endpoint to Get User by ID
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session=Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# ------------------------------
# Task 8 - Create an Endpoint to Get User by Email
@app.get("/users/email/{user_email}", response_model=schemas.User)
def read_user_by_email(user_email: str, db: Session=Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# ------------------------------
# Task 9 - Create an Endpoint to Add a User
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session=Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# ------------------------------
# Task 10 - Create an Endpoint to Update a User
@app.put("/users/", response_model=schemas.User)
def update_user(user: schemas.UserCreate, db: Session=Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        return crud.update_user(db=db, user=user)
    raise HTTPException(status_code=400, detail="User not found")

# ------------------------------
# Task 11 - Create an Endpoint to Delete a User
@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session=Depends(get_db)):
    db_user = crud.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
 
# ------------------------------