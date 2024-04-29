from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Olá mundo!</p>"

# $ flask --app 02-basic run
# Acessar no navegador: https://localhost:5000 ou https://127.0.0.1:5000
# Na internet: $ flask --app 02-basic run --host=0.0.0.0
#Feito pelo professor