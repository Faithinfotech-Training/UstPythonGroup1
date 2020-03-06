from flask import render_template, flash, redirect, url_for
from app_package import app, db,mongo
from app_package.resourceforms import AddResourceForm,ModifyResourceForm


check=True
res_id=0
@app.route("/")

def menu():
    return redirect(url_for("display_resource"))
    
    
@app.route("/add_resource",methods=["GET","POST"])
def add_resource():
    global res_id,check
    form=AddResourceForm()
    
    if form.validate_on_submit():
        fields=["_id","name","capacity","rent","status","typeofuse"]
        res_id+=1
        if form.capacity.data<=0 and form.rent.data<=0:
            values=[res_id,form.name.data,form.capacity.data,form.rent.data,form.status.data,form.typeofuse.data]
            resource=dict(zip(fields,values))
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
            resource["_id"]=res_id
            tmp=res_col.insert_one(resource)
            if tmp.inserted_id==res_id:
                flash("Resource added")
                return redirect(url_for("menu"))
            else:
                flash("Problem adding Resource")
                return redirect(url_for("logout"))
        else:
            flash("Negative value")
            return redirect(url_for("menu"))
    else:                
        return render_template("add_resource.html",form=form)  
                                            
                                            
@app.route("/modify_resource/<int:a>",methods=["GET","POST"])
      
def modify_resource(a):
    form=ModifyResourceForm()
    res_col=mongo.db.resources
    resource=res_col.find_one({"_id":a})
    if form.validate_on_submit():
        values=dict()
        res_col=mongo.db.resources
        
        if form.rent.data!="":values["rent"]=form.rent.data
        if form.status.data!="":values["status"]=form.status.data
        if form.typeofuse.data!="":values["typeofuse"]=form.typeofuse.data 
        new_data={"$set":values}
        query={"_id":a}
        res_col=mongo.db.resources
        res_col.update_one(query,new_data)
        flash("Resource updated")
        return redirect(url_for("menu"))
    else:
        return render_template("modify_resource.html",form=form,resource=resource)       
        
        
                                            
@app.route("/display_resource")
       
def display_resource():
    res_col=mongo.db.resources
    resources=res_col.find()
    return render_template("display_resource.html",resources=resources)                                                    