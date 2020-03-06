from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class ModifyAdmissionForm(FlaskForm):

    id=IntegerField("Id to be modified: ",validators=[DataRequired()])
    photo=StringField("Photo: ")
    address=StringField("Address: ")
    submit=SubmitField("Modify Employee")

class AddAdmissionForm(FlaskForm):

    photo=StringField("Photo URL:",validators=[DataRequired()])
    address=StringField("Address:",validators=[DataRequired()])
    previouscourse=StringField("Previous Course:",validators=[DataRequired()])
    eq_id=IntegerField("Enquiry id:",validators=[DataRequired()])
    submit=SubmitField("Add Admission")

