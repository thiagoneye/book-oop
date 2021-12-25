"""Exemplo do uso da classe Carro"""

from carro import Carro

ESTACIONAMENTO = list()

for i in range(0, 5):
    OBJ = Carro()
    ESTACIONAMENTO.append(OBJ)

ESTACIONAMENTO[0].set_modelo('Monza')
ESTACIONAMENTO[0].set_cor('azul')
ESTACIONAMENTO[0].set_ano(1992)
ESTACIONAMENTO[0].set_ano('aaaa')

Carro.total()
del ESTACIONAMENTO[1]

for CARRO in ESTACIONAMENTO:
    print(CARRO.get_modelo() + ' - ' + CARRO.get_ano())

Carro.stotal(ESTACIONAMENTO[0])
