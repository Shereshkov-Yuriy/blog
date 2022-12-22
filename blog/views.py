from flask import Blueprint, render_template

index = Blueprint("index", __name__, static_folder="./static")


@index.route("/")
def index_page():
    return render_template("index.html", name="Yuriy")
