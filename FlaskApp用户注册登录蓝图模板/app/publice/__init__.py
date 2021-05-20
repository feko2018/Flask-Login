# -*- coding:utf-8 -*-

from  flask import Blueprint

#创建蓝图对象app_index
app_index = Blueprint("app_index",__name__,template_folder="templates")
from .index import index