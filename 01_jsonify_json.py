# -*- coding:utf-8 -*-
from flask import Flask,jsonify
import json

app=Flask(__name__)

@app.route("/")
def index():
    # 字典与json字符串 互转
    data={"name":"python",
          "age":18}

    # 方法一: 自己转换成json字符串,并返回,需要import json
    # json_str=json.dumps(data)
    # return json_str,200,{"Conten-Type":"application/json"}

    # 推荐,方法二: jsonify 帮助转为json字符串,并设置咱应头"Conten-Type":"application/json",
    # 需要from flask import jsonify
    # return jsonify(data)

    # 或者直接以等于形式传递字典
    # return jsonify(name="python",age=19)


if __name__=="__main__":
    app.run()