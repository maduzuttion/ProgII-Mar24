from flask import Flask, render_template, request, redirect
from pony.orm import *

db = Database()
app = Flask(__name__)

class Produto(db.Entity):
    nome_prod=Required(str)
    cod_barra=Required(str)
    preco_prod=Required(float)
    tipo_prod=Optional(str)
    def __str__(self):
        return f'{self.nome_prod},{self.preco_prod}'