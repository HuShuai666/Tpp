# coding: utf-8
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Area(db.Model):
    __tablename__ = 'area'

    area_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    parent_id = db.Column(db.Integer, index=True)
    pingyin = db.Column(db.String(100), nullable=False, index=True)
    key = db.Column(db.String(10))
    is_hot = db.Column(db.Integer)


class User(db.Model):
    __tablename__ = 'user'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(255), nullable=False, unique=True)
