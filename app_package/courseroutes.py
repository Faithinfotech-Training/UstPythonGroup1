from flask import render_template, flash, redirect, url_for
from app_package import app, db,mongo
from app_package.courseforms import AddCourseForm,UpdateCourseForm
check=True
course_id=0
@app.route("/")
def menu():
    return redirect(url_for("display_course"))
@app.route("/add_course",methods=["GET","POST"])            
def add_course():
    global course_id,check 
    form=AddCourseForm()
    if form.validate_on_submit():
        
        fields=["_c_id","name","duration","fee","status","description"]
        course_id+=1
        if form.fee.data!="" and form.fee.data>0:
            values=[course_id,form.name.data,form.duration.data,form.fee.data,form.status.data,form.description.data]
        else:
            flash("Please enter valid fee")
            return render_template("add_course.html",form=form)
        
        course=dict(zip(fields,values))
        course_col=mongo.db.courses 
        if check:
            check=False
            if course_col.count==0:
                course_id=0
            else:
                cour=course_col.find().sort("_c_id",-1).limit(1)
                tmp=cour.next()
                course_id=tmp["_c_id"]
        course_id+=1
        course["_c_id"]=course_id
        tmp=course_col.insert_one(course)
        if tmp.inserted_id==course_id:
            flash("Course added")
            return redirect(url_for("display_course"))
        else:
            flash("Problem adding Course")
            return redirect(url_for("display_course"))
    else:
        return render_template("add_course.html",form=form)

@app.route("/update_course/<int:a>",methods=["GET","POST"])
def update_course(a):
    form=UpdateCourseForm()
    course_col=mongo.db.courses
    course=course_col.find_one({"_c_id":a})
    if form.validate_on_submit():
        values=dict()
        course_col=mongo.db.courses
        if form.duration.data!="":values["duration"]=form.duration.data
        if form.fee.data!="" and form.fee.data>0:values["fee"]=form.fee.data
        else:
            flash("Please enter valid fee")
            return render_template("update_course.html",form=form,course=course)
        if form.status.data!="":values["status"]=form.status.data   
        if form.duration.data!="":values["duration"]=form.duration.data
        if form.status.data!="":values["status"]=form.status.data
        new_data={"$set":values}
        query={"_c_id":a}
        
        course_col.update_one(query,new_data)
        flash("course modified")
        return redirect(url_for("display_course"))
    else:
        return render_template("update_course.html",form=form,course=course)

@app.route("/display_course")
def display_course():
    course_col=mongo.db.courses
    courses=course_col.find()
    return render_template("display_course.html",courses=courses)

