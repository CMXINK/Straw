from exts import db


class menus(db.Model):
    # 一级标题
    id = db.Column(db.String(128), primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    icon = db.Column(db.String(128), nullable=True, unique=False)
    child = db.relationship('menu_child', backref="menu")


class menu_child(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    sec_title = db.Column(db.String(20), unique=True, nullable=False)
    icon = db.Column(db.String(128), nullable=True, unique=False)
    menu_id = db.Column(db.String(128), db.ForeignKey('menus.id'), nullable=False)
    child = db.relationship('menu_thr_child', backref="menu_child")

    # article_id_menu_sec = db.relationship('article', backref="menu_child")


class menu_thr_child(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    thr_title = db.Column(db.String(20), unique=True, nullable=False)
    icon = db.Column(db.String(128), nullable=True, unique=False)
    menu_sec_id = db.Column(db.String(128), db.ForeignKey('menu_child.id'), nullable=False)
    # article_id_menu_thr = db.relationship('article', backref="menu_thr_child")
