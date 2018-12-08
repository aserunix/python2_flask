# -*- coding:utf-8 -*-
from flask import Flask,make_response

app=Flask(__name__)

@app.route("/")
def index():
    # 1 使用元组，返回自定义的响应信息
    # 响应体 状态码[ 状态码的描述信息,使用时要带引号，可选] 其它响应头（每对kv以元组形式对应）
    #除了响应体，其它都是可选的
    # return "index page"
    # return "index page", 400, [("testheader","ok"),("City","Guangzhou")]
    # return "index page", "666 VeryGood", [("testheader","ok"),("City","Guangzhou")]

    # 2 使用 make_response 来构造响应信息(from flask import make_response)
    resp=make_response("index page")
    resp.status="666 VeryGood"
    resp.headers["testheader"]="ok"
    resp.headers["City"]="gz"
    return resp

if __name__=="__main__":
    app.run()