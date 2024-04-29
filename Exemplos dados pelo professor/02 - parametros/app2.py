from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/soma/<int:n1>/<int:n2>")
def soma(n1, n2):
    a = int(n1)
    b = int(n2)
    return f'A soma é: <h2>{a+b}</h2>'

#flask --app app2 run
#Para acessar no navegador: localhost:5000/soma/5/10