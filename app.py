from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


DEBUG = True
SECRET_KEY = '0c19e6ed-08a3-46cf-aecf-584f9213ee55'
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
# SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(__name__)


db = SQLAlchemy(app)


class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    login = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(500), nullable=False)
    users = db.Column(db.Integer, default=0)
    creator = db.Column(db.String(16), nullable=False, default='root')
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<group {self.id}>'


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(16), unique=True)
    name = db.Column(db.String(32), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    course = db.Column(db.Integer, nullable=False)
    creator = db.Column(db.String(16), nullable=False, default='root')
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<student {self.id}>'
