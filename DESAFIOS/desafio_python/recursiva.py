'''
Função recursiva
Crie uma função recursiva para descobrir o menor número inteiro divisível por 2, 3 e 10 ao mesmo tempo. Quando encontrá-lo, imprima-o na tela.
'''


def recursiva(num=1):
    if num % 2 == 0 and num % 3 == 0 and num % 10 == 0:
        return num
    else:
        return recursiva(num + 1)


print(f"O menor número inteiro divisivel por 2, 3 e 10 ao mesmo tempo é: {recursiva()}")
