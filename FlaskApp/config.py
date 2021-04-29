# 设置连接mysql数据库的URL
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://feko:123456@192.168.1.22:3306/test01'
# 设置每次请求结束后会自动提交数据库的改动
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
# 查询时显示原始SQL语句
#app.config['SQLALCHEMY_ECHO'] = True

SECRET_KEY='xxaa968524jsdfasfasdxzfasfds'