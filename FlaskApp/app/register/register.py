# -*- coding:utf-8 -*-
from  . import app_register
from flask import render_template,request,flash,redirect,url_for
from app import db,Users

@app_register.route("/")
def index():
    return render_template('register.html')

@app_register.route("/register_write_mysql",methods=['POST'])
def register_write_mysql():
    if request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        if not username or not passwd:
            flash('输入有误')
        else:
            users = Users.query.filter_by(username=username).all()  ##查询是否有用户，有就返回列表
            if len(users) == 0:
                sql = Users(request.form['username'],request.form['passwd'])
                db.session.add(sql)
                db.session.commit()
                flash('创建用户成功')
            else:
                flash('用户已存在')
    return redirect(url_for('app_register.index'))

