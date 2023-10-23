# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 18:54:58 2023

@author: moura
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#if __name__ == "__main__":
    app.run(debug=True) 