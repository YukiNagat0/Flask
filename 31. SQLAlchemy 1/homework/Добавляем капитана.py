from typing import List

from data import db_session

from data.users import User

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


def main():
    db_session.global_init(DATABASE)

    add_users(MEMBERS)


if __name__ == '__main__':
    main()
