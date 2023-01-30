import click
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command("create-admin")
@with_appcontext
def create_admin():
    """
    Run in your terminal: flask create-admin
    > Done! Created admin: <User 1:'admin'>
    """
    from blog.models import User

    admin = User(
        first_name="admin",
        last_name="admin",
        username="admin",
        email="admin@ru.ru",
        password=generate_password_hash("admin"),
        is_staff=True,
        )
    db.session.add(admin)
    db.session.commit()
    click.echo(f"Done! Created admin: {admin}")


@click.command("create-tags")
@with_appcontext
def create_tags():
    """
    Run in your terminal: flask create-tags
    > Done! Created tags: flask, django, ...
    """
    from blog.models import Tag

    tags = ["flask", "django", "python", "sqlalchemy", "news"]
    for name in tags:
        db.session.add(Tag(name=name))
    db.session.commit()
    click.echo(f"Done! Created tags: {', '.join(tags)}")
