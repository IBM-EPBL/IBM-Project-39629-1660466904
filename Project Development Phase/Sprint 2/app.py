from flask import Flask, render_template, request, redirect, session,flash
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'fasdgfdgdfg'


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/signup')
def signup():
   return render_template('Signup.html')

@app.route('/login')
def login():
   return render_template('Login.html')

@app.route('/signupfn',methods = ['POST', 'GET'])
def signupfn():
   if request.method == 'POST':
      try:
         emailid = request.form['emailid']
         passwrd = request.form['password']
         usrname = request.form['username']
         
         with sql.connect("ntapp.db") as con:
            cur1 = con.cursor()
            cur1.execute("select * from user_login where email=?",(emailid))
            check=cur1.rowcount
         if(check!=0):
            error1="User with this Email ID already Exists !!"
         else:
            cur = con.cursor()
            cur.execute("INSERT INTO user_login (email,password,name) VALUES (?,?,?)",(emailid,passwrd,usrname) )
            con.commit()
            error1="User Sign Up Successfull ! Proceed Login"
            flash("Record successfully added!")
      except:
         con.rollback()
      
      finally:
         return render_template("Signup.html",error=error1)
         con.close()

@app.route('/loginfn',methods = ['POST', 'GET'])
def loginfn():  
    emailid = request.form["emailid"]
    passwrd = request.form["password"]  
    with sql.connect("ntapp.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("select * from user_login where email=? and password=? limit 1"(emailid,passwrd))  
            records=cur.fetchall  
        except:  
            msg = "Incorrect Password / No Such Users Found"  
        finally:  
            return render_template("userfeed.html",msg=records) 

if __name__ == '__main__':
   app.run(debug = True)