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

## 🧠 Introdução aos Conceitos

### 🧵 O que é um compilador?

Um **compilador** é um programa que traduz código-fonte escrito em uma linguagem de programação de alto nível (como C, Java, Python) para uma linguagem de mais baixo nível (como código de máquina ou bytecode).

Esse processo de tradução é realizado em várias etapas chamadas **fases da compilação**, e o objetivo é permitir que o computador entenda e execute o que foi escrito pelo programador.

Além da tradução, um compilador pode detectar erros, realizar otimizações e gerar alertas sobre boas práticas. Ele é composto por vários módulos internos, como analisadores léxicos, sintáticos e semânticos.

---

### 🗣️ O que é uma linguagem, uma gramática e uma sentença?

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

---

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

### ❌ Sentença inválida - Erro léxico:

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

Nenhuma biblioteca externa é necessária. O projeto usa apenas a biblioteca padrão `re` (expressões regulares).

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

- [Wikipedia: Compiler](https://en.wikipedia.org/wiki/Compiler)
- [Python re Module (docs)](https://docs.python.org/3/library/re.html)
- [Livro recomendado: Compiladores - Princípios, Técnicas e Ferramentas (Dragon Book)](https://pt.wikipedia.org/wiki/Compiladores:_Princ%C3%ADpios,_T%C3%A9cnicas_e_Ferramentas)

---

## 🪪 Licença

Este projeto está licenciado sob a **Licença MIT**.
