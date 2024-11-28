# Funções de Exemplo com Diferentes Complexidades

# O(log n): Busca binária, reduz o intervalo de busca pela metade a cada iteração
# Best : O(log n) Time | O(1) Space
# Average : O(log n) Time | O(1) Space
# Worst : O(log n) Time | O(1) Space
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:  # Laço principal de busca
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Caminho 1: Encontrou o elemento
        elif arr[mid] < target:
            left = mid + 1  # Caminho 2: Busca na metade direita
        else:
            right = mid - 1  # Caminho 3: Busca na metade esquerda
    return -1  # Caminho 4: Elemento não encontrado


# O(n): Busca linear, percorre a lista sequencialmente para encontrar o elemento
# Best : O(n) Time | O(1) Space
# Average : O(n) Time | O(1) Space
# Worst : O(n) Time | O(1) Space
def linear_search(arr, target):
    for i, val in enumerate(arr):  # Itera por todos os elementos da lista
        if val == target:
            return i  # Retorna o índice do elemento se encontrado
    return -1  # Retorna -1 se o elemento não for encontrado


# O(n): Soma todos os elementos de uma lista, percorrendo-a uma vez
# Best : O(n) Time | O(1) Space
# Average : O(n) Time | O(1) Space
# Worst : O(n) Time | O(1) Space
def sum_list(arr):
    total = 0
    for num in arr:  # Loop simples que percorre todos os elementos
        total += num
    return total


# O(n log n): Ordenação Merge Sort, divide o problema e o resolve recursivamente
# Best : O(n log n) Time | O(n) Space
# Average : O(n log n) Time | O(n) Space
# Worst : O(n log n) Time | O(n) Space
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)  # Divide a metade esquerda
        merge_sort(right)  # Divide a metade direita
        i = j = k = 0
        while i < len(left) and j < len(right):  # Mescla as metades
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


# O(n log n): Ordenação Quick Sort, usa um pivô para dividir e conquistar
# Best : O(n log n) Time | O(log n) Space
# Average : O(n log n) Time | O(log n) Space
# Worst : O(n²) Time | O(log n) Space
def quick_sort(arr):
    if len(arr) <= 1:  # Caso base: lista de tamanho 0 ou 1
        return arr
    pivot = arr[0]  # Escolhe o primeiro elemento como pivô
    left = [x for x in arr[1:] if x <= pivot]  # Elementos menores ou iguais ao pivô
    right = [x for x in arr[1:] if x > pivot]  # Elementos maiores que o pivô
    return quick_sort(left) + [pivot] + quick_sort(right)  # Ordena recursivamente


# O(n²): Ordenação Bubble Sort, compara todos os pares de elementos
# Best : O(n²) Time | O(1) Space
# Average : O(n²) Time | O(1) Space
# Worst : O(n²) Time | O(1) Space
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # Laço externo: percorre a lista
        for j in range(0, n - i - 1):  # Laço interno: compara pares consecutivos
            if arr[j] > arr[j + 1]:
                # Troca os elementos se estiverem fora de ordem
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Outras funções de sort:
# https://github.com/Alfex4936/python-bigO-calculator/blob/master/bigO/algorithm.py