from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, url_for, request, flash, session, redirect
from app import app, db, User, logger, Logs


@app.route('/admin/', methods=['POST', 'GET'])
def admin():
    if 'user_id' not in session or session['user_status'] != 3:
        return redirect(url_for('index'))

    context = {
        'title': 'Админка',
        'User': User,
        'Logs': Logs
    }

    # TODO: Добавить проверку на пустые поля.
    if request.method == 'POST':
        form = request.form
        print(form)

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

    return render_template('admin.html', context=context)
