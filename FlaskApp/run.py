from app import app  #从app工程目录导入init里面的app对象


@app.errorhandler(404)
def page_not_found(e):
    return "404"

@app.errorhandler(500)
def internal_server_error(e):
    return "500"

if __name__ == "__main__":
    app.run('0.0.0.0',5000,debug=True)