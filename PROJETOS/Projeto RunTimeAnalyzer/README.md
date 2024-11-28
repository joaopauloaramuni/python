# Projeto RunTimeAnalyzer

Este projeto é uma ferramenta para analisar o tempo de execução e a complexidade assintótica de algoritmos usando a biblioteca **Big O Calculator**.

## Dependências

Para rodar este projeto, você pode instalar a dependência do Big O Calculator com o seguinte comando:

```bash
pip install big-O-calculator
```

## Ambiente Virtual

### Passo 1: Criar e ativar o ambiente virtual

É recomendável usar um ambiente virtual para gerenciar suas dependências. Siga os passos abaixo para configurar um ambiente virtual:

1. Crie um ambiente virtual usando o seguinte comando:

```bash
python3 -m venv .venv
```

2. Ative o ambiente virtual:
    - No macOS e Linux:
        ```bash
        source .venv/bin/activate
        ```
    - No Windows:
        ```bash
        .venv\Scripts\activate
        ```

3. Instale a dependência do Big O Calculator:

```bash
pip install big-O-calculator
```

### Passo 2: Executar o script

Após ativar o ambiente virtual, execute o script principal:

```bash
python main.py
```

## Versão do Python

Este projeto foi desenvolvido na versão **3.13.0** do Python.

## Explicação das funções

### Arquivo: main.py

- **Objetivo:** Este arquivo principal configura e executa a análise de complexidade e tempo de execução de diferentes funções.
- **Descrição das funções:**

#### `measure_runtime(func, size=1000)`
- Mede o tempo de execução de uma função utilizando entradas aleatórias.
- **Parâmetros:**
  - `func`: Função cujo tempo de execução será medido.
  - `size`: Tamanho da entrada gerada para os testes (padrão: 1000).
- **Retorno:**
  - Tempo médio de execução da função em segundos.

#### Estrutura do arquivo
- Importa os módulos e funções necessárias: `BigO`, wrappers e funções.
- Inicializa o analisador de complexidade `BigO`.
- Define uma lista de funções que serão analisadas, algumas envolvidas por wrappers para ajuste de comportamento.
- Para cada função:
  - Mede o tempo de execução usando entradas aleatórias.
  - Mede a complexidade assintótica Big-O.
  - Exibe os resultados no terminal, incluindo tempo de execução e complexidade estimada.

---

### Arquivo: `functions.py`

- **Objetivo:** Implementa funções com diferentes classes de complexidade.

#### `binary_search(arr, target)`
- **Complexidade:** O(log n)
- Busca o índice de um elemento em uma lista ordenada, dividindo o intervalo pela metade a cada iteração.

#### `linear_search(arr, target)`
- **Complexidade:** O(n)
- Percorre a lista sequencialmente até encontrar o elemento desejado.

#### `sum_list(arr)`
- **Complexidade:** O(n)
- Percorre uma lista e soma todos os elementos.

#### `merge_sort(arr)`
- **Complexidade:** O(n log n)
- Ordena uma lista dividindo-a em sublistas e as mesclando de forma ordenada.

#### `quick_sort(arr)`
- **Complexidade:** O(n log n) no caso médio e melhor caso, O(n²) no pior caso.
- Ordena uma lista usando um pivô para dividir os elementos e realizar chamadas recursivas.

#### `bubble_sort(arr)`
- **Complexidade:** O(n²)
- Ordena uma lista comparando elementos adjacentes e trocando-os quando necessário.

---

### Arquivo: `wrapper.py`

- **Objetivo:** Adapta funções para ajustarem suas entradas e saídas ao formato necessário.

#### `binary_search_wrapper(arr)`
- Envolve a função `binary_search`.
- Busca o último elemento de uma lista e retorna o resultado em uma lista.

#### `linear_search_wrapper(arr)`
- Envolve a função `linear_search`.
- Busca o último elemento de uma lista e retorna o resultado em uma lista.

#### `sum_list_wrapper(arr)`
- Envolve a função `sum_list`.
- Soma os elementos de uma lista e encapsula o resultado em uma lista.

- **Estrutura do arquivo:**
  - Importa as funções do arquivo `functions.py`.
  - Adiciona camadas de abstração para facilitar o uso em análises automáticas.

## Saída da Execução

```
Analisando a função: binary_search_wrapper
Running binary_search_wrapper(len 1000 random array)
Took 0.00001s to sort binary_search_wrapper(random)
Tempo de execução 'binary_search_wrapper': 0.000007 segundos
Complexidade Big-O estimada para 'binary_search_wrapper': O(log(n))

Analisando a função: linear_search_wrapper
Running linear_search_wrapper(len 1000 random array)
Took 0.00003s to sort linear_search_wrapper(random)
Tempo de execução 'linear_search_wrapper': 0.000030 segundos
Complexidade Big-O estimada para 'linear_search_wrapper': O(n)

Analisando a função: sum_list_wrapper
Running sum_list_wrapper(len 1000 random array)
Took 0.00002s to sort sum_list_wrapper(random)
Tempo de execução 'sum_list_wrapper': 0.000022 segundos
Complexidade Big-O estimada para 'sum_list_wrapper': O(n)

Analisando a função: merge_sort
Running merge_sort(len 1000 random array)
Took 0.00121s to sort merge_sort(random)
Tempo de execução 'merge_sort': 0.001206 segundos
Complexidade Big-O estimada para 'merge_sort': O(nlog(n))

Analisando a função: quick_sort
Running quick_sort(len 1000 random array)
Took 0.00094s to sort quick_sort(random)
Tempo de execução 'quick_sort': 0.000941 segundos
Complexidade Big-O estimada para 'quick_sort': O(nlog(n))

Analisando a função: bubble_sort
Running bubble_sort(len 1000 random array)
Took 0.02882s to sort bubble_sort(random)
Tempo de execução 'bubble_sort': 0.028822 segundos
Complexidade Big-O estimada para 'bubble_sort': O(n^2)
```

## Documentação e links úteis

- [GitHub - BigO-calculator](https://github.com/Alfex4936/python-bigO-calculator/)
- [Built-in algorithms list - BigO-calculator](https://github.com/Alfex4936/python-bigO-calculator/blob/master/bigO/algorithm.py)
- [PyPI - BigO-calculator](https://pypi.org/project/big-O-calculator/)

## Licença

Este projeto está licenciado sob a Licença MIT.
