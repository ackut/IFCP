from app import app
from flask import Flask, render_template, url_for, request, flash


@app.route('/auth/', methods=['POST', 'GET'])
def auth():
    return render_template('auth.html')
