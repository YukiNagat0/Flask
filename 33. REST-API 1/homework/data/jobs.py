import sqlalchemy as sa
from sqlalchemy import orm

from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    team_leader_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    team_leader = orm.relationship('Users', back_populates='jobs')

    job = sa.Column(sa.String)
    work_size = sa.Column(sa.Integer)
    collaborators = sa.Column(sa.String)
    start_date = sa.Column(sa.DateTime)
    end_date = sa.Column(sa.DateTime)
    is_finished = sa.Column(sa.Boolean)

    def __repr__(self):
        return f'<Job> {self.job}'
