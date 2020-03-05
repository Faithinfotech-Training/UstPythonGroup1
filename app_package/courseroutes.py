from flask import render_template, flash, redirect, url_for
from app_package import app, db,mongo
from app_package.forms import AddCourseForm,UpdateCourseForm,HideCourseForm


@app.route("/add_course",methods=["GET","POST"])            
def add_course():
    global course_id 
    form=AddCourseForm()
    if form.validate_on_submit():
        fields=["_c_id","name","duration","fee","status","description"]
        course_id+=1
        values=[course_id,form.name.data,form.duration.data,form.fee.data,form.status.data,form.description.data]
        course=dict(zip(fields,values))
        course_col=mongo.db.courses#here 'mongo' is a variable which we have created which comes with an attirute,'db' ...we are calling the collection as 'employees' 
        tmp=course_col.insert_one(course)
        if tmp.inserted_id==course_id:
            flash("Course added")
            return redirect(url_for("menu"))
        else:
            flash("Problem adding Course")
            return redirect(url_for("logout"))
    else:
        return render_template("add_course.html",form=form)

@app.route("/update_course",methods=["GET","POST"])
def update_course():
    form=UpdateCourseForm()
    if form.validate_on_submit():
        values=dict()
        if form.fee.data!="":values["fee"]=form.fee.data
        if form.duration.data!="":values["duration"]=form.duration.data
        new_data={"$set":values}
        query={"_c_id":form.id.data}
        course_col=mongo.db.courses
        course_col.update_one(query,new_data)
        flash("course modified")
        return redirect(url_for("menu"))
    else:
        return render_template("update_course.html",form=form)

@app.route("/display_course")
def display_courses():
    course_col=mongo.db.courses
    courses=course_col.find()
    return render_template("display_course.html",courses=courses)

@app.route("/hide_course",methods=["GET","POST"])
def hide_course():
    form=HideCourseForm()
    if form.validate_on_submit():
        values=dict()
        if form.status.data!="":values["status"]=form.status.data
        
        new_data={"$set":values}
        query={"_c_id":form.id.data}
        course_col=mongo.db.courses
        course_col.update_one(query,new_data)
        flash("status modified")
        return redirect(url_for("menu"))
    else:
        return render_template("hide_course.html",form=form)