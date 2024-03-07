from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Olá mundo!</p>"

# $ flask run
# Na internet: $ flask run --host=0.0.0.0