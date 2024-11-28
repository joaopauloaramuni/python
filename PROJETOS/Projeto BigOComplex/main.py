from bigO import BigO
from wrapper import *  # Importa os wrappers
from functions import *  # Importa os wrappers

# Inicializa o analisador de complexidade
tester = BigO()

# Lista de funções para análise, com wrappers onde necessário
functions = [
    binary_search_wrapper,      # Wrapper para O(log n)
    linear_search_wrapper,      # Wrapper para O(n)
    sum_list_wrapper,           # Wrapper para O(n)
    merge_sort,                 # O(n log n)
    quick_sort,                 # O(n log n)
    bubble_sort,                # O(n²)
]

# Função auxiliar para medir a complexidade
def measure_complexity(func):
    """
    Mede a complexidade de tempo de uma função usando o BigO Calculator.
    A função executa o teste de complexidade sobre a função fornecida com entradas aleatórias.
    
    Args:
        func (Callable): A função para a qual a complexidade de tempo será medida.
        
    Returns:
        str: A complexidade assintótica estimada (e.g., "O(n)", "O(n^2)", etc.) para a função dada.
    """
    result = tester.test(func, 'random')  # Entradas aleatórias
    return result

# Testando o Código
if __name__ == "__main__":
    for func in functions:
        print(f"\nAnalisando a função: {func.__name__}")
        # Mede a complexidade da função
        complexity = measure_complexity(func)
        print(f"Big O '{func.__name__}': {complexity}")


# pip install big-O-calculator