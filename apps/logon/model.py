from exts import db
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGTEXT

class custom(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(256), unique=True, nullable=True)
    phone = db.Column(db.String(19), unique=True, nullable=True)
    userIcon = db.Column(LONGTEXT, nullable=True)
    WeChat = db.Column(LONGTEXT, nullable=True)
    QQ = db.Column(LONGTEXT, nullable=True)
    DD = db.Column(LONGTEXT, nullable=True)  # 钉钉
    sex = db.Column(db.Boolean, nullable=True)
    birth = db.Column(db.DateTime, default=datetime.now)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    PIN = db.Column(db.String(6))
