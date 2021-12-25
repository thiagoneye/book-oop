"""Classe comporta de vedação"""

class ComportaVedacao(object):
    """Comporta de vedação"""

    def __init__(self):
        """Construtor"""
        print("Construtor da classe comporta de vedação")
        self.status = "FECHADO"

    def __del__(self):
        """Destrutor"""
        print("Removendo comporta de vedação: endereco {}".format(id(self)))

    def abrir(self, vazao=None):
        """Abertura da comporta de vedação"""
        if vazao == None:
            print("Comporta de vedação aberta. Saindo toda a água")
        else:
            print("Comporta de vedação aberta. Saindo " + str(vazao) + "de água")

        self.status = "ABERTO"

    def fechar(self):
        """Fechamento da comporta de vedação. Água saindo ..."""
        print("Comporta de vedação fechada")
        self.status = "FECHADO"

    def get_status(self):
        """Status da comporta de vedação (aberta ou fechada)"""
        return self.status
