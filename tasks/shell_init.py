# flake8: noqa F401
from app import model as m
from app.database import db as dbo

db = dbo.Session()
