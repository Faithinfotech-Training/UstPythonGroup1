from flask import Flask
from app_package.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate=Migrate(app,db)
mongo=PyMongo(app)


from app_package import resourceroutes