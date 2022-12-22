from flask import Flask

from blog import views as v
from blog.users import views


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(views.user)
    app.register_blueprint(v.index)
