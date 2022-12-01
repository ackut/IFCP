from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, url_for, request, flash, session, redirect
from app import app, db, Groups, Students


@app.route('/admin/', methods=['POST', 'GET'])
def admin():
    context = {
        'title': '',
        'groups': Groups.query.order_by(Groups.course).all(),
        'students': Students.query.order_by(Students.name).all()
    }

    # TODO: Добавить проверку на пустые поля.
    if request.method == 'POST':
        form = request.form
        try:
            if 'create_group' in form:
                hashed_password = generate_password_hash(form['group_password'])
                group = Groups(
                    name=form['group_name'].strip(),
                    course=form['group_course'],
                    login=form['group_login'].strip(),
                    password=hashed_password,
                    creator=session['user']
                )
                db.session.add(group)
                db.session.commit()

            if 'add_student' in form:
                student = Students(
                    login=form['student_login'].strip(),
                    name=form['student_name'].strip(),
                    group=form['student_group'],
                    course=form['student_course'],
                    creator=session['user']
                )
                db.session.add(student)
                db.session.commit()

            return redirect(url_for('admin'))

        except Exception as ex:
            db.session.rollback()
            print(f'Ошибка БД: Не удалось добавить запись.\n{ex}')

    return render_template('admin.html', context=context)
