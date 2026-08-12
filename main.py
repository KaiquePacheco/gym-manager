from flask import Flask

app = Flask(__name__)

app.config.from_pyfile("config.py")
host = app.config["APP_HOST"]
port = app.config["APP_PORT"]
debug = app.config["APP_DEBUG"]

from rotas import *

if __name__ == "__main__":
    app.run(host, port=port, debug=debug)