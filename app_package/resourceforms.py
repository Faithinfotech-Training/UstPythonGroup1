from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,SelectField
from wtforms.validators import DataRequired, EqualTo

            

class AddResourceForm(FlaskForm):
    
    name=StringField("Name:",validators=[DataRequired()])
    capacity=IntegerField("Capacity:",validators=[DataRequired(message='Enter valid capacity.')]) 
    rent=IntegerField("Rent:",validators=[DataRequired(message='Enter a valid rent')]) 
    
    status=SelectField('status',choices=[('available','available'),('not available','not available')])
    typeofuse=StringField("Type of use:",validators=[DataRequired(message='Enter a valid use')]) 
    submit=SubmitField("Add Resource")      
    
    

class ModifyResourceForm(FlaskForm):
   
    
    rent=IntegerField("Rent:",validators=[DataRequired()]) 
    
    status=SelectField('status:',choices=[('available','available'),('not available','not available')])
    typeofuse=StringField("Type of use:",validators=[DataRequired()]) 
    submit=SubmitField("Modify Resource")            
