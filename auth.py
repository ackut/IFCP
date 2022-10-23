from app import app
from flask import Flask, render_template, url_for, request, flash


@app.route('/auth/', methods=['POST', 'GET'])
def auth():
    if request.method == 'POST':
        unique = request.form['unique']

        # TODO: Добавить проверки.
        if not unique:
            flash('Пожалуйста, введите свой уникальный код', category='warning')
            return render_template('auth.html')

        if unique and (6 > len(unique) < 8):
            flash('Длина', category='warning')


    return render_template('auth.html')
