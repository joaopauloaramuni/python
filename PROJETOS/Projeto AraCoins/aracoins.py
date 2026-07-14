"""
AraCoins - Sistema de Compras e Recompensas
=============================================

Sistema interativo para registro de compras e cálculo de recompensas
simbólicas, desenvolvido com base nos princípios de Test-Driven
Development (TDD).

Cada compra é armazenada como uma tupla (produto, valor) dentro de
uma lista, permitindo consultas, ordenações e cálculo de totais.
"""


# ---------------------------------------------------------------------------
# Tópico 1 e 2: Regras de recompensa (TDD + estruturas condicionais)
# ---------------------------------------------------------------------------
def calcular_recompensa(valor):
    """
    Calcula a recompensa simbólica com base no valor de uma compra.

    Regras de negócio:
        - valor < 20:            1 ponto
        - 20 <= valor < 100:     5 pontos
        - valor >= 100:          10 pontos

    Args:
        valor (float): valor pago na compra.

    Returns:
        int: quantidade de pontos de recompensa.
    """
    if valor < 0:
        raise ValueError("O valor da compra não pode ser negativo.")

    if valor >= 100:
        return 10
    elif valor >= 20:
        return 5
    else:
        return 1


# ---------------------------------------------------------------------------
# Tópico 4: Registro de compras (listas e tuplas)
# ---------------------------------------------------------------------------
def registrar_compra(compras, produto, valor):
    """
    Registra uma nova compra na lista de compras.

    Cada compra é representada por uma tupla (produto, valor), que é
    adicionada à lista com .append().

    Args:
        compras (list): lista de tuplas (produto, valor) já registradas.
        produto (str): nome do produto.
        valor (float): valor pago pelo produto.

    Returns:
        list: a própria lista de compras, já atualizada.
    """
    if not produto or not produto.strip():
        raise ValueError("O nome do produto não pode ser vazio.")
    if valor < 0:
        raise ValueError("O valor da compra não pode ser negativo.")

    compras.append((produto, valor))
    return compras


# ---------------------------------------------------------------------------
# Tópico 5: Exibição e totalização (laço for + soma acumulada)
# ---------------------------------------------------------------------------
def calcular_total(compras):
    """
    Calcula o total gasto somando o valor de todas as compras.

    Args:
        compras (list): lista de tuplas (produto, valor).

    Returns:
        float: soma total dos valores pagos. Retorna 0 para lista vazia.
    """
    total = 0
    for item in compras:
        total += item[1]
    return total


def exibir_compras(compras):
    """
    Exibe, de forma organizada, todas as compras registradas.

    Args:
        compras (list): lista de tuplas (produto, valor).
    """
    if not compras:
        print("Nenhuma compra registrada até o momento.")
        return

    print("=== Compras Registradas ===")
    for item in compras:
        produto, valor = item[0], item[1]
        print(f"{produto:<18}- R$ {valor:.2f}")

    print(f"\nTotal gasto: R$ {calcular_total(compras):.2f}")


# ---------------------------------------------------------------------------
# Tópico 6: Consultas, ordenações e análises (sorted, max, min, lambda)
# ---------------------------------------------------------------------------
def item_mais_caro(compras):
    """
    Identifica o item de maior valor entre as compras registradas.

    Args:
        compras (list): lista de tuplas (produto, valor).

    Returns:
        tuple | None: a tupla (produto, valor) mais cara, ou None se
        a lista estiver vazia.
    """
    if not compras:
        return None
    return max(compras, key=lambda item: item[1])


def item_mais_barato(compras):
    """
    Identifica o item de menor valor entre as compras registradas.

    Args:
        compras (list): lista de tuplas (produto, valor).

    Returns:
        tuple | None: a tupla (produto, valor) mais barata, ou None se
        a lista estiver vazia.
    """
    if not compras:
        return None
    return min(compras, key=lambda item: item[1])


def ordenar_compras(compras, crescente=True):
    """
    Ordena as compras de acordo com o valor pago.

    Args:
        compras (list): lista de tuplas (produto, valor).
        crescente (bool): se True, ordena do menor para o maior valor;
            se False, ordena do maior para o menor.

    Returns:
        list: nova lista de tuplas ordenada (a lista original não é
        modificada).
    """
    return sorted(compras, key=lambda item: item[1], reverse=not crescente)


# ---------------------------------------------------------------------------
# Tópico 3: Menu interativo (laço while + validação de entrada)
# ---------------------------------------------------------------------------
def ler_valor(mensagem):
    """
    Solicita e valida um valor numérico digitado pelo usuário.

    Repete a solicitação enquanto o valor informado não for um número
    válido e não negativo.

    Args:
        mensagem (str): texto exibido ao solicitar o valor.

    Returns:
        float: valor numérico validado.
    """
    while True:
        entrada = input(mensagem)
        try:
            valor = float(entrada)
            if valor < 0:
                print("⚠ O valor não pode ser negativo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("⚠ Valor inválido. Digite um número (ex.: 12.50).")


def exibir_menu():
    """Exibe as opções do menu principal do AraCoins."""
    print("\n=== AraCoins - Sistema de Compras e Recompensas ===")
    print("1. Adicionar compra")
    print("2. Exibir compras e total")
    print("3. Consultar item mais caro/mais barato")
    print("4. Ordenar compras por valor")
    print("5. Sair")


def executar_opcao_adicionar(compras):
    """Executa o fluxo de adicionar uma nova compra via terminal."""
    produto = input("\nNome do produto: ").strip()
    valor = ler_valor("Valor pago: ")

    registrar_compra(compras, produto, valor)
    recompensa = calcular_recompensa(valor)
    print(f"✓ Compra registrada! Recompensa: {recompensa} ponto(s)")


def executar_opcao_analise(compras):
    """Executa o fluxo de consulta de item mais caro/mais barato."""
    if not compras:
        print("\nNenhuma compra registrada para analisar.")
        return

    caro = item_mais_caro(compras)
    barato = item_mais_barato(compras)

    print("\n=== Análise de Compras ===")
    print(f"Item mais caro:  {caro[0]} - R$ {caro[1]:.2f}")
    print(f"Item mais barato: {barato[0]} - R$ {barato[1]:.2f}")


def executar_opcao_ordenar(compras):
    """Executa o fluxo de ordenação das compras por valor."""
    if not compras:
        print("\nNenhuma compra registrada para ordenar.")
        return

    ordem = input("\nOrdenar em ordem (C)rescente ou (D)ecrescente? ").strip().lower()
    crescente = ordem != "d"

    ordenadas = ordenar_compras(compras, crescente=crescente)
    titulo = "crescente" if crescente else "decrescente"

    print(f"\n=== Compras Ordenadas ({titulo}) ===")
    for produto, valor in ordenadas:
        print(f"{produto:<18}- R$ {valor:.2f}")


def main():
    """Executa o laço principal do sistema AraCoins."""
    compras = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            executar_opcao_adicionar(compras)
        elif opcao == "2":
            print()
            exibir_compras(compras)
        elif opcao == "3":
            executar_opcao_analise(compras)
        elif opcao == "4":
            executar_opcao_ordenar(compras)
        elif opcao == "5":
            print("\nEncerrando o AraCoins. Até a próxima!")
            break
        else:
            print("\n⚠ Opção inválida. Escolha um número entre 1 e 5.")


if __name__ == "__main__":
    main()
