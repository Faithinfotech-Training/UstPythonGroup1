from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateTimeField, SelectField
from wtforms.validators import DataRequired, EqualTo

class AddBatchForm(FlaskForm):
    batch_name=StringField("Batch Name: ",validators=[DataRequired()])
    start_date=DateTimeField("Start Date: ", format='%Y-%m-%d', validators=[DataRequired()])
    end_date=DateTimeField("End Date: ", format='%Y-%m-%d',validators=[DataRequired()])
    course_id=IntegerField("Course : ",validators=[DataRequired()])
    status=SelectField("Status : ",choices=[('Active','Active'),('Inactive','Inactive')])
    submit=SubmitField("Add Batch")
    

class ModifyBatchForm(FlaskForm):
    batch_name=StringField("Batch Name: ")
    start_date=DateTimeField("Start Date: ", format='%Y-%m-%d')
    end_date=DateTimeField("End Date: ", format='%Y-%m-%d')
    status=SelectField("Status : ",choices=[('Active','Active'),('Inactive','Inactive')])
    submit=SubmitField("Modify Batch")
