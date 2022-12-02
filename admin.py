from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, url_for, request, flash, session, redirect
from app import app, db, Group, Student, Subject, Grade, Teacher, TeacherSubject, logger, Logs, Admin


@app.route('/admin/', methods=['POST', 'GET'])
def admin():
    if 'user' not in session or session['status'] != 3:
        return redirect(url_for('index'))

    context = {
        'title': 'Админка',
        'admins': Admin.query.all(),
        'groups': Group.query.order_by(Group.name).all(),
        'students': Student.query.order_by(Student.name).all(),
        'subjects': Subject.query.order_by(Subject.name).all(),
        'teachers': Teacher.query.order_by(Teacher.name).all(),
        'logs': Logs.query.order_by(Logs.creation_date).all()
    }

    # TODO: Добавить проверку на пустые поля.
    if request.method == 'POST':
        form = request.form

        if 'add_admin' in form:
            try:
                admin = Admin(
                    login=form['admin_login'].strip(),
                    password=generate_password_hash(form['admin_password'].strip()),
                    creator=session['user']
                )
                db.session.add(admin)
                db.session.commit()
                logger(3, session['user_id'], f'{session["user"]} добавил администратора {admin.login}')

            except Exception as ex:
                print('Ошибка добавления админа.\n' + ex)

        if 'create_group' in form:
            try:
                group = Group(
                    name=form['group_name'].strip(),
                    login=form['group_login'].strip(),
                    password=generate_password_hash(form['group_password'].strip()),
                    creator=session['user']
                )
                db.session.add(group)
                db.session.commit()
                logger(0, session['user_id'], f'{session["user"]} добавил группу {group.name} ({group.login})')
                
            except Exception as ex:
                print('Ошибка добавления группы.\n' + ex)
                logger(2, session['user_id'], 'Ошибка добавления группы')

        if 'add_student' in form:
            try:
                student = Student(
                    name=form['student_name'].strip(),
                    group=form['student_group'],
                    login=form['student_login'].strip(),
                    creator=session['user']
                )
                db.session.add(student)
                db.session.commit()

            except Exception as ex:
                print('Ошибка добавления студента.\n' + ex)

        if 'add_subject' in form:
            try:
                subject = Subject(
                    name=form['subject_name'].strip(),
                    creator=session['user']
                )
                db.session.add(subject)
                db.session.commit()

            except Exception as ex:
                print('Ошибка добавления предмета.\n' + ex)

        if 'add_teacher' in form:
            try:
                teacher = Teacher(
                    name=form['teacher_name'].strip(),
                    login=form['teacher_login'].strip(),
                    password=generate_password_hash(form['teacher_password'].strip()),
                    creator=session['user']
                )
                db.session.add(teacher)
                db.session.flush()

                for subject_id in form.getlist('teacher_subject'):
                    teacher_subject = TeacherSubject(
                        teacher_id=teacher.id,
                        subject_id=int(subject_id)
                    )
                    db.session.add(teacher_subject)
                db.session.commit()

            except Exception as ex:
                print('Ошибка добавления преподавателя.\n' + ex)

        return redirect(url_for('admin'))

    return render_template('admin.html', context=context)
