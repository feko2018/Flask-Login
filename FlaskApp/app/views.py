from app import app
from .publice import app_index
from .user import app_user
from .register import app_register
from .login import app_login
#注册蓝图对象和定义url入口
app.register_blueprint(app_index, url_prefix='/')
app.register_blueprint(app_user, url_prefix='/user')
app.register_blueprint(app_register, url_prefix='/register')
app.register_blueprint(app_login, url_prefix='/login')