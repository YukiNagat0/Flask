from data import db_session

from data.users import User
from data.jobs import Jobs
from data.departments import Department


def print_colonists(db_name):
    db_session.global_init(db_name)
    db_sess = db_session.create_session()

    department = db_sess.query(Department).filter(Department.id == 1).first()
    members_ids = list(map(int, department.members.split(', ')))

    for member in db_sess.query(User).filter(User.id.in_(members_ids)).join(Jobs, User.id == Jobs.id).all():
        jobs = db_sess.query(Jobs).filter(Jobs.team_leader_id == member.id).all()
        number_of_hours = sum(map(lambda x: x.work_size, jobs))
        if number_of_hours > 25:
            print(member.surname, member.name)

    db_sess.close()


def main():
    db_name = input()

    print_colonists(db_name)


if __name__ == '__main__':
    main()
