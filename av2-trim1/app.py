from flask import Flask, render_template, request, redirect
from pony.orm import *

db = Database()
app = Flask(__name__)

class Produto(db.Entity):
    cod_barra=Required(str)
    nome_prod=Required(str)
    preco_prod=Required(float)
    qtd=Required(str)
    tipo_prod=Optional(str)

    def __str__(self):
        return f'{self.nome_prod},{self.preco_prod}'