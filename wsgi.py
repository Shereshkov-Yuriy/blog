from werkzeug.security import generate_password_hash

from blog.app import create_app, db
from blog.models import User

app = create_app()
