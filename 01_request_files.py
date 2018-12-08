# -*- coding:utf-8 -*-
from flask import Flask,request

app=Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file_obj = request.files.get('pic')
    if file_obj is None:
        # 表示没有发送文件过来
        return "未上传文件"
    # 一、 request中保存文件的方法
    # file_obj.save("./demo.png")

    # 二、 文件保存，普通方法
    # try:
    #     f = open("./demo.png", "wb")
    #     data = file_obj.read()
    #     f.write(data)
    # except Exception:
    #     print("保存文件异常: {0}".format(Exception))
    # finally:
    #     f.close()

    # 三、文件保存，with上下文管理器
    # with open("./demo.png","wb") as f:
    #     data=file_obj.read()
    #     f.write(data)

    return "上传成功"

if __name__ == "__main__":
    app.run()