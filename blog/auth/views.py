from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash

from blog.models import User

auth = Blueprint("auth", __name__, static_folder="../static")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for("user.profile", pk=current_user.id))
        return render_template("auth/login.html")

    email = request.form.get("email")
    password = request.form.get("password")

    _user = User.query.filter_by(email=email).first()
    if not _user or not check_password_hash(_user.password, password):
        flash("Check your login details")
        return redirect(url_for(".login"))

    login_user(_user)
    return redirect(url_for("user.profile", pk=_user.id))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))
