# Projeto CyclomaticComplex

## Sobre o Projeto

O **CyclomaticComplex** é um projeto educativo desenvolvido para analisar a complexidade ciclomática de funções Python e explorar a relação entre a complexidade ciclomática e a notação Big-O. Este projeto utiliza a biblioteca padrão do Python, garantindo que seja simples de rodar e entender, mesmo em ambientes isolados.

## O que é Complexidade Ciclomática?

A complexidade ciclomática é uma métrica usada para medir a complexidade do fluxo de controle de um programa. Ela calcula o número de caminhos independentes no código, considerando estruturas como loops (`for`, `while`) e condicionais (`if`, `try/except`). Quanto maior o valor, mais complexo é o código.

**Fórmula:**  
\(
M = E - N + 2P
\)  

Onde:  
- \(M\): Complexidade Ciclomática  
- \(E\): Número de arestas (transições) no grafo do controle de fluxo  
- \(N\): Número de nós (blocos de código)  
- \(P\): Componentes conectados (geralmente 1 para programas simples)  

## O que é a notação Big-O?

A notação Big-O mede como o tempo de execução ou o uso de memória de um algoritmo cresce em relação ao tamanho da entrada. Ela ajuda a prever a escalabilidade do código.

**Diferença para a complexidade ciclomática:**  
- **Big-O:** Foca no tempo e espaço (eficiência).  
- **Complexidade Ciclomática:** Foca no número de caminhos possíveis (fluxo de controle).  

Ambas são importantes para entender a qualidade e a eficiência do código.

## Sobre as bibliotecas utilizadas

### `ast`  
O módulo **`ast`** permite analisar e manipular o código Python em forma de Árvore de Sintaxe Abstrata (AST). Ele é usado neste projeto para identificar estruturas como loops e condicionais.

### `inspect`  
A biblioteca **`inspect`** permite acessar detalhes do código em tempo de execução. Aqui, é usada para obter o código-fonte das funções para análise.

### AST e sua importância no desenvolvimento  
O AST permite que desenvolvedores criem ferramentas de análise estática de código, linters e otimizadores. Ele é uma representação intermediária poderosa para entender o funcionamento interno do código.

## Por que analisar a complexidade ciclomática?  
Analisar a complexidade ciclomática ajuda a identificar:
- Código propenso a erros devido à alta complexidade.
- Funções que precisam de mais testes para garantir cobertura total.
- Áreas do código que podem ser refatoradas.

## Ambiente virtual

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

### Passo 2: Executar o script

Após ativar o ambiente virtual, execute o script principal:
```bash
python main.py
```

## Versão do Python

Este projeto foi desenvolvido na versão **3.13.0** do Python e **não exige a instalação de nenhuma dependência adicional**.

## Explicação das funções

### Arquivo `main.py`

- **`calculate_cyclomatic_complexity(code)`**  
    Calcula a complexidade ciclomática de um código Python. Percorre a AST para identificar bifurcações no fluxo de controle.

- **`measure_complexity(func)`**  
    Mede a complexidade ciclomática de uma função específica.

### Arquivo `functions.py`

Este arquivo contém exemplos de funções com diferentes complexidades:

1. **`get_first_element`** (O(1)): Retorna o primeiro elemento de uma lista.  
2. **`binary_search`** (O(log n)): Realiza busca binária em uma lista ordenada.  
3. **`linear_search`** (O(n)): Percorre a lista para encontrar um elemento.  
4. **`sum_list`** (O(n)): Soma os elementos de uma lista.  
5. **`factorial_iterative`** (O(n)): Calcula o fatorial de forma iterativa.  
6. **`factorial_recursive`** (O(n)): Calcula o fatorial de forma recursiva.  
7. **`merge_sort`** (O(n log n)): Ordena uma lista utilizando Merge Sort.  
8. **`quick_sort`** (O(n log n)): Ordena uma lista utilizando Quick Sort.  
9. **`bubble_sort`** (O(n²)): Ordena uma lista utilizando Bubble Sort.  
10. **`fibonacci`** (O(2ⁿ)): Calcula o n-ésimo número de Fibonacci recursivamente.

## Saída da Execução

### Análise da Complexidade Ciclomática por Função

- **Função:** `get_first_element`  
  **Complexidade Ciclomática:** 2  

- **Função:** `binary_search`  
  **Complexidade Ciclomática:** 4  

- **Função:** `linear_search`  
  **Complexidade Ciclomática:** 3  

- **Função:** `sum_list`  
  **Complexidade Ciclomática:** 2  

- **Função:** `factorial_iterative`  
  **Complexidade Ciclomática:** 2  

- **Função:** `factorial_recursive`  
  **Complexidade Ciclomática:** 3  

- **Função:** `merge_sort`  
  **Complexidade Ciclomática:** 7  

- **Função:** `quick_sort`  
  **Complexidade Ciclomática:** 2  

- **Função:** `bubble_sort`  
  **Complexidade Ciclomática:** 4  

- **Função:** `fibonacci`  
  **Complexidade Ciclomática:** 2  

## Licença

Este projeto está licenciado sob a Licença MIT.
