from flask import render_template,flash,redirect,url_for
from app_package import app,db,mongo
from app_package.resource_forms import AddResourceForm,UpdateResourceForm
#from flask_login import current_user,login_user,logout_user,login_required




check=True
res_id=0
@app.route("/add_resource",methods=["GET","POST"])  
def add_resource():
    global res_id
    global check
    form=AddResourceForm()
    if form.validate_on_submit():
        fields=["_id","res_name","res_capacity","res_rent","res_status","type_of_use"]
        res_col=mongo.db.resources
        if check:
                check=False
                if res_col.count()==0:
                    res_id=0
                else:
                    res=res_col.find().sort("_id",-1).limit(1)
                    tmp=res.next()
                    res_id=tmp["_id"]
        res_id+=1
        values=[res_id,form.res_name.data,form.res_capacity.data,form.res_rent.data,form.res_status.data,form.type_of_use.data]
        resource=dict(zip(fields,values))
        res_col=mongo.db.resources
        query={"res_name":form.res_name.data}
        resources=res_col.find_one(query)
        if not bool(resources) :
            temp=res_col.insert_one(resource)
            if temp.inserted_id==res_id:
                flash("Resource added")
                return redirect(url_for("display_resources"))
        else:
            flash("Resource Already Added")
            return redirect(url_for("add_resource"))
    else:
        return render_template("add_resource.html",form=form)



            
    
@app.route("/display_resources",methods=["GET","POST"])
def display_resources():    
    res_col=mongo.db.resources
    resources=res_col.find()
    return render_template("display_resources.html",resources=resources) 


        
@app.route("/update_resource/<int:a>",methods=["GET","post"])
def update_resource(a):
    form=UpdateResourceForm()
    res_col=mongo.db.resources
    resources=res_col.find_one({"_id":a})
    if form.validate_on_submit():
        values=dict()
        if form.res_capacity.data!="":values["res_capacity"]=form.res_capacity.data
        if form.res_rent.data!="":values["res_rent"]=form.res_rent.data
        if form.res_status.data!="":values["res_status"]=form.res_status.data
        if form.type_of_use.data!="":values["type_of_use"]=form.type_of_use.data
        new_data={"$set":values}
        query={"_id":a}
        res_col=mongo.db.resources
        resources=res_col.find_one(query)
        res_col.update_one(query,new_data)    
        flash("Resourse Updated")
        return redirect(url_for("display_resources"))
        
    else:
        return render_template("update_resource.html",form=form,resources=resources)  
        