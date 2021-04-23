import sqlalchemy as sa
from sqlalchemy import orm

from db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)

    chief = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    chief_object = orm.relationship('User', back_populates='departments')

    members = sa.Column(sa.String)
    email = sa.Column(sa.String)
