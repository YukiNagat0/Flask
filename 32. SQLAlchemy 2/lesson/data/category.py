import sqlalchemy as sa
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


association_table = sa.Table(
    'association',
    SqlAlchemyBase.metadata,
    sa.Column('news', sa.Integer, sa.ForeignKey('news.id')),
    sa.Column('category', sa.Integer, sa.ForeignKey('category.id'))
)


class Category(SqlAlchemyBase):
    __tablename__ = 'category'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)

    news = orm.relation('News', secondary='association',
                        back_populates='categories')
