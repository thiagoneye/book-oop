"""Classe Vereador"""

from Politico import Politico

class Vereador(Politico):
    """Classe Vereador"""

    def __init__(self, nome, partido, estado, municipio):
        """Construtor da classe Vereador"""

        Politico.__init__(self)
        self.set_nome(nome)
        self.set_partido(partido)
        self.set_estado(estado)
        self.__municipio = municipio
        self.set_funcao("propor leis municipais em benefício da população.")

    def set_municipio(self, municipio):
        """Setar o municipio do politico"""

        if type(municipio) == str:
            self.__municipio = municipio

    def get_municipio(self):
        """Retorna o nome do municipio do político."""
        return self.__municipio

    def apresentacao(self):
        Politico.apresentacao(self)
        print('sou Vereador: ' + self.get_municipio() + '/' + self.get_estado())
        print('Minha função é ' + self.get_funcao())
        print('Fui eleito por ' + self.get_estado())
        print('==============================')
