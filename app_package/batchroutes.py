from flask import render_template, flash, redirect, url_for
from app_package import app, mongo
from app_package.batchforms import AddBatchForm, ModifyBatchForm

check=True
batch_id=0
@app.route("/",methods=["GET","POST"])
def index():
     return redirect(url_for("display_batch"))

@app.route("/add_batch",methods=["GET","POST"])
def add_batch():
    global check,batch_id
    form=AddBatchForm()
    if form.validate_on_submit():
        fields=["_id","batch_name","start_date","end_date","course_id","status"]
        batch_col=mongo.db.batches
        if check:
                check=False
                if batch_col.count()==0: 
                    batch_id=0
                else:
                    batch=batch_col.find().sort("_id",-1).limit(1)
                    tmp=batch.next()
                    batch_id=tmp["_id"]
        batch_id+=1
        values=[batch_id,form.batch_name.data,form.start_date.data,form.end_date.data,form.course_id.data,form.status.data]
        batch=dict(zip(fields,values))

        if form.start_date.data>form.end_date.data:
            flash("enddate must be greater than start date")
            return render_template("add_batch.html",form=form)
        else:
            batch_col=mongo.db.batches
            tmp=batch_col.insert_one(batch)
            if tmp.inserted_id==batch_id:
                flash("Batch added")
                return redirect(url_for("display_batch"))
            else:
                flash("Problem adding batch")
                
    else:
        return render_template("add_batch.html",form=form)
    
@app.route("/modify_batch/<int:a>",methods=["GET","POST"])
def modify_batch(a):
    form=ModifyBatchForm()
    batch_col=mongo.db.batches
    batch=batch_col.find_one({"_id":a})
    if form.validate_on_submit():
        values=dict()
        if form.start_date.data>form.end_date.data:
            flash("enddate must be greater than start date")
            return render_template("modify_batch.html",form=form)
        else:
            batch_col=mongo.db.batches
            if form.batch_name.data!="":values["batch_name"]=form.batch_name.data
            if form.start_date.data!="":values["start_date"]=form.start_date.data
            if form.end_date.data!="":values["end_date"]=form.end_date.data
            if form.status.data!="":values["status"]=form.status.data
            new_data={"$set":values}
            query={"_id":a}
            batch_col.update_one(query,new_data)
            flash("Batch succesfully modified")
            return redirect(url_for("display_batch"))
    else:
        return render_template("modify_batch.html",form=form,batch=batch)
        
@app.route("/display_batch")

def display_batch():   
    batch_col=mongo.db.batches
    batches=batch_col.find()
    return render_template("display_batch.html", batches= batches) 



