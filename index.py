from flask import Flask, render_template, url_for, request, flash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'krutoiklu4'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/auth/', methods=['POST', 'GET'])
def auth():
    if request.method == 'POST':
        unique = request.form['unique']

        if not unique:
            flash('Пусто')
            return render_template('auth.html')

        if unique and (6 > len(unique) < 8):
            flash('Длина')


    return render_template('auth.html')


if __name__ == '__main__':
    app.run(debug=True)
