from flask import render_template,flash,redirect,url_for
from app_package import app,db,mongo
#from flask_login import current_user,login_user,logout_user,login_required
from app_package.course_forms import AddCourseForm,ModifyCourseForm

   
@app.route("/",methods=["GET","POST"])
def dashboard():
    return render_template("dashboard.html")