# -*- coding:utf-8 -*-
from  . import app_user
from flask import render_template,session,redirect

@app_user.route("/")
def index():
    if 'username' in session:
        status = session['username']
    else:
        status = None
    return render_template('user.html', status=status)