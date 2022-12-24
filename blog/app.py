from flask import Flask

from blog import views as vi
from blog.articles import views as va
from blog.users import views as vu


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(va.article)
    app.register_blueprint(vu.user)
    app.register_blueprint(vi.index)
