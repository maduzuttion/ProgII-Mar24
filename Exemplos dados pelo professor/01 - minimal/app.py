from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/soma")
def soma():
    return str(8+10)

# $flsk run(https://localhost:500)
# Na internet: $flask run --host=0.0.0.0