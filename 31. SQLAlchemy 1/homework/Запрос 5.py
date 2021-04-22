from data import db_session

from data.jobs import Jobs


def print_jobs(db_name):
    db_session.global_init(db_name)
    db_sess = db_session.create_session()

    for job in db_sess.query(Jobs).filter(Jobs.work_size < 20, Jobs.is_finished == 0).all():
        print(job)

    db_sess.close()


def main():
    db_name = input()

    print_jobs(db_name)


if __name__ == '__main__':
    main()
