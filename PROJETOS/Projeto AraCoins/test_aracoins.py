"""
Testes do Sistema AraCoins (TDD)
==================================

Testes escritos com assert, seguindo o ciclo Red -> Green -> Refactor
do Desenvolvimento Orientado por Testes (TDD).

Cada teste descreve, de forma isolada, um comportamento esperado do
sistema antes (ou depois) de sua implementação.
"""

from aracoins import (
    calcular_recompensa,
    registrar_compra,
    calcular_total,
    item_mais_caro,
    item_mais_barato,
    ordenar_compras,
)


# ---------------------------------------------------------------------------
# Testes de registro de compras
# ---------------------------------------------------------------------------
def test_registrar_compra():
    """Testa se uma compra é corretamente adicionada à lista."""
    compras = []

    registrar_compra(compras, "Chocolate", 12.50)

    assert len(compras) == 1
    assert compras[0] == ("Chocolate", 12.50)
    print("✓ Teste de registro de compra passou")


# ---------------------------------------------------------------------------
# Testes de cálculo de recompensa (faixas de valor)
# ---------------------------------------------------------------------------
def test_calcular_recompensa_faixa_baixa():
    """Testa se compras de valor baixo (< 20) retornam 1 ponto."""
    assert calcular_recompensa(12.50) == 1
    assert calcular_recompensa(0) == 1
    print("✓ Teste de cálculo de recompensa (faixa baixa) passou")


def test_calcular_recompensa_faixa_media():
    """Testa se compras de valor médio (20 <= valor < 100) retornam 5 pontos."""
    assert calcular_recompensa(20) == 5
    assert calcular_recompensa(89.90) == 5
    print("✓ Teste de cálculo de recompensa (faixa média) passou")


def test_calcular_recompensa_faixa_alta():
    """Testa se compras de valor alto (>= 100) retornam a recompensa correta."""
    recompensa_esperada = 10

    assert calcular_recompensa(100) == recompensa_esperada
    assert calcular_recompensa(200000000) == recompensa_esperada
    print("✓ Teste de cálculo de recompensa (faixa alta) passou")


# ---------------------------------------------------------------------------
# Testes de totalização
# ---------------------------------------------------------------------------
def test_calcular_total():
    """Testa se o total gasto é calculado corretamente."""
    compras = [
        ("Chocolate", 12.50),
        ("Fone de Ouvido", 89.90),
        ("Livro", 45.00),
    ]

    assert calcular_total(compras) == 147.40
    print("✓ Teste de cálculo do total de compras passou")


# ---------------------------------------------------------------------------
# Testes de análises (item mais caro / mais barato)
# ---------------------------------------------------------------------------
def test_item_mais_caro_e_mais_barato():
    """Testa se os itens mais caro e mais barato são identificados corretamente."""
    compras = [
        ("Chocolate", 12.50),
        ("Fone de Ouvido", 89.90),
        ("Livro", 45.00),
    ]

    assert item_mais_caro(compras) == ("Fone de Ouvido", 89.90)
    assert item_mais_barato(compras) == ("Chocolate", 12.50)
    print("✓ Teste de item mais caro e mais barato passou")


# ---------------------------------------------------------------------------
# Testes de ordenação
# ---------------------------------------------------------------------------
def test_ordenar_compras():
    """Testa se a ordenação crescente e decrescente funciona corretamente."""
    compras = [
        ("Fone de Ouvido", 89.90),
        ("Chocolate", 12.50),
        ("Livro", 45.00),
    ]

    crescente = ordenar_compras(compras, crescente=True)
    decrescente = ordenar_compras(compras, crescente=False)

    assert crescente == [
        ("Chocolate", 12.50),
        ("Livro", 45.00),
        ("Fone de Ouvido", 89.90),
    ]
    assert decrescente == [
        ("Fone de Ouvido", 89.90),
        ("Livro", 45.00),
        ("Chocolate", 12.50),
    ]
    # A lista original não deve ser modificada
    assert compras[0] == ("Fone de Ouvido", 89.90)
    print("✓ Teste de ordenação por valor passou")


# ---------------------------------------------------------------------------
# Testes de cenários extremos (lista vazia)
# ---------------------------------------------------------------------------
def test_lista_vazia():
    """Testa se as funções de análise lidam corretamente com lista vazia."""
    compras = []

    assert calcular_total(compras) == 0
    assert item_mais_caro(compras) is None
    assert item_mais_barato(compras) is None
    assert ordenar_compras(compras) == []
    print("✓ Teste de lista vazia passou")


def executar_testes():
    """Executa todos os testes do sistema AraCoins em sequência."""
    print("=== Executando Testes do Sistema AraCoins ===\n")

    test_registrar_compra()
    test_calcular_recompensa_faixa_baixa()
    test_calcular_recompensa_faixa_media()
    test_calcular_recompensa_faixa_alta()
    test_calcular_total()
    test_item_mais_caro_e_mais_barato()
    test_ordenar_compras()
    test_lista_vazia()

    print("\n=== Todos os testes passaram! ===")


if __name__ == "__main__":
    executar_testes()
