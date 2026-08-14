from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Base

app = Flask(__name__)

app.config.from_pyfile("config.py")
host = app.config["APP_HOST"]
port = app.config["APP_PORT"]
debug = app.config["APP_DEBUG"]

db = SQLAlchemy(model_class=Base)
db.init_app(app)

from rotas import *

if __name__ == "__main__":
    app.run(host, port=port, debug=debug)