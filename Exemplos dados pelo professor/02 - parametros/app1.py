from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Olá mundo!</p>"

@app.route("/soma")
def soma():
    a = int(request.args.get('n1'))
    b = int(request.args.get('n2'))
    return str(a+b)

# $ flask --app app1 run
#pesquisar no navegador: localhost:5000/soma?n1=5&n2=10 -----> resultato da soma aparente:15
#números escritos na barra de pesquisa