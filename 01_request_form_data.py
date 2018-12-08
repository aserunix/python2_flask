# -*- coding:utf-8 -*-
from flask import Flask,request

app=Flask(__name__)

@app.route("/index",methods=["GET","POST"])
def index():
    name=request.form.get("name")    #form提取请求体中的表单格式该键的第一个数据，是一个类字典的对象
    age=request.form.get("age")    #如果表单中没带该值，则默认为None
    gender=request.form.get("gender")
    name_list=request.form.getlist("name")    #如果传递了多个name，则可以通过request.form.getlist以列表方式拿出该键的所有值
    print("request.data: {0}".format(request.data))

    city=request.args.get("city")        #argst提取查询字符串QueryString中的值，如:127.0.0.1:5000/index?city=gz
    return "hello name={0}, age={1}, city={2},gender={3},name_list={4}".format(name,age,city,gender,name_list)

if __name__=="__main__":
    app.run(debug=True)