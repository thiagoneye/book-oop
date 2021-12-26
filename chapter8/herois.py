""" módulo Heróis """

from poderes import *

class Hulk(Pessoa, SuperForca):
    def __init__(self):
        Pessoa.__init__(self)
        SuperForca.__init__(self)
        self.vai_pescar()

    def ficar_nervoso(self):
        print("Hulk ESMAGA !!!")
        self.set_nome("HUULLLKKKK !!!!!")
        self.set_ocupacao("Esmagador profissional")
        self.set_altura(3.20)
        self.set_peso(500)
        self.set_forca(10000)

    def vai_pescar(self):
        print("Hulk Calmo ...")
        self.set_nome("Bruce Banner")
        self.set_ocupacao("Cientista físico nuclear especialista em raio gama")
        self.set_altura(1.73)
        self.set_peso(72)
        self.set_forca(30)

    def get_dados(self):
        print("")
        Pessoa.get_dados(self)
        SuperForca.get_dados(self)
        print("")

class IronMan(Pessoa, SuperForca, Voar):
    def __init__(self):
        Pessoa.__init__(self)
        SuperForca.__init__(self)
        Voar.__init__(self)
        self.armaduraAtivada = False
        self.set_nome("Antony Stark")
        self.set_ocupacao("Empresário, gênio, bilionário, playboy e filantropo")
        self.set_altura(1.74)
        self.set_peso(80)
        self.set_forca(30)

    def ativar_armadura(self):
        self.armaduraAtivada = True
        print("\nJavis diz: Pronto para o combate, senhor")
        self.set_forca(200)

    def desativar_armadura(self):
        print("\nJavis diz: Desativando a armadura de combate, senhor")
        self.armaduraAtivada = False
        self.set_forca(30)
        self.set_altitude(0)

    def set_altitude(self, altitude):
        if self.armaduraAtivada:
            self.altitude = altitude
        else:
            print("Javis diz: Não consigo voar sem a armadura, senhor")

    def get_dados(self):
        print("")
        if self.armaduraAtivada:
            print("Armadura ativada: modo Homem de Ferro")
        Pessoa.get_dados(self)
        SuperForca.get_dados(self)
        Voar.get_dados(self)
        print("")

class Thor(Pessoa, SuperForca, Voar):
    def __init__(self):
        Pessoa.__init__(self)
        SuperForca.__init__(self)
        self.set_nome("Donald Black")
        self.set_ocupacao("Médico e Deus do Trovão")
        self.set_altura(1.80)
        self.set_peso(85)
        self.set_forca(5000)

    def get_dados(self):
        print("")
        print("Sou um Deus, filho de Odin, mas só ...")
        Pessoa.get_dados(self)
        SuperForca.get_dados(self)
        print("")

class CapitaoAmerica(Pessoa, SuperForca):
    def __init__(self):
        Pessoa.__init__(self)
        SuperForca.__init__(self)
        self.set_nome("Steven Grant 'Steve' Rogers")
        self.set_ocupacao("Soldado geneticamente modificado")
        self.set_altura(1.80)
        self.set_peso(85)
        self.set_forca(1000)

    def get_dados(self):
        print("")
        Pessoa.get_dados(self)
        SuperForca.get_dados(self)
        print("")

class ViuvaNegra(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.set_nome("Natasha Alianovna Romanoff")
        self.set_ocupacao("Agente sevreta da KGB")
        self.set_sexo("Feminino")
        self.set_altura(1.70)
        self.set_peso(60)

    def get_dados(self):
        print("")
        Pessoa.get_dados(self)
        print("")

class Arqueiro(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.set_nome("Clinton Francis 'Clint' Barton")
        self.set_ocupacao("Arqueiro por hobby e profissão")
        self.set_altura(1.75)
        self.set_peso(65)

    def get_dados(self):
        print("")
        Pessoa.get_dados(self)
        print("")
