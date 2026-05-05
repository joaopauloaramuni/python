"""
Testes unitários para a classe Filme usando TDD.
"""

from filme import Filme


def test_criacao_filme():
    """Testa se um filme é criado corretamente com os atributos esperados."""
    filme = Filme("Matrix", 63000000, 465000000, "Ficção")
    
    assert filme.titulo == "Matrix"
    assert filme.orcamento == 63000000
    assert filme.receita == 465000000
    assert filme.genero == "Ficção"
    print("✓ Teste de criação de filme passou")


def test_valores_numericos():
    """Testa se a validação de valores numéricos funciona corretamente."""
    filme_valido = Filme("Avatar", 237000000, 2847000000, "Ficção")
    filme_invalido = Filme("Teste", "texto", 1000000, "Drama")
    
    assert filme_valido.valores_sao_numericos() == True
    assert filme_invalido.valores_sao_numericos() == False
    print("✓ Teste de valores numéricos passou")


def test_calculo_lucro():
    """Testa se o cálculo de lucro está correto."""
    filme = Filme("Titanic", 200000000, 2200000000, "Drama")
    lucro_esperado = 2000000000
    
    assert filme.lucro() == lucro_esperado
    print("✓ Teste de cálculo de lucro passou")


def test_representacao_string():
    """Testa a representação em string do filme."""
    filme = Filme("Joker", 55000000, 1074000000, "Drama")
    
    assert str(filme) == "Joker (Drama)"
    print("✓ Teste de representação string passou")


def test_filme_sem_genero():
    """Testa criação de filme sem gênero especificado."""
    filme = Filme("Filme Teste", 1000000, 5000000)
    
    assert filme.titulo == "Filme Teste"
    assert filme.genero is None
    assert str(filme) == "Filme Teste (None)"
    print("✓ Teste de filme sem gênero passou")


def executar_todos_testes():
    """Executa todos os testes definidos."""
    print("\n=== Executando Testes da Classe Filme ===\n")
    
    test_criacao_filme()
    test_valores_numericos()
    test_calculo_lucro()
    test_representacao_string()
    test_filme_sem_genero()
    
    print("\n=== Todos os testes passaram! ===\n")


if __name__ == "__main__":
    executar_todos_testes()