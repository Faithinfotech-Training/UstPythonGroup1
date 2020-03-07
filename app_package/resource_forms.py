from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,SelectField
from wtforms.validators import DataRequired,EqualTo,NumberRange



class AddResourceForm(FlaskForm):   
    res_name=StringField("ResourceName:",validators=[DataRequired()])
    res_capacity=IntegerField("ResourceCapacity:",validators=[DataRequired(),NumberRange(min=0)])
    res_rent=IntegerField("ResourceRent:", validators=[DataRequired(),NumberRange(min=0)])
    res_status=SelectField('Status', choices = [('Avilable','Avilable'),('NotAvilable','NotAvilable')])
    type_of_use=SelectField('Type of Use', choices = [('Seminar','Seminar'),('Practical','Practical'),('Lab','Lab')])
    submit=SubmitField("Add Resource",validators=[DataRequired()])


class UpdateResourceForm(FlaskForm): 
    
    res_capacity=IntegerField("ResourceCapacity:",validators=[DataRequired(),NumberRange(min=0)])
    res_rent=IntegerField("ResourceRent:", validators=[DataRequired(),NumberRange(min=0)])
    res_status=SelectField('Status', choices = [('Avilable','Avilable'),('NotAvilable','NotAvilable')])
    type_of_use=SelectField('Type of Use', choices = [('Seminar','Seminar'),('Practical','Practical'),('Lab','Lab')])
    submit=SubmitField("Modify Employee")
    