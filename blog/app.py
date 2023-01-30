from combojsonapi.event import EventPlugin
from combojsonapi.permission import PermissionPlugin
from combojsonapi.spec import ApiSpecPlugin
from flask import Flask, redirect, url_for

from blog import commands
from blog.extensions import admin, api, csrf, db, login_manager, migrate
from blog.models import User


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("blog.config")

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    admin.init_app(app)
    api.plugins = [
        EventPlugin(),
        PermissionPlugin(),
        ApiSpecPlugin(
            app=app,
            tags={
                "Article": "Article API",
                "Author": "Author API",
                "Tag": "Tag API",
                "User": "User API",
            },
        ),
    ]
    api.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(pk: int):
        return User.query.get(int(pk))

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for("auth.login"))


def register_blueprints(app: Flask):
    from blog import admin
    from blog import views as index
    from blog.api import views as api
    from blog.articles import views as article
    from blog.auth import views as auth
    from blog.authors import views as author
    from blog.tags import views as tag
    from blog.users import views as user

    app.register_blueprint(index.index)
    app.register_blueprint(auth.auth)
    app.register_blueprint(author.author)
    app.register_blueprint(user.user)
    app.register_blueprint(article.article)
    app.register_blueprint(tag.tag)
    app.register_blueprint(api.api_bp)
    
    admin.register_admin_views()


def register_commands(app: Flask):
    app.cli.add_command(commands.create_admin)
    app.cli.add_command(commands.create_tags)
