import datetime
from typing import List

from flask import Flask, render_template

from data import db_session

from data.users import User
from data.jobs import Jobs

app = Flask(__name__)

DATABASE = 'db/mars_explorer.db'

MEMBERS = [
    {
        'surname': 'Scott',
        'name': 'Ridley',
        'age': 21,
        'position': 'captain',
        'speciality': 'research engineer',
        'address': 'module_1',
        'email': 'scott_chief@mars.org'
    },
    {
        'surname': 'Andy',
        'name': 'Weir',
        'age': 48,
        'position': 'pilot',
        'speciality': 'astrologist',
        'address': 'module_1',
        'email': 'Andy@mars.org'
    },
    {
        'surname': 'Watney',
        'name': 'Mark',
        'age': 30,
        'position': 'pilot',
        'speciality': 'engineer',
        'address': 'module_1',
        'email': 'Watney@mars.org'
    },
    {
        'surname': 'Bean',
        'name': 'Sean',
        'age': 40,
        'position': 'pilot',
        'speciality': 'meteorologist',
        'address': 'module_1',
        'email': 'Bean@mars.org'
    }
]

JOBS = [
    {
        'team_leader_id': 1,
        'job': 'deployment of residential modules 1 and 2',
        'work_size': 15,
        'collaborators': '2, 3',
        'start_date': datetime.datetime.now(),
        'is_finished': False
    }
]


def add_users(users: List[dict]):
    db_sess = db_session.create_session()

    for user in users:
        if db_sess.query(User).filter(User.email == user['email']).first():
            db_sess.close()

            raise ValueError(f'Пользователь с email {user["email"]} уже существует.')

        user_object = User(**user)
        db_sess.add(user_object)

    db_sess.commit()
    db_sess.close()


def add_jobs(jobs: List[dict]):
    db_sess = db_session.create_session()

    for job in jobs:
        job_object = Jobs(**job)
        db_sess.add(job_object)

    db_sess.commit()
    db_sess.close()


@app.route('/journal')
def index():
    db_sess = db_session.create_session()

    jobs = db_sess.query(Jobs).all()

    return render_template('journal.html', jobs=jobs)


def main():
    db_session.global_init(DATABASE)

    # add_users(MEMBERS)
    # add_jobs(JOBS)

    app.run('127.0.0.1', 8080)


if __name__ == '__main__':
    main()
