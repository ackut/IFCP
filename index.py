from flask import Flask, render_template, url_for, request, flash, session, redirect
from app import app, Student, Group, Subject, Teacher, TeacherSubject


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user' not in session:
        return redirect(url_for('auth'))

    table_selected = {}
    if request.method == 'POST':
        form = request.form
        table_selected['group'] = int(form['table__group-select'])
        table_selected['subject'] = int(form['table__subject-select'])

    context = {
        'title': 'Таблица',
        'Group': Group,
        'Student': Student,
        'Subject': Subject,
        'Teacher': Teacher,
        'TeacherSubject': TeacherSubject,
        'table_selected': table_selected
    }


    return render_template('index.html', context=context)
    