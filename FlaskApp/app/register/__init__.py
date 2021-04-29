# -*- coding:utf-8 -*-

from  flask import Blueprint
#创建蓝图对象创建蓝图对象app_register
app_register = Blueprint("app_register",__name__,template_folder="templates")
from .register import index