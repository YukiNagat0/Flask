from data import db_session

from data.users import User


def update_users(db_name):
    db_session.global_init(db_name)
    db_sess = db_session.create_session()

    db_sess.query(User).filter(User.address == 'module_1', User.age < 21).update({'address': 'module_3'},
                                                                                 synchronize_session=False)

    db_sess.commit()
    db_sess.close()


def main():
    db_name = input()

    update_users(db_name)


if __name__ == '__main__':
    main()
