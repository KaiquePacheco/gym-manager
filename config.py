from dotenv import load_dotenv
from os import getenv

load_dotenv(".env")

APP_HOST = getenv("APP_HOST")
APP_PORT = int(getenv("APP_PORT"))
APP_DEBUG = bool(getenv("APP_DEBUG"))