import time
from datetime import datetime
from random import randint
import threading
from .model import custom as user_db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, session, jsonify
from exts import db, mail, base64
from flask_mail import Message
import uuid

logon = Blueprint('logon', __name__)


@logon.route('/logon', methods=["GET", "POST"])
def user_logon():
    email = base64.decode(request.form.get("email"))
    password = base64.decode(request.form.get("PW"))
    pw_hash = user_db.query.filter(user_db.email == email).first()
    try:
        if pw_hash.password and check_password_hash(pw_hash.password, password):
            session["secretKey"] = uuid.uuid3(uuid.NAMESPACE_DNS, str(uuid.uuid4()))
            custom = {
                'code': 200,
                'username': pw_hash.username,
                'phone': pw_hash.phone,
                'email': pw_hash.email,
                'sex': pw_hash.sex,
                'birth': pw_hash.birth,
                'userIcon': pw_hash.userIcon,
            }
            return jsonify(custom)
    except:
        return jsonify({'code': 404})

    return jsonify({'code': 404})


@logon.route('/register', methods=['POST'])
def register():
    # phone = base64.decode(request.form.get("userPhone"))
    PW = base64.decode(request.form.get("PW"))
    rePW = base64.decode(request.form.get("rePW"))
    email = base64.decode(request.form.get("email"))
    PIN = base64.decode(request.form.get("PIN"))
    time.sleep(2)
    if PW == rePW and not user_db.query.filter(user_db.email == email).first():
        sql = user_db(password=generate_password_hash(PW), email=email)
        db.session.add(sql)
        db.session.commit()
        return jsonify({'code': 200, 'msg': '注册成功了'})
    elif PW != rePW:
        return jsonify({'code': 404, 'msg': '两次密码不一致'})
    elif user_db.query.filter(user_db.email == email).first():
        return jsonify({'code': 404, 'msg': '邮箱已经被注册'})


@logon.route('/forget', methods=["GET", "POST"])
def user_forget_password():
    newPW = base64.decode(request.form.get("PW"))
    reNewPW = base64.decode(request.form.get("rePW"))
    email = base64.decode(request.form.get("email"))
    PIN = base64.decode(request.form.get("PIN"))
    if newPW != reNewPW:
        return jsonify({'code': 404, 'msg': '两次密码不一致'})
    else:
        res = user_db.query.filter(user_db.email == email).first()
        if not res:
            return jsonify({'code': 404})
        res_PIN = res.PIN
        if res_PIN == PIN:
            print("new_PW:", newPW, type(newPW))
            res.password = generate_password_hash(newPW)
            res.PIN = ""
            db.session.add(res)
            db.session.commit()
            return jsonify({'code': 200, 'msg': '修改密码成功,'})
        else:
            return jsonify({'code': 404, 'msg': '验证码错误'})


@logon.route('/send/<string:ifCheck>', methods=["GET", "POST"])
def email_sender(ifCheck=False):
    f_email = request.args.get("email")
    if ifCheck == 'true':
        res = user_db.query.filter(user_db.email == f_email).first()
        print('res==>', res)
        if not res:
            PIN = str(randint(100000, 999999))
            send_email(f_email, PIN)
            return jsonify({"code": 200, base64.encode("PIN"): base64.encode(PIN)
                            })  # base64加密PIN, 由前端进行解密
        else:
            return jsonify({'code': 404})
    elif ifCheck == 'false':
        res = user_db.query.filter(user_db.email == f_email).first()
        if res:
            PIN = str(randint(100000, 999999))
            res.PIN = PIN
            db.session.add(res)
            db.session.commit()
            send_email(f_email, PIN)
            return jsonify({"code": 200, base64.encode("PIN"): base64.encode(PIN)})
        else:
            return jsonify({"code": 404})


def send_email(getter, PIN):
    msg = Message("CMX博客群",
                  recipients=[getter])
    msg.charset = "utf-8"
    msg.html = render_template("f_Email.html", PIN=PIN,
                               datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    t = threading.Thread(target=async_send_mail, args=(msg,))
    t.start()


def async_send_mail(msg):
    from app import app
    with app.app_context():
        mail.send(msg)
