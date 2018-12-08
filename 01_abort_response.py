# -*- coding:utf-8 -*-
from flask import Flask,request,abort,Response

app=Flask(__name__)

@app.route("/login",methods=["GET"])
def login():
    #name=request.form.get("name")
    #pwd=request.form.get("pwd")
    name=""
    pwd=""
    if name != "zhangsan" or pwd != "admin":
        # abort 会立即终止视图函数的执行，并可以返回特定的信息，后面的return不会被执行
        # 1. 传递状态码，只能传递标准http状态码，自定义的状态码程序会异常
        abort(404)
        # 2. 传递响应体信息，状态码是正常的200
        # resp=Response("login faied")
        # abort(resp)

    return "login sucess"

@app.errorhandler(404)
def handle_404_error(err):
    """自定义的状态码方法"""
    #这个函数的返回值是前端用户看到的最终结果
    # return u"出现了404错误，错误信息：{0}".format(err)
    return u"出现了666错误，错误信息："


if __name__=="__main__":
    app.run(debug=True)