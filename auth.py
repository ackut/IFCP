from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, url_for, request, flash, session, redirect
from app import app, db, User


@app.route('/auth/', methods=['POST', 'GET'])
def auth():
    if not User.query.all():
        db.session.add(
            User(
                login='root',
                password=generate_password_hash('root'),
                status=3,
                name='root',
                creator='system'
            )
        )
        db.session.commit()

    if 'user_id' in session:
        return redirect(url_for('index'))

    elif request.method == 'POST':
        form = request.form
        if form['login'] and form['password']:
            user = User.query.filter_by(login=form['login']).first()
            if not user:
                print(f'Неверный логин пользователя: {form["login"]}.')
                return redirect(url_for('auth'))

            if not check_password_hash(user.password, form['password']):
                print(f'Неверный пароль пользователя {form["login"]}.')
                return redirect(url_for('auth'))

            session['user_id'] = user.id
            session['user_login'] = user.login
            session['user_status'] = user.status
            session['user_name'] = user.name

            print(f'Успешная авторизация. Пользователь: {user.name} ({user.login}).')

        return redirect(url_for('index'))

    context = {
        'title': 'Авторизация'
    }

    return render_template('auth.html', context=context)
