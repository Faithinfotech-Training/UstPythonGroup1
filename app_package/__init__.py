from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_pymongo import PyMongo
from app_package.config import Config


app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate=Migrate(app,db)
mongo=PyMongo(app)

<<<<<<< HEAD
from app_package import resource_routes,batch_routes,course_routes,routes,enquiry_routes,qualification_routes
=======
from app_package import resource_routes,batch_routes,course_routes,routes,enquiry_routes,moduleroutes
>>>>>>> a4a6fb84d826065792b51efce2e498fce5a0b55e
