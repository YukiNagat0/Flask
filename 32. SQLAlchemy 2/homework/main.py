import datetime

from flask import Flask, render_template, redirect
from flask_wtf import CSRFProtect

from flask_login import LoginManager, login_user, logout_user, login_required

from data import db_session

from data.users import Users

from forms.login_form import LoginForm
from forms.registration_form import RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
csrf_protect = CSRFProtect(app)

app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=360)

login_manager = LoginManager()
login_manager.init_app(app)

DATA_BASE = 'db/mars_explorers.db'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(Users).get(user_id)


@app.route('/')
@app.route('/index')
def index():
    return render_template('journal.html', title='Works log')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()

        if db_sess.query(Users).filter(Users.email == form.email.data).first():
            return render_template('registration.html', title='Registration', form=form,
                                   message='Такой пользователь уже зарегистрирован.')

        user = Users()
        user.email = form.email.data
        user.surname = form.surname.data
        user.name = form.name.data
        user.age = form.age.data
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.address = form.address.data
        user.set_password(form.password_1.data)

        db_sess.add(user)
        db_sess.commit()

        login_user(user, remember=True)

        db_sess.close()

        return redirect('/')

    return render_template('registration.html', title='Registration', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()

        user = db_sess.query(Users).filter(Users.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html', title='Login', message='Неправильный логин или пароль', form=form)

    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


def main():
    db_session.global_init(DATA_BASE)

    app.run('127.0.0.1', 8080)


if __name__ == '__main__':
    main()
