# Programa: cadastro
""" Cadastro de Pessoas"""

class Pessoa(object):
    """ Classe Pessoa: responsável em armazenar dados de uma pessoa """

    __nome = ""
    __idade = -1
    __sexo = ''

    def __init__(self):
        """ Construtor Python """

    def cadastra(self):
        """ Método cadastra: permite receber os dados de uma pessoa """
        self.__nome = input("Digite o seu nome: ")

        while self.__idade < 0:
            try:
                self.__idade = int(input("Digite sua idade: "))
            except ValueError:
                print("Digite um número inteiro!")

        self.__sexo = input("Sexo: M para masculino ou F para feminino: ")
        self.__sexo = self.__sexo.upper()
        if self.__sexo != 'F':
            self.__sexo = 'M'

    def mostra(self):
        """ Método mostra: apresenta os dados cadastrados de uma pessoa """
        if self.__sexo == 'F' and self.__idade > 30:
            print(self.__nome + ' idade secreta ' + self.__sexo)
        else:
            print(self.__nome + ' ' + str(self.__idade) + ' ' + self.__sexo)

PESSOAS = list()
for i in range(0, 3):
    OBJ = Pessoa()
    OBJ.cadastra()
    PESSOAS.append(OBJ)

for PESSOA in PESSOAS:
    PESSOA.mostra()
