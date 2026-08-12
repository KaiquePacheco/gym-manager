from flask import Flask

app = Flask(__name__)

app.config.from_pyfile("config.py")
host = app.config["APP_HOST"]
port = app.config["APP_PORT"]
debug = app.config["APP_DEBUG"]

@app.route("/", methods=["GET"])
def index():
    return "Hello world!"

if __name__ == "__main__":
    app.run(host, port=port, debug=debug)