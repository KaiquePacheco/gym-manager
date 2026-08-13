from main import app
from flask import render_template

@app.route("/cadastro")
def index():
    return render_template("cadastro.html")