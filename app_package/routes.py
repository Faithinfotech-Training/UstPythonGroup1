from flask import render_template, flash, redirect, url_for
from app_package import app, mongo

from app_package.forms import AddBatchForm, ModifyBatchForm




@app.route("/",methods=["GET","POST"])

def menu():
    return render_template("menu.html")



b_id=0

@app.route("/add_batch",methods=["GET","POST"])

def add_batch():
    global b_id
    form=AddBatchForm()
    if form.validate_on_submit():
        fields=["_id","b_name","start_date","end_date","b_status", "c_id"]
        b_id+=1
        values=[b_id,form.b_name.data,form.start_date.data,form.end_date.data,form.b_status.data,form.c_id.data]
        batch=dict(zip(fields,values))
        batch_col=mongo.db.batchs
        tmp=batch_col.insert_one(batch)
        if tmp.inserted_id==b_id:
            flash("Batch added")
            return redirect(url_for("menu"))
        else:
            flash("Problem adding batch")
            return redirect(url_for("menu"))
    else:
        return render_template("add_batch.html",form=form)

@app.route("/display_batchs")

def display_batchs():
    batch_col=mongo.db.batchs
    batchs=batch_col.find()
    return render_template("display_batchs.html",batchs=batchs)

@app.route("/modify_batch",methods=["GET","POST"])
def modify_batch():
    form=ModifyBatchForm()
    if form.validate_on_submit():
        values=dict()
        if form.start_date.data!="":values["start_date"]=form.start_date.data
        if form.end_date.data!="":values["end_date"]=form.end_date.data
        if form.b_status.data!="":values["b_status"]=form.b_status.data
        new_data={"$set":values}
        query={"_id":form.b_id.data}
        batch_col=mongo.db.batchs
        batch_col.update_one(query,new_data)
        flash("Batch details updated")
        return redirect(url_for("menu"))
    else:
        return render_template("modify_batch.html",form=form)
