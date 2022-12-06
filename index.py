from flask import Flask, render_template, url_for, request, flash, session, redirect
from app import app, Student, Subject, TeacherSubject


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth'))

    table_selected = {}
    if request.method == 'POST':
        form = request.form
        table_selected['group'] = int(form['table__group-select'])
        table_selected['subject'] = int(form['table__subject-select'])

    context = {
        'title': 'Таблица',
        'Student': Student,
        'Subject': Subject,
        'TeacherSubject': TeacherSubject,
        'table_selected': table_selected
    }


    return render_template('index.html', context=context)
    