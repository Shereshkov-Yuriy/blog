import os

from dotenv import load_dotenv

from blog.enums import EnvType

load_dotenv()

ENV = os.getenv("FLASK_ENV", default=EnvType.production)
DEBUG = ENV == EnvType.development

SECRET_KEY = os.getenv("SECRET_KEY")

# при деплое переменная DATABASE_URL для меня не работает
# SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
# поэтому добавил новую переменную в секреты
SQLALCHEMY_DATABASE_URI = os.getenv("PG_DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False

API_URL = os.getenv("API_URL")

WTF_CSRF_ENABLED = True

FLASK_ADMIN_SWATCH = "solar"

OPENAPI_URL_PREFIX = "/api/swagger"
OPENAPI_SWAGGER_UI_PATH = "/"
OPENAPI_SWAGGER_UI_VERSION = "3.22.0"
