from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, url_for, request, flash, session, redirect
from app import app, db, User, logger, Logs, Student, Subject, UserSubject


@app.route('/admin/', methods=['POST', 'GET'])
def admin():
    if 'user_id' not in session or session['user_status'] != 3:
        return redirect(url_for('index'))

    context = {
        'title': 'Админка',
        'User': User,
        'Logs': Logs,
        'Student': Student,
        'Subject': Subject,
        'UserSubject': UserSubject
    }

    # TODO: Добавить проверку на пустые поля.
    if request.method == 'POST':
        form = request.form

        if 'create_user' in form:
            try:
                user = User(
                    login = form['login'].strip(),
                    password = generate_password_hash(form['password'].strip()),
                    status = form['status'],
                    name = form['name'],
                    creator = session['user_name']
                )
                db.session.add(user)
                db.session.commit()

                logger(1, session['user_name'], f'Пользователь добавлен: {user.name} | {user.login} | {user.status}')

            except Exception as ex:
                logger(3, session['user_id'], 'Ошибка добавления пользователя', str(ex))

        if 'add_student' in form:
            try:
                student = Student(
                    name = form['name'].strip(),
                    login = form['login'].strip(),
                    group_id = form['group_id'],
                    creator = session['user_name']
                )
                db.session.add(student)
                db.session.commit()

                logger(1, session['user_name'], f'Студент добавлен: {student.name} | {student.login} | {student.group_id}')

            except Exception as ex:
                logger(3, session['user_name'], 'Ошибка добавления студента', str(ex))

        if 'add_teacher' in form:
            try:
                user_subjects_id = []
                user_subjects = UserSubject.query.filter_by(user_id=form['user_id']).all()
                if user_subjects:
                    for user_subject in user_subjects:
                        user_subjects_id.append(user_subject.id)

                for subject_id in form.getlist('subject_id'):
                    if subject_id not in user_subjects_id:
                        user_subject = UserSubject(
                            user_id = form['user_id'],
                            subject_id = subject_id
                        )
                        db.session.add(user_subject)
                        db.session.commit()

                teacher = User.query.filter_by(id=user_subject.user_id).first()

                logger(1, session['user_name'], f'Преподаватель добавлен: {teacher.name}')

            except Exception as ex:
                logger(3, session['user_name'], 'Ошибка добавления преподавателя', str(ex))

        if 'add_subject' in form:
            try:
                subject = Subject(
                    name = form['name'],
                    creator = session['user_name']
                )
                db.session.add(subject)
                db.session.commit()

                logger(1, session['user_name'], f'Предмет добавлен: {subject.name}')

            except Exception as ex:
                logger(3, session['user_name'], 'Ошибка добавления предмета', str(ex))

        return redirect(url_for('admin'))

    return render_template('admin.html', context=context)
