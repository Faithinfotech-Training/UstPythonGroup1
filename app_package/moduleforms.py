from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,SelectField
from wtforms.validators import DataRequired, EqualTo

            

class AddModuleForm(FlaskForm):
    
    name=StringField("Module Name:",validators=[DataRequired()])
    
    submit=SubmitField("Add Module")      
    
    

class ModifyModuleForm(FlaskForm):
   
    
    name=StringField("Module Name:",validators=[DataRequired()])
    submit=SubmitField("Modify Module")            

class DeleteModuleForm(FlaskForm):
    
    name=StringField("Module Name:",validators=[DataRequired()])
    submit=SubmitField("Delete Module")