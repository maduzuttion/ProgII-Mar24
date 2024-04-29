from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "System ok"

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/fat")
def fat():
    a = int(request.args.get('n1'))
    f=1
    for i in range(1, a+1):
        f=f*i
    
    fat=f
    return render_template("fat.html", total = fat)

# $ flask run 