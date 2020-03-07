from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateTimeField, SelectField, SubmitField
from wtforms.validators import DataRequired

class AddBatchForm(FlaskForm):  		
	batch_name=StringField("Batch Name: ",validators=[DataRequired()])
	start_date=DateTimeField("Start date: ", validators=[DataRequired()])	
	end_date=DateTimeField("End date: ", validators=[DataRequired()])
	course_id=IntegerField("Course ID: ", validators=[DataRequired()])   
	b_status=SelectField('Status: ', choices = [('Active','Active'),('Disabled','Disabled')])
        #status=SelectField('Status: ', choices = [('Active','Active'),('Disabled','Disabled')])
	submit=SubmitField("Submit")

class ModifyBatchForm(FlaskForm):
   
    start_date=DateTimeField("Start Date: ")
    end_date=DateTimeField("End Date: ")
    b_status=SelectField('Status: ', choices = [('Active','Active'),('Disabled','Disabled')])
    submit=SubmitField("Update")
    