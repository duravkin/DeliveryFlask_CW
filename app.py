# app.py
from flask import Flask
from flask_admin import Admin
from flask_babel import Babel
from models import db
from routes import main_routes
from admin import admin_views


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config.Config')

    db.init_app(app)

    app.config['BABEL_DEFAULT_LOCALE'] = 'ru'
    babel = Babel(app)

    admin = Admin(app, name='Админ-панель "Автодоставка"',
                  template_mode='bootstrap3', url='/admin')

    app.register_blueprint(main_routes)

    for view in admin_views:
        admin.add_view(view)

    return app
