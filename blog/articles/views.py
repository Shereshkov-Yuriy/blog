from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms.article import CreateArticleForm
from blog.models import Article, Author

article = Blueprint(
    "article",
    __name__,
    static_folder="../static",
    url_prefix="/articles/",
)


@article.route("/", methods=["GET"])
def article_list():
    articles = Article.query.all()
    return render_template(
        "articles/list.html",
        articles=articles,
    )


@article.route("/<int:pk>")
@login_required
def article_details(pk: int):
    _article = Article.query.filter_by(id=pk).one_or_none()
    if _article is None:
        raise NotFound
    return render_template(
        "articles/details.html",
        article=_article,
    )


@article.route("/create", methods=["GET"])
@login_required
def create_article_form():
    form = CreateArticleForm(request.form)
    return render_template("articles/create.html", form=form)


@article.route("/", methods=["POST"])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), body=form.body.data)
        db.session.add(_article)

        if current_user.author:
            _article.author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id = author.id

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for(".article_details", pk=_article.id))

    return render_template("articles/create.html", form=form)
