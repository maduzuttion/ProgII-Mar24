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

# $ flask run
#pesquisar no navegador: localhost:5000/soma?n1=5&n2=10
###Sendo escrito os números na barra de pesquisa como mostrado anteriormente