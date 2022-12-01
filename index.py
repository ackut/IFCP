from app import app
from flask import Flask, render_template, url_for, request, flash, session, redirect


@app.route('/')
def index():
    context = {'title': ''}

    if 'user' not in session:
        return redirect(url_for('auth'))

    return render_template('index.html', context=context)
    