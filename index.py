from flask import Flask, render_template, url_for, request, flash, session, redirect
from app import app, Student, Subject, User, UserSubject


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth'))

    context = {
        'title': 'Таблица',
        'Student': Student,
        'Subject': Subject,
        'User': User,
        'UserSubject': UserSubject,
    }


    return render_template('index.html', context=context)
    