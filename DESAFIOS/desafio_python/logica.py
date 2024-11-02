'''
Lógica de programação
Pensando em todos os números naturais inferiores a 10 que são múltiplos de 3 ou 5, temos 3, 5, 6 e 9. Somando esses múltiplos obtemos o valor 23.
Utilize um algorítimo para calcular a soma de todos os múltiplos de 3 ou 5 abaixo de 1000
'''


def e_multiplo(numero=None, multiplos=None):
    """Entrada:
        Numero: int
        Multiplo: array de int ou um int
    Saída esperada:
        Boolean se número é multiplo"""
    if not (isinstance(numero, int) and isinstance(multiplos, (int, list, tuple))):
        raise Exception("'numero' deve ser um int e 'multiplos' deve ser um int ou uma lista/tupla de int")

    if isinstance(multiplos, int):
        return numero % multiplos == 0
    else:
        for multiplo in multiplos:
            if not isinstance(multiplo, int):
                raise Exception("'multiplos' deve ser um int ou uma lista/tupla de int")
            if numero % multiplo == 0:
                return True
        return False


numeros = []
teste_multiplos = (3, 5)
for numero in range(1000):
    if e_multiplo(numero, teste_multiplos):
        numeros.append(numero)

print(f"A soma de todos os múltiplos de 3 ou 5 abaixo de 1000 é: {sum(numeros)}")
