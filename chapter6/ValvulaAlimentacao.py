"""Classe válvula de alimentação"""

class ValvulaAlimentacao(object):
    """Válvula de alimentação"""

    def __init__(self):
        """Construtor"""
        print("Construtor da válvula de alimentação")
        self.capacidade_vazao = 1.1

    def __del__(self):
        """Destrutor"""
        print("Removendo válvula de alimentação: endereço {}".format(id(self)))

    def encher_agua(self):
        """Descarga inteligente. Opção 1: Urina. Opção 2: Fezes"""
        print("Vazão: " + str(self.capacidade_vazao) + " litros/seg")

    def get_vazao(self):
        """Retorna a capacidade de vazão do vaso"""
        return self.capacidade_vazao
