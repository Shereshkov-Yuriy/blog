import re
from datetime import datetime

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
@app.route("/<name>")
@app.route("/greet/<name>")
def greet_name(name="Friend"):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = f"<h1>Hello there, {clean_name}! It's {formatted_now}</h1>"
    return content


@app.route("/user/")
def reed_user():
    user = request.args.get("name")
    headers = request.headers
    return f"Hello, {user}!\n{headers}"
