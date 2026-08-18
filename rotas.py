from main import app
from flask import render_template, request, redirect
import controllers.contas as contas

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    if contas.cadastrar(request.form["email"], request.form["senha"]):
        return redirect("/")
    return redirect("/cadastro")

@app.route("/login")
def login():
    return render_template("login.html")