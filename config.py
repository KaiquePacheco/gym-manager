from dotenv import load_dotenv
from os import getenv

load_dotenv(".env", override=True)

APP_HOST = getenv("APP_HOST")
APP_PORT = int(getenv("APP_PORT"))
APP_DEBUG = bool(getenv("APP_DEBUG"))

SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")

SECRET_KEY = getenv("SECRET_KEY")