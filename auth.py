from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, url_for, request, flash, session, redirect, flash
from app import app, db, Admin, Group, Teacher


@app.route('/auth/', methods=['POST', 'GET'])
def auth():
    admins = Admin.query.all()
    if not admins:
        db.session.add(Admin(login='root', password=generate_password_hash('root')), creator='system')
        db.session.commit()

    if 'user' in session:
        return redirect(url_for('index'))

    elif request.method == 'POST':
        form = request.form
        if form['user_login'] and form['user_password']:
            if form['user_status'] == '1':
                group = Group.query.filter_by(login=form['user_login']).all()
                if not group:
                    print(f'Неверный логин группы: {form["user_login"]}.')
                    flash('Неверный логин группы')
                    return redirect(url_for('auth'))

                if not check_password_hash(group[0].password, form['user_password']):
                    print(f'Неверный пароль группы {form["user_login"]}.')
                    flash('Неверный пароль группы')
                    return redirect(url_for('auth'))

                print(f'Новая авторизация в группе {group[0].name} ({group[0].login}).')
                session['user'] = group[0].login
                session['status'] = 1
                session['user_id'] = group[0].id

            if form['user_status'] == '2':
                teacher = Teacher.query.filter_by(login=form['user_login']).all()
                if not teacher:
                    print(f'Неверный логин преподавателя: {form["user_login"]}.')
                    flash('Неверный логин преподавателя')
                    return redirect(url_for('auth'))

                if not check_password_hash(teacher[0].password, form['user_password']):
                    print(f'Неверный пароль преподавателя {form["user_login"]}.')
                    flash('Неверный пароль преподавателя')
                    return redirect(url_for('auth'))

                print(f'Преподаватель {teacher[0].name} авторизовался ({teacher[0].login}).')
                session['user'] = teacher[0].login
                session['status'] = 2
                session['user_id'] = teacher[0].id
            
            if form['user_status'] == '3':
                admin = Admin.query.filter_by(login=form['user_login']).all()
                if not admin:
                    print(f'Неверный логин администратора: {form["user_login"]}.')
                    flash('Неверный логин администратора')
                    return redirect(url_for('auth'))

                if not check_password_hash(admin[0].password, form['user_password']):
                    print(f'Неверный пароль администратора {form["user_login"]}.')
                    flash('Неверный пароль администратора')
                    return redirect(url_for('auth'))

                print(f'Администратор {admin[0].login} авторизовался.')
                session['user'] = admin[0].login
                session['status'] = 3
                session['user_id'] = admin[0].id
                return redirect(url_for('admin'))

        # session['user'] = request.form['user_login']
        return redirect(url_for('index'))

    context = {
        'title': ''
    }

    return render_template('auth.html', context=context)
    