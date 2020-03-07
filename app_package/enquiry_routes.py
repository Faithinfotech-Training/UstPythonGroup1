from flask import render_template,flash,redirect,url_for
from app_package import app, db,mongo
from app_package.enquiry_forms import NewEnquiryForm,UpdateEnquiryForm,EnquirySearchForm

e_id=0
check=True
@app.route("/newenquiry", methods=["GET","POST"])
def newenquiry() :
    global e_id
    global check
    form=NewEnquiryForm()
    if form.validate_on_submit() :
        fields=["_id","name","age","qualification","phone","passout_year","email","course","source_of_lead","status"]
        e_col=mongo.db.enquiries
        if check:
            check=False
            if e_col.count()==0 :
                e_id=0
            else:
                enq=e_col.find().sort("_id",-1).limit(1)
                tmp=enq.next()
                e_id=tmp["_id"]
        e_id+=1
        qualification = dict(form.qualification.choices).get(form.qualification.data)
        course = dict(form.course.choices).get(form.course.data)
        source_of_lead = dict(form.source_of_lead.choices).get(form.source_of_lead.data)
        status = dict(form.status.choices).get(form.status.data)
        values=[e_id,form.name.data,form.age.data,qualification,form.phone.data,form.passout_year.data,form.email.data,course,source_of_lead,status]
        new_added_enquiry=dict(zip(fields,values))
        e_col=mongo.db.enquiries
        tmp=e_col.insert_one(new_added_enquiry)
        if tmp.inserted_id==e_id:
            flash("Success")
            return redirect(url_for("viewenquiry"))
        else:
            flash("Problem adding enquiry")
            return render_template("newenquiry.html",form=form)
    else:
        return render_template("newenquiry.html",form=form)
    

@app.route("/searchenquiry/<int:e_id>",methods=["GET","POST"])
def searchenquiry(e_id):
    form=UpdateEnquiryForm()
    e_col=mongo.db.enquiries
    data=e_col.find_one({"_id":e_id})
    if form.validate_on_submit():
        values=dict()
        qualification=dict(form.qualification.choices).get(form.qualification.data)
        course=dict(form.course.choices).get(form.course.data)
        status=dict(form.status.choices).get(form.status.data)
        values["age"]=form.age.data
        values["qualification"]=qualification
        values["phone"]=form.phone.data
        values["passout_year"]=form.passout_year.data
        values["email"]=form.email.data
        values["course"]=course
        values["status"]=status
        new_data={"$set":values}
        query={"_id":e_id}
        e_col.update_one(query,new_data)
        flash("Enquiry details modified")
        return redirect(url_for("viewenquiry"))
    else:
        return render_template("searchenquiry.html",form=form,data=data)

@app.route("/enquiry")
def enquiry():
    return render_template("enquiry.html")
    
@app.route("/viewenquiry")
def viewenquiry():
    e_col=mongo.db.enquiries
    enquiries=e_col.find()
    return render_template("viewenquiry.html",enquiries=enquiries)

@app.route("/enquirysearch",methods=["GET","POST"])
def enquirysearch():
    form=EnquirySearchForm()
    if form.validate_on_submit:
        e_col=mongo.db.enquiries
        search=form.e_type.data
        if search=='Enquiry Id':
            e_id=int(form.e_name.data)
            e_query={"_id":e_id}
            e_data=e_col.find(e_query)
            if e_data is not None:
                return render_template("viewenquirysearch.html",e_data=e_data)
            else: 
                flash("Enquiry does not exist")
                return render_template("enquirysearch.html",form=form)
        elif search=='Name':
            n_query={"name":form.e_name.data}
            e_data=e_col.find(n_query)
            if e_data is not None:
                return render_template("viewenquirysearch.html",e_data=e_data)
            else: 
                flash("Enquiry does not exist")
                return render_template("enquirysearch.html",form=form)
        elif search=='Phone':
            e_phone=int(form.e_name.data)
            p_query={"phone":e_phone}
            e_data=e_col.find(p_query)
            if e_data is not None:
                return render_template("viewenquirysearch.html",e_data=e_data)
            else: 
                flash("Enquiry does not exist")
                return render_template("enquirysearch.html",form=form)
        elif search=='Status':
            e_status=form.e_name.data
            s_query={"status":e_status}
            e_data=e_col.find(s_query)
            if e_data is not None:
                return render_template("viewenquirysearch.html",e_data=e_data)
            else: 
                flash("Enquiry does not exist")
                return render_template("enquirysearch.html",form=form)
        else:
            return render_template("enquirysearch.html",form=form)
    else:
        flash("Not Avilable")
        return render_template("enquirysearch.html",form=form)