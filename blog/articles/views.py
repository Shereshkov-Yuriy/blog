from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

from blog.articles.constants import ARTICLES

article = Blueprint(
    "article",
    __name__,
    static_folder="../static",
    url_prefix="/articles/",
)


@article.route("/")
def article_list():
    return render_template(
        "articles/list.html",
        articles=ARTICLES,
    )


@article.route("/<int:pk>")
@login_required
def get_article(pk: int):
    try:
        article_data = ARTICLES[pk]
    except KeyError:
        raise NotFound(f"Articles id {pk} not found.")
    return render_template(
        "articles/details.html",
        article_id=pk,
        article_data=article_data,
    )
