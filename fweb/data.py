from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = ("sqlite:///test1.db")
db = SQLAlchemy(app)


class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Integer, unique=True, nullable=False)

def __init__(self, id, username, password):
    self.id = id
    self.username = username
    self.password = password


class Register(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True, nullable=False)
	email = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, unique=True, nullable=False)
	number = db.Column(db.Integer, unique=True, nullable=False)

def __init__(self, id, firstname, lastname, username, email, password, confirmpassword):

   self.id = id
   self.username = username
   self.email = email
   self.password = password
   self.number = number