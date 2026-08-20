from main import app
from flask import render_template, request, redirect, session, url_for
import controllers.contas as contas

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    if request.form["senha"] != request.form["confirmar_senha"]:
        return redirect(url_for("cadastro"))

    usuario = contas.cadastrar(request.form["email"], request.form["senha"])

    if usuario:
        session["usuario_id"] = usuario.id
        return redirect(url_for("index"))
    return redirect(url_for("cadastro"))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/autenticar", methods=["POST"])
def autenticar():
    usuario = contas.login(request.form["email"], request.form["senha"])

    if usuario != None:
        session["usuario_id"] = usuario.id
        return redirect(url_for("index"))

    return redirect(url_for("login"))

@app.route("/")
def index():
    if session["usuario_id"] == None or not session["usuario_id"]:
        return redirect(url_for("login"))
    return render_template("index.html")