from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, url_for, request, flash, session, redirect
from app import app, db, User, Student, Subject, Grade, TeacherSubject, logger, Logs


@app.route('/admin/', methods=['POST', 'GET'])
def admin():
    if 'user_id' not in session or session['user_status'] != 3:
        return redirect(url_for('index'))

    context = {
        'title': 'Админка',
        'User': User,
        'Student': Student,
        'Subject': Subject,
        'Logs': Logs
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

        # if 'add_admin' in form:
        #     try:
        #         admin = Admin(
        #             login=form['admin_login'].strip(),
        #             password=generate_password_hash(form['admin_password'].strip()),
        #             creator=session['user']
        #         )
        #         db.session.add(admin)
        #         db.session.commit()
        #         logger(3, session['user_id'], f'{session["user"]} добавил администратора {admin.login}')

        #     except Exception as ex:
        #         logger(3, session['user_id'], 'Ошибка добавления администратора', str(ex))

        # if 'create_group' in form:
        #     try:
        #         group = Group(
        #             name=form['group_name'].strip(),
        #             login=form['group_login'].strip(),
        #             password=generate_password_hash(form['group_password'].strip()),
        #             creator=session['user']
        #         )
        #         db.session.add(group)
        #         db.session.commit()
        #         logger(0, session['user_id'], f'{session["user"]} добавил группу {group.name} ({group.login})')
                
        #     except Exception as ex:
        #         logger(2, session['user_id'], 'Ошибка добавления группы', str(ex))

        # if 'add_student' in form:
        #     try:
        #         student = Student(
        #             name=form['student_name'].strip(),
        #             group=form['student_group'],
        #             login=form['student_login'].strip(),
        #             creator=session['user']
        #         )
        #         db.session.add(student)
        #         db.session.commit()
        #         logger(0, session['user_id'], f'{session["user"]} добавил студента {student.name} ({student.login})')

        #     except Exception as ex:
        #         logger(0, session['user_id'], 'Ошибка добавления студента', str(ex))

        # if 'add_subject' in form:
        #     try:
        #         subject = Subject(
        #             name=form['subject_name'].strip(),
        #             creator=session['user']
        #         )
        #         db.session.add(subject)
        #         db.session.commit()
        #         logger(0, session['user_id'], f'{session["user"]} добавил предмет ({subject.name})')

        #     except Exception as ex:
        #         logger(0, session['user_id'], 'Ошибка добавления предмета', str(ex))

        # if 'add_teacher' in form:
        #     try:
        #         teacher = Teacher(
        #             name=form['teacher_name'].strip(),
        #             login=form['teacher_login'].strip(),
        #             password=generate_password_hash(form['teacher_password'].strip()),
        #             creator=session['user']
        #         )
        #         db.session.add(teacher)
        #         db.session.flush()

        #         for subject_id in form.getlist('teacher_subject'):
        #             teacher_subject = TeacherSubject(
        #                 teacher_id=teacher.id,
        #                 subject_id=int(subject_id)
        #             )
        #             db.session.add(teacher_subject)
        #         db.session.commit()
        #         logger(0, session['user_id'], f'{session["user"]} добавил преподавателя {teacher.name} ({teacher.login})')

        #     except Exception as ex:
        #         logger(0, session['user_id'], 'Ошибка добавления преподавателя', str(ex))

        return redirect(url_for('admin'))

    return render_template('admin.html', context=context)
