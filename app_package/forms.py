from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FloatField, RadioField
from wtforms.validators import DataRequired, EqualTo
from app_package.models import User