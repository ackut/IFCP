from flask import url_for, session, redirect, g
from app import app
import index, auth, admin


@app.route('/clear/')
def clear():
    session.clear()
    return redirect(url_for('auth'))


if __name__ == '__main__':
    app.run()
