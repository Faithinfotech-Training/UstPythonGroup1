from flask import render_template, flash, redirect, url_for
from app_package import app, mongo
from app_package.batch_forms import AddBatchForm, ModifyBatchForm

batch_id=0
check = True


@app.route("/display_batchs")
def display_batchs():
    batch_col=mongo.db.batchs
    batchs=batch_col.find()
    return render_template("display_batchs.html",batchs=batchs)

@app.route("/add_batch",methods=["GET","POST"])
#@login_required
def add_batch():
    global batch_id
    global check
    form=AddBatchForm()
    if form.validate_on_submit():
        fields=["_id","batch_name","start_date", "end_date", "course_id", "b_status"]
        batch_col=mongo.db.batchs
        if check:
            check=False
            if batch_col.count()==0:
                batch_id=0
            else:
                batch=batch_col.find().sort("_id",-1).limit(1)
                tmp=batch.next()
                batch_id=tmp["_id"]    
        batch_id+=1

        if form.start_date.data>form.end_date.data:
            flash("End date must be greater than start date")
            return render_template("add_batch.html", form=form)
        else: 

            values=[batch_id,form.batch_name.data,form.start_date.data,form.end_date.data,form.course_id.data,form.b_status.data]
            batch=dict(zip(fields,values))
            batch_col=mongo.db.batchs
            tmp=batch_col.insert_one(batch)
            if tmp.inserted_id==batch_id:
                flash("New batch added")
                return redirect(url_for("display_batchs"))
            else:
                flash("Problem adding batch")
                return redirect(url_for("display_batchs"))
    else:
        return render_template("add_batch.html",form=form)

@app.route("/modify_batch/<int:a>",methods=["GET","POST"])
def modify_batch(a):
    form=ModifyBatchForm()
    batch_col=mongo.db.batchs
    batch=batch_col.find_one({"_id":a})
    if form.validate_on_submit():
        values=dict()
        if form.start_date.data!="":values["start_date"]=form.start_date.data
        if form.end_date.data!="":values["end_date"]=form.end_date.data
        if form.b_status.data!="":values["b_status"]=form.b_status.data
        new_data={"$set":values}
        query={"_id":a}
        batch_col=mongo.db.batchs
        batch_col.update_one(query,new_data)
        if form.end_date.data<form.start_date.data:
            flash("End date must be earlier than start date")
            return render_template("modify_batch.html", form=form, batch=batch)
        flash("Batch details updated")
        return redirect(url_for("display_batchs"))
    else:
        return render_template("modify_batch.html",form=form, batch=batch)
