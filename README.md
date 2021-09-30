# daytine
API  to create timed tasks for a user and track them.

## Technologies used:
- FastAPI as framework for building web application
- SQLAlchemy as ORM for db interaction
- Sqlite as the primary database
- gvicorn for running the server

## How to setup the product
1. Install [virtualenv](https://realpython.com/python-virtual-environments-a-primer/) and use python3
2. Go to the project folder and setup virtualenv by running `virtualenv envproj -p $(which python3)`
3. Activate env by running `source envproj/bin/activate`
4. Run `pip install -r requirements.txt`
5. Run server - `uvicorn app.main:app --reload`

## To views swagger and API documentation:
1. Swagger - http://localhost:8000/docs
2. Redoc - http://localhost:8000/redoc

## To add a new package in the product, do the following:
1. Add <new_package> in requirements.in. Specify the version if you want to install specific version else write only the name
2. Run `pip-compile requirements.in > requirements.txt`
3. Run `pip install -r requirements.txt` to install the new package. Make sure virtual environment is active.
