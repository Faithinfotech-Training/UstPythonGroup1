from flask import render_template, flash, redirect, url_for
from app_package import app, db,mongo
from app_package.forms_admission import AddAdmissionForm,ModifyAdmissionForm
check=True
adm_id=0

@app.route("/")
def menu():
    return render_template("menu.html")

@app.route("/add_admission",methods=["GET","POST"])
def add_admission():
    global adm_id,check
    form=AddAdmissionForm()
    if form.validate_on_submit():
        fields=["_id","photo","address","previouscourse","eq_id"]
        adm_id+=1
        values=[adm_id,form.photo.data,form.address.data,form.previouscourse.data,form.eq_id.data]
        admission=dict(zip(fields,values))
        adm_col=mongo.db.admission
        if check:
            check=False
            if adm_col.count==0:
                adm_id=0
            else:
                admit=adm_col.find().sort("_id",-1).limit(1)
                tmp=admit.next()
                adm_id=tmp["_id"]
        adm_id+=1
        admission["_id"]=adm_id
        tmp=adm_col.insert_one(admission)
        if tmp.inserted_id==adm_id:
            flash("Student added")
            return redirect(url_for("menu"))
        else:
            flash("Problem adding student")
    else:
        return render_template("add_admission.html",form=form)



@app.route("/modify_admission",methods=["GET","POST"])
def modify_admission():
    form=ModifyAdmissionForm()
    if form.validate_on_submit():
        values=dict()
        if form.photo.data!="":values["photo"]=form.photo.data
        if form.address.data!="":values["address"]=form.address.data
        new_data={"$set":values}
        query={"_id":form.id.data}
        adm_col=mongo.db.admission
        adm_col.update_one(query,new_data)
        flash("Admisiion modified")
        return redirect(url_for("menu"))
    else:
        return render_template("modify_admission.html",form=form)

@app.route("/display_admission")
def display_admission():
    adm_col=mongo.db.admission
    admission=adm_col.find()
    return render_template("display_admission.html",admission=admission)