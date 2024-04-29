from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    # redirect to the form
    return redirect(url_for('form'))

@app.route("/form")
def form():
    # init list of values
    valores = []
    # try to get some values
    valores.append(request.args.get('campo_caixa') if request.args.get('campo_caixa') else "")
    valores.append(request.args.get('campo_area') if request.args.get('campo_area') else "")
    valores.append(request.args.get('campo_select') if request.args.get('campo_select') else "")
    valores.append(request.args.get('campo_radio') if request.args.get('campo_radio') else "")
    valores.append(request.args.get('campo_datalist') if request.args.get('campo_datalist') else "")
    valores.append(request.args.get('campo_caixa_idade') if request.args.get('campo_caixa_idade') else "50")
    
    # prepare values at checkbox
    s = ""
    s += " " + request.args.get('campo_salgada') if request.args.get('campo_salgada') else ""
    s += " " + request.args.get('campo_doce') if request.args.get('campo_doce') else ""
    s += " " + request.args.get('campo_mineira') if request.args.get('campo_mineira') else ""
    s += " " + request.args.get('campo_tailandesa') if request.args.get('campo_tailandesa') else ""
    valores.append(s)
    
    # open the form
    return render_template("form.html", valores = valores)
