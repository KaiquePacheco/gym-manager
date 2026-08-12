from flask import Flask

host = "0.0.0.0"
port = 5500
debug=True

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Hello world!"

if __name__ == "__main__":
    app.run(host, port=port, debug=debug)