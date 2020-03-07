from flask import render_template,flash,redirect,url_for
from app_package import app,db,mongo
#from flask_login import current_user,login_user,logout_user,login_required
from app_package.course_forms import AddQualificationForm

check=True    
q_id=0
@app.route("/addqualification",methods=["GET","POST"])
def addqualification():
    global q_id
    global check
    form=AddQualificationForm()
    if form.validate_on_submit():
        fields=["_id","qualificationName"]
        qualification_col=mongo.db.qualifications
        if check:
            check=False
            if qualification_col.count()==0:
                q_id=0
            else:
                qual=qualification_col.find().sort("_id",-1).limit(1)
                tmp=qual.next()
                q_id=tmp["_id"]
        q_id+=1
        values=[q_id,form.qualificationName.data]
        qualification=qualification_col.find_one({"qualificationName":form.qualificationName.data})
        if not bool(qualification):
            qualification=dict(zip(fields,values))
            temp=qualification_col.insert_one(qualification)
            if temp.inserted_id==q_id:
                flash("qualification added")
                return redirect(url_for("viewqualification"))
            else:
                flash("problem on adding qualification ")
                return redirect(url_for("addqualification"))
        else:
            flash("qualification name already exist")
            return redirect(url_for("addqualification"))
           
    else:
        return render_template("addqualification.html",form=form)
       
       
       


@app.route("/viewqualification",methods=["GET","POST"])
def viewqualification():
    qualification_col=mongo.db.qualifications
    qualifications=qualification_col.find()
   
    return render_template("viewqualification.html",qualifications=qualifications)
