
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms.article import CreateArticleForm
from blog.models import Article, Author, Tag

article = Blueprint(
    "article",
    __name__,
    static_folder="../static",
    url_prefix="/articles/",
)


@article.route("/", methods=["GET"])
def article_list():
    articles = Article.query.all()
    # call RPC method
    # count_articles: Dict = requests.get(
    #     f"{API_URL}/api/articles/event_get_count/").json()
    return render_template(
        "articles/list.html",
        articles=articles,
        # count_articles=count_articles["count"],
    )


@article.route("/<int:pk>")
@login_required
def article_details(pk: int):
    _article = Article.query.filter_by(id=pk).options(joinedload(Article.tags)).one_or_none()
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
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    return render_template("articles/create.html", form=form)


@article.route("/", methods=["POST"])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), body=form.body.data)

        if current_user.author:
            _article.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id = author.id

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for("article.article_details", pk=_article.id))

    return render_template("articles/create.html", form=form)
