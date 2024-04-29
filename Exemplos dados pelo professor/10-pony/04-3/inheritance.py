from pony.orm import *

db = Database()

class Veiculo(db.Entity):
    placa = Optional(str)
    cor = Required(str)
    marca = Required(str)
    modelo = Required(str)
    def __str__(self):#comando str do veiculo
        s = f'{self.cor}, {self.marca}, {self.modelo}'
        if self.placa:
            s += self.placa
        return s

class Carro(Veiculo):
    lugares = Required(int)
    def __str__(self):
        s = super().__str__()
        s += f', {self.lugares}'#se o veiculo for carro printa lugares do carro, além das informações de veiculo
        return s
    
class Moto(Veiculo):
    cilindradas = Required(int)
    def __str__(self):
        s = super().__str__()
        s += f', {self.cilindradas}'#se o veiculo for moto printa cilindradas da moto, além das informações de veiculo
        return s

db.bind(provider='sqlite', filename='person.db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:#Iniciando sessão
    v1 = Carro(placa="FXX 1234", cor = "azul", 
               marca = "ford", modelo = "ka", lugares = 5)
    v2 = Moto(cor = "preta", marca = "honda",
              modelo = "biz", cilindradas = 150)
    commit()

    print(v1)
    print(v2)

# Feito pelo professor