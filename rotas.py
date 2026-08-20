from main import app
from flask import render_template, request, redirect, session
import controllers.contas as contas

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    if request.form["senha"] != request.form["confirmar_senha"]:
        return redirect("/cadastro")

    usuario = contas.cadastrar(request.form["email"], request.form["senha"])

    if usuario:
        session["usuario_id"] = usuario.id
        return redirect("/")
    return redirect("/cadastro")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/autenticar", methods=["POST"])
def autenticar():
    usuario = contas.login(request.form["email"], request.form["senha"])

    if usuario != None:
        session["usuario_id"] = usuario.id
        return redirect("/")

    return redirect("/login")