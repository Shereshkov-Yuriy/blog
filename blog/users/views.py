from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.users import constants as USERS

user = Blueprint(
    "user",
    __name__,
    static_folder="../static",
    url_prefix="/users/",
)


@user.route("/")
def user_list():
    return render_template(
        "users/list.html",
        users=USERS.USERS,
    )


@user.route("/<int:pk>")
def get_user(pk: int):
    try:
        user_name = USERS.USERS[pk]
    except KeyError:
        raise NotFound(f"User id {pk} not found.")
    return render_template(
        "users/details.html",
        user_id=pk,
        user_name=user_name,
    )
