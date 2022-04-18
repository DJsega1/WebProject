import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    postal_code = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)


class Material(SqlAlchemyBase):
    __tablename__ = 'materials'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)


class Color(SqlAlchemyBase):
    __tablename__ = 'colors'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)


class Type(SqlAlchemyBase):
    __tablename__ = 'types'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)


class Sex(SqlAlchemyBase):
    __tablename__ = 'sex'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)


class Item(SqlAlchemyBase):
    __tablename__ = 'items'
    article = sqlalchemy.Column(sqlalchemy.Integer, index=True, unique=True, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    amount = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    material = sqlalchemy.Column(sqlalchemy.ForeignKey("materials.id"), nullable=False)
    color = sqlalchemy.Column(sqlalchemy.ForeignKey("colors.id"), nullable=False)
    type = sqlalchemy.Column(sqlalchemy.ForeignKey("types.id"), nullable=False)
    sex = sqlalchemy.Column(sqlalchemy.ForeignKey("sex.id"), nullable=False)
    is_hot = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    is_new = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)


class Admin(SqlAlchemyBase):
    __tablename__ = 'admins'
    id = sqlalchemy.Column(sqlalchemy.Integer, index=True, unique=True, primary_key=True, autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
