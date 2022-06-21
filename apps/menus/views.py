from flask import request, Blueprint, jsonify
from .model import menus as Menus
from .model import menu_child as Menu_child
from .model import menu_thr_child as Menu_three
menus = Blueprint("menus", __name__)


@menus.route("/initmenus")
def Init():
    if request.method == "GET":
        init_menus = Menus.query.all()
        init_sectitle = Menu_child.query.all()
        data = [{"id": i.id,
                 "title": i.title,
                 "child_list": [{"id": j.id,
                                 "title": j.sec_title,
                                 "thr_list": [{
                                     "id": k.id,
                                     "title": k.thr_title,
                                 } for k in Menu_three.query.filter_by(menu_sec_id=j.id)
                                 ]
                                 } for j in Menu_child.query.filter_by(menu_id=i.id)]} for i
                in init_menus]
        import time
        time.sleep(2)
        return jsonify(data)


 # 适配跨域请求
# @menus.after_request
# def cors(environ):
#     environ.headers['Access-Control-Allow-Origin'] = '*'
#     environ.headers['Access-Control-Allow-Method'] = '*'
#     environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
#     return environ
