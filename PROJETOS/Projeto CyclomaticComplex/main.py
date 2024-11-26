import ast  # Importa o módulo AST (Abstract Syntax Tree) para análise do código
import inspect  # Importa o módulo inspect para obter o código-fonte de funções em tempo de execução
from functions import *  # Importa todas as funções do arquivo functions.py

def calculate_cyclomatic_complexity(code):
    """
    Calcula a complexidade ciclomática de um código Python.
    A complexidade ciclomática mede o número de caminhos independentes possíveis em um fluxo de controle.
    Quanto maior o valor, mais complexo o código.
    """
    # Converte o código-fonte em uma Árvore de Sintaxe Abstrata (AST)
    tree = ast.parse(code)
    
    # Imprime a representação estruturada da AST para depuração
    # print("Árvore de Sintaxe Abstrata (AST):")
    # print(ast.dump(tree, indent=4))  # O parâmetro 'indent' deixa a saída mais legível

    # Inicializa a complexidade com 1. O valor inicial representa o caminho base do programa
    complexity = 1

    # Percorre todos os nós da árvore AST
    for node in ast.walk(tree):
        # Verifica se o nó representa um ponto de bifurcação no fluxo de controle
        if isinstance(node, (ast.If, ast.For, ast.While, ast.And, ast.Or, ast.Try, ast.ExceptHandler)):
            # Cada bifurcação adiciona um novo caminho independente, então incrementamos a complexidade
            complexity += 1

        # Verifica se o nó atual é uma definição de função
        elif isinstance(node, ast.FunctionDef):
            # Verifica os valores padrão nos argumentos da função
            for arg in node.args.defaults:
                # Se houver lógica nos valores padrão, calcula a complexidade recursivamente
                complexity += calculate_cyclomatic_complexity(arg)

    # Retorna a soma da complexidade calculada
    return complexity

def measure_complexity(func):
    """
    Mede a complexidade ciclomática de uma função Python.
    """
    # Obtém o código-fonte da função como uma string
    func_code = inspect.getsource(func)

    # Passa o código-fonte da função para a calculadora de complexidade
    return calculate_cyclomatic_complexity(func_code)

# Testando o Código
if __name__ == "__main__":
    # Lista de funções para análise, organizada em ordem de complexidade
    functions = [
        get_first_element,       # O(1)
        binary_search,           # O(log n)
        linear_search,           # O(n)
        sum_list,                # O(n)
        factorial_iterative,     # O(n)
        factorial_recursive,     # O(n)
        merge_sort,              # O(n log n)
        quick_sort,              # O(n log n)
        bubble_sort,             # O(n²)
        fibonacci,               # O(2ⁿ)
    ]

    for func in functions:
        print(f"\nAnalisando a função: {func.__name__}")
        # Mede a complexidade da função
        complexity = measure_complexity(func)
        print(f"Complexidade ciclomática da função '{func.__name__}': {complexity}")
