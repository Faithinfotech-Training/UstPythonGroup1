from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,SelectField,SelectField,FloatField
from wtforms.validators import DataRequired,EqualTo,ValidationError,NumberRange

class AddCourseForm(FlaskForm):
   
    courseName=StringField("CourseName: ",validators=[DataRequired(message="Enter valid data")])
    courseDuration=IntegerField("Courseduration:(in weeks) ",validators=[DataRequired(message="Enter valid data"),NumberRange(min=1)])
    courseFee=FloatField("Course Fee: ",validators=[DataRequired(message="Enter valid data"),NumberRange(min=10000)])
    courseDescription=StringField("CourseDescription: ",validators=[DataRequired(message="Enter valid data")])
    courseStatus=SelectField("CourseStatus: ",choices=[("Active","Active"),("Inactive","Inactive")])
    submit=SubmitField("Add Course")
   
class ModifyCourseForm(FlaskForm):
   
    courseDuration=IntegerField("CourseDuration:(in weeks)  ",validators=[DataRequired(message="Enter valid data"),NumberRange(min=1)])
    courseDescription=StringField("CourseDescription: ",validators=[DataRequired(message="Enter valid data")])
    courseFee=FloatField("Course Fee: ",validators=[DataRequired(message="Enter valid data"),NumberRange(min=10000)])
    courseStatus=SelectField("CourseStatus: ",choices=[("Active","Active"),("Inactive","Inactive")])
    submit=SubmitField("Update Course")

class AddQualificationForm(FlaskForm):
    qualificationName=StringField("Qualification: ",validators=[DataRequired(message="Enter valid data")])
    submit=SubmitField("ADD")