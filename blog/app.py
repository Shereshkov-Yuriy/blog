from combojsonapi.spec import ApiSpecPlugin
from flask import Flask, redirect, url_for
from flask_combo_jsonapi import Api

from blog import commands
from blog.extensions import admin, csrf, db, login_manager, migrate
from blog.models import User


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("blog.config")

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_api(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    admin.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(pk: int):
        return User.query.get(int(pk))

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for("auth.login"))


def register_api(app: Flask):
    from blog.api.article import ArticleDetail, ArticleList
    from blog.api.author import AuthorDetail, AuthorList
    from blog.api.tag import TagDetail, TagList
    from blog.api.user import UserDetail, UserList

    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
            "Article": "Article API",
            "Author": "Author API",
            "Tag": "Tag API",
            "User": "User API",
        }
    )

    api = Api(
        app,
        plugins=[
            api_spec_plugin,
        ]
    )

    api.route(ArticleList, "article_list", "/api/articles/", tag="Article")
    api.route(ArticleDetail, "article_detail",
              "/api/articles/<int:id>/", tag="Article")
    api.route(AuthorList, "author_list", "/api/authors/", tag="Author")
    api.route(AuthorDetail, "author_detail",
              "/api/authors/<int:id>/", tag="Author")
    api.route(TagList, "tag_list", "/api/tags/", tag="Tag")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/", tag="Tag")
    api.route(UserList, "user_list", "/api/users/", tag="User")
    api.route(UserDetail, "user_detail", "/api/users/<int:id>/", tag="User")


def register_blueprints(app: Flask):
    from blog import admin
    from blog import views as index
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
    admin.register_admin_views()


def register_commands(app: Flask):
    app.cli.add_command(commands.create_admin)
    app.cli.add_command(commands.create_tags)
