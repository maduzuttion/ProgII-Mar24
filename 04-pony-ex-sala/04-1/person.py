# pip3 install pony(para instalar o pony)

from pony.orm import *

db = Database()# conectar-se com o banco

class Pessoa(db.Entity):
    nome = Required(str)
    email = Required(str)
    telefone = Optional(str)

db.bind(provider='sqlite', filename='person.db', create_db=True)# provider(); f ilename(É o nome do banco de dados); create_db(código que cria o db caso ele não exista).

db.generate_mapping(create_tables=True)# Cria as tabelas

with db_session:# iniciando a sessão
    jo = Pessoa(nome='João da Silva', email='josilva@gmail.com')# passando os dados
    commit()# salvando os dados
    print(jo.nome, jo.email)# exibindo os dados