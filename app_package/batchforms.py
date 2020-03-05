from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, SubmitField, RadioField, IntegerField

from wtforms.validators import DataRequired, ValidationError

class AddBatchForm(FlaskForm):
    
    b_name=StringField("Batch Name: ", validators=[DataRequired()])
    start_date=StringField("Start Date: ",validators=[DataRequired()])
    end_date=StringField("End Date: ",validators=[DataRequired()])
    b_status=RadioField('batch status', choices = [('active','active'),('inactive','inactive')])
    c_id=StringField("Course ID: ",validators=[DataRequired()])
    submit=SubmitField("Add Batch")

class ModifyBatchForm(FlaskForm):
    b_id=IntegerField("Id of batch to be updated: ",validators=[DataRequired()])
    start_date=StringField("Start Date: ")
    end_date=StringField("End Date: ")
    b_status=RadioField('Status: ', choices = [('active','active'),('inactive','inacive')])
    submit=SubmitField("Update")
