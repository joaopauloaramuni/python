# Funções de Exemplo com Diferentes Complexidades

# O(1): Acesso direto ao primeiro elemento da lista, independente do tamanho
def get_first_element(arr):
    if arr:  # Verifica se a lista não está vazia
        return arr[0]  # Retorna o primeiro elemento
    return None  # Retorna None se a lista estiver vazia

# O(log n): Busca binária, reduz o intervalo de busca pela metade a cada iteração
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
def linear_search(arr, target):
    for i, val in enumerate(arr):  # Itera por todos os elementos da lista
        if val == target:
            return i  # Retorna o índice do elemento se encontrado
    return -1  # Retorna -1 se o elemento não for encontrado

# O(n): Soma todos os elementos de uma lista, percorrendo-a uma vez
def sum_list(arr):
    total = 0
    for num in arr:  # Loop simples que percorre todos os elementos
        total += num
    return total

# O(n): Calcula fatorial iterativamente
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):  # Itera de 1 até n
        result *= i  # Multiplica cada valor na sequência
    return result

# O(n): Calcula fatorial recursivamente
def factorial_recursive(n):
    if n == 0 or n == 1:  # Caso base: Fatorial de 0 ou 1 é 1
        return 1
    # Chamada recursiva reduzindo o problema
    return n * factorial_recursive(n - 1)

# O(n log n): Ordenação Merge Sort, divide o problema e o resolve recursivamente
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
def quick_sort(arr):
    if len(arr) <= 1:  # Caso base: lista de tamanho 0 ou 1
        return arr
    pivot = arr[0]  # Escolhe o primeiro elemento como pivô
    left = [x for x in arr[1:] if x <= pivot]  # Elementos menores ou iguais ao pivô
    right = [x for x in arr[1:] if x > pivot]  # Elementos maiores que o pivô
    return quick_sort(left) + [pivot] + quick_sort(right)  # Ordena recursivamente

# O(n²): Ordenação Bubble Sort, compara todos os pares de elementos
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # Laço externo: percorre a lista
        for j in range(0, n - i - 1):  # Laço interno: compara pares consecutivos
            if arr[j] > arr[j + 1]:
                # Troca os elementos se estiverem fora de ordem
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# O(2ⁿ): Calcula Fibonacci recursivamente, com muitas chamadas aninhadas
def fibonacci(n):
    if n <= 1:  # Caso base: Fibonacci(0) = 0, Fibonacci(1) = 1
        return n
    # Chamada recursiva para os dois números anteriores
    return fibonacci(n - 1) + fibonacci(n - 2)
