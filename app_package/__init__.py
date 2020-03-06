from flask import Flask
from app_package.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_pymongo import PyMongo
<<<<<<< HEAD
#from flask_login import LoginManager
=======
>>>>>>> 40d33d9ef7ba783aa7d020222d3556892d498d56

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate=Migrate(app,db)
mongo=PyMongo(app)
<<<<<<< HEAD
#login_manager=LoginManager(app)
#login_manager.login_view="index"

from app_package import courseroutes
=======

from app_package import routes_admission
>>>>>>> 40d33d9ef7ba783aa7d020222d3556892d498d56
