import click
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command("create-admin")
@with_appcontext
def create_admin():
    """
    Run in your terminal: flask create-admin
    > Done! created admin: <User 1:'admin'>
    """
    from blog.models import User

    admin = User(username="admin", email="admin@ru.ru", password=generate_password_hash("admin"), is_staff=True)
    db.session.add(admin)
    db.session.commit()
    print("Done! created admin:", admin)
