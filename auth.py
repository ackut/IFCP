from flask import Flask, render_template, url_for, request, flash, session, redirect
from app import app


@app.route('/auth/', methods=['POST', 'GET'])
def auth():
    context = {'title': ''}

    if 'user' in session:
        return redirect(url_for('index'))

    elif request.method == 'POST' and (request.form['user_login'], request.form['user_password']) == ('ASKIT', 'asdasd'):
        session['user'] = request.form['user_login']
        return redirect(url_for('index'))

    return render_template('auth.html', context=context)
    