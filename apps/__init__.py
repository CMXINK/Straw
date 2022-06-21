from flask import Flask, render_template

from settings import DevelopmentConfig
from apps.pages.views import pages

from apps.menus.views import menus as menu_bp
from apps.logon.views import logon as logon_bp
from exts import db, mail


def create_app():
    app = Flask(__name__, static_folder="../static", template_folder="../templates")
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(blueprint=menu_bp, url_prefix="/menus/")
    app.register_blueprint(blueprint=pages, url_prefix="/pages/")
    app.register_blueprint(blueprint=logon_bp, url_prefix='/logon/')
    db.init_app(app)
    mail.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    # CSRFProtect(app)
    @app.errorhandler(404)
    def error_page(d):
        return "没有找到"

    return app
