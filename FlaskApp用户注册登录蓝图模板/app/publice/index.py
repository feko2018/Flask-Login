# -*- coding:utf-8 -*-
from  . import app_index
from flask import render_template,session

@app_index.route("/")
def index():
    if 'username' in session:
        status = session['username']
    else:
        status = None
    return render_template('index.html',status=status)