import datetime

import re

from flask import Flask, render_template, redirect
from flask_wtf import CSRFProtect

from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from data import db_session

from data.users import Users
from data.jobs import Jobs

from forms.login_form import LoginForm
from forms.registration_form import RegistrationForm
from forms.edit_job_form import EditJobForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
csrf_protect = CSRFProtect(app)

app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=360)

login_manager = LoginManager()
login_manager.init_app(app)

DATA_BASE = 'db/mars_explorers.db'


class UserIdError(Exception):
    pass


def check_users_ids_existence(*users_ids):
    db_sess = db_session.create_session()
    for user_id in users_ids:
        if not db_sess.query(Users).filter(Users.id == user_id).first():
            db_sess.close()

            return False, user_id

    db_sess.close()

    return True, None


def validate_and_edit_job_and_return_view(form: EditJobForm, current_user_id: int, can_set_team_leader_id: bool):
    """ Проверяет правильность формы добавления/редактирования job, добавляет job в базу данных, возвращает страницу """
    job_title = form.job.data
    team_leader_id = form.team_leader_id.data  # пустая строка, если current_user != 1 или капитан ничего не ввел
    work_size = form.work_size.data
    collaborators = form.collaborators.data
    is_finished = form.is_finished.data

    try:
        # Человек в качестве тимлида может указать только себя. Только капитан может назначать тим-лидов.
        if can_set_team_leader_id:
            # вдруг капитан плохой человек и ввел несуществующий или некорректный team_leader_id
            if not (team_leader_id and re.fullmatch('^[1-9]\d*$', team_leader_id)):
                raise UserIdError('Team leader id должен быть натуральным числом.')

            team_leader_id = int(team_leader_id)
            all_users_ids_exist, bad_user_id = check_users_ids_existence(team_leader_id)
            if not all_users_ids_exist:
                raise UserIdError(f'Пользователя с id {team_leader_id} не существует.')
        else:
            team_leader_id = current_user_id

        all_users_ids_exist, bad_user_id = check_users_ids_existence(*map(int, collaborators.split(', ')))
        if not all_users_ids_exist:
            raise UserIdError(f'В списке collaborators ids есть несуществующий пользователь с id {bad_user_id}.')

    except UserIdError as e:
        message = e
    except ValueError:
        message = 'В списке collaborators ids могут быть только натуральные числа, разделенные ", ". Например: "2, 3".'
    except Exception as e:
        message = f'Непредвиденная ошибка "{type(e).__name__}: {e}". Обратитесь в службу поддержки.'
    else:
        job = Jobs()

        job.job = job_title
        job.team_leader_id = team_leader_id
        job.work_size = work_size
        job.collaborators = collaborators
        job.is_finished = is_finished

        db_sess = db_session.create_session()
        team_leader_ = db_sess.query(Users).filter(Users.id == team_leader_id).first()
        team_leader_.jobs.append(job)
        db_sess.commit()
        db_sess.close()

        return redirect('/')

    return render_template('edit_job.html', title='Adding a job', action_type='Adding a job',
                           form=form, can_set_team_leader_id=can_set_team_leader_id, message=message)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(Users).get(user_id)
    db_sess.close()
    return user


@app.route('/')
@app.route('/index')
def index():
    db_sess = db_session.create_session()

    jobs = db_sess.query(Jobs).all()
    view = render_template('journal.html', title='Works log', jobs=jobs)

    db_sess.close()

    return view


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


@app.route('/add_job', methods=['GET', 'POST'])
@login_required
def add_job():
    current_user_id = current_user.id
    can_set_team_leader_id = current_user_id == 1

    form = EditJobForm()
    if form.validate_on_submit():
        return validate_and_edit_job_and_return_view(form, current_user_id, can_set_team_leader_id)

    return render_template('edit_job.html', title='Adding a job', action_type='Adding a job',
                           form=form, can_set_team_leader_id=can_set_team_leader_id)


def main():
    db_session.global_init(DATA_BASE)

    app.run('127.0.0.1', 8080)


if __name__ == '__main__':
    main()
