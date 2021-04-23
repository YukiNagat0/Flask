import sqlalchemy as sa
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    surname = sa.Column(sa.String)
    name = sa.Column(sa.String)
    age = sa.Column(sa.Integer)
    position = sa.Column(sa.String)
    speciality = sa.Column(sa.String)
    address = sa.Column(sa.String)
    email = sa.Column(sa.String, unique=True)
    hashed_password = sa.Column(sa.String)
    modified_date = sa.Column(sa.DateTime)

    jobs = orm.relationship('Jobs', back_populates='team_leader')

    departments = orm.relationship('Department', back_populates='chief_object')

    def __repr__(self):
        return f'<Colonist> {self.id} {self.surname} {self.name}'
