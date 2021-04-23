from data import db_session

from data.users import User
from data.jobs import Jobs


def print_team_leads(db_name):
    db_session.global_init(db_name)
    db_sess = db_session.create_session()

    data = sorted(db_sess.query(User).join(User.jobs).all(), key=lambda x: len(x.jobs))

    print(data)
    n = len(data)
    if n:
        prv = data[0]
        print(prv)
        i = 1
        while i < n and data[i] == prv:
            prv = data[i]
            print(prv)
            i += 1

    db_sess.close()


def print_team_leads_lyceum_version(db_name):
    db_session.global_init(db_name)
    db_sess = db_session.create_session()

    data = db_sess.query(User, Jobs).filter(Jobs.team_leader_id == User.id).all()
    colonists_and_jobs = dict()
    for (colonist, job) in data:
        colonist = f'{colonist.surname} {colonist.name}'
        job = job.job
        colonists_and_jobs[colonist] = colonists_and_jobs.get(colonist, []) + [job]

    sorted_colonists_and_number_of_jobs = sorted(map(lambda x: (x[0], len(x[1])), colonists_and_jobs.items()),
                                                 key=lambda x: -x[1])

    n = len(sorted_colonists_and_number_of_jobs)
    if n:
        name, prv = sorted_colonists_and_number_of_jobs[0]
        print(name)
        i = 1
        while i < n and sorted_colonists_and_number_of_jobs[i][1] == prv:
            name, prv = sorted_colonists_and_number_of_jobs[0]
            print(name)
            i += 1

    db_sess.close()


def main():
    db_name = input()

    print_team_leads_lyceum_version(db_name)


if __name__ == '__main__':
    main()
