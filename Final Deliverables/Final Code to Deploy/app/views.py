from app import app
from flask import render_template
from .request import businessArticles, entArticles, get_news_source, healthArticles, publishedArticles, randomArticles, scienceArticles, sportArticles, techArticles, topHeadlines
from flask import Flask, render_template, request, redirect, session,flash
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=32328;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=fbx61194;PWD=WaR9CKMLetS23Zag",'','')

print (conn)
print('Connection successful++')

# app = Flask(__name__)
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
         #    cur1 = con.cursor()
         #    cur1.execute("select * from user_login where email=?",(emailid))
         #    check=cur1.rowcount
         # if(check!=0):
         #    error1="User with this Email ID already Exists !!"
         # else:
            cur = con.cursor()
            cur.execute("INSERT INTO user_login (email,password,name) VALUES (?,?,?)",(emailid,passwrd,usrname) )
            con.commit()
            error1="User Sign Up Successfull ! Proceed Login"
            flash("Record successfully added!")
      except:
         con.rollback()
      
      finally:
         return render_template("Signup.html",error="     User Sign Up Successfull ! Proceed Login")
         con.close()

@app.route('/loginfn',methods = ['POST', 'GET'])
def loginfn():  
    id = request.form["emailid"]  
    with sql.connect("ntapp.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("select email from user_login")  
            records=cur.fetchall
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("category.html") 
 
@app.route('/newsfeed')
def newsfeed():
    articles = publishedArticles()

    return  render_template('newsfeed.html', articles = articles)


@app.route('/headlines')
def headlines():
    headlines = topHeadlines()

    return  render_template('headlines.html', headlines = headlines)

@app.route('/articles')
def articles():
    random = randomArticles()

    return  render_template('articles.html', random = random)

@app.route('/sources')
def sources():
    newsSource = get_news_source()

    return  render_template('sources.html', newsSource = newsSource)

@app.route('/category/business')
def business():
    sources = businessArticles()

    return  render_template('business.html', sources = sources)

@app.route('/category/tech')
def tech():
    sources = techArticles()

    return  render_template('tech.html', sources = sources)

@app.route('/category/entertainment')
def entertainment():
    sources = entArticles()

    return  render_template('entertainment.html', sources = sources)

@app.route('/category/science')
def science():
    sources = scienceArticles()

    return  render_template('science.html', sources = sources)

@app.route('/category/sports')
def sports():
    sources = sportArticles()

    return  render_template('sport.html', sources = sources)

@app.route('/category/health')
def health():
    sources = healthArticles()

    return  render_template('health.html', sources = sources)