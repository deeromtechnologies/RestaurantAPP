from flask import Flask,render_template,redirect,url_for,session,request,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators,IntegerField
from wtforms.validators import DataRequired
from flask_mail import Mail, Message

import pdb
app = Flask(__name__)

app.config['DEBUG'] =True
app.config['TESTING'] = False
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465


app.config['MAIL_USERNAME'] = '******'
app.config['MAIL_PASSWORD'] = '*****'

app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)



app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = ("sqlite:///test3.db")
db = SQLAlchemy(app)


app.secret_key="564#654"


class MyForm(FlaskForm):
	uid = IntegerField('id',validators=[DataRequired()])
	username = StringField('Username', [validators.Length(min=4, max=25)])
	email = StringField('Email Address', [validators.Length(min=6, max=35)])
	password = PasswordField('New Password', [validators.DataRequired(),validators.EqualTo('confirm', message='Passwords must match')])
	confirm = PasswordField('Repeat Password')
	number= IntegerField('Number')

class BForm(FlaskForm):
	bid = IntegerField('uid',validators=[DataRequired()])
	uid = IntegerField('bid',validators=[DataRequired()])
	username = StringField('Username', [validators.Length(min=4, max=25)])
	about = StringField('about', [validators.Length(min=4, max=25)])
	description = StringField('description', [validators.Length(min=4, max=25)])
    

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

@app.route('/blog/<int:bid>/update',methods=["GET","POST"])
def update(bid):
	form = BForm(request.form)
	emp=Blog.query.filter_by(bid=bid).first()
	if request.method=='POST':
		if emp:
			db.session.delete(emp)
			db.session.commit()
			uid=form.uid.data
			username=form.username.data
			about=form.about.data
			description=form.description.data
			emp=Blog(bid=bid,uid=uid,username=username,datecreated=date,about=about,description=description)
			db.session.add(emp)
			db.session.commit()
			return redirect(url_for('dess'))
		return f"User with id = {bid} Does not exist"
	return render_template('update.html', emp = emp)

@app.route('/blog/<int:bid>/delete',methods=["GET","POST"])
def delete(bid):
	form=BForm(request.form)
	emp1=Blog.query.filter_by(bid=bid).first()
	if request.method=="POST":
		if emp1:
			db.session.delete(emp1)
			db.session.commit()
			return redirect(url_for('dess'))
		abort(404)
	return render_template('delete.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	#pdb.set_trace()
	form = MyForm(request.form)
	if request.method=='POST' and form.validate_on_submit():
		email=form.email.data
<<<<<<< HEAD
		msg = Message("Hello",sender="***",recipients=[email])
=======
		msg = Message("Hello",sender="*****",recipients=[email])
>>>>>>> d639615d6a311ee824003659223cad60427a00fb
		msg.body = "Thank you for registering with us"
		mail.send(msg)
		regi=Register(uid=form.uid.data,username=form.username.data,email=form.email.data,password=form.password.data,number=form.number.data)
		db.session.add(regi)
		db.session.commit()
		return redirect(url_for('showall'))
	return render_template('register.html', form=form)


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
@app.route('/edit')
def edit():
	return render_template('update')


@app.route('/')
def index():
	
	#return 'Message has been sent!'
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
	form = BForm(request.form)
	if request.method =="POST":
		obj=Blog(bid=form.bid.data,uid=form.uid.data,username=form.username.data,datecreated=date,about=form.about.data,description=form.description.data)
		db.session.add(obj)
		db.session.commit()
		return redirect(url_for('dess'))
	else:
		return render_template("blog.html",form=form)

#@app.route("/register",methods=['GET','POST'])
#def register():
	#pdb.set_trace()
#	if request.method =="POST":
#		reg=Register(uid=request.form['uid'],username=request.form['username'],email=request.form['email'],password=request.form['password'],number=request.form['number'])
#		db.session.add(reg)
#		db.session.commit()

#		return redirect(url_for('showall'))
#	else:
#		return render_template("register.html")


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
