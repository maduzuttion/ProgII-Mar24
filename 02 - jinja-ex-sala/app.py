from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "System ok"

@app.route("/sum")
def soma():
    a = int(request.args.get('n1'))
    b = int(request.args.get('n2'))
    sum = a + b
    return render_template("sum.html", total = sum)

# $ flask run