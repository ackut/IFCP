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


class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(500), nullable=False)
    creator = db.Column(db.String(16), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<admin {self.id}>'


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)  # Фамилия Имя преподавателя.
    login = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(500), nullable=False)
    creator = db.Column(db.String(16), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<teacher {self.id}>'


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
    name = db.Column(db.String(32), nullable=False)  # Фамилия Имя студента.
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
    creator = db.Column(db.String(16), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<subject {self.id}>'


class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)  # Название предмета.
    student = db.Column(db.Integer, nullable=False)  # Студент.
    creator = db.Column(db.String(16), nullable=False)  # Преподаватель.
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<grade {self.id}>'


class TeacherSubject(db.Model):
    __tablename__ = 'teacher_subject'
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, nullable=False)  # Преподаватель.
    subject_id = db.Column(db.Integer, nullable=False)  # Предмет.

    def __repr__(self):
        return f'<teacher_subject {self.id}>'



class Logs(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    priority = db.Column(db.Integer, default=0)
    creator_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(500), nullable=False)
    exception = db.Column(db.String(500))
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<logs {self.id}>'


def logger(priority: int, creator_id: int, text: str, exception: str =''):
    logs = Logs(priority=priority, creator_id=creator_id, text=text, exception=exception)
    db.session.add(logs)
    db.session.commit()
