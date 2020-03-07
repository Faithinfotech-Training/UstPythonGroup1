from flask import render_template, flash, redirect, url_for
from app_package import app, db,mongo
from app_package.moduleforms import AddModuleForm,ModifyModuleForm,DeleteModuleForm


check=True
m_id=0
@app.route("/")

def menu():
    return redirect(url_for("display_module"))
    
    
@app.route("/add_module",methods=["GET","POST"])
def add_module():
    global m_id,check
    form=AddModuleForm()
    
    if form.validate_on_submit():
        fields=["_id","name"]
        m_id+=1
        values=[m_id,form.name.data]
        module=dict(zip(fields,values))
        m_col=mongo.db.modules
        if check:
            check=False
            if m_col.count()==0:
                m_id=0
            else:
                m=m_col.find().sort("_id",-1).limit(1)
                tmp=m.next()
                m_id=tmp["_id"]
        m_id+=1
        module["_id"]=m_id
        
        tmp=m_col.insert_one(module)
        if tmp.inserted_id==m_id:
            flash("Module added")
            return redirect(url_for("menu"))
        else:
               flash("Problem adding Module")
               return redirect(url_for("logout"))
        
                
         
         
    else:                
            return render_template("add_module.html",form=form)  
                                            
                                            
@app.route("/modify_module/<int:a>",methods=["GET","POST"])
      
def modify_module(a):
    form=ModifyModuleForm()
    m_col=mongo.db.modules
    module=m_col.find_one({"_id":a})
    if form.validate_on_submit():
        values=dict()
        m_col=mongo.db.modules
        
        if form.name.data!="":values["name"]=form.name.data
        
        new_data={"$set":values}
        query={"_id":a}
        m_col=mongo.db.modules
        m_col.update_one(query,new_data)
        flash("Module updated")
        return redirect(url_for("menu"))
    else:
        return render_template("modify_module.html",form=form,module=module)       
        
@app.route("/delete_module",methods=["GET","POST"])

def delete_module():
    form=DeleteModuleForm()
    if form.validate_on_submit():
        m_col=mongo.db.modules
        query={"name":form.name.data} 
        m_col.delete_one(query)
        flash("Module deleted")
        return redirect(url_for("menu"))
    else:
        return render_template("delete_module.html",form=form) 
                                                   
                                            
@app.route("/display_module")
       
def display_module():
    m_col=mongo.db.modules
    modules=m_col.find()
    return render_template("display_module.html",modules=modules)                                                    
