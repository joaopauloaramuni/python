from visualizador import desenhar_automato
from linguagens import *

def main():
    print("Escolha o autômato:")
    print("1. Linguagem que aceita apenas strings compostas pelos símbolos 'a' e 'b'")
    print("2. Linguagem que aceita apenas strings terminadas em 'ab'")
    print("3. Linguagem que aceita strings com um número par de 'a's")
    print("4. Linguagem que aceita strings contendo 'aa' como subcadeia")
    print("5. Linguagem que aceita apenas padrões 'ab' repetidos (com estado de erro)")

    escolha = input("Digite o número correspondente: ")

    # Criação dos 5 autômatos
    automatos = [
        linguagem_apenas_a_b(),
        linguagem_terminadas_em_ab(),
        linguagem_par_de_as(),
        linguagem_contem_aa(),
        linguagem_somente_ab_repetido()
    ]

    # Selecionar o autômato baseado na escolha
    if escolha in ['1', '2', '3', '4', '5']:
        indice = int(escolha) - 1
        automato = automatos[indice]
    else:
        print("Escolha inválida!")
        return

    # Solicitar a palavra para testar no autômato escolhido
    entrada = input("Digite a palavra para testar: ")
    resultado, caminho = automato.simular_entrada(entrada)

    # Exibir o resultado do teste
    print(f"Entrada: {entrada}, Resultado: {'Aceita' if resultado else 'Rejeita'}, Caminho: {caminho}")

    # Desenhar todos os autômatos gerados
    print("\nGerando gráficos dos autômatos...")
    for i, automato in enumerate(automatos, start=1):
        desenhar_automato(automato, f"automato_{i}")
        print(f"Automato {i} gerado: automato_{i}.png")

if __name__ == "__main__":
    main()

# brew install graphviz
# pip install graphviz
