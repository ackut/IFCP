from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, url_for, request, flash, session, redirect
from app import app, db, User, logger, Logs, StudentUser, Student


@app.route('/admin/', methods=['POST', 'GET'])
def admin():
    if 'user_id' not in session or session['user_status'] != 3:
        return redirect(url_for('index'))

    context = {
        'title': 'Админка',
        'User': User,
        'Logs': Logs,
        'Student': Student
    }

    # TODO: Добавить проверку на пустые поля.
    if request.method == 'POST':
        form = request.form

        if 'create_user' in form:
            try:
                user = User(
                    login=form['login'].strip(),
                    password=generate_password_hash(form['password'].strip()),
                    status=form['status'],
                    name=form['name'],
                    creator=session['user_name']
                )
                db.session.add(user)
                db.session.commit()

                logger(1, session['user_name'], f'Пользователь добавлен: {user.name} | {user.login} | {user.status}')

            except Exception as ex:
                logger(3, session['user_id'], 'Ошибка добавления пользователя', str(ex))

        if 'add_student' in form:
            try:
                student = Student(
                    name=form['name'].strip(),
                    login=form['login'].strip(),
                    group_id=form['group_id'],
                    creator=session['user_name']
                )
                db.session.add(student)
                db.session.flush()

                student_user = StudentUser(
                    student_id=student.id,
                    user_id=student.group_id
                )
                db.session.add(student_user)
                db.session.commit()

                logger(1, session['user_name'], f'Студент добавлен: {student.name} | {student.login} | {student.group_id}')

            except Exception as ex:
                logger(3, session['user_name'], 'Ошибка добавления студента', str(ex))

        redirect(url_for('admin'))

    return render_template('admin.html', context=context)
