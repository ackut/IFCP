from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Главная',
    }
    return render_template('index.html', context=context)


@app.route('/about/')
def about():
    return 'about'


if __name__ == '__main__':
    app.run(debug=True)