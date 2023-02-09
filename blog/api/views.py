from flask import Blueprint

from blog.api.article import ArticleDetail, ArticleList
from blog.api.author import AuthorDetail, AuthorList
from blog.api.tag import TagDetail, TagList
from blog.api.user import UserDetail, UserList
from blog.extensions import api, csrf

api_bp = Blueprint("api", __name__)
csrf.exempt(api_bp)

api.route(ArticleList, "article_list", "/api/articles/",
          tag="Article", blueprint=api_bp)
api.route(ArticleDetail, "article_detail",
          "/api/articles/<int:id>/", tag="Article", blueprint=api_bp)
api.route(AuthorList, "author_list", "/api/authors/",
          tag="Author", blueprint=api_bp)
api.route(AuthorDetail, "author_detail",
          "/api/authors/<int:id>/", tag="Author", blueprint=api_bp)
api.route(TagList, "tag_list", "/api/tags/", tag="Tag", blueprint=api_bp)
api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/",
          tag="Tag", blueprint=api_bp)
api.route(UserList, "user_list", "/api/users/", tag="User", blueprint=api_bp)
api.route(UserDetail, "user_detail", "/api/users/<int:id>/",
          tag="User", blueprint=api_bp)
