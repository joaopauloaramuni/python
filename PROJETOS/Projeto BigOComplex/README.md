# BigOComplex

O **BigOComplex** é um projeto desenvolvido para ajudar a entender e analisar a complexidade de algoritmos com base na notação **Big O**. Este projeto utiliza o pacote `big-O-calculator` para determinar a complexidade assintótica de funções, como busca binária, ordenação por fusão, ordenação rápida, busca linear e ordenação por bolha.

## Notação Big O

A notação **Big O** é uma maneira de descrever o desempenho ou a complexidade de um algoritmo em termos do tempo ou espaço que ele consome à medida que o tamanho da entrada aumenta. Ela é uma métrica importante para programadores e desenvolvedores, pois ajuda a determinar a eficiência de um algoritmo, o que é crucial para garantir que sistemas com grandes volumes de dados ou alta demanda de processamento continuem funcionando de forma eficiente.

A notação Big O descreve o pior cenário possível de execução de um algoritmo e não se preocupa com as variações no desempenho que podem ocorrer dependendo da implementação ou do ambiente de execução. Alguns exemplos comuns de notação Big O incluem:

- **O(1)**: Complexidade constante, o tempo de execução não depende do tamanho da entrada.
- **O(n)**: Complexidade linear, o tempo de execução aumenta proporcionalmente ao tamanho da entrada.
- **O(n^2)**: Complexidade quadrática, o tempo de execução cresce de forma quadrática em relação ao tamanho da entrada.
- **O(log n)**: Complexidade logarítmica, o tempo de execução cresce de forma logarítmica.

## Complexidade Assintótica

A **complexidade assintótica** é uma maneira de expressar o comportamento de um algoritmo quando o tamanho da entrada tende ao infinito. Ela descreve o tempo ou espaço de execução de um algoritmo em termos do tamanho da entrada, ignorando fatores como o hardware ou o tempo de execução real. A complexidade assintótica ajuda a comparar a eficiência de diferentes algoritmos de forma mais objetiva, independentemente das condições do sistema.

## Diferença entre Complexidade Assintótica e Complexidade Ciclomática

A **complexidade assintótica** refere-se ao comportamento de um algoritmo à medida que a entrada aumenta, enquanto a **complexidade ciclomática** mede a complexidade do código de um programa com base no número de caminhos lineares independentes no código. A complexidade ciclomática é útil para determinar a quantidade de testes necessários para garantir a cobertura adequada do código.

Para testar a complexidade ciclomática, você pode consultar o projeto **CyclomaticComplex** deste repositório.

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

- **Objetivo:** Este arquivo principal configura e executa a análise de complexidade de diferentes funções.
- **Descrição das funções:**

#### `measure_complexity(func)`
- Mede a complexidade assintótica de uma função utilizando entradas aleatórias.
- **Parâmetros:**
  - `func`: Função cuja complexidade será medida.
- **Retorno:**
  - Complexidade estimada (ex.: O(n), O(log n)).
  
#### Estrutura do arquivo
- Importa os módulos e funções necessárias: `BigO`, wrappers e funções.
- Inicializa o analisador de complexidade `BigO`.
- Define uma lista de funções que são analisadas, algumas envolvidas por wrappers para ajuste de comportamento.
- Analisa cada função e imprime a complexidade estimada no terminal.

---

### Arquivo: functions.py

- **Objetivo:** Implementa funções com diferentes classes de complexidade.

#### `binary_search(arr, target)`
- **Complexidade:** O(log n)
- Busca o índice de um elemento em uma lista ordenada, dividindo o intervalo pela metade a cada iteração.

#### `linear_search(arr, target)`
- **Complexidade:** O(n)
- Percorre a lista sequencialmente até encontrar o elemento desejado.

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

### Arquivo: wrapper.py

- **Objetivo:** Adapta funções para ajustarem suas entradas e saídas ao formato necessário.

#### `binary_search_wrapper(arr)`
- Envolve a função `binary_search`.
- Busca o último elemento de uma lista e retorna o resultado em uma lista.

#### `linear_search_wrapper(arr)`
- Envolve a função `linear_search`.
- Busca o último elemento de uma lista e retorna o resultado em uma lista.

- **Estrutura do arquivo:**
  - Importa as funções do arquivo `functions.py`.
  - Adiciona camadas de abstração para facilitar o uso em análises automáticas.

## Saída da Execução

### Análise da Complexidade Assintótica por Função

```
Analisando a função: `binary_search_wrapper`  
Running `binary_search_wrapper(random array)`...  
Completed `binary_search_wrapper(random array)`: O(log(n))  
Big O `binary_search_wrapper`: O(log(n))

Analisando a função: `linear_search_wrapper`  
Running `linear_search_wrapper(random array)`...  
Completed `linear_search_wrapper(random array)`: O(n)  
Big O `linear_search_wrapper`: O(n)

Analisando a função: `merge_sort`  
Running `merge_sort(random array)`...  
Completed `merge_sort(random array)`: O(nlog(n))  
Big O `merge_sort`: O(nlog(n))

Analisando a função: `quick_sort`  
Running `quick_sort(random array)`...  
Completed `quick_sort(random array)`: O(nlog(n))  
Big O `quick_sort`: O(nlog(n))

Analisando a função: `bubble_sort`  
Running `bubble_sort(random array)`...  
Completed `bubble_sort(random array)`: O(n^2)  
Big O `bubble_sort`: O(n^2)
```

## Documentação e links úteis

- [GitHub - BigO-calculator](https://github.com/Alfex4936/python-bigO-calculator/)
- [Built-in algorithms list - BigO-calculator](https://github.com/Alfex4936/python-bigO-calculator/blob/master/bigO/algorithm.py)
- [PyPI - BigO-calculator](https://pypi.org/project/big-O-calculator/)

## Licença

Este projeto está licenciado sob a Licença MIT.
