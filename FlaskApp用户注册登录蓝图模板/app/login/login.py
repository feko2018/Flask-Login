# -*- coding:utf-8 -*-
from  . import app_login
from flask import render_template,request,flash,redirect,url_for,session,make_response
from app import db,Users
from werkzeug.security import generate_password_hash,check_password_hash
#import bcrypt



@app_login.route("/")
def index():
        ##访问默认是get请求
        ##判断是否登录过
        if 'username' in session:
            print("已登录过，跳转到用户后台")
            return redirect('/user')
        else:
            ##判断是否记住密码，如果记住密码就从cookie中取出username到session中，跳到主页
            if 'username' in request.cookies:
                print("有密码记录，从cookie中读出username到session,实现免密码登录")
                username = request.cookies.get('username')
                session['username'] = username
                return redirect('/user')
        return render_template('login.html')


@app_login.route('/login_from_mysql',methods=['POST'])
def login_from_mysql():
    if request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        issaved = request.form.get('issaved') ###获取不到返回None
        print("正在登录的用户密码是" + username + " " + passwd)
        if not username or not passwd:
            flash("用户或密码不能为空")
            return redirect(url_for('app_login.index'))

        users = Users.query.filter_by(username=username).first() ##返回列表
        if not users:
            print("用户不存在")
            flash("用户不存在")
            return redirect(url_for('app_login.index'))
        ret = check_password_hash(users.passwd,passwd)  ##hash判断密码是否正确
        #ret = bcrypt.checkpw(bytes(passwd, encoding ="utf-8"), bytes(users.passwd, encoding ="utf-8")) ##bcrypt判断密码是否正确
        if not ret:
            print("用户或密码不对")
            flash("用户或密码不对")
            return redirect(url_for('app_login.index'))
        else:
            # 登录成功
            print('登录成功')
            resp = redirect('/user')
            # 登录成功，把用户名存储到session,session默认存储在用户浏览器的cookie里
            session['username'] = username
            # 若记住密码则把,username记录在cookie里,下次直接从cookie里出到session里
            if issaved:
                print('记住密码选项，把用户名写入cookie,有效期7天')
                resp.set_cookie('username', username, 60 * 60 * 24 * 7)
            # 跳到主页
            return resp


@app_login.route('/logout')
def logout():
    print(session['username'] + " 用户退出登录，删除session和cookie")
    session.pop('username',None)
    resp = make_response(redirect('/user'))
    resp.delete_cookie('username')
    return resp