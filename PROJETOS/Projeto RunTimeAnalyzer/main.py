import sys
from bigO import BigO
from wrapper import *  # Importa os wrappers
from functions import *  # Importa as funções originais

# Inicializa o analisador de complexidade
tester = BigO()

# Lista de funções para análise
functions = [
    binary_search_wrapper,           # Wrapper para O(log n)
    linear_search_wrapper,           # Wrapper para O(n)
    sum_list_wrapper,                # Wrapper para O(n)
    merge_sort,                      # O(n log n)
    quick_sort,                      # O(n log n)
    bubble_sort,                     # O(n²)
]

# Ajusta o limite de recursão para o Quick Sort
sys.setrecursionlimit(2000)

# Função auxiliar para medir a complexidade
def measure_complexity(func):
    """
    Mede a complexidade de tempo de uma função usando o BigO Calculator.
    A função executa o teste de complexidade sobre a função fornecida com entradas aleatórias.
    
    Args:
        func (Callable): A função cuja complexidade será medida.
        
    Returns:
        str: A complexidade assintótica estimada (e.g., "O(n)", "O(log n)", "O(n^2)") para a função fornecida.
    """
    result = tester.test(func, 'random')  # Gera entradas aleatórias e mede a complexidade
    return result

# Função auxiliar para medir o tempo de execução
def measure_runtime(func, size=1000):
    """
    Mede o tempo de execução de uma função usando o BigO Calculator.
    Executa a função fornecida com uma entrada de tamanho especificado e retorna o tempo médio de execução.

    Args:
        func (Callable): A função cujo tempo de execução será medido.
        size (int): O tamanho da entrada aleatória gerada para os testes (padrão: 1000).

    Returns:
        float: O tempo médio de execução da função em segundos.
    """
    runtime, _ = tester.runtime(func, "random", size=size)  # Gera entrada aleatória e mede o tempo
    return runtime

# Testando o Código
if __name__ == "__main__":
    for func in functions:
        print(f"\nAnalisando a função: {func.__name__}")
        
        # Mede o tempo de execução da função
        try:
            runtime = measure_runtime(func, size=1000)
            print(f"Tempo de execução '{func.__name__}': {runtime:.6f} segundos")
        except Exception as runtime_exception:
            print(f"Erro ao medir tempo de execução para '{func.__name__}': {runtime_exception}")
        
        # Mede a complexidade Big-O da função
        try:
            # Mede a complexidade da função
            complexity = measure_complexity(func)
            print(f"Complexidade Big-O estimada para '{func.__name__}': {complexity}")
        except Exception as bigO_exception:
            print(f"Erro ao medir a complexidade Big-O para '{func.__name__}': {bigO_exception}")
