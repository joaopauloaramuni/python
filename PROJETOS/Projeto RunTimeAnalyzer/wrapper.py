from functions import *  # Importa todas as funções do arquivo functions.py

# Wrappers para funções específicas

def binary_search_wrapper(arr):
    """
    Envolve a função `binary_search` e ajusta o retorno para uma lista.
    """
    if not arr:  # Se a lista estiver vazia, retorna uma lista vazia
        return []
    target = arr[-1]  # Define o último elemento como o alvo de busca
    return [binary_search(arr, target)]  # Encapsula o retorno em uma lista

def linear_search_wrapper(arr):
    """
    Envolve a função `linear_search` e ajusta o retorno para uma lista.
    """
    if not arr:  # Se a lista estiver vazia, retorna uma lista vazia
        return []
    target = arr[-1]  # Define o último elemento como o alvo de busca
    return [linear_search(arr, target)]  # Encapsula o retorno em uma lista

def sum_list_wrapper(arr):
    """
    Wrapper para encapsular o retorno de `sum_list` como uma lista.
    """
    result = sum_list(arr)
    return [result] if result is not None else []