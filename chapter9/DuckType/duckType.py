""" Exemplo de DuckType """

class Pato:
    def nadar(self):
        print("quack, quack, quack")

    def som(self):
        print("QUAACCCKKKKK !!!!!!!!")

class PatinhoFeio:
    def nadar(self):
        print("Quãã... Quãã...")

    def som(self):
        print("Quãã...")

class Pluto:
    def som(self):
        print("Au Au Au !!!")

class Donald(Pato):
    pass
