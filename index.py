from app import app
from flask import Flask, render_template, url_for, request, flash


@app.route('/')
def index():
    return render_template('index.html')
    