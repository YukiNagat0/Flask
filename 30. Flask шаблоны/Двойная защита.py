from flask import Flask, redirect, render_template
from flask_wtf.csrf import CSRFProtect

from forms.loginform import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
csrf = CSRFProtect(app)


@app.route('/success')
def success():
    params = {
        'title': 'Аварийный доступ'
    }

    return render_template('success.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    params = {
        'title': 'Аварийный доступ'
    }

    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', **params, form=form)


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
