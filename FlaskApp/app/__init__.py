# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
class Users(db.Model): ##继承父类Model
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    passwd = db.Column(db.String(100))
    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd
# 这里引入蓝图的配置,引入蓝图要放到后面
from app import views

