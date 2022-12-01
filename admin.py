from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, url_for, request, flash, session, redirect
from app import app, db, Group, Student


@app.route('/admin/', methods=['POST', 'GET'])
def admin():
    context = {
        'title': '',
        'groups': Group.query.order_by(Group.name).all(),
        'students': Student.query.order_by(Student.name).all()
    }

    # TODO: Добавить проверку на пустые поля.
    if request.method == 'POST':
        form = request.form
        try:
            if 'create_group' in form:
                hashed_password = generate_password_hash(form['group_password'].strip())
                group = Group(
                    name=form['group_name'].strip(),
                    login=form['group_login'].strip(),
                    password=hashed_password,
                    creator=session['user']
                )
                db.session.add(group)
                db.session.commit()

            if 'add_student' in form:
                student = Student(
                    name=form['student_name'].strip(),
                    group=form['student_group'],
                    login=form['student_login'].strip(),
                    creator=session['user']
                )
                db.session.add(student)
                db.session.commit()

            return redirect(url_for('admin'))

        except Exception as ex:
            db.session.rollback()
            print(f'Ошибка БД: Не удалось добавить запись.\n{ex}')

    return render_template('admin.html', context=context)
