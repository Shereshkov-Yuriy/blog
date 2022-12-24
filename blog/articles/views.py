from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.articles import constants as ARTICLES

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
        articles=ARTICLES.ARTICLES,
    )


@article.route("/<int:pk>")
def get_article(pk: int):
    try:
        article_data = ARTICLES.ARTICLES[pk]
    except KeyError:
        raise NotFound(f"Articles id {pk} not found.")
    return render_template(
        "articles/details.html",
        article_id=pk,
        article_data=article_data,
    )
