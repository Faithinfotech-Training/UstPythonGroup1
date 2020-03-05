from flask import render_template, flash, redirect, url_for
from app_package import app, db,mongo
from app_package.forms import AddAdmissionForm,ModifyAdmissionForm,DisplayAdmissionForm



@app.route("/add_student",methods=["GET","POST"])
@login_required
def add_student():
    global stud_id
    form=AddJoinedStudentForm()
    if form.validate_on_submit():
        fields=["_id","name","age","idproof","address","previouscourse"]
        stud_id+=1
        values=[cnd_id,form.name.data,form.age.data,form.idproof.data,form.address.data,form.previouscourse.data]
        student=dict(zip(fields,values))
        stud_col=mongo.db.students
        tmp=stud_col.insert_one(student)
        if tmp.inserted_id==stud_id:
            flash("Student added")
            return redirect(url_for("menu"))
        else:
            flash("Problem adding student")
            return redirect(url_for("logout"))
    else:
        return render_template("add_student.html",form=form)