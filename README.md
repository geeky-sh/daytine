# daytine

## (Daily + Routine)

API to create timed tasks for a user and track them.

## Technologies used:
- [FastAPI](https://fastapi.tiangolo.com/) as framework for building web application
- [SQLAlchemy](https://docs.sqlalchemy.org/en/14/) as ORM for DB interactions
- [Sqlite](https://www.sqlite.org/index.html) as the primary database
- [uvicorn](https://www.uvicorn.org/) for running the server

## How to setup the product
1. Install [virtualenv](https://realpython.com/python-virtual-environments-a-primer/) and use python3
2. Go to the project folder and setup virtualenv by running `virtualenv envproj -p $(which python3)`
3. Activate env by running `source envproj/bin/activate`
4. Run `pip install -r requirements.txt`
5. Run server - `uvicorn app.main:app --reload`

## To view Swagger and Redoc API documentation:
1. Swagger - http://localhost:8000/docs
2. Redoc - http://localhost:8000/redoc

## To add a new package in the product, do the following:
1. Add <new_package> in requirements.in. Specify the version if you want to install specific version else write only the name
2. Run `pip-compile requirements.in > requirements.txt`
3. Run `pip install -r requirements.txt` to install the new package. Make sure virtual environment is active.

## Alembic
[Alembic](https://alembic.sqlalchemy.org/en/latest/) is used to do migration versioning

### Configuration
`prepend_sys_path = ..` - had to do this so that alembic command recognises it's parent folder as a package. In simple words, due to this, we can do `from app.task.models import Base` in `alembic/env.py`.

(This is a classic `ImportNotFound` error due to python unable to recognise a package. See [here](https://stackoverflow.com/questions/43728431/relative-imports-modulenotfounderror-no-module-named-x). Thoughtfully, amembic provides a way to resolve this issue via its `prepend_sys_path` option)

Comparison to Django Migration Framework:
- alembic versions is django's migrations
- alembic upgrade is django's migrate
- alembic history is django's showmigrations


## Commands:
- `alembic revision --autogenerate -m "<message>"` - Generate migration based on models defined
- `alembic upgrade head` - migrate to the latest revision

## Resources
- SQLAlchemy query tutorial - https://www.pythoncentral.io/overview-sqlalchemys-expression-language-orm-queries/

## Deployment steps
- Configure aws proflie - `aws configure --profile <profile_name>`)
- Run `sam build --profile <profile_name> --region us-east-1`
- Run `sam deploy --guided`
