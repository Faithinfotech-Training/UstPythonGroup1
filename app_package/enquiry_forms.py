from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,RadioField,SelectField
from wtforms.validators import DataRequired,EqualTo,ValidationError,Length,Email,NumberRange
from wtforms.validators import Regexp
from wtforms.fields.html5 import EmailField


class NewEnquiryForm(FlaskForm):
    name=StringField("Name: ",validators=[DataRequired(message="Enter Your Name")])
    age=IntegerField("Age: ",validators=[DataRequired(message="Enter Your Age"),NumberRange(min=1,max=80,message="Please enter valid age")])
    qualification=SelectField("Qualification: ",[DataRequired(message="Please select an option")],choices=[('1', 'B Tech'), ('2', 'M Tech'), ('3', 'MCA')])
    phone=StringField("Mobile no", validators=[DataRequired(message="Enter Your Phone Number"),Length(min=10, max=10,message="Please enter corect value")])
    passout_year=IntegerField("Year of passout : ",validators=[DataRequired(message="Enter Your Year of Passout"),NumberRange(min=1990,max=2020,message="Please enter corect value")])
    email=EmailField("Email: ",validators=[DataRequired(message="Enter Your Email Id"),Email("Please enter your email address.")])
    course=SelectField("Course: ",[DataRequired(message="Please select an option")],choices=[('1', 'Python'), ('2', 'Java'), ('3', 'Testing')])
    source_of_lead=SelectField("Source: ",[DataRequired(message="Please select an option")],choices=[('1', 'Automatic'), ('2', 'Manual')])
    status=SelectField("Enquiry Status: ",[DataRequired(message="Please select an option")],choices=[('1', 'New'), ('2', 'Interested'), ('3', 'Not Interested'), ('4', 'Exam Passed'), ('5', 'Exam Failed'), ('6', '  Joined')])
    submit=SubmitField("Submit Enquiry")      
    
    
class EnquirySearchForm(FlaskForm):
    e_type=RadioField("Type:",validators=[DataRequired(message="Please select an option")],choices=[('Enquiry Id','Enquiry Id'),('Name','Name'),('Phone','Phone'),('Status','Status')])
    e_name=StringField("Search:",validators=[DataRequired(message="Enter Your Name")])
    submit=SubmitField("Search")
    
class UpdateEnquiryForm(FlaskForm):
    age=IntegerField("Age: ",validators=[DataRequired(message="Enter Your Age"),NumberRange(min=0,max=80,message="Please enter valid age")])
    qualification=SelectField("Qualification: ",[DataRequired(message="Please select an option")],choices=[('1', 'B Tech'), ('2', 'M Tech'), ('3', 'MCA')])
    phone=StringField("Mobile no", validators=[DataRequired(message="Enter Your Phone Number"),Length(min=10, max=10,message="Please enter corect value")])
    passout_year=IntegerField("Year of passout : ",validators=[DataRequired(message="Enter Your Year of Passout"),NumberRange(min=1990,max=2020,message="Please enter corect value")])
    email=EmailField("Email: ",validators=[DataRequired(message="Enter Your Email Id"),Email("Please enter your email address.")])
    course=SelectField("Course: ",[DataRequired(message="Please select an option")],choices=[('1', 'Python'), ('2', 'Java'), ('3', 'Testing')])
    status=SelectField("Enquiry Status: ",[DataRequired(message="Please select an option")],choices=[('1', 'New'), ('2', 'Interested'), ('3', 'Not Interested'), ('4', 'Exam Passed'), ('5', 'Exam Failed'), ('6', '  Joined')])
    submit=SubmitField("Update Status")
