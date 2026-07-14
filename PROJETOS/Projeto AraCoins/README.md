# 💰 AraCoins - Sistema de Compras e Recompensas

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green)

**AraCoins** é um sistema educacional interativo de registro de compras e cálculo de recompensas simbólicas desenvolvido em Python. O projeto demonstra conceitos fundamentais de programação, como estruturas condicionais, laços de repetição, listas, tuplas e desenvolvimento orientado por testes (TDD), aplicados a um cenário real de controle de gastos e recompensas.

## 📋 Sobre o Projeto

O AraCoins permite:

- ✅ Registrar múltiplas compras de forma contínua, informando produto e valor pago
- 🎯 Calcular recompensas simbólicas automaticamente, com base em regras de negócio
- 📃 Exibir todas as compras registradas e calcular o total gasto
- 🖥️ Navegar por um menu interativo, com validação de entradas
- 📊 Consultar o item mais caro, o mais barato e ordenar as compras por valor
- 🧪 Aplicar desenvolvimento orientado por testes (TDD)

### Objetivos Educacionais

Este projeto foi desenvolvido para ensinar:

1. **Pensamento orientado por testes (TDD)**, escrevendo comportamentos esperados antes da implementação
2. **Estruturas condicionais** (`if`, `elif`, `else`) para representar regras de negócio
3. **Laços de repetição** (`while` e `for`) para criar fluxos interativos e percorrer coleções
4. **Estruturas de dados** com listas e tuplas para armazenar registros compostos
5. **Consultas e ordenações** com `sorted()`, `max()`, `min()` e `lambda`

## 🚀 Funcionalidades

### 1. Registro de Compras

- Cadastro contínuo de produtos e valores em uma lista de tuplas
- Uso de `.append()` para inserir novos registros
- Validação de entradas numéricas

### 2. Cálculo de Recompensas

- Regras de recompensa baseadas em faixas de valor
- Estruturas condicionais encadeadas (`if`, `elif`, `else`)
- Comparações com operadores relacionais (`>`, `<`, `>=`, `==`)

### 3. Exibição e Totalização

- Iteração com `for` sobre a lista de compras
- Exibição formatada de cada item (produto e valor)
- Soma acumulada para cálculo do total gasto

### 4. Menu Interativo

- Laço `while` controlando o fluxo principal do programa
- Opções para adicionar compras, consultar dados ou encerrar (sentinela)
- Validação de opções inválidas no menu

### 5. Consultas e Análises Avançadas

- Identificação do item mais caro e do mais barato com `max()` e `min()`
- Ordenação crescente e decrescente das compras com `sorted()` e `lambda`
- Tratamento de cenários como lista vazia ou valores repetidos

## 📦 Dependências

O AraCoins utiliza apenas a **biblioteca padrão do Python**, não sendo necessária a instalação de pacotes externos:

```
Python >= 3.8
```

## 🔧 Instalação

### Pré-requisitos

- Python 3.8 ou superior

### Passo 1: Clone o repositório

```bash
git clone https://github.com/seu-usuario/aracoins.git
cd aracoins
```

### Passo 2 (opcional): Crie um ambiente virtual

#### Windows

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
venv\Scripts\activate
```

#### Linux / macOS

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate
```

Como o projeto não depende de bibliotecas externas, este passo é opcional, mas recomendado para manter o ambiente organizado.

## 💻 Como Usar

### Executar Testes

```bash
python test_aracoins.py
```

Saída esperada:

```
=== Executando Testes do Sistema AraCoins ===

✓ Teste de registro de compra passou
✓ Teste de cálculo de recompensa (faixa baixa) passou
✓ Teste de cálculo de recompensa (faixa média) passou
✓ Teste de cálculo de recompensa (faixa alta) passou
✓ Teste de cálculo do total de compras passou
✓ Teste de item mais caro e mais barato passou
✓ Teste de ordenação por valor passou
✓ Teste de lista vazia passou

=== Todos os testes passaram! ===
```

### Executar o Sistema

```bash
python aracoins.py
```

Isso irá:

1. Exibir o menu interativo no terminal
2. Permitir o registro contínuo de compras
3. Calcular a recompensa simbólica de cada compra
4. Exibir todas as compras e o total gasto
5. Disponibilizar consultas de item mais caro, mais barato e ordenações

### Exemplo de Uso Programático

```python
from aracoins import calcular_recompensa, calcular_total, item_mais_caro, item_mais_barato

# Registrar compras (lista de tuplas: produto, valor)
compras = [
    ("Chocolate", 12.50),
    ("Fone de Ouvido", 89.90),
    ("Livro", 45.00)
]

# Calcular recompensa de uma compra
recompensa = calcular_recompensa(89.90)
print(f"Recompensa: {recompensa} pontos")

# Calcular total gasto
total = calcular_total(compras)
print(f"Total gasto: R$ {total:.2f}")

# Identificar extremos
mais_caro = item_mais_caro(compras)
mais_barato = item_mais_barato(compras)
print(f"Mais caro: {mais_caro[0]} - R$ {mais_caro[1]:.2f}")
print(f"Mais barato: {mais_barato[0]} - R$ {mais_barato[1]:.2f}")
```

## 📁 Estrutura do Projeto

```
aracoins/
│
├── aracoins.py           # Sistema principal (menu, registro, recompensas, análises)
├── test_aracoins.py      # Testes unitários (TDD)
├── README.md             # Este arquivo
└── LICENSE               # Licença MIT
```

## 📊 Exemplo de Saída

### Menu Interativo

```
=== AraCoins - Sistema de Compras e Recompensas ===
1. Adicionar compra
2. Exibir compras e total
3. Consultar item mais caro/mais barato
4. Ordenar compras por valor
5. Sair
Escolha uma opção: 1

Nome do produto: Chocolate
Valor pago: 12.50
✓ Compra registrada! Recompensa: 1 ponto(s)
```

### Compras Registradas e Total

```
=== Compras Registradas ===
Chocolate         - R$ 12.50
Fone de Ouvido    - R$ 89.90
Livro             - R$ 45.00

Total gasto: R$ 147.40
```

### Consultas e Ordenação

```
=== Análise de Compras ===
Item mais caro:  Fone de Ouvido - R$ 89.90
Item mais barato: Chocolate - R$ 12.50

=== Compras Ordenadas (crescente) ===
Chocolate         - R$ 12.50
Livro             - R$ 45.00
Fone de Ouvido    - R$ 89.90
```

## 🧪 Desenvolvimento Orientado por Testes (TDD)

O projeto segue princípios de TDD:

1. **Red**: Escrever teste que falha
2. **Green**: Implementar código mínimo para passar
3. **Refactor**: Melhorar o código mantendo testes passando

Exemplo de teste:

```python
def test_calcular_recompensa_faixa_alta():
    """Testa se compras de valor alto retornam a recompensa correta."""
    recompensa_esperada = 10

    assert calcular_recompensa(100) == recompensa_esperada
    print("✓ Teste de cálculo de recompensa (faixa alta) passou")
```

## 📚 Conceitos Abordados

### Desenvolvimento Orientado por Testes (TDD)

- Ciclo Red → Green → Refactor
- Uso do `assert` como ferramenta de raciocínio
- Testes como documentação do comportamento esperado

### Estruturas Condicionais

- `if`, `elif`, `else` para regras de recompensa
- Operadores relacionais (`>`, `<`, `>=`, `==`)
- Decisões encadeadas para múltiplos cenários

### Laços de Repetição

- `while` para o menu principal e controle por sentinela
- `for` para iteração sobre a lista de compras
- Validação de entradas do usuário

### Estruturas de Dados

- Tuplas para representar pares (produto, valor)
- Listas para armazenar coleções dinâmicas de compras
- Indexação (`item[0]`, `item[1]`) para acessar informações

### Consultas e Análises

- `sorted()` com `key` e `lambda` para ordenação
- `max()` e `min()` para identificar extremos
- Tratamento de listas vazias e valores repetidos

## 🔗 Links Úteis

### Documentação Oficial

- [Python](https://docs.python.org/3/) - Documentação oficial do Python
- [Estruturas de Controle de Fluxo](https://docs.python.org/3/tutorial/controlflow.html) - Documentação sobre `if`, `while` e `for`
- [Tipos de Dados Integrados](https://docs.python.org/3/library/stdtypes.html) - Listas, tuplas e outras estruturas
- [Funções Built-in](https://docs.python.org/3/library/functions.html) - `sorted()`, `max()`, `min()` e outras

### Tutoriais Recomendados

- [Real Python](https://realpython.com/) - Tutoriais Python de qualidade
- [Test-Driven Development with Python](https://www.obeythetestinggoat.com/) - Livro sobre TDD com Python
- [Python Sorting HOW TO](https://docs.python.org/3/howto/sorting.html) - Guia oficial sobre ordenação

### Comunidades

- [Stack Overflow](https://stackoverflow.com/questions/tagged/python) - Perguntas e respostas
- [Python Brasil](https://python.org.br/) - Comunidade brasileira
- [r/learnpython](https://www.reddit.com/r/learnpython/) - Subreddit para iniciantes

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

### Diretrizes

- Mantenha o código simples e educacional
- Adicione testes para novas funcionalidades
- Documente o código adequadamente
- Siga a PEP 8 para estilo de código

## 📝 Licença

Este projeto está licenciado sob a Licença MIT.
