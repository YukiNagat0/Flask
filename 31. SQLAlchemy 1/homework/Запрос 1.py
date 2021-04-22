import argparse

from data import db_session

from data.users import User


def print_colonists(db_name):
    db_session.global_init(db_name)
    db_sess = db_session.create_session()

    for colonist in db_sess.query(User).all():
        print(colonist)

    db_sess.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('db_name', type=str)

    args = parser.parse_args()
    db_name = args.db_name

    print_colonists(db_name)


if __name__ == '__main__':
    main()
