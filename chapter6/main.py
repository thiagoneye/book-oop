"""Exemplo do uso da caixa acoplada"""

from CaixaAcoplada import CaixaAcoplada

VASO = CaixaAcoplada()
VASO.acionar()
print('\n\n')
VASO.acionar(1)
print('\n\n')
VASO.acionar(2)
print('\n\n')
VASO.acionar(3) # Descarga inválida
VASO.relatorio()
