from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_pymongo import PyMongo
<<<<<<< HEAD
<<<<<<< HEAD
#from flask_login import LoginManager
=======
>>>>>>> 40d33d9ef7ba783aa7d020222d3556892d498d56
=======
from app_package.config import Config
>>>>>>> 0987dab6490f7a7ce1b6835359032cb2752eb37d

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate=Migrate(app,db)
mongo=PyMongo(app)
<<<<<<< HEAD
#login_manager=LoginManager(app)
#login_manager.login_view="index"

<<<<<<< HEAD
from app_package import courseroutes
=======

from app_package import routes_admission
>>>>>>> 40d33d9ef7ba783aa7d020222d3556892d498d56
=======
#login_manager=LoginManager(app)
#login_manager.login_view="index"

from app_package import batchroutes
<<<<<<< HEAD
=======
>>>>>>> 0987dab6490f7a7ce1b6835359032cb2752eb37d
>>>>>>> 4f596225df58ab46abebfce94bbe5a0984a7fa97
