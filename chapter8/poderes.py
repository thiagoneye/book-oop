""" Módulo Poderes """

class SuperForca:
    def __init__(self):
        print("Tenho poder de super força.")
        self.forca = 0

    def get_forca(self):
        return self.forca

    def set_forca(self, forca):
        self.forca = forca

    def get_dados(self):
        print("Força:" + str(self.get_forca()))

class Voar:
    def __init__(self):
        print("Consigo voar.")
        self.altitude = 0

    def get_altitude(self):
        return self.altitude

    def set_altitude(self, altitude):
        self.altitude = altitude

    def get_dados(self):
        if self.get_altitude() > 0:
            print("Voo em:" + str(self.get_altitude()) + " metros.")

class Pessoa:
    def __init__(self):
        print("Sou uma pessoa.")
        self.nome = "NÃO REVELADO"
        self.ocupacao = "NÃO REVELADO"
        self.sexo = "Masculino"
        self.peso = 0
        self.altura = 0

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_ocupacao(self):
        return self.ocupacao

    def set_ocupacao(self, ocupacao):
        self.ocupacao = ocupacao

    def get_sexo(self):
        return self.sexo

    def set_sexo(self, sexo):
        self.sexo = sexo

    def get_peso(self):
        return self.peso

    def set_peso(self, peso):
        self.peso = peso

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

    def get_dados(self):
        print("Nome: " + self.get_nome())
        print("Sexo: " + self.get_sexo())
        print("Função: " + self.get_ocupacao())
        print("Peso: " + str(self.get_peso()))
        print("Altura: " + str(self.get_altura()))
