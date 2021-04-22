from data.users import User

from data import db_session


def print_colonists(db_name):
    db_session.global_init(db_name)
    db_sess = db_session.create_session()

    for colonist in db_sess.query(User).filter(User.age < 18).all():
        print(colonist, f'{colonist.age} years')

    db_sess.close()


def main():
    db_name = input()

    print_colonists(db_name)


if __name__ == '__main__':
    main()
