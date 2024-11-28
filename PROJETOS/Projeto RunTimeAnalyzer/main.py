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

# Função auxiliar para medir o tempo de execução
def measure_runtime(func, size=1000):
    runtime, _ = tester.runtime(func, "random", size=size)
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
            bigOcomplex = tester.test(func, "random")
            print(f"Complexidade Big-O estimada para '{func.__name__}': {bigOcomplex}")
        except Exception as bigO_exception:
            print(f"Erro ao medir a complexidade Big-O para '{func.__name__}': {bigO_exception}")
