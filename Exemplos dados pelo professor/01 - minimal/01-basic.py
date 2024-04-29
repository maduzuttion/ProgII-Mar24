from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()

#play no vs code 
#ou no terminal: $ python3 01-basic.py
#Acessar no navegador: https://localhost:5000 ou https://127.0.0.1:5000
#Feit pelo professor