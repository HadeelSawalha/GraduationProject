import mysql.connector

mydb = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='pnumeniafinal'
)

mycursor = mydb.cursor()


def signup(identitynumber, firstname,lastname, password, email):
    phone = '0599999999'
    gender = 'Male'
    city = 'palestine'
    username=firstname+' '+lastname
    print(username,"username")
    specialization="notSpecific"
    office_houre="notspecific"
    type=0
    sql1= f"INSERT INTO `user` (`id_user`, `user_name`,`pass`,`email`,`phone`, `gender`,`city`,`type`)  VALUES  ('{identitynumber}','{username}','{password}','{email}','{phone}','{gender}','{city}','{type}')"
    sql2= f"INSERT INTO `doctor` (`id_doctor`, `specialization`,`office_houre`)  VALUES  ('{identitynumber}','{specialization}','{office_houre}')"

    mycursor.execute(sql1)
    mydb.commit()
    mycursor.execute(sql2)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


def login(identityNumber, password):
    sql = "SELECT id_user,pass,type  FROM user  "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:

        #  id=tuple(x[0])
        # passwordd=tuple(x)
        if identityNumber in x[0] and password in x[1]:
            # status=True
            status = x[2]
            break

        else:
            status = -1



    return status


def editprofiledoctor1(idsession):
    sql1 = "SELECT *  FROM user where id_user= {}".format(idsession)
    sql2 = "SELECT *  FROM doctor where id_doctor= {}".format(idsession)
    mycursor.execute(sql1)
    myresult = mycursor.fetchall()

    mycursor.execute(sql2)
    myresult2 = mycursor.fetchall()
    return myresult,myresult2


def editprofiledoctorINsert( username, password, email,phone ,city,specialization,officehour,idsession,gender):

    sql1 = """UPDATE user SET user_name = %s,pass= %s,email= %s,phone= %s,city= %s,gender=%s WHERE id_user = %s"""
    input_data=(username,password,email,phone,city,gender,idsession)
    sql2 = """UPDATE doctor SET specialization = %s,office_houre= %s WHERE id_doctor  = %s"""
    input_data2=(specialization,officehour,idsession)

    mycursor.execute(sql1,input_data)
    mydb.commit()
    mycursor.execute(sql2, input_data2)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

#addpatient
def addpatient(IdentityNumber,firstname,lastname,password,email,city,phone,dateofbirth,Gender,today,type,idsession):
    allergiy_to_medication="notspesific"
    chronic_diseases="notspesific "
    username=firstname+' '+lastname
    sql1 = f"INSERT INTO `user` (`id_user`, `user_name`,`pass`,`email`,`phone`, `gender`,`city`,`type`)  VALUES  ('{IdentityNumber}','{username}','{password}','{email}','{phone}','{Gender}','{city}','{type}')"
    sql2 = f"INSERT INTO `patient` (`id_patient`, `birth_date`,`date`, `chronic_diseases`,`allergiy_to_medication`)  VALUES  ('{IdentityNumber}','{dateofbirth}','{today}','{chronic_diseases}','{allergiy_to_medication}')"
    sql3 = f"INSERT INTO `doctor_patient` (`id_doctor`, `id_patient`)  VALUES  ('{idsession}','{IdentityNumber}')"


    mycursor.execute(sql1)
    mydb.commit()
    mycursor.execute(sql2)
    mydb.commit()
    mycursor.execute(sql3)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

#Examinations_doctor
def Examinations_doctor1(idoctor,patientid,today,whiteBloodCells,Neutrophils,Lymphocytes,crp,Confusion,Respiratory,Systolic,Diastolic,bun,score,type,chronic_diseases,AllergiyToMedication):
    ###true
    sql=" SELECT MAX(id_information)from information where id_patient = {}".format(patientid)
    mycursor.execute(sql)
    idInformation1 = mycursor.fetchall()
    idInformation=idInformation1[0][0]

    sql3 = "SELECT result  FROM information where id_patient = {} and id_information =(SELECT MAX(id_information) from information where id_patient= {})".format(patientid,patientid)
    mycursor.execute(sql3)
    myresult3 = mycursor.fetchall()
    result=myresult3[0][0]
    if result=="Normal":

        sql2 = """UPDATE patient SET chronic_diseases = %s,allergiy_to_medication= %s WHERE id_patient   = %s"""
        input_data2 = (chronic_diseases, AllergiyToMedication, patientid)

        mycursor.execute(sql2, input_data2)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")

    else:
        sql1 = f"INSERT INTO `medicalexaminations` (`id_doctor`, `id_patient`,`date`, `whitebloodcells`,`neutrophils`,`lymphocytes`, `c_rp`,`confusion`,`respiratory`,`systolic`,`diastolic`,`bun`, `score`,`type`,`id_inform`)  " \
           f"VALUES  ('{idoctor}','{patientid}','{today}','{whiteBloodCells}','{Neutrophils}','{Lymphocytes}','{crp}','{Confusion}','{Respiratory}','{Systolic}','{Diastolic}','{bun}','{score}','{type}',{idInformation})"
        sql2 = """UPDATE patient SET chronic_diseases = %s,allergiy_to_medication= %s WHERE id_patient   = %s"""
        input_data2=(chronic_diseases,AllergiyToMedication,patientid)
        mycursor.execute(sql1)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        print("sql11",sql1)
        mycursor.execute(sql2, input_data2)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")

#isNormal(disable)
def isnormal(patientid):
  sql3 = "SELECT result  FROM information where id_patient = {} and id_information =(SELECT MAX(id_information)" \
         " from information where id_patient= {})".format(patientid,patientid)
  mycursor.execute(sql3)
  myresult3 = mycursor.fetchall()
  result=myresult3[0][0]
  return result


   #medicalNormal
def medicalNormal(idoctor,patientid,today):
    sql = " SELECT MAX(id_information)from information where id_patient = {}".format(patientid)
    mycursor.execute(sql)
    idInformation1 = mycursor.fetchall()
    idInformation = idInformation1[0][0]
    normal = "-"
    print("idInformation",idInformation)
    sql1 = f"INSERT INTO `medicalexaminations` (`id_doctor`, `id_patient`,`date`, `whitebloodcells`,`neutrophils`,`lymphocytes`, `c_rp`,`confusion`,`respiratory`,`systolic`,`diastolic`,`bun`, `score`,`type`,`id_inform`) " \
               f"VALUES  ('{idoctor}','{patientid}','{today}','{normal}','{normal}','{normal}','{normal}','{normal}','{normal}','{normal}','{normal}','{normal}','{normal}','{normal}','{idInformation}')"

    mycursor.execute(sql1)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")



def birthday(patientid):
    #true
    sql1 = "SELECT birth_date  FROM patient where 	id_patient= {}".format(patientid)
    mycursor.execute(sql1)
    myresult = mycursor.fetchall()
    print("myresult",myresult)
    #print("birthdate[0]",myresult[0])
    #print("birthdate[0][0]",myresult[0][0])

    return myresult


#patientFile
def uploadfile(patientid,filename,date,result):
   if result=="Normal":
       symptoms="not exist"
       treatment="The patient is Normal,does not need treatment"
       sql = f"INSERT INTO `information` (`id_patient`, `img`,`result`, `symptoms`,`treatment`,`date`)  VALUES  ('{patientid}','{filename}','{result}','{symptoms}','{treatment}','{date}')"
       mycursor.execute(sql)
       mydb.commit()
       print(mycursor.rowcount, "record inserted.")
   else:
       symptoms = "notspesific"
       treatment = "notready"
       sql=f"INSERT INTO `information` (`id_patient`, `img`,`result`, `symptoms`,`treatment`,`date`)  VALUES  ('{patientid}','{filename}','{result}','{symptoms}','{treatment}','{date}')"
       mycursor.execute(sql)
       mydb.commit()
       print(mycursor.rowcount, "record inserted.")

#symptoms
def symptoms(patientId,listname):
    ###true
    sql3 = "SELECT result  FROM information where id_patient = {} and id_information =(SELECT MAX(id_information) from information where id_patient= {}) ".format(patientId,patientId)
    mycursor.execute(sql3)
    myresult3 = mycursor.fetchall()
    result = myresult3[0][0]
    if result == "Pneumonia":
        str1=","
        str=str1.join(listname)
        #true
        sql2 = """UPDATE information SET symptoms = %s WHERE id_patient  = %s and id_information =(SELECT MAX(id_information) from information where id_patient= %s) """
        input_data2=( str,patientId,patientId)
        mycursor.execute(sql2, input_data2)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")


#acccount
def account(idsession):
    sql1 = "SELECT *  FROM user where id_user= {}".format(idsession)
    sql2 = "SELECT *  FROM doctor where id_doctor= {}".format(idsession)
    mycursor.execute(sql1)
    myresult = mycursor.fetchall()

    mycursor.execute(sql2)
    myresult2 = mycursor.fetchall()
    return myresult, myresult2

#Patientfile
def patientfile(idsession):
    sql1="SELECT id_patient,user_name FROM user,doctor_patient  where user.isactive=0 and doctor_patient.id_doctor = {} and user.id_user =doctor_patient.id_patient  ".format(idsession)
    #sql1 = "SELECT *  FROM user where id_user= {}".format(idsession)

    mycursor.execute(sql1)
    myresult1= mycursor.fetchall()
    print(myresult1,"patientfile")
    return myresult1

#patentMaintain
def patientmaintain(idsession):
    sql1= "SELECT id_user,user_name,email,phone,city,gender,date   " \
          "FROM user,patient where user.id_user=patient.id_patient and user.id_user in (select doctor_patient.id_patient from" \
          " doctor_patient,user where user.isactive=0 and doctor_patient.id_doctor = {} and user.id_user =doctor_patient.id_patient )".format(idsession)

    mycursor.execute(sql1)
    myresult = mycursor.fetchall()
    print("myresultpatientmaintain",myresult)
    return myresult

def patientmaintainRow(patientid):
    sql1 =" SELECT user_name,email,phone,gender,city,datem FROM user,patient where user.id_user= {} and patient.id_patient= {}".format(patientid,patientid)
    mycursor.execute(sql1)
    myresult = mycursor.fetchall()
    print("patientmaintainRow", myresult)
    return myresult
#patientresult
def patientResult(idsession):
    sql="SELECT user.id_user,user.user_name,information.date,information.result ,medicalexaminations.type,medicalexaminations.score  FROM user,information,medicalexaminations where user.isactive=0 and user.id_user=information.id_patient and information.id_patient= medicalexaminations.id_patient  and information.id_information =medicalexaminations.id_inform and user.id_user in (select doctor_patient.id_patient  from user,doctor_patient where  doctor_patient.id_doctor = {} and user.id_user=doctor_patient.id_patient)".format(idsession)
      #  "SELECT user.id_user,user.user_name,information.date,information.result ," \
       #  "medicalexaminations.type,medicalexaminations.score  FROM user,information,medicalexaminations where " \
        # " user.isactive=0 and user.id_user=information.id_patient and information.id_patient= medicalexaminations.id_patient  " \
         #" information.id_information =medicalexaminations.id_inform and user.id_user in (select doctor_patient.id_patient  from user,doctor_patient where  " \
         #"  doctor_patient.id_doctor = {} and user.id_user=doctor_patient.id_patient ".format(idsession)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult


#patientresult_patient
def patientResultpatient(idsession):
    sql="SELECT user.id_user,user.user_name,information.date,information.result ,medicalexaminations.type,medicalexaminations.score  FROM user,information,medicalexaminations where user.isactive=0 and user.id_user=information.id_patient and information.id_patient= medicalexaminations.id_patient  and information.id_information =medicalexaminations.id_inform and user.id_user in (select doctor_patient.id_patient  from user,doctor_patient where  doctor_patient.id_patient = {} and user.id_user=doctor_patient.id_patient)".format(idsession)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult
#Treatmant Row
def patientresultTreatRow(patientid,date):
    print("dateindatabase",date)
    print("patientideindatabase",patientid)

    sql1= "SELECT treatment from information where id_patient ={} and date='{}'".format(patientid,date)
    print("sql1",sql1)
    mycursor.execute(sql1)
    myresult3 = mycursor.fetchall()
    print("here is liat1 database patientresultTreatRow",myresult3)
    return  myresult3


def updateTreatRow(patientid,datee,treat):
    sql1 = """UPDATE information SET treatment = %s  WHERE id_patient  = %s and date =%s """
    input_data = ( treat,patientid,datee)
    mycursor.execute(sql1, input_data)
    mydb.commit()

# true
def getImg(patientid,date):
    sql1 = "SELECT img from information where id_patient ={} and  date='{}'".format(patientid, date)
    mycursor.execute(sql1)
    myresult3 = mycursor.fetchall()
    print("here is liat1 database patientresultTreatRow", myresult3)
    return myresult3

def getSym(patientid,date):

    sql1 = "SELECT symptoms from information where id_patient ={}  and date='{}'".format(patientid, date)
    mycursor.execute(sql1)
    myresult3 = mycursor.fetchall()
    print("here is liat1 database patientresultTreatRow", myresult3)
    return myresult3
"""
    sql1 = "SELECT id_user,user_name FROM user where type='1'  "
    sql2 = "SELECT result,date FROM information "
    sql3= "SELECT type,score FROM medicalexaminations "
  
  

    mycursor.execute(sql2)
    myresult2 = mycursor.fetchall()

    mycursor.execute(sql3)
    myresult3 = mycursor.fetchall()"""

#type
def TreatmentAndScore(patientid,score,type,treatment):
    sql3="SELECT result  FROM information where id_patient = {} and id_information=(SELECT MAX(id_information) from information where id_patient = {})".format(patientid,patientid)
    mycursor.execute(sql3)
    myresult3 = mycursor.fetchall()
    result=myresult3[0][0]
    if result=="Pneumonia":
        sql1 = """UPDATE medicalexaminations SET type = %s, score= %s  WHERE id_patient  = %s and id_examinations =(SELECT MAX(id_examinations)
        from medicalexaminations where id_patient  = %s)"""
        input_data = (type, score,patientid,patientid)
        sql2= """UPDATE information SET treatment = %s  WHERE id_patient  = %s and id_information =(SELECT MAX(id_information) from information where id_patient= %s) """
        input_data2= ( treatment, patientid,patientid)
        mycursor.execute(sql1, input_data)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        mycursor.execute(sql2, input_data2)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")

#viewfile

def viewfile(idpatient):
    #true
    sql1 = "SELECT * FROM user where id_user = {}".format(idpatient)
    mycursor.execute(sql1)
    myresult = mycursor.fetchall()
    #treatment symptoms
    # true
    sql2="SELECT result,img,symptoms,treatment from information where id_patient= {} and id_information =(SELECT MAX(id_information) from information where id_patient= {})" .format(idpatient,idpatient)
    mycursor.execute(sql2)
    myresult2 = mycursor.fetchall()
    # true
    sql3="SELECT * from medicalexaminations where id_patient = {} and   id_examinations =(SELECT MAX(id_examinations) " \
         "from medicalexaminations where id_patient = {})".format(idpatient,idpatient)



    mycursor.execute(sql3)
    myresult3 = mycursor.fetchall()
    print("sql1",sql1)
    print("sql2",sql2)

    print("sql3",sql3)

    print("database list1,2,3,for patientfile")
    print("list1",myresult)
    print("list2",myresult2)
    print("list3",myresult3)

    return myresult,myresult2,myresult3


def homepagestatistic():
    sql1="SELECT id_user FROM user where type ='1'"
    mycursor.execute(sql1)
    patient = mycursor.fetchall()

    sql2 = "SELECT id_user FROM user where type ='0'"
    mycursor.execute(sql2)
    doctor = mycursor.fetchall()


    sql3="SELECT result FROM user,information  where   user.id_user =information.id_patient and information.result='Pneumonia' "
    mycursor.execute(sql3)
    pnumonia = mycursor.fetchall()

    sql4="SELECT result FROM user,information  where   user.id_user =information.id_patient and information.result='Normal' "
    mycursor.execute(sql4)
    Normal = mycursor.fetchall()
    return patient,doctor,pnumonia,Normal


def dashboardtatistic(idsession):
    sql1="SELECT id_patient FROM user,doctor_patient where doctor_patient.id_doctor = {} and user.id_user =doctor_patient.id_patient  and user.gender='Male' ".format(idsession)
    mycursor.execute(sql1)
    male = mycursor.fetchall()
    print("len(male",len(male))
    sql2 = "SELECT id_patient FROM user,doctor_patient where doctor_patient.id_doctor = {} and user.id_user =doctor_patient.id_patient  and user.gender='Female' ".format( idsession)
    mycursor.execute(sql2)
    Female = mycursor.fetchall()
    print("len(male", len(Female))
    sql3 = "SELECT result FROM user,information,doctor_patient where   id_information in (SELECT max(id_information)from information GROUP BY id_patient) and doctor_patient.id_patient = information.id_patient and   " \
           " user.id_user =information.id_patient and information.result='Pneumonia' and doctor_patient.id_doctor = {}".format(idsession)
    mycursor.execute(sql3)
    pnumonia = mycursor.fetchall()
    print("len(pnumonia", len(pnumonia))
    sql4 = "SELECT result FROM user,information,doctor_patient where   id_information in (SELECT max(id_information)from information GROUP BY id_patient) " \
           "and doctor_patient.id_patient = information.id_patient and    user.id_user =information.id_patient and information.result='Normal' and doctor_patient.id_doctor = {}".format(idsession)
    mycursor.execute(sql4)
    Normal = mycursor.fetchall()
    print("len(Normal", len(Normal))
    return male,Female,pnumonia,Normal

def checkdoctor():
    sql="SELECT id_doctor from doctors_syndicate"
    mycursor.execute(sql)
    iddoctors = mycursor.fetchall()
    return  iddoctors
###########################################
###############
############
########
###
#patientt
def editprofilepatient1(idsession):
    sql1 = "SELECT *  FROM user where id_user= {}".format(idsession)
    mycursor.execute(sql1)
    myresult = mycursor.fetchall()

    return myresult


def editprofilepatientINsert(username, password, email,phone ,city,idsession):
    print("username", username)
    print("password", password)
    print("city", city)
    print("email", email)
    print("phone", phone)

    sql1 = """UPDATE user SET user_name = %s,pass= %s,email= %s,phone= %s,city= %s WHERE id_user = %s"""
    input_data = (username, password, email, phone, city, idsession)

    mycursor.execute(sql1, input_data)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")


def getImg1(patientid,date):
    sql1 = "SELECT img from information where id_patient ={} and  date='{}'".format(patientid, date)
    mycursor.execute(sql1)
    myresult3 = mycursor.fetchall()
    print("here is liat1 database patientresultTreatRow", myresult3)
    return myresult3

def getSym1(patientid,date):
    sql1="SELECT symptoms from information where id_patient ={}  and date='{}' and id_information =(SELECT max(id_information)FROM information WHERE id_patient={})".format(patientid, date,patientid)
    mycursor.execute(sql1)
    myresult3 = mycursor.fetchall()
    print("here is liat1 database patientresultTreatRow", myresult3)
    return myresult3
#Treatmant Row
def patientresultTreatRow1(patientid,date):
    print("dateindatabase",date)
    print("patientideindatabase",patientid)

    sql1= "SELECT treatment from information where id_patient ={} and date='{}'".format(patientid,date)
    print("sql1",sql1)
    mycursor.execute(sql1)
    myresult3 = mycursor.fetchall()
    print("here is liat1 database patientresultTreatRow",myresult3)
    return  myresult3
def deleteRow(id):
    print(" database", id)
    sql= "UPDATE user SET isactive = 1  WHERE  id_user  ={} ".format(id)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
"""
    sql1= "DELETE FROM information WHERE id_patient  ={}".format(id)
    mycursor.execute(sql1)
    mydb.commit()
    sql2 = "DELETE FROM medicalexaminations WHERE id_patient   ={}".format(id)
    mycursor.execute(sql2)
    mydb.commit()
    sql4 = "DELETE FROM doctor_patient WHERE id_patient   ={}".format(id)
    mycursor.execute(sql4)
    mydb.commit()
    sql3="DELETE FROM patient WHERE id_patient   ={}".format(id)
    mycursor.execute(sql3)
    mydb.commit()

    sql = "DELETE FROM user WHERE id_user ={}".format(id)
    print("after after database")
    print("sql",sql)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
    return 'true'"""
#editRow
def editroww(id,name,email,phone,gender,city):
    sql1 = """UPDATE user SET user_name = %s, email= %s ,phone=%s,gender=%s,city=%s WHERE id_user  = %s """
    input_data = (name, email, phone, gender, city,id)

    mycursor.execute(sql1, input_data)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
