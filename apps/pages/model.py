from datetime import datetime

from sqlalchemy.dialects.mysql import LONGTEXT

from exts import db


class article(db.Model):
    # 一级标题
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    time = db.Column(db.DateTime, default=datetime.now)
    content = db.Column(LONGTEXT, nullable=True)  # 文章内容
    public = db.Column(db.Boolean, default=False)  # 是否发布
    if_setup = db.Column(db.Boolean, default=False)  # 是否顶置
    pos_menus_two = db.Column(db.String(128), db.ForeignKey('menu_child.id'), nullable=True)
    pos_menus_three = db.Column(db.String(128), db.ForeignKey('menu_thr_child.id'), nullable=True)
    cover = db.Column(LONGTEXT, nullable=True)  # 文章封面
