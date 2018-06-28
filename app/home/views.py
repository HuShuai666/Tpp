from flask import Blueprint
from sqlalchemy import func
from sqlalchemy.sql.functions import count

from app.home.models import Area, Movies
from app.utils.json_utils import to_list

home=Blueprint('home',__name__)



# @home.route('/areas/')
# def get_areas():
#     result={}



from flask import Blueprint, jsonify


# from app.utils.json_utils import to_list

home = Blueprint('home', __name__)
'''

'''

keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


@home.route('/areas/')
def get_ares():
    result = {}
    # with_entities 过滤列
    # 相当于 db.session
    ares = {}
    try:
        for key in keys:
            # ares[key] = Area.query.with_entities(Area.name, Area.area_id).filter(Area.key == key).all()
            area_list = Area.query.filter(Area.key == key).all()
            if area_list:
                ares[key] = to_list(area_list)
        result.update(msg='success', status=200, ares=ares)
    except Exception as e:
        result.update(msg='查询失败', status=404)
    return jsonify(result)


#SELECT COUNT(*) FROM MOVIES GROUP BY FLAG
@home.route('/moves/',methods=['POST','GET'])
def movies():
    result={}
    try:
        movie={

        }
        #分组查询热门影片和热映的影片数量
        # counts=Movies.query.with_entities(Movies.flag,func.count('*')).group_by(Movies.flag).all()
        counts= Movies.query.excute('SELECT COUNT('*') FROM movies GROUP BY flag')
        #查询热门影片的前五部
        hot_movies=Movies.query.filter(Movies.flag==1).limit(5).all()
        show_movies=Movies.query.filter(Movies.flag==2).limit(5).all()
        movie.update(counts=counts,hot_movies=to_list(hot_movies),show_movies=to_list(show_movies))
        result.update(status=200,msg='success',data=movie)
    except:
        result.update(status=404,msg='fial')
    return jsonify(result)


    return '1111'

