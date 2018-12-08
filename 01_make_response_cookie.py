# -*- coding:utf-8 -*-
from flask import Flask, make_response,request

app = Flask(__name__)

@app.route("/set_cookie")
def set_cookie():
    resp = make_response("successed")
    # 设置cookie,默认有效期为浏览器关闭时失效
    resp.set_cookie("Itcast", "Python")
    resp.set_cookie("Itcast1", "Python1")
    # 设置有效期为3600s
    resp.set_cookie("Itcast2", "Python2",max_age=3600)
    # set_cookie原理:是响应头中设置set-cookie头部,所以也可以直接写header
    # resp.headers["Set-Cookie"]="Itcast2=Python2; Expires=Sat, 08-Dec-2018 11:33:13 GMT; Max-Age=3600; Path=/"
    return resp

@app.route("/get_cookie")
def get_cooke():
    c=request.cookies.get("Itcast") # 获取cookie中的值
    return c

@app.route("/delete_cookie")
def delete_cookie():
    resp=make_response("del sucess")
    # 删除cookie, 浏览器并不是真正删除, 只是将过期时间设置为创建时间
    resp.delete_cookie("Itcast1")
    return resp

if __name__ == "__main__":
    app.run(debug=True)