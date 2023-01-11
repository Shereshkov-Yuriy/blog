from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash

from blog.forms.login import LoginForm
from blog.models import User

auth = Blueprint("auth", __name__, static_folder="../static")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for("index.index_page"))
        return render_template("auth/login.html", form=LoginForm(request.form))

    form = LoginForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        _user = User.query.filter_by(email=form.email.data).first()
        if not _user or not check_password_hash(_user.password, form.password.data):
            flash("Check your login details")
            return redirect(url_for(".login"))

        login_user(_user)
        return redirect(url_for("index.index_page"))

    return render_template("auth/login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))
