import sqlalchemy as sa
from sqlalchemy import orm

from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Departments(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'departments'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)

    chief_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    chief = orm.relationship('Users', back_populates='departments')

    members = sa.Column(sa.String)
    email = sa.Column(sa.String)
