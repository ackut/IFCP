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


class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)  # Название группы / специальность.
    login = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(500), nullable=False)
    creator = db.Column(db.String(16), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<group {self.id}>'


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)  # Имя Фамилия студента.
    login = db.Column(db.String(6), unique=True)  # Номер зачётки.
    group = db.Column(db.Integer, nullable=False)
    creator = db.Column(db.String(16), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<student {self.id}>'


class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)  # Название предмета.
    student = db.Column(db.Integer, nullable=False)  # Студент.
    creator = db.Column(db.String(16), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<subject {self.id}>'


class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)  # Название предмета.
    student = db.Column(db.Integer, nullable=False)  # Студент.
    creator = db.Column(db.String(16), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<grade {self.id}>'
