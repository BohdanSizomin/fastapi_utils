import jinja2

# patch https://jinja.palletsprojects.com/en/3.0.x/changes/
# pass_context replaces contextfunction and contextfilter.
jinja2.contextfunction = jinja2.pass_context
# flake8: noqa F402

from fastapi import FastAPI
from sqladmin import Admin

from app.database import db
from app.router import router

from app.database import db


engine = db.get_engine()

app = FastAPI()


app.include_router(router)


@app.get("/")
def root():
    return {"message": "Hello"}
