from flask import Blueprint, render_template
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.models import Tag

tag = Blueprint(
    "tag",
    __name__,
    static_folder="../static",
    url_prefix="/tags/",
)


@tag.route("/", methods=["GET"])
def tag_list():
    tags = Tag.query.all()
    return render_template(
        "tags/list.html",
        tags=tags,
    )


@tag.route("/<int:pk>")
def tag_details(pk: int):
    _tag = Tag.query.filter_by(id=pk).options(joinedload(Tag.articles)).one_or_none()
    if _tag is None:
        raise NotFound
    return render_template(
        "tags/details.html",
        tag=_tag,
    )
