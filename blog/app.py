from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from blog import views as index
from blog.articles import views as article
from blog.auth import views as auth
from blog.users import views as user

db = SQLAlchemy()
login_manager = LoginManager()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "5k=7%%j6s=ucb^hpdbrl$&7$wy41zph-_85&sc+1a7_)ujp@du"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from blog.models import User

    @login_manager.user_loader
    def load_user(pk: int):
        return User.query.get(pk)

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for("auth.login"))

    db.init_app(app)

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(article.article)
    app.register_blueprint(auth.auth)
    app.register_blueprint(user.user)
    app.register_blueprint(index.index)
