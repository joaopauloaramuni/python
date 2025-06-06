# 🛠️ Projeto MiniCompiler

Bem-vindo ao **MiniCompiler** — um projeto educacional simples criado para introduzir os conceitos básicos de **compiladores** para estudantes de Engenharia de Software da PUC Minas que participam das oficinas de python do DevLabs.

---

## 🎯 Objetivo do Projeto

Este mini compilador tem como objetivo **reconhecer sentenças simples de programas em uma linguagem C-like**, evoluindo em duas versões v1 e v2.

Ele realiza duas etapas fundamentais da compilação: **análise léxica** e **análise sintática**.

---

### ✅ Versão 1 – Analisador Léxico + Sintático (Declarações)

Realiza:
- **Análise léxica:** quebra o código em tokens válidos  
- **Análise sintática:** valida sentenças de **declaração de variáveis**

Tokens reconhecidos:
- Palavras-chave: `int`, `float`  
- Operadores: `=`  
- Identificadores e números  
- `;` (ponto e vírgula)

**Exemplo válido:**

```c
int x = 42;
float y = 3.14;
```

---

### ✅ Versão 2 – Analisador Léxico + Sintático (Comandos de controle)

Amplia a análise para reconhecer:
- Blocos (`{}`)  
- Comando `if` com expressão condicional  
- Comando `while` com expressão condicional

**Exemplo válido:**

```c
int x = 5;
if (x > 0) {
    float y = 3.14;
}
```

**Exemplo inválido (erro sintático – bloco não fechado):**

```c
int x = 5;
if (x > 0) {
    float y = 3.14;
```

---

### 🔍 Componentes

- **Analisador Léxico:** usa expressões regulares para extrair tokens
- **Analisador Sintático:** estrutura o código e valida regras gramaticais simples

---

### 🚧 Limitações

- Não reconhece expressões aritméticas complexas
- Não suporta funções, escopos múltiplos ou tipos compostos
- Apenas aceita `int`, `float`, `if`, `while` e blocos básicos

---

### 👨‍💻 Aplicação didática

Ideal para introduzir conceitos de compiladores como:
- Tokens, gramática e análise sintática recursiva
- Reconhecimento de erros léxicos e sintáticos
- Simulação de parsing top-down

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

  Exemplo de sentença válida (versão 1):
  ```c
  int x = 42;
  ```

  Exemplo de sentença inválida (versão 1):
  ```c
  int = x 42;
  ```

  Exemplo de sentença válida (versão 2):
  ```c
    int x = 5;
    if (x > 0) {
        float y = 3.14;
    }
  ```

    Exemplo de sentença inválida (versão 2):
  ```c
    int x = 5;
    if (x > 0) {
        float y = 3.14;
    
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

### 🔍 Passos principais — Analisador Léxico (Lexer)

1. **Definição dos padrões (`token_specification`)**

Cada token tem um nome e uma expressão regular que define seu padrão no texto. Exemplos de tokens comuns:

| Nome do Token | Expressão Regular         | Significado                                |
|---------------|---------------------------|--------------------------------------------|
| `'INT'`       | `r'int\b'`                | palavra-chave `int`                        |
| `'IF'`        | `r'if\b'`                 | palavra-chave `if`                         |
| `'ELSE'`      | `r'else\b'`               | palavra-chave `else`                       |
| `'WHILE'`     | `r'while\b'`              | palavra-chave `while`                      |
| `'RETURN'`    | `r'return\b'`             | palavra-chave `return`                     |
| `'ID'`        | `r'[a-zA-Z_]\w*'`         | identificadores (variáveis, nomes de funções etc.) |
| `'NUMBER'`    | `r'\d+(\.\d+)?'`          | números inteiros ou decimais               |
| `'ASSIGN'`    | `r'='`                    | símbolo de atribuição                      |
| `'EQ'`        | `r'=='`                   | igualdade lógica                           |
| `'NEQ'`       | `r'!='`                   | diferença lógica                           |
| `'LT'`        | `r'<'`                    | menor que                                  |
| `'GT'`        | `r'>'`                    | maior que                                  |
| `'PLUS'`      | `r'\+'`                   | adição                                     |
| `'MINUS'`     | `r'-'`                    | subtração                                  |
| `'MULT'`      | `r'\*'`                   | multiplicação                              |
| `'DIV'`       | `r'/'`                    | divisão                                    |
| `'LPAREN'`    | `r'\('`                   | parêntese esquerdo                         |
| `'RPAREN'`    | `r'\)'`                   | parêntese direito                          |
| `'LBRACE'`    | `r'\{'`                   | chave esquerda                             |
| `'RBRACE'`    | `r'\}'`                   | chave direita                              |
| `'SEMICOLON'` | `r';'`                    | ponto e vírgula                            |
| `'COMMENT'`   | `r'//.*'`                 | comentários de linha                       |
| `'SKIP'`      | `r'[ \t]+'`               | espaços e tabulações (ignorados)           |
| `'NEWLINE'`   | `r'\n'`                   | quebra de linha (ignorada)                 |
| `'MISMATCH'`  | `r'.'`                    | caractere inválido (gera erro léxico)      |

> 🧠 As palavras-chave precisam ser verificadas **antes** dos identificadores para evitar que `if` ou `while` sejam interpretados como `ID`.

---

2. **Combinação das expressões**

As expressões são unidas com o operador `|` (OU lógico), usando **grupos nomeados**:

```python
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
```

Isso cria uma expressão regular grande que reconhece qualquer tipo de token esperado.


3. **Extração dos tokens com `re.finditer`**

- Percorre o código-fonte, encontrando cada trecho que bate com algum padrão.
- Identifica o tipo de token pelo grupo nomeado (`match.lastgroup`).
- Ignora espaços, quebras de linha e lança erro para caracteres inválidos.
- Retorna uma lista de tokens (tuplas do tipo e valor).

---

**Esse processo é fundamental para converter o código fonte em uma sequência de tokens que o analisador sintático pode entender e validar.**

### 🧹 O que faz um Analisador Léxico (Lexer)?

O **analisador léxico** é a primeira etapa do compilador. Sua função é **ler o código-fonte caractere por caractere** e **quebrá-lo em tokens** — unidades básicas com significado, como palavras-chave, operadores, identificadores e números.

### v1

Por exemplo, ao ler `int x = 42;`, o lexer pode produzir os seguintes tokens:

```
('INT', 'int')
('ID', 'x')
('ASSIGN', '=')
('NUMBER', '42')
('SEMICOLON', ';')
```

Se ele encontrar um caractere inesperado, como `@`, ele emite um erro léxico.

### v2

Expande os tokens da v1 com novos tipos:

- `'IF', 'ELSE', 'WHILE'`
- `'EQ': r'=='`, `'LT': r'<'`, `'GT': r'>'`
- Parênteses e chaves: `'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE'`

---

### 🧱 O que faz um Analisador Sintático (Parser)?

O **analisador sintático** verifica se a sequência de tokens obtida do lexer **segue as regras da gramática da linguagem**.

Ou seja, ele não apenas olha os pedaços individuais do código (tokens), mas como eles estão **organizados**.

### v1

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

### v2

Suporta comandos condicionais e de repetição:

- Declarações (`int x = 42;`)
- Estruturas condicionais `if (...) { ... }`
- Laços `while (...) { ... }`
- Blocos compostos com `{ }`

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

### ✅ v1 - Sentença válida:

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

### ❌ v1 - Sentença inválida - Erro léxico (tem um @ em int@):

```
>>> Código fonte:
int@ x = 42;

>>> Análise léxica (tokens):
Erro léxico: Caractere inesperado: @
```

### ❌ v1 - Sentença inválida - Erro sintático (falta ponto e vírgula ao final da sentença):

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

### ✅ v2 - Sentença válida com if e bloco

```
>>> Código fonte:
int x = 5;
if (x > 0) {
    float y = 3.14;
}

>>> Análise léxica:
('INT', 'int') ('ID', 'x') ('ASSIGN', '=') ('NUMBER', '5') ('SEMICOLON', ';')
('IF', 'if') ('LPAREN', '(') ('ID', 'x') ('GT', '>') ('NUMBER', '0') ('RPAREN', ')')
('LBRACE', '{') ('FLOAT', 'float') ('ID', 'y') ('ASSIGN', '=') ('NUMBER', '3.14') ('SEMICOLON', ';') ('RBRACE', '}')

>>> Análise sintática:
Código válido!
```


### ❌ v2 - Sentença inválida com if e bloco

```
>>> Código fonte:
int x = 5;
if (x > 0) {
    float y = 3.14;

>>> Análise léxica (tokens):
('INT', 'int') ('ID', 'x') ('ASSIGN', '=') ('NUMBER', '5') ('SEMICOLON', ';')
('IF', 'if') ('LPAREN', '(') ('ID', 'x') ('GT', '>') ('NUMBER', '0') ('RPAREN', ')')
('LBRACE', '{') ('FLOAT', 'float') ('ID', 'y') ('ASSIGN', '=') ('NUMBER', '3.14') ('SEMICOLON', ';')

>>> Análise sintática:
Erro sintático: ("Esperado RBRACE, mas encontrei ('EOF')",)
```

---

## 📦 Dependências

Nenhuma biblioteca externa é necessária. O projeto usa apenas a biblioteca padrão `re` para expressões regulares.

---

## 🧪 Ambiente Virtual (Recomendado)

### Passo 1: Criar e ativar o ambiente virtual

É recomendado criar um ambiente virtual para isolar as dependências do projeto. Para configurar o ambiente virtual:

1. **Criar o ambiente virtual**:
   ```bash
   python -m venv venv
   ```

2. **Ativar o ambiente virtual**:
   - No Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Passo 2: Executar o script

Após ativar o ambiente virtual, execute o script principal:
```bash
python minicompiler.py
```

---

## 📚 Documentação e Links Úteis

- [Python re Module (docs)](https://docs.python.org/3/library/re.html)
- [Veja o material de compiladores do Prof. Aramuni aqui](https://github.com/joaopauloaramuni/compiladores/tree/main/PDF)
- [Livro recomendado: Compiladores - Princípios, Técnicas e Ferramentas (Dragon Book)](https://www.amazon.com.br/Compiladores-princ%C3%ADpios-ferramentas-Alfred-Aho/dp/8588639246/)

---

## 🪪 Licença

Este projeto está licenciado sob a **Licença MIT**.
