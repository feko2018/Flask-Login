# -*- coding:utf-8 -*-

from  flask import Blueprint

#创建蓝图对象创建蓝图对象app_login
app_login = Blueprint("app_login",__name__,template_folder="templates")
from .login import index