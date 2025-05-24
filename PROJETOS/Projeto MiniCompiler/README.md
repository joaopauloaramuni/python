# 🛠️ Projeto MiniCompiler

Bem-vindo ao **MiniCompiler** — um projeto educacional simples criado para introduzir os conceitos básicos de **compiladores** para estudantes de Engenharia de Software da PUC Minas que participam das oficinas de python do DevLabs.

---

## 🎯 Objetivo do Projeto

Este mini compilador tem como objetivo **reconhecer sentenças simples de declaração de variáveis**, como por exemplo:

```c
int x = 42;
float y = 3.14;
```

Ele realiza duas etapas fundamentais da compilação: **análise léxica** e **análise sintática**.

---

## 🧠 Introdução aos conceitos

### 🧵 O que é um compilador?

Um **compilador** é um programa que traduz código-fonte escrito em uma linguagem de programação de alto nível (como C, Java, Python) para uma linguagem de mais baixo nível (como código de máquina ou bytecode).

Esse processo de tradução é realizado em várias etapas chamadas **fases da compilação**, e o objetivo é permitir que o computador entenda e execute o que foi escrito pelo programador.

Além da tradução, um compilador pode detectar erros, realizar otimizações e gerar alertas sobre boas práticas. Ele é composto por vários módulos internos, como analisadores léxicos, sintáticos e semânticos.

---

# Conceitos básicos de Linguagens e Expressões Regulares

## 🗣️ O que é uma linguagem, uma gramática e uma sentença?

- **Linguagem de programação**: É um conjunto de regras sintáticas e semânticas que definem como escrever programas. Exemplo: Python, C, Java.

- **Gramática formal**: São regras matemáticas que definem todas as sentenças válidas de uma linguagem. Uma gramática pode ser descrita como um conjunto de produções, que descrevem como formar frases válidas.

  Exemplo de produção simplificada para declaração de variável:
  ```
  DECLARACAO → TIPO ID = NUMERO ;
  ```

- **Sentença**: É uma sequência específica de símbolos da linguagem. Uma sentença pode estar ou não correta segundo a gramática.

  Exemplo de sentença válida:
  ```c
  int x = 42;
  ```

  Exemplo de sentença inválida:
  ```c
  int = x 42;
  ```

## 🗣️ O que é uma expressão regular?

- **Expressão regular**: Uma expressão regular (ou regex, de regular expression) é uma forma compacta de descrever padrões de texto. Ela permite que você procure, valide ou extraia partes de uma string com base em regras específicas.

  Exemplo para uma máscara de telefone: Suponha que você queira verificar se uma string contém um número de telefone no formato (99) 9999-9999.

  ```python
  import re
  
  texto = "Meu telefone é (11) 1234-5678"
  padrao = r"\(\d{2}\) \d{4}-\d{4}"
  resultado = re.search(padrao, texto)
  
  if resultado:
    print("Número encontrado:", resultado.group())
  ```

  Aqui, o padrão `\(\d{2}\) \d{4}-\d{4}` quer dizer:
  
  - `\(` e `\)` — o parêntese literal;
  - `\d{2}` — dois dígitos (para o DDD);
  - espaço;
  - `\d{4}` — quatro dígitos;
  - `-`;
  - `\d{4}` — mais quatro dígitos.

## ⚙️ Como funciona o módulo `re` no Python?

A biblioteca `re` fornece funções para usar expressões regulares, como:

- `re.search(padrao, texto)` — procura o padrão em qualquer parte da string;
- `re.match(padrao, texto)` — verifica se o padrão aparece no início da string;
- `re.findall(padrao, texto)` — retorna todas as ocorrências que combinam com o padrão;
- `re.sub(padrao, substituto, texto)` — substitui partes do texto que combinam com o padrão;
- `re.compile(padrao)` — compila o padrão para uso repetido, melhorando performance.

---

## Uso do `re` no analisador léxico deste projeto

No código do analisador léxico, o `re` **transforma a string do código-fonte em tokens** (unidades léxicas). Ele é essencial para reconhecer padrões no texto do código-fonte e transformá-lo em tokens que o parser vai processar.

### Passos principais:

1. **Definição dos padrões (`token_specification`)**

Cada token tem um nome e uma expressão regular que define seu padrão no texto, por exemplo:

- `'INT'`: `r'int\b'` — palavra-chave `int`
- `'ID'`: `r'[a-zA-Z_]\w*'` — identificadores
- `'NUMBER'`: `r'\d+(\.\d+)?'` — números inteiros ou decimais
- `'SKIP'`: `r'[ \t]+'` — espaços e tabulações (ignorados)
- `'MISMATCH'`: `r'.'` — caractere inválido (gera erro)

2. **Combinação das expressões**

- Usando `|` (OU lógico), todas as regex são unidas em uma só com grupos nomeados:

```python
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
```

3. **Extração dos tokens com `re.finditer`**

- Percorre o código-fonte, encontrando cada trecho que bate com algum padrão.
- Identifica o tipo de token pelo grupo nomeado (`match.lastgroup`).
- Ignora espaços, quebras de linha e lança erro para caracteres inválidos.
- Retorna uma lista de tokens (tuplas do tipo e valor).

---

**Esse processo é fundamental para converter o código fonte em uma sequência de tokens que o analisador sintático pode entender e validar.**

### 🧹 O que faz um Analisador Léxico (Lexer)?

O **analisador léxico** é a primeira etapa do compilador. Sua função é **ler o código-fonte caractere por caractere** e **quebrá-lo em tokens** — unidades básicas com significado, como palavras-chave, operadores, identificadores e números.

Por exemplo, ao ler `int x = 42;`, o lexer pode produzir os seguintes tokens:

```
('INT', 'int')
('ID', 'x')
('ASSIGN', '=')
('NUMBER', '42')
('SEMICOLON', ';')
```

Se ele encontrar um caractere inesperado, como `@`, ele emite um erro léxico.

---

### 🧱 O que faz um Analisador Sintático (Parser)?

O **analisador sintático** verifica se a sequência de tokens obtida do lexer **segue as regras da gramática da linguagem**.

Ou seja, ele não apenas olha os pedaços individuais do código (tokens), mas como eles estão **organizados**.

Por exemplo, ele reconhece que:

```c
int x = 42;
```

é uma **declaração válida**, pois segue a estrutura:

```
TIPO ID = NUMERO ;
```

Mas:

```c
int x 42;
```

é uma **declaração inválida**, pois está faltando o sinal de igual (`=`) e o ponto e vírgula (`;`).

---

### 🎓 E o Analisador Semântico?

O **analisador semântico** (não implementado neste projeto) é uma etapa posterior à análise sintática. Ele verifica **se a sentença faz sentido no contexto da linguagem**.

Exemplos do que o analisador semântico faria:

- Verificar se uma variável foi usada sem ter sido declarada.
- Verificar se há tentativa de atribuir um número `float` a uma variável `int` sem conversão.
- Verificar se tipos de variáveis são compatíveis em expressões.

Enquanto o lexer e o parser verificam a forma (estrutura e sintaxe), o analisador semântico verifica o **significado**.

---

## 💻 Saída no Terminal

### ✅ Sentença válida:

```
>>> Código fonte:
int x = 42;

>>> Análise léxica (tokens):
('INT', 'int')
('ID', 'x')
('ASSIGN', '=')
('NUMBER', '42')
('SEMICOLON', ';')

>>> Análise sintática:
Declaração válida!
```

### ❌ Sentença inválida - Erro léxico (tem um @ em int@):

```
>>> Código fonte:
int@ x = 42;

>>> Análise léxica (tokens):
Erro léxico: Caractere inesperado: @
```

### ❌ Sentença inválida - Erro sintático (falta ponto e vírgula ao final da sentença):

```
>>> Código fonte:
int x = 42

>>> Análise léxica (tokens):
('INT', 'int')
('ID', 'x')
('ASSIGN', '=')
('NUMBER', '42')

>>> Análise sintática:
Erro sintático: Esperado SEMICOLON, mas encontrei EOF
```

---

## 📦 Dependências

Nenhuma biblioteca externa é necessária. O projeto usa apenas a biblioteca padrão `re` para expressões regulares.

---

## 🧪 Ambiente Virtual (Recomendado)

É recomendável usar um ambiente virtual para isolar seu ambiente de desenvolvimento.

1. Crie um ambiente virtual:
```bash
python3 -m venv .venv
```

2. Ative o ambiente virtual:
- macOS e Linux:
```bash
source .venv/bin/activate
```
- Windows:
```bash
.venv\Scripts\activate
```

---

## 📚 Documentação e Links Úteis

- [Python re Module (docs)](https://docs.python.org/3/library/re.html)
- [Veja o material de compiladores do Prof. Aramuni aqui](https://github.com/joaopauloaramuni/compiladores/tree/main/PDF)
- [Livro recomendado: Compiladores - Princípios, Técnicas e Ferramentas (Dragon Book)](https://www.amazon.com.br/Compiladores-princ%C3%ADpios-ferramentas-Alfred-Aho/dp/8588639246/)

---

## 🪪 Licença

Este projeto está licenciado sob a **Licença MIT**.
