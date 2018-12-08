# -*- coding: utf-8 -*-    #一定要加，不然注释用中文，python会报错

from flask import Flask
from flask import url_for
from flask import redirect
from werkzeug.routing import BaseConverter
# 创建flask的应用对象
# __name__表示当前的模块名字
#                        模块名，flask以这个模块所在目录为根目录
#                            statick 静态目录
#                            templates 模板目录
app = Flask(__name__)

@app.route('/')        #app对象中的route
def index():            #定义的视图函数
    return "hello flask"

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/goods/<int:goods_id>')    #匹配127.0.0.1:5000/goods/123
def goods_detail(goods_id):
    return 'goods detail page for {0}'.format(goods_id)

##通用正则转换器
class RegexConverter(BaseConverter):  # 需from werkzeug.routing import BaseConverter
    """ """
    # url_map 接收的是127.0.0.1:5000/send/18811112222；
    # regex    接收到的是18811112222
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(RegexConverter, self).__init__(url_map)

        # 将正则表达式的参数保存到对象的属性中，flask会使用这个属性来进行路由的正则匹配
        self.regex = regex

app.url_map.converters["re"] = RegexConverter

@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")    #127.0.0.1:5000/send/18811112222
def send_sms(mobile):
    return "send sms to {0}".format(mobile)

##普通转换器
class MobileConverter(BaseConverter):
    def __init__(self,url_map):
        super(MobileConverter,self).__init__(url_map)
        self.regex=r'1[34578]\d{9}'

    def to_python(self,value):
        print("to_python方法被调用")
        #return "aa{0}".format(value) #传给视图 mobile_num的值会被加上前缀 aa
        return "{0}".format(value)    #返回原始值，不进行修改

    def to_url(self,value): #从url_for调转过来时被调用
        print("to_url方法被调用")
        return "bb{0}".format(value)
        # return "{0}".format(value)

app.url_map.converters["mobile"]=MobileConverter

@app.route("/send2/<mobile:mobile_num>")
def send_sms2(mobile_num):
    return "send2 sms to {0}".format(mobile_num)

@app.route("/send2_to_url")
def send2_to_url():
    # url=url_for("send_sms2",mobile_num)
    url=url_for("send_sms2",mobile_num="18822223333")      # 访问/send2_to_url时，会被跳转到/send_sms2/18822223333，然后被to_url加前缀 bb
    return redirect(url)

# print(app.url_map)
if __name__ == '__main__':
    app.run(debug=True)    #启动flask程序
