from flask import Flask
from flask_admin import Admin
from models import db
from routes import main_routes
from admin import admin_views
from flask_babel import Babel

app = Flask(__name__)
app.config.from_object('config.config.Config')

db.init_app(app)

# Настройка Flask-Babel для локализации
app.config['BABEL_DEFAULT_LOCALE'] = 'ru'
babel = Babel(app)

admin = Admin(app, name='Админ-панель "Автодоставка"',
              template_mode='bootstrap3', url='/admin')

app.register_blueprint(main_routes)

for view in admin_views:
    admin.add_view(view)


if __name__ == '__main__':
    app.run(debug=True)
