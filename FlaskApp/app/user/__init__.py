# -*- coding:utf-8 -*-

from  flask import Blueprint

#创建蓝图对象app_user
app_user = Blueprint("app_user",__name__,template_folder="templates")
from .user import index