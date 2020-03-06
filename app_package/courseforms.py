from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,FloatField,SubmitField,SelectField
from wtforms.validators import DataRequired,EqualTo,ValidationError


class AddCourseForm(FlaskForm):
    name=StringField("name:",validators=[DataRequired(message="please enter valid name")])
    duration=IntegerField("Duration:",validators=[DataRequired(message="please enter duration in days",NumberRange(min=1))])
    fee=FloatField("Fee:",validators=[DataRequired(message="please enter valid fee")])
    status=SelectField("Status:",choices=[('available','available'),('not available','not available')])
    description=StringField("Description:",validators=[DataRequired()])
    
    submit=SubmitField("ADD")
    
    
class UpdateCourseForm(FlaskForm):
    #c_id=IntegerField("c_id:",validators=[DataRequired()])
    duration=IntegerField("Duration:",validators=[DataRequired()])
    fee=FloatField("fee:",validators=[DataRequired()])
    status=SelectField("Status:",choices=[('available','available'),('not available','not available')])
    submit=SubmitField("update")
    
    



    

    
    
    