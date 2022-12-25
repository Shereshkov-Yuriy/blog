from flask_login import UserMixin

from blog.app import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, default=False)

    def __init__(self, username, email, password, is_staff):
        self.username = username
        self.email = email
        self.password = password
        self.is_staff = is_staff

    def __repr__(self):
        return f"<User {self.id!r}:{self.username!r}>"
