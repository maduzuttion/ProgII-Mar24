from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")#rota para puxar o template home.html
def home():
    return render_template("home.html")

@app.route("/about")#rota para puxar o template about.html
def about():
    return render_template("about.html")

@app.route("/table")#rota para puxar o template table.html
def tabela():
    return render_template("table.html")
