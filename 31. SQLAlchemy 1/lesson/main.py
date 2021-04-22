from flask import Flask, render_template, redirect
from flask_wtf import CSRFProtect

from data import db_session

from data.users import User
from data.news import News

from forms.user import RegisterForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
csrf_protection = CSRFProtect(app)


@app.route('/')
@app.route('/index')
def index():
    db_sess = db_session.create_session()

    news = db_sess.query(News).filter(News.is_private != True)
    print(news)

    db_sess.close()

    return render_template('index.html', news=news)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', titile='Регистрация',
                                   form=form,
                                   message='Пароли не совпадают')

        db_sess = db_session.create_session()

        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', titile='Регистрация',
                                   form=form,
                                   message='Такой пользователь уже есть')

        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )

        user.set_password(form.password.data)

        db_sess.add(user)
        db_sess.commit()
        db_sess.close()

        return redirect('/login')

    return render_template('register.html',
                           title='Регистрация', form=form)


def main():
    db_session.global_init('db/blogs.db')
    app.run('127.0.0.1', 8080)


if __name__ == '__main__':
    main()

# Можно в класс сесси добавить метод контекстного менеджера для открытия, коммита и клоуза
