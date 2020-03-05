from flask import render_template, flash, redirect, url_for
from app_package import app, db,mongo
from app_package.forms import AddBatchForm,ModifyBatchForm,DisplayBatchForm



@app.route("/add_batch",methods=["GET","POST"])
def add_batch():
    global batch_id
    form=AddBatchForm()
    if form.validate_on_submit():
        fields=["_b_id","batch_name","start_date","end_date","c_id","status"]
        stud_id+=1
        values=[batch_id,form.batch_name.data,form.start_date.data,form.end_date.data,form.course_id.data,form.status.data]
        batch=dict(zip(fields,values))
        batch_col=mongo.db.batches
        tmp=batch_col.insert_one(batch)
        if tmp.inserted_id==batch_id:
            flash("Batch added")
            return redirect(url_for("menu"))
        else:
            flash("Problem adding batch")
            return redirect(url_for("logout"))
    else:
        return render_template("add_batch.html",form=form)

@app.route("/modify_batch",methods=["GET","POST"])
def modify_employee():
    form=ModifyBatchForm()
    if form.validate_on_submit():
        values=dict()
        if form.start_date.data!="":values["start_date"]=form.start_date.data
        if form.end_date.data!="":values["end_date"]=form.end_date.data
        if form.batch_name.data!="":values["batch_name"]=form.batch_name.data
        new_data={"$set":values}
        query={"_b_id":form.b_id.data}
        batch_col=mongo.db.batches
        batch_col.update_one(query,new_data)
        flash("Batch modified")
        return redirect(url_for("menu"))
    else:
        return render_template("modify_batch.html",form=form)
        
@app.route("/display_batches")
def display_employees():
    batch_col=mongo.db.batches
    batches=batch_col.find()
    return render_template("display_batches.html",batches=batches)