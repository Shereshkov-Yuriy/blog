from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash

from blog.extensions import db
from blog.forms.user import UserRegisterForm
from blog.models import User

user = Blueprint(
    "user",
    __name__,
    static_folder="../static",
    url_prefix="/users/",
)


@user.route("register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("user.profile", pk=current_user.id))

    form = UserRegisterForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        _user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data),
        )

        db.session.add(_user)
        db.session.commit()

        login_user(_user)
        return redirect(url_for("index.index_page"))

    return render_template("users/register.html", form=form)


@user.route("/")
@login_required
def user_list():
    from blog.models import User

    users = User.query.all()
    return render_template(
        "users/list.html",
        users=users,
    )


@user.route("/<int:pk>")
@login_required
def profile(pk: int):
    from blog.models import User

    user = User.query.filter_by(id=pk).one_or_none()
    if user is None:
        raise NotFound(f"User #{pk} doesn't exist!")
    return render_template(
        "users/profile.html",
        user=user,
    )
