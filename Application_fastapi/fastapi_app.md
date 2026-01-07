crud.py: This file will be used to perform operations on the database.
database.py: This file will connect with the database.
main.py: This file will be used to create all the endpoints in the API.
models.py: This file will be used to create models in the API.
schemas.py: This file will store the schemas of the models to interact with the database.

Run the following command to excute the application:
cd /usercode/Application/ && uvicorn main:app --host=0.0.0.0 --reload