# -*- coding:utf-8 -*-
from flask import Flask, session

app = Flask(__name__)

# flask的session 需要用到密钥字符串
app.config["SECRET_KEY"]="ADGJ;K;LKCX;Z;LKA;SDFLK;K;23K4"   #随便写的字符串

# flask 默认把session信息加密后存储到cookie中，正常情况下，会放到后端存储中（数据库、其它...）

@app.route("/login")
def login():
    # 设置session数据，类似字典
    # 生成session后，前端浏览器中的cookie会记录此用户的session_id(或者不放浏览器，放url中,xx/index.html?session_id=1)，flask也会把session_id记录到后端存储中（数据库、其它,由扩展实现）
    session["name"]="python"
    session["mobile"]="11122223333"
    return "login sucess"

@app.route("/index")
def index():
    # 获取session数据
    # 获取前端的cookie的session_id，然后由此从后端存储中获取对应用户的session信息（name,mobile等）
    name = session.get("name")
    return "hello {0}".format(name)

if __name__ == "__main__":
    app.run(debug=True)