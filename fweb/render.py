from flask import Flask,render_template,redirect,url_for,session,request,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import date
#import pdb
app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = ("sqlite:///test3.db")
db = SQLAlchemy(app)


app.secret_key="564#654"

class Register(db.Model):
	uid = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(120), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(120), unique=True, nullable=False)
	number = db.Column(db.Integer, unique=True, nullable=False)

def __init__(self, uid, firstname, lastname, username, email, password, number):

   self.uid = uid
   self.username = username
   self.email = email
   self.password = password
   self.number = number

class Blog(db.Model):
	bid = db.Column(db.Integer, primary_key=True)
	uid = db.Column(db.Integer,db.ForeignKey('register'))
	username = db.Column(db.String(120),unique=False, nullable=False)
	#d1=date.today()
	datecreated=db.Column(db.DateTime, nullable=False)
	about= db.Column(db.String(120), unique=True, nullable=False)
	description= db.Column(db.String(120), unique=True, nullable=False)
def __init__(self,bid,uid,username,datecreated,about,description):
	self.bid = bid
	self.uid = uid
	self.username = username
	self.datecreated =datecreated
	self.about = about
	self.description = description
date=date.today()
@app.route('/showall')
def showall():
	result1=Register.query.all()
	return render_template('showall.html',result=result1)
@app.route('/detailpage/<uid>')
def detailpage(uid):
	result1=Register.query.filter_by(uid=uid).first()
	return render_template('detailpage.html',result=result1)
@app.route('/dess')
def dess():
	ress=Blog.query.all()
	return render_template('dess.html',result=ress)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")
@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/menu')
def menu():
	return render_template("menu.html")

@app.route('/tradition')
def tradition():
	return render_template("home.html")

@app.route('/gallery')
def gallery():
	return render_template("gallery.html")

@app.route('/blog',methods=['GET','POST'])
def blog():
	if request.method =="POST":
		obj=Blog(bid=request.form['bid'],uid=request.form['uid'],username=request.form['username'],datecreated=date,about=request.form['about'],description=request.form['description'])
		db.session.add(obj)
		db.session.commit()
		return redirect(url_for('dess'))
	else:
		return render_template("blog.html")

@app.route("/register",methods=['GET','POST'])
def register():
	#pdb.set_trace()
	if request.method =="POST":
		reg=Register(uid=request.form['uid'],username=request.form['username'],email=request.form['email'],password=request.form['password'],number=request.form['number'])
		db.session.add(reg)
		db.session.commit()

		return redirect(url_for('showall'))
	else:
		return render_template("register.html")


@app.route('/login',methods=['GET','POST'])
def login():
	if request.method =="POST":

		username=request.form['username']
		
		session["username"]=username
		print(username)
		password=request.form['password']
		session["password"]=password
		# if username =="admin" and password=="admin":
		return redirect(url_for('menu'))
	else:

		return render_template("login.html")


@app.route("/username")
def username():
	if "username" in session:
		username=session["username"]
		return f"<h1>{username}</h1>"
	else:
		return redirect(url_for("login"))

@app.route('/logout')
def logout():
	session.pop("username",None)
	flash("you have been logged out!")
	return redirect(url_for("index"))



if __name__=="__main__":
	db.create_all()
	app.run(debug=True)
