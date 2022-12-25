import click
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command("init-db")
@with_appcontext
def init_db():
    """
    Run in your terminal: flask init-db
    """
    db.create_all()
    print("Done!")


@click.command("create-users")
@with_appcontext
def create_users():
    """
    Run in your terminal: flask create-users
    > Done! created users: <User 1:'admin'> <User 2:'georgy'>
    """
    from blog.models import User

    admin = User(username="admin", email="admin@ru.ru", password=generate_password_hash("admin"), is_staff=True)
    georgy = User(username="georgy", email="georgy@ru.ru", password=generate_password_hash("georgy"), is_staff=False)
    yuriy = User(username="yuriy", email="yuriy@ru.ru", password=generate_password_hash("yuriy"), is_staff=False)
    db.session.add(admin)
    db.session.add(georgy)
    db.session.add(yuriy)
    db.session.commit()
    print("Done! created users:", admin, georgy, yuriy)
