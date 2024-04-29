from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/")
def home():
    return "System ok"

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/eq")
def eq():
    a=int(request.args.get('n1'))
    b=int(request.args.get('n2'))
    c=int(request.args.get('n3'))
    m=(b**2)-4*a*c
    n=math.sqrt(m)
    if m<0:
        total="não há raiz real"
    elif m==0:
        r1=(b*(-1))/2*a
        total="a raiz real é:" + r1
    elif m>0:
        r1=((b*(-1))+n)/2*a
        r2=((b*(-1))-n)/2*a
        total="As raizes reais são:" + "X1=" + r1 +"e X2=" + r2
    return render_template("fat.html", total=total)

# $ flask run 