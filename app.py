from flask import Flask, request, render_template, redirect,url_for,session,flash
import pandas as pd
import mysql.connector
import numpy as np
from flask_mail import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
app=Flask(__name__)
app.secret_key='Lakshmi'
import hashlib
import datetime
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    port=3307,
    database="block_chain"
)
mycursor = mydb.cursor()
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/doctor')
def doctor():
    return render_template("doctor.html")
@app.route('/doctorback',methods=['POST','GET'])
def doctorback():
    if request.method=='POST':
        print("gekjhiuth")
        name=request.form['name']
        gen=request.form['gen']
        email=request.form['email']
        pwd=request.form['pwd']
        dob=request.form['dob']
        addr=request.form['addr']
        cpwd=request.form['cpwd']
        pno=request.form['pno']
        dtype=request.form['dtype']
        print(addr)
        sql="select * from doctor"
        result=pd.read_sql_query(sql,mydb)
        email1=result['email'].values
        print(email1)
        if email in email1:
            flash("email already existed","success")
            print("hhhhhhhhhhhhhhhhhhhhh")
            return render_template('doctor.html')
        if(pwd==cpwd):
            print("kkkkkkkkkkkkkkkkkkkkkkk")
            sql = "INSERT INTO doctor (name,dtype,email,pwd,dob,addr,pno,gen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (name,dtype,email,pwd,dob,addr,pno,gen)
            mycursor.execute(sql, val)
            mydb.commit()
            flash("Successfully Registered","warning")
            return render_template('ulog.html')
        else:
            flash("Password and Confirm Password not same")
    return render_template('doctor.html')
@app.route('/doctorlog')
def doctorlog():
    return render_template("ulog.html")

@app.route('/logback',methods=['POST', 'GET'])
def logback():
    if request.method == "POST":

        email = request.form['email']

        password1 = request.form['pwd']
        print('p')

        sql = "select * from doctor where email='%s' and pwd='%s'" % (email, password1)
        print('q')
        x = mycursor.execute(sql)
        print(x)
        results = mycursor.fetchall()
        print(results)
        global name
        session['email'] = email
        if len(results) > 0:
            flash("Welcome ", "primary")
            return render_template('doctorhome.html', msg=results[0][1])
        else:
            flash("Invali Email/Password ", "danger")
            return render_template('ulog.html', msg="invalid value")

    return render_template('ulog.html')

@app.route('/doctorhome')
def doctorhome():
    return render_template("doctorhome.html")

@app.route('/patient')
def patient():
    return render_template("register.html")

@app.route('/regback',methods=['POST','GET'])
def regback():
    if request.method=='POST':
        print("gekjhiuth")
        name=request.form['name']
        gen=request.form['gen']
        email=request.form['email']
        pwd=request.form['pwd']
        addr=request.form['addr']
        cpwd=request.form['cpwd']
        pno=request.form['pno']
        dob=request.form['dob']
        print(addr)

        sql="select * from patient"
        result=pd.read_sql_query(sql,mydb)
        email1=result['email'].values
        print(email1)
        if email in email1:
            flash("email already existed","success")
            return render_template('register.html')
        if(pwd==cpwd):
            sql = "INSERT INTO patient (name,email,pwd,gen,addr,dob,pno) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            val = (name,email,pwd,gen,addr,dob,pno)
            mycursor.execute(sql, val)
            mydb.commit()
            flash("Successfully Registered","warning")
            return render_template('login.html')
        else:
            flash("Password and Confirm Password not same")
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/loginback',methods=['POST', 'GET'])
def loginback():
    if request.method == "POST":

        email = request.form['email']

        password1 = request.form['pwd']
        print('p')

        sql = "select * from patient where email='%s' and pwd='%s' " % (email, password1)
        print('q')
        x = mycursor.execute(sql)
        print(x)
        results = mycursor.fetchall()

        print(results)
        global name
        session['email'] = email

        if len(results) > 0:
            flash("Welcome ", "primary")
            return render_template('patienthome.html', msg=results[0][1])
        else:
            flash("Invalid Email/Password ", "primary")
            return render_template('login.html', msg="invalid value")

    return render_template('login.html')

@app.route('/patienthome')
def patienthome():
    return render_template("patienthome.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/searchback",methods=['POST','GET'])
def searchback():
    print("dfhlksokhso")
    if request.method == 'POST':
        print("gekjhiuth")
        #fname = request.form['fname']
        dtype = request.form['dtype']

        print("Reading BLOB data from python_employee table")

        sql = "select * from doctor where dtype LIke '%"+dtype+"%' "
        x = pd.read_sql_query(sql, mydb)
        print("^^^^^^^^^^^^^")
        print(type(x))
        print(x)
        x = x.drop(['pwd'], axis=1)
        x = x.drop(['dob'], axis=1)
        x = x.drop(['addr'], axis=1)
        return render_template("searchback.html", col_name=x.columns.values, row_val=x.values.tolist())
    return render_template("searchback.html")

@app.route("/bookslot/<s1>/<s2>/<s3>/<s4>/<s5>")
def bookslot(s1=0,s2='',s3='',s4='',s5=''):
    global g,f1,a1,a2,a3
    g=s1
    f1=s2
    a1=s3
    a2=s4
    a3=s5
    return render_template("bookslot.html",g=g,f1=f1,a1=a1,a2=a2,a3=a3)


@app.route('/bookslotback',methods=['POST','GET'])
def bookslotback():
    if request.method=='POST':
        name = request.form['name']
        id = request.form['id']
        email = request.form['email']
        pname = request.form['pname']
        sym = request.form['sym']
        age = request.form['age']
        pno = request.form['pno']
        dtype = request.form['dtype']
        date = request.form['date']
        print(date)
        date2 = datetime.now().strftime('%Y-%m-%d')
        mycursor = mydb.cursor()
        pemail = session.get('email')
        if date >= date2:
            sql = "insert into bookslot(dname,pname,demail,pemail,sym,age,dtype,dno,date) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(name,pname,email,pemail,sym,age,dtype,pno,date)
            mycursor.execute(sql,val)
            mydb.commit()
            flash("slot Booking Successfully Completed","primary")
        else:
            flash("Slot booking not acceptable because the previous date not acceptable","warning")
    return render_template("searchback.html")

@app.route("/viewslot")
def viewslot():
    print("dfhlksokhso")
    print("Reading BLOB data from python_employee table")
    email = session.get('email')
    print(email)
    sql = "select * from bookslot where status='pending' and demail='%s' "%(email)
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['dname'], axis=1)
    x = x.drop(['demail'], axis=1)
    x = x.drop(['dtype'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['dno'], axis=1)
    return render_template("viewslot.html", col_name=x.columns.values, row_val=x.values.tolist())


@app.route('/accept/<s1>/<s2>/<s3>')
def accept(s1=0,s2='',s3=''):
    otp = "Dear  "
    msg1 = 'Your appointment is fixed with the same date as you requested.'
    msg = 'Thanks for choosing online slot booking.'
    t = 'Regards,'
    t1 = 'Online Health Services.'
    mail_content = otp + s2 +'\n'+ msg + msg1 +'\n'+'\n'+t+'\n'+t1
    sender_address = 'rameshreddymarthala025@gmail.com'
    sender_pass = 'cvjceozsxvillmde'
    receiver_address = s3
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Enhancing the Data Security in Cloud using Block Chain'
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    status='Completed'
    sql = "update bookslot set status='%s' where id='%s' "%(status,s1)
    mycursor.execute(sql)
    mydb.commit()
    flash("Slot accepted ","primary")
    return redirect(url_for('viewslot'))

@app.route('/reject/<s1>/<s2>/<s3>')
def reject(s1=0,s2='',s3=''):
    otp = "Dear  "
    msg1 = 'Your appointment is rejected. Kindly choose another date'
    msg = 'Thanks for choosing online slot booking.'
    t = 'Regards,'
    t1 = 'Online Health Services.'
    mail_content = otp + s2 +'\n'+ msg + msg1 +'\n'+'\n'+t+'\n'+t1
    sender_address = 'rameshreddymarthala025@gmail.com'
    sender_pass = 'cvjceozsxvillmde'
    receiver_address = s3
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Enhancing the Data Security in Cloud using Block Chain'
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    status='Rejected'
    sql = "update bookslot set status='%s' where id='%s' "%(status,s1)
    mycursor.execute(sql)
    mydb.commit()
    flash("Slot accepted ","primary")
    return redirect(url_for('viewslot'))


@app.route("/upload")
def upload():
    print("dfhlksokhso")
    print("Reading BLOB data from python_employee table")
    email = session.get('email')
    print(email)
    sql = "select * from bookslot where status='Completed' and demail='%s' and action='waiting' "%(email)
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['dname'], axis=1)
    x = x.drop(['demail'], axis=1)
    x = x.drop(['dtype'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['dno'], axis=1)
    x = x.drop(['action'], axis=1)


    return render_template("upload.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route("/upback/<s1>/<s2>/<s3>/<a>")
def upback(s1='',s2='',s3='',a=0):
    global g,f1,a1

    return render_template("upback.html",g=s1,f1=s2,a1=s3,a=a)


@app.route("/upback1",methods=["POST","GET"])
def upback1():
    if request.method=="POST":
        pname = request.form['pname']
        id = request.form['id']
        pemail = request.form['pemail']
        sym = request.form['sym']
        file =request.form['file']
        # email = session.get('email')

        dd = "text_files/" + file
        f = open(dd, "r")
        data = f.read()

       # print(data)
        dataleee=len(data)
        datalen=int(len(data)/3)
        print(datalen,len(data))
        g=0
        a = ''
        b = ''
        c = ''
        for i in range(0,2):
            if i==0:
                a=data[g: datalen:1]
                print(a)
                print("===================================")
                result = hashlib.sha1(a.encode())
                hash1 = result.hexdigest()
                print(hash1)
                print("++++++++++++++++++++++++++")

            # if i==1:
            #     g = datalen + 1
            #     # b=  datalen = datalen + datalen
            #     print(g)
            #     b=data[g: len(data):1]
            #     print(b)
            #     # print(datalen)
            #
            #     print("===================================")
            #     print("*****************************")
            #     result = hashlib.sha1(b.encode())
            #     hash2 = result.hexdigest()
            #     print(hash2)
            # print(data[g: datalen:1])
            #
            # print(g)
            # print(datalen)
        print(g)
        print(len(data))
        c=data[datalen: len(data):1]
        print(c)
        print("===================================")


        print("*****************************")
        result = hashlib.sha1(c.encode())
        hash2 = result.hexdigest()
        print(hash2)

        from datetime import datetime
        now = datetime.now()
        currentDay = datetime.now().strftime('%Y-%m-%d')
        sql = "INSERT INTO reports (fid,block1,block2,hash1,hash2,pname,pemail,sym,date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (id, a, c, hash1, hash2, pname,pemail,sym,now)
        mycursor.execute(sql, val)
        mydb.commit()
        otp = "Dear "
        msg='Here I am sending your reports pls refer it.'
        m1="You can download your health report now."
        m2='Hash values for downloading the file.'
        
        mail_content = otp + pname+ ','+msg + m1 + currentDay+'\n'+m2+hash1+' and '+ hash2
        sender_address = 'rameshreddymarthala025@gmail.com'
        sender_pass = 'cvjceozsxvillmde'
        receiver_address = pemail
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Enhancing the Data Security in Cloud using Block Chain'
        
        message.attach(MIMEText(mail_content, 'plain'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()

        status = 'Success'
        sql = "update bookslot set action='%s' where id='%s' " % (status, id)
        mycursor.execute(sql)
        mydb.commit()

        sql = "select * from reports where fid='%s' " % (id)
        x = pd.read_sql_query(sql, mydb)
        print("^^^^^^^^^^^^^")
        print(type(x))
        print(x)
        x = x.drop(['pname'], axis=1)
        # x = x.drop(['demail'], axis=1)
        x = x.drop(['pemail'], axis=1)
        x = x.drop(['block1'], axis=1)
        x = x.drop(['block2'], axis=1)
        x = x.drop(['date'], axis=1)
        x = x.drop(['fid'], axis=1)
        x = x.drop(['sym'], axis=1)
        flash("file uploaded successfully", "success")
    return render_template("upback1.html",col_name=x.columns.values, row_val=x.values.tolist())
@app.route('/viewreport<s1>/<s2>/<s3>')
def viewreport(s1=0,s2='',s3=''):
    return render_template('viewreport.html',s1=s1,s2=s2,s3=s3)
    
@app.route("/reportback",methods=['POST','GET'])
def reportback():
    print("dfhlksokhso")
    if request.method == 'POST':
        print("gekjhiuth")
        hash1 = request.form['hash1']
        id = request.form['id']
        hash2 = request.form['hash2']
        sql = "select count(*),CONCAT(block1,block2,'') from reports where hash1='"+hash1+"' and hash2='"+hash2+"'"
        x = pd.read_sql_query(sql, mydb)
        count=x.values[0][0]
        print(count)
        asss=x.values[0][1]
        asss=asss.decode('utf-8')
        print("^^^^^^^^^^^^^")
        return render_template("reportback.html", msg=asss)

@app.route("/down")
def down():
    email = session.get('email')
    print(email)
    sql = "select * from reports where pemail='%s'" %(email)
    x = pd.read_sql_query(sql, mydb)
    x = x.drop(['block1'], axis=1)
    x = x.drop(['fid'], axis=1)
    x = x.drop(['block2'], axis=1)
    x = x.drop(['pemail'], axis=1)
    x = x.drop(['hash1'], axis=1)
    x = x.drop(['hash2'], axis=1)
    x = x.drop(['pname'], axis=1)
    # x = x.drop(['date'], axis=1)

    # x["View Data"] = " "
    # x["Send Request"] = ""

    return render_template("down.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route("/download/<s1>/<s2>/<s3>")
def download(s1=0,s2='',s3=''):
    global g,f1,a1
    g=s1
    f1=s2
    a1=s3
    return render_template("download.html",g=g,f1=f1,a1=a1)

@app.route("/downfile",methods=['POST','GET'])
def downfile():
    print("dfhlksokhso")
    if request.method == 'POST':
        print("gekjhiuth")
        hash1 = request.form['hash1']
        id = request.form['id']
        hash2 = request.form['hash2']
        print()
        sql = "select CONCAT(block1,block2,'') from reports where hash1='"+hash1+"' and hash2='"+hash2+"'"
        x = pd.read_sql_query(sql, mydb)
        asss=x.values[0][0]
        print(asss)
        asss = asss.decode()
       
        return render_template("downfile.html", msg=asss)
    

    



if __name__=='__main__':
    app.run(debug=True)