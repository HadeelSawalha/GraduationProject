
from urllib import response
import tkinter

import flask
from django.core import mail
from flask import *
import database
import nuralnetwork.cnn
import randomforest.Testrandomforest
import os
import datetime
import cv2
import numpy as np
import cv2
import scipy.ndimage
import os
import glob
import treatment
from flask_mail import Mail, Message
app = Flask(__name__)

app.secret_key = "hadeel"
"""response = flask. Response()
response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')"""
#mail team70733@gmail.com Team123*?





app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'team70733@gmail.com'
app.config['MAIL_PASSWORD'] = 'Team123*?'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail= Mail(app)



""""qqqq
from flask_mail import Mail, Message
app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost/flask_app_db'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'infooveriq@gmail.com'  # enter your email here
app.config['MAIL_DEFAULT_SENDER'] = 'infooveriq@gmail.com' # enter your email here
app.config['MAIL_PASSWORD'] = 'password' # enter your password here

manager = Manager(app)
manager.add_command('db', MigrateCommand)
db = SQLAlchemy(app)
mail = Mail(app)"""
########
#homepage
@app.route('/')
def home():
    patient, doctor, pnumonia, Normal=database.homepagestatistic()
    numpatient=len(patient)
    numdoctor=len(doctor)
    numpnumonia=len(pnumonia)
    numNormal=len(Normal)
    print("patient",patient)
    print("doctor",doctor)
    print("pnumonia",pnumonia)
    print("Normal",Normal)
    #mail
  #  msg = Message('Hello', sender='hadeelrebhe05@gmail.com', recipients=['someone1@gmail.com'])
   # msg.body = "Hello Flask message sent from Flask-Mail"
    #mail.send(msg)
    return render_template("/project/html/homepage/homepage.html",numpatient=numpatient,numdoctor=numdoctor,numpnumonia=numpnumonia,numNormal=numNormal,succ=1)



@app.route('/send_message',methods=['Get','POST'])
def send_message():
    if request.method=='POST':
        email = request.form['email']
        subject=request.form['subject']
        msg = request.form['message']
        message=Message(subject,sender="team70733@gmail.com",recipients=[email])
        message.body=msg
        mail.send(message)
        success="seccus message"
        return render_template("/project/html/homepage/result.html",success=success)
@app.route('/What_Is_pneumonia')
def What_Is_pneumonia():
    return render_template("/project/html/homepage/homepage.html")


@app.route('/Diagnosis')

def Diagnosis():
    return render_template("/project/html/homepage/Diagnosis.html")


@app.route('/Type_of_pneumonia')

def Type_of_pneumonia():
    return render_template("/project/html/homepage/Type_of_pneumonia.html")



@app.route('/login2')

def login2():
    return render_template("/project/html/logsign/login.html")



@app.route('/forget')
def forget():
    return render_template("/project/html/logsign/forget.html")

#logout
@app.route('/logout')
def logout():
   # response = flask.Response()
    #response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    if 'identitynumber' in session:
        session.pop('identitynumber', None)
        return redirect('/')
        #return redirect(url_for('/project/html/homepage/homepage.html'))
        #return render_template('/project/html/homepage/homepage.html')



#login
@app.route('/project/html/logsign/login',methods=['POST'])
def login():
    identituNumber = request.form['identitynumber']
    password=request.form['password']
    stat =  database.login(identituNumber,password)
    if stat == -1:
        return render_template("/project/html/logsign/login.html",error=1)
    session['identitynumber'] = identituNumber
    if stat == 0:
       return  redirect('/dashboardDoctor22')
        #return render_template('/project/html/dashboard_doctor/dashboardDoctor22.html')
    return redirect('/dashboardPatient')
   # return render_template("/project/html/dashboard_patient/dashboardPatient.html")



#dashboardDoctor

@app.route('/dashboardDoctor22')
def dashboardDoctor22():
    print("offficeour out if")
    if 'identitynumber' in session:
        print("offficeour in if")
        x, y = database.account(session['identitynumber'])
        print("x",x)
        print("y",y)
        username = x[0][1]
        email = x[0][3]
        phone = x[0][4]
        specialization = y[0][1]
        officehour = y[0][2]
        print("officeour",officehour)
        male, Female, pnumonia, Normal=database.dashboardtatistic(session['identitynumber'])
        nummale=len(male)
        numfemale=len(Female)
        numpnumonia=len(pnumonia)
        numnormal=len(Normal)

        print("male",nummale)
        print("pnumonia",numpnumonia)
        print("femal",numfemale)
        print("normal",numnormal)

        return render_template("/project/html/dashboard_doctor/dashboardDoctor22.html", username=username,
                               email=email, phone=phone, specialization=specialization,
                               officehour=officehour,nummale=nummale,numfemale=numfemale,numpnumonia=numpnumonia,numnormal=numnormal)
        # return render_template('/project/html/dashboard_doctor/dashboardDoctor22.html')
    else:
        return render_template('/project/html/homepage/homepage.html')

    # if request.method == "POST":
    #     session['identitynumber'] = request.form['identitynumber']


@app.route('/EditProfile')
def EditProfile():
    w, z = database.account(session['identitynumber'])

    username = w[0][1]
    email = w[0][3]
    phone = w[0][4]
    specialization = z[0][1]
    officehour = z[0][2]
    x, y = database.editprofiledoctor1(session['identitynumber'] )
    print(x,"x")
    print("y",y)
    usernameEdit = x[0][1]
    passwordEdit = x[0][2]
    cityEdit = x[0][6]
    emailEdit = x[0][3]
    phoneEdit = x[0][4]
    specializationEdit = y[0][1]
    officehouredit = y[0][2]
    return render_template("/project/html/dashboard_doctor/EditProfile.html", usernameEdit=usernameEdit,
                           passwordEdit=passwordEdit,cityEdit=cityEdit,emailEdit=emailEdit,phoneEdit=phoneEdit,specializationEdit=specializationEdit,
                           officehouredit=officehouredit ,  username=username,
                           email=email, phone=phone, specialization=specialization,
                           officehour=officehour)



@app.route('/AddPatient')
def AddPatient():
    w, z = database.account(session['identitynumber'])

    username = w[0][1]
    email = w[0][3]
    phone = w[0][4]
    specialization = z[0][1]
    officehour = z[0][2]
    return render_template("/project/html/dashboard_doctor/AddPatient.html",username=username,email=email,phone=phone,specialization=specialization,officehour=officehour)


@app.route('/Files')
def Files():
    w, z = database.account(session['identitynumber'])

    username = w[0][1]
    email = w[0][3]
    phone = w[0][4]
    specialization = z[0][1]
    officehour = z[0][2]
    listpatient= database.patientfile(session['identitynumber'])
    #patientid=request.form['patientfile']


    return render_template("/project/html/dashboard_doctor/Files.html", listpatient=listpatient
                        ,username=username, email=email,
                           phone=phone, specialization=specialization, officehour=officehour)

@app.route('/infoforonerow',methods=['POST'])
def Viewfile():
   patientid = request.form['patientid']
   list1, list2, list3 = database.viewfile(patientid)
   list4=list1,list2,list3
   print("list4",list4)
   return  jsonify(results=list4)

# return render_template("/project/html/dashboard_doctor/Files.html")



@app.route('/symptomss')
def symptomss():
    w, z = database.account(session['identitynumber'])

    username = w[0][1]
    email = w[0][3]
    phone = w[0][4]
    specialization = z[0][1]
    officehour = z[0][2]
    return render_template("/project/html/dashboard_doctor/symptomss.html",username=username, email=email,
                           phone=phone, specialization=specialization,officehour=officehour)


@app.route('/Examinations')
def Examinations():
    w, z = database.account(session['identitynumber'])

    username = w[0][1]
    email = w[0][3]
    phone = w[0][4]
    specialization = z[0][1]
    officehour = z[0][2]


    return render_template("/project/html/dashboard_doctor/Examinations.html",username=username, email=email,
                           phone=phone, specialization=specialization,officehour=officehour)


@app.route('/maintain')
def maintain():
    w, z = database.account(session['identitynumber'])

    username = w[0][1]
    email = w[0][3]
    phone = w[0][4]
    specialization = z[0][1]
    officehour = z[0][2]

    listpatient = database.patientmaintain(session['identitynumber'])
    print(listpatient,"listpatient")
    return render_template("/project/html/dashboard_doctor/maintain.html", listpatient=listpatient, username=username, email=email,
                           phone=phone, specialization=specialization, officehour=officehour)


@app.route('/infoROwonemaintain',methods=['POST'])
def maintainRow():
   patientid = request.form['patientid']
   list1 = database.patientmaintainRow(patientid)
   print("list4",list1)
   return  jsonify(results=list1)
@app.route('/Result')
def Result():
    w, z = database.account(session['identitynumber'])

    username = w[0][1]
    email = w[0][3]
    phone = w[0][4]
    specialization = z[0][1]
    officehour = z[0][2]

    #listpatient = database.patientmaintain(session['identitynumber'])
    #print(listpatient, "listpatient")

    listname = database.patientResult(session['identitynumber'])
   #score=listname[0][5]
    return render_template("/project/html/dashboard_doctor/Result.html",listname=listname, username=username, email=email,
                           phone=phone, specialization=specialization, officehour=officehour)




 #return render_template("/project/html/dashboard_doctor/Result.html")





# return render_template("/project/html/dashboard_doctor/Files.html")

#signup



@app.route('/signup2')

def signup2():
    return render_template("/project/html/logsign/signUp.html")



@app.route('/project/html/logsign/signUp',methods=['POST'])

def signUp():

    firstname = request.form['firstname']
    lastname=request.form['lastname']
    identitynumber=request.form['identitynumber']
    password=request.form['password']
    confirmpassword=request.form['confirmpassword']
    email=request.form['email']
    #username=firstname+lastname

    if password !=confirmpassword:
        return render_template("/project/html/logsign/signUp.html",error=1)
    iddoctorsList=database.checkdoctor()
    #print("iddoctorsList[0]",iddoctorsList [:][0])
    for i in iddoctorsList:
        for j in i:
            print("j",j)
            if identitynumber ==j:
              database.signup(identitynumber, firstname,lastname,password, email)
              return render_template("/project/html/logsign/login.html")

    return render_template("/project/html/logsign/signUp.html", error2=1)



#addpatient

@app.route('/project/html/dashboard_doctor/AddPatient',methods=['POST'])

def addpatient_doctor():

    IdentityNumber=request.form['IdentityNumber']
    firstname = request.form['firstname']
    lastname=request.form['lastname']
    password=request.form['password']
    confirmpassword=request.form['confirmpassword']
    email=request.form['email']
    city=request.form['city']
    phone=request.form['phone']
    dateofbirth=request.form['dateofbirth']
    Gender=request.form['Gender']
    today = datetime.date.today()
    #idSession = idsession

    if password !=confirmpassword:
        return render_template("/project/html/dashboard_doctor/AddPatient.html",error=1)
    database.addpatient(IdentityNumber,firstname,lastname,password,email,city,phone,dateofbirth,Gender,today,1,session['identitynumber'])
    w, z = database.account(session['identitynumber'])

    usernamee = w[0][1]
    emaile = w[0][3]
    phonee = w[0][4]
    specializatione = z[0][1]
    officehoure = z[0][2]

    return render_template("/project/html/dashboard_doctor/AddPatient.html",username=usernamee,email=emaile,phone=phonee,specialization=specializatione,officehour=officehoure)




#editprofile


@app.route('/project/html/dashboard_doctor/EditProfile',methods=['POST'])

def editProfile_doctor():

    username = request.form['username']
    password=request.form['password']
    conformpassword=request.form['conformpassword']
    city=request.form['city']
    email=request.form['email']
    phone = request.form['phone']
    specialization = request.form['specialization']
    officehour = request.form['officehour']
    Gender=request.form['Gender']

    #idsession='556788888'

    if password !=conformpassword:
          return render_template("/project/html/dashboard_doctor/EditProfile.html",error=1)

    database.editprofiledoctorINsert( username, password, email,phone ,city,specialization,officehour, session['identitynumber'],Gender)

    w, z = database.account(session['identitynumber'])

    usernamee = w[0][1]
    emaile = w[0][3]
    phonee = w[0][4]
    specializatione = z[0][1]
    officehoure = z[0][2]
    return render_template("/project/html/dashboard_doctor/EditProfile.html",username=usernamee,email=emaile,phone=phonee,specialization=specializatione,officehour=officehoure)



#symptoms

@app.route('/project/html/dashboard_doctor/symptomss',methods=['POST'])
def symptomss_doctor():
    listname = []
    idpatient=request.form['patientid']
    if request.form.get("paininchest"):
         listname.append("Pain in chest")
    if request.form.get("Nausea"):
        listname.append("Nausea")
    if request.form.get("Cough"):
        listname.append("Cough")
    if request.form.get("muddle"):
         listname.append("muddle")
    if request.form.get("fever"):
         listname.append("Fever")
    if request.form.get("Temperature"):
        listname.append("Temperature(below normal)")
    if request.form.get("diarrhea"):
         listname.append("Diarrhea")
    if request.form.get("Shivering"):
             listname.append("Shivering")
    if request.form.get("shortnessofbreath"):
        listname.append("Shortness of breath")

    database.symptoms(idpatient,listname)
    w, z = database.account(session['identitynumber'])

    usernamee = w[0][1]
    emaile = w[0][3]
    phonee = w[0][4]
    specializatione = z[0][1]
    officehoure = z[0][2]
    return render_template("/project/html/dashboard_doctor/symptomss.html", username=usernamee, email=emaile,
                           phone=phonee, specialization=specializatione, officehour=officehoure)

#files
UPLOAD_FOLDER = 'static\\img\\img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    listpatient = database.patientfile(session['identitynumber'])
    patientid=request.form['patientfile']
    today = datetime.date.today()
    if request.method == 'POST':
       f = request.files['file']
       f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename ))
       filenamee='static\\img\\img\\'+f.filename
#Filter
       img = cv2.imread(filenamee)
       blur_image = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)
       cv2.imwrite("static/img/img/%s.jpeg" % (str(patientid)), blur_image)
       imgpath="static/img/img/%s.jpeg" % (str(patientid))

#result
       result=nuralnetwork.cnn.nueralImg(imgpath)
       database.uploadfile(patientid,imgpath,today,result)
       if result == "Normal":
           database.medicalNormal(session['identitynumber'], patientid, today)


       return render_template("/project/html/dashboard_doctor/Files.html", listpatient=listpatient)



#########Examiniation

@app.route('/project/html/dashboard_doctor/Examinations',methods=['POST'])
def Examinations_doctor():
    patientid=request.form['patientid']
    whiteBloodCells=request.form['whiteBloodCells']
    Neutrophils=request.form['Neutrophils']
    Lymphocytes=request.form['Lymphocytes']
    crp=request.form['crp']
    Confusion=request.form['Confusion']
    bun=request.form['bun']
    Respiratory=request.form['Respiratory']
    Systolic=request.form['Systolic']
    Diastolic=request.form['Diastolic']
    chronic_diseases=request.form['chronic_diseases']
    AllergiyToMedication=request.form['AllergiyToMedication']

    today = datetime.date.today()
    birthdate=database.birthday(patientid)
    yearNow = today.year
    birthdatee=birthdate[0][0]
    yearbirthday=birthdatee.year
    age=yearNow-yearbirthday

    x='0'
    y='0'
    xx=str(x)
    yy=str(y)
    database.Examinations_doctor1(session['identitynumber'] ,patientid,today,whiteBloodCells,Neutrophils,Lymphocytes,crp,Confusion,Respiratory,Systolic,Diastolic,bun,xx,yy,chronic_diseases,AllergiyToMedication)

    Type=randomforest.Testrandomforest.determineType(whiteBloodCells,Neutrophils,Lymphocytes,crp)
    Score=treatment.determinescore(Confusion,int(Respiratory),int(Systolic),int(Diastolic),int(bun),int(age))
    treatmentpatient=treatment.determinetreatment(Score,Type,chronic_diseases)
    score=str(Score)
    type=str(Type)
    if type=='0':
        database.TreatmentAndScore(patientid,score,'Viral',treatmentpatient)
    else:
        database.TreatmentAndScore(patientid,score,'Bacterial',treatmentpatient)

    w, z = database.account(session['identitynumber'])
    usernamee = w[0][1]
    emaile = w[0][3]
    phonee = w[0][4]
    specializatione = z[0][1]
    officehoure = z[0][2]

    return render_template("/project/html/dashboard_doctor/Examinations.html", username=usernamee, email=emaile,
                           phone=phonee, specialization=specializatione, officehour=officehoure)
@app.route('/resultRowImg',methods=['POST'])
def gettImg():
   patientid = request.form['patientid']
   datee=request.form['datee']
   print("idpaitientIngetimg",patientid)
   print("dateeIngetimg",datee)
   list1 = database.getImg(patientid,datee)
   print("list1img",list1)
   return  jsonify(results=list1)


@app.route('/SymForonerow',methods=['POST'])
def gettSym():
   patientid = request.form['patientid']
   datee = request.form['datee']
   list1 = database.getSym(patientid,datee)
   print("list1symptoms",list1)
   return  jsonify(results=list1)


#resultRowTreatment
@app.route('/resultRowTreatment',methods=['POST'])
def ResultRowTreatment():
   patientid = request.form['patientid']
   datee=request.form['datee']
   list1 = database.patientresultTreatRow(patientid,datee)
   print("here is list1 in ResultRowTreatment",list1)
   return  jsonify(results=list1)


@app.route('/updateTreatRow', methods=['POST'])
def updateTreatRow():
   id = request.form['id']
   date = request.form['date']
   treat=request.form['treat']
   print("treat",treat)
   list1= database.updateTreatRow(id,date,treat)
   print("here is list1 in ResultRowTreatment",list1)
   return  jsonify(results=list1)



@app.route('/deleteRow', methods=['POST'])
def deketeRow():
   print("xvxccx")
   id = request.form['id']
   print("id is",id)
   list1= database.deleteRow(id)
   print("here is list1 in ResultRowTreatment",list1)
   return  jsonify(results=list1)

@app.route('/deleteRowFile', methods=['POST'])
def deketeRowFile():
   print("xvxccx")
   id = request.form['id']
   print("id is",id)
   list1= database.deleteRow(id)
   print("here is list1 in ResultRowTreatment",list1)
   return  jsonify(results=list1)
#editrow

@app.route('/editRow', methods=['POST'])
def editRow():
   print("xvxccx")
   id = request.form['id']
   name= request.form['name']
   email = request.form['email']
   phone = request.form['phone']
   gender = request.form['gender']
   city = request.form['city']

   print("id is",id)
   list1= database.editroww(id,name,email,phone,gender,city)
   print("here is list1 in ResultRowTreatment",list1)
   return  jsonify(results=list1)

#disableelement
@app.route('/disableelement', methods=['POST'])
def disableelement():
   id = request.form['id']
   print("id is",id)
   list1= database.isnormal(id)
   if list1=="Normal":
     return '0'
   else:
       return '1'


#disableelementSymptoms
#
@app.route('/disableelementSymptoms', methods=['POST'])
def disableelementSymptoms():
   id = request.form['id']
   print("id is",id)
   list1= database.isnormal(id)
   if list1=="Normal":
     return '0'
   else:
       return '1'
#######################################################################################
######################################################
###Dashboard patient

#patientRout Show




@app.route('/EditProfilepatient')
def EditProfilepatient():
    w, z = database.account(session['identitynumber'])

    usernamee = w[0][1]
    emaile = w[0][3]
    phonee = w[0][4]
    x = database.editprofilepatient1(session['identitynumber'] )

    usernameEdit = x[0][1]
    passwordEdit = x[0][2]
    cityEdit = x[0][6]
    emailEdit = x[0][3]
    phoneEdit = x[0][4]
    return render_template("/project/html/dashboard_patient/EditProfilepatient.html",usernamee=usernamee,emaile=emaile,phonee=phonee, usernameEdit=usernameEdit,
                           passwordEdit=passwordEdit,cityEdit=cityEdit,emailEdit=emailEdit,phoneEdit=phoneEdit)



@app.route('/dashboardPatient')
def dashboardPatient():
    w, z = database.account(session['identitynumber'])

    usernamee = w[0][1]
    emaile = w[0][3]
    phonee = w[0][4]

    return render_template("/project/html/dashboard_patient/dashboardPatient.html", usernamee=usernamee,
                       emaile=emaile,
                       phonee=phonee)







#editprofile


@app.route('/project/html/dashboard_patient/EditProfilepatient',methods=['POST'])

def editProfile_patient():
    print("session['identitynumber']",session['identitynumber'])
    w, z = database.account(session['identitynumber'])

    usernamee = w[0][1]
    emaile = w[0][3]
    phonee = w[0][4]

    #listpatient = database.patientmaintain(session['identitynumber'])
    #print(listpatient, "listpatient")

    username = request.form['username']
    password=request.form['password']
    conformpassword=request.form['confirmpass']
    city=request.form['city']
    email=request.form['email']
    phone = request.form['phone']


    #idsession='556788888'
    if password!=conformpassword:
                    return render_template("/project/html/dashboard_patient/EditProfilepatient.html",error2=1)
    else:

      database.editprofilepatientINsert(username, password, email,phone ,city, session['identitynumber'] )

      return render_template("/project/html/dashboard_patient/EditProfilepatient.html",
                           usernamee=usernamee,
                           emaile=emaile,
                           phonee=phonee,error2=0)


@app.route('/Resultpatient')
def Resultpatient():

    w, z = database.account(session['identitynumber'])

    usernamee = w[0][1]
    emaile = w[0][3]
    phonee = w[0][4]


    listname = database.patientResultpatient(session['identitynumber'])
    print("listname",listname)
    return render_template("/project/html/dashboard_patient/Resultpatient.html",usernamee=usernamee, emaile=emaile, phonee=phonee,
                              listname=listname)

@app.route('/resultRowImg1',methods=['POST'])
def gettImg1():
  # patientid = request.form['patientid']
   datee=request.form['datee']
   print("dateeIngetimg",datee)
   list1 = database.getImg1(session['identitynumber'],datee)
   print("list1img",list1)
   return  jsonify(results=list1)


@app.route('/SymForonerow1',methods=['POST'])
def gettSym1():
 #  patientid = request.form['patientid']
   datee = request.form['datee']
   list1 = database.getSym1(session['identitynumber'],datee)
   print("list1symptoms",list1)
   return  jsonify(results=list1)


#resultRowTreatment
@app.route('/resultRowTreatment1',methods=['POST'])
def ResultRowTreatment1():
  # patientid = request.form['patientid']
   datee=request.form['datee']
   list1 = database.patientresultTreatRow1(session['identitynumber'],datee)
   print("here is list1 in ResultRowTreatment",list1)
   return  jsonify(results=list1)

if __name__ == '__main__':
    app.run(debug=True)