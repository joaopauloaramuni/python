'''
Orientação a objeto
Crie uma classe contendo 3 propriedades com seus respectivos gets e sets e um método que multiplique as 3 retornando o produto. Deixe um exemplo de utilização da sua classe no final do código.
'''


class Exemplo:
    def __init__(self):
        # iniciando em 1 para não dar erro na multiplicação caso passe menos de 3 números.
        self.__atributo1 = 1
        self.__atributo2 = 1
        self.__atributo3 = 1

    def produto(self):
        return self.getAtributo1() * self.getAtributo2() * self.getAtributo3()

    def getAtributo1(self):
        return self.__atributo1

    def setAtributo1(self, num=None):
        if not isinstance(num, (int, float)):
            return False
        self.__atributo1 = num
        return True

    def getAtributo2(self):
        return self.__atributo2

    def setAtributo2(self, num=None):
        if not isinstance(num, (int, float)):
            return False
        self.__atributo2 = num
        return True

    def getAtributo3(self):
        return self.__atributo3

    def setAtributo3(self, num=None):
        if not isinstance(num, (int, float)):
            return False
        self.__atributo3 = num
        return True


### Exemplo de uso abaixo
exemplo = Exemplo()
exemplo.setAtributo1(5)
exemplo.setAtributo2(7)
exemplo.setAtributo3(10)
print(f"O produto de {exemplo.getAtributo1()}*{exemplo.getAtributo2()}*{exemplo.getAtributo3()} é: {exemplo.produto()}")
