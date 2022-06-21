from flask import Blueprint, jsonify
from .model import article as article_list

pages = Blueprint('pages', __name__)


@pages.route('/<string:title>/<string:current_page>')
def get_pages(title, current_page):
    pagination = article_list.query.filter(article_list.public == 1,
        (article_list.pos_menus_three == title or article_list.pos_menus_two == title)).order_by(
        article_list.time.desc()).paginate(page=int(current_page), per_page=9, max_per_page=9)
    page = [{
        'title': i.title,
        'cover': i.cover[1:-1],
        'date': str(i.time).replace("-", '年').replace('-', '月').replace(' ', '日 '),
        'content': i.content,
    } for i in pagination.items]
    page.insert(0, {
        "title": '',
        "ifNextPage": pagination.has_next,
        "ifPrePage": pagination.has_prev,
        "currentPage": pagination.page,
        "showArray": [i for i in range(pagination.page, pagination.page + 1 + (7 if (pagination.pages - pagination.page) > 7 else (pagination.pages - pagination.page)))],
    })
    return jsonify(page)


#  适配跨域请求
# @pages.after_request
# def cors(environ):
#     environ.headers['Access-Control-Allow-Origin'] = '*'
#     environ.headers['Access-Control-Allow-Method'] = '*'
#     environ.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
#     return environ
