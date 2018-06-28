import json

from  flask import Blueprint,request,jsonify
from  flask_mail import Message
from app.ext import  db,mail
from app.home.models import Area

from app.home.views import keys
from app.user.models import User

user=Blueprint('user',__name__)


@user.route('/login10/',methods=['GET','POST'])
def login():
    return '1111'


@user.route('/register/',methods=['GET','POST'])
def register():
    result={}
    if request.method=='POST':
        username=request.values.get('username')
        password=request.values.get('password')
        email=request.values.get('email')
        if username and password and email:
            user=User.query.filter(User.username==username or User.email==email).all()
            if user:
                result.update(msg='账号或者密码已经存在',status=-2)
            else:
                user=User(username=username,password=password,email=email)
                db.session.add(user)
                db.session.commit()
            msg=Message('hello',sender='15586177428@163.com',
                        recipients=['15586177428@163.com'])

            mail.send(msg)
        else:
            result.update(msg='必要参数不能为空',status=-1)
    else:
        result.update(msg='错误的请求方式',status=400)
    return jsonify(result)

@user.route('/1/',methods=['POST','GET'])
def test_send():
    msg=Message('激活邮件',
                body='用户您好！！',
                html="<a href=''>激活</a>",
                sender='15586177428@163.com',
                recipients=['15586177428@163.com'])
    mail.send(msg)
    return '请激活'



@user.route('/add/')
def add_json_data():

    with open(r'D:\pycharm\Tpp\json\area.json','r',encoding='utf-8') as f:
        data= json.load(f)
        obj=data.get('returnValue')
        for key in keys:
            cities=obj.get(key)
            for city in cities:
                db.session.add(Area(name=city.get('regionName'),
                                    pingyin=city.get('pinYin'),
                                    parent_id=city.get('parentId'),
                                    area_id=city.get('cityCode'),
                                    key=key,
                                    ))
                db.session.commit()
    return 'success'