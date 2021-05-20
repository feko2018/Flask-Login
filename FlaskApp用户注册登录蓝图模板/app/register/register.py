# -*- coding:utf-8 -*-
from  . import app_register
from flask import render_template,request,flash,redirect,url_for
from app import db,Users
from werkzeug.security import generate_password_hash,check_password_hash
import pyotp
import os
import traceback
from qrcode import QRCode, constants

@app_register.route("/")
def index():
    return render_template('register.html')

@app_register.route("/register_write_mysql",methods=['POST'])
def register_write_mysql():
    if request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        passwd = generate_password_hash(passwd)  ##密码hash加密
        gtoken = pyotp.random_base32(64)  # 获取随机密钥，用于谷歌验证器,随机64位
        if not username or not passwd:
            flash('输入有误')
        else:
            users = Users.query.filter_by(username=username).all()  ##查询是否有用户，有就返回列表
            if len(users) == 0:
                sql = Users(username,passwd,gtoken)
                db.session.add(sql)
                db.session.commit()
                flash('创建用户成功')
                read_static()
            else:
                flash('用户已存在')
    return redirect(url_for('app_register.index'))


def read_static():
    print(app_register.root_path)
    # 读取文件 /home/bjhee/flask-app/admin/files/info.txt
    with app_register.open_resource('static/file/readtest.txt') as f:
        info = f.read()
    print(info)