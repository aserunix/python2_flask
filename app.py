# -*- coding:utf-8 -*-
from flask import Flask, make_response

app = Flask(__name__)


@app.route("/set_cookie")
def set_cookie1():
    resp = make_response("successed")
    # 设置cookie,默认有效期为浏览器关闭时失效
    resp.set_cookie = ('Itcast', 'Python')
    # resp.set_cookie=("Itcast1", "Python1")
    # 设置有效期为3600s
    # resp.set_cookie=("Itcast2", "Python2")
    return resp


if __name__ == "__main__":
    app.run(debug=True)