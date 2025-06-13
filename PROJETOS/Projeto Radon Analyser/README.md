# Projeto Radon Analyser

## 📋 O que é este projeto?

Este projeto é uma ferramenta simples para analisar a **complexidade ciclomatica** de códigos Python em repositórios GitHub usando a biblioteca [Radon](https://pypi.org/project/radon/).  
Ele clona um repositório, busca os arquivos `.py`, calcula a complexidade de cada função, classe ou bloco, gera um relatório no console e salva um arquivo de texto com os resultados.

---

## 🧮 O que é Radon?

[Radon](https://radon.readthedocs.io/en/latest/) é uma biblioteca Python para análise estática de código, que calcula métricas de qualidade como:  
- Complexidade ciclomática  
- Métricas brutas (LOC, comentários, etc.)  
- Métricas Halstead  
- Índice de Manutenibilidade (MI)  

## 🔁 Complexidade Ciclomática

A **complexidade ciclomática** é uma métrica que quantifica o número de caminhos de execução independentes dentro de um trecho de código.  
Na prática, ela indica quantas ramificações ou decisões existem, como `if`, `for`, `while`, `try`, etc.

⚠️ **Quanto maior o valor da complexidade ciclomática, mais complexo, difícil de entender, testar e manter é o código.**  

Essa métrica ajuda a identificar funções ou métodos que podem precisar ser simplificados para aumentar a qualidade e a manutenibilidade do software.

---

## ⚙️ Descrição das funções do script

- `clonar_repositorio(repo_url, local_path)`  
  Clona o repositório Git a partir da URL fornecida para o caminho local, usando o comando `git clone` via subprocess.

- `encontrar_arquivos_py(caminho)`  
  Busca recursivamente arquivos `.py` dentro do diretório informado, retornando a lista de caminhos completos dos arquivos encontrados.

- `analisar_arquivo(arquivo)`  
  Lê o conteúdo do arquivo Python e executa análises utilizando o Radon para obter:  
  - complexidade ciclomática (blocos)  
  - métricas brutas (LOC, comentários, linhas em branco, etc.)  
  - métricas Halstead (volume, dificuldade, esforço, bugs estimados)  
  - índice de manutenibilidade (Maintainability Index)  
  Retorna os resultados dessas análises.

- `gerar_relatorio(blocos, raw, halstead, mi, arquivo)`  
  Gera e imprime no console um relatório detalhado do arquivo analisado, incluindo a complexidade de cada função/método/classe, métricas brutas, Halstead e índice de manutenibilidade.

- `exportar_relatorio_txt(blocos, raw, halstead, mi, arquivo, arquivo_saida)`  
  Exporta o relatório de análise para um arquivo texto, no mesmo formato exibido no console, acrescentando ao arquivo existente.

- `analisar_repositorio(caminho_repositorio, caminho_saida_txt)`  
  Orquestra a análise completa do repositório: encontra todos os arquivos `.py`, analisa cada um, gera os relatórios no console e os exporta para arquivo.

- `limpar_repositorio(caminho)`  
  Remove o diretório do repositório clonado para limpeza após a análise.

- `main()`  
  Função principal que executa o fluxo completo: verifica se o arquivo de saída existe e remove, clona o repositório remoto, realiza a análise, exporta os relatórios e limpa os arquivos temporários, finalizando com mensagem.

---

## 📦 Dependências

- [Radon](https://pypi.org/project/radon/) (instale com `pip install radon`)

---

## ⚙️ Ambiente virtual

1. **Crie o ambiente virtual:**
```bash
python -m venv .venv
```

2. **Ative o ambiente virtual:**

- **Windows:**
```bash
.venv\Scripts\activate
```

- **Linux/macOS:**
```bash
source .venv/bin/activate
```

---

## 📊 Métricas disponíveis

### 🔁 Complexidade Ciclomática (Cyclomatic Complexity)

O Radon fornece a função `cc_visit` para analisar a complexidade de funções, métodos e classes.

### Exemplo de uso:

```python
from radon.complexity import cc_visit, cc_rank

code = '''
def soma(a, b):
    return a + b
'''

resultados = cc_visit(code)
for bloco in resultados:
    print(bloco.name, bloco.lineno, bloco.complexity, cc_rank(bloco.complexity))
```

### Intervalos de complexidade (`cc_rank`):

| Complexidade | Nota | Interpretação                              |
|--------------|------|--------------------------------------------|
| 1 - 5        | A    | Baixo risco (bloco simples)                |
| 6 - 10       | B    | Baixo risco (bem estruturado)              |
| 11 - 20      | C    | Risco moderado                             |
| 21 - 30      | D    | Risco mais elevado                         |
| 31 - 40      | E    | Alto risco                                 |
| 41+          | F    | Risco muito alto (propenso a erros)        |

---

### 🧮 Métricas Halstead

Permitem medir a complexidade cognitiva com base em operadores e operandos.

```python
from radon.metrics import h_visit

relatorio = h_visit(code)
print(relatorio.total.volume, relatorio.total.effort, relatorio.total.bugs)
```

| Campo     | Descrição                                             |
|-----------|-------------------------------------------------------|
| `volume`  | Volume de Halstead (tamanho informacional do código) |
| `effort`  | Esforço para compreender o código                     |
| `bugs`    | Estimativa de erros no código                         |

---

### 📉 Índice de Manutenibilidade (Maintainability Index)

Permite avaliar o quão fácil é manter um código-fonte.

```python
from radon.metrics import mi_visit, mi_rank

mi = mi_visit(code, multi=True)
print(mi, mi_rank(mi))
```

| Nota | Faixa de valor | Interpretação           |
|------|----------------|--------------------------|
| A    | > 19           | Excelente                |
| B    | 10–19          | Razoável                 |
| C    | ≤ 9            | Precisa de atenção       |

---

### 📏 Métricas brutas

Usadas para obter estatísticas gerais do código, como número de linhas, comentários e linhas em branco.

```python
from radon.raw import analyze

resultado = analyze(code)
print(resultado.loc, resultado.comments, resultado.blank)
```

| Campo     | Descrição                                |
|-----------|--------------------------------------------|
| `loc`     | Linhas totais                             |
| `lloc`    | Linhas lógicas                             |
| `sloc`    | Linhas de código (exclui comentários)      |
| `comments`| Linhas de comentário                       |
| `blank`   | Linhas em branco                           |

---

### 🧰 Ordenação dos resultados

Você pode ordenar os blocos analisados com `sorted_results`:

```python
from radon.complexity import sorted_results, SCORE, LINES, ALPHA

sorted_by_score = sorted_results(resultados, order=SCORE)
```

Valores possíveis para `order`:
- `SCORE` (padrão): por complexidade (maior para menor)
- `LINES`: por linha
- `ALPHA`: por nome (A-Z)

---

### 📦 Harvesters (Avançado)

Radon também oferece classes chamadas *Harvesters* que permitem análise em lote e exportação em JSON, XML e Code Climate.

Principais classes:
- `CCHarvester`: análise de complexidade ciclomática.
- `RawHarvester`: análise de métricas brutas.
- `MIHarvester`: análise do índice de manutenibilidade.

---

## 📊 Exemplo de saída da análise

- Arquivo: `rich/status.py`
- Repositório: "https://github.com/Textualize/rich.git"

```text
📄 Arquivo: ./repo_temp/rich/status.py
  ↳ Status (linha 11): complexidade 2 - nota A
  ↳ __init__ (linha 23): complexidade 1 - nota A
  ↳ renderable (linha 45): complexidade 1 - nota A
  ↳ console (linha 49): complexidade 1 - nota A
  ↳ update (linha 53): complexidade 5 - nota A
  ↳ start (linha 85): complexidade 1 - nota A
  ↳ stop (linha 89): complexidade 1 - nota A
  ↳ __rich__ (linha 93): complexidade 1 - nota A
  ↳ __enter__ (linha 96): complexidade 1 - nota A
  ↳ __exit__ (linha 100): complexidade 1 - nota A

  [Métricas Brutas]
    LOC: 131 | LLOC: 65 | SLOC: 94 | Comentários: 1 | Blanks: 18

  [Halstead]
    Volume: 47.55 | Dificuldade: 1.43 | Esforço: 67.93 | Bugs estimados: 0.02

  [Maintainability Index]
    MI: 69.25 - nota A
```

---

## 📁 Arquivo de saída

O relatório completo é salvo no arquivo `relatorio_radon.txt`, que estará na pasta do projeto (no seu diretório local após rodar o script).

📁 O relatório completo está disponível em:  
- [relatorio_radon.txt](./relatorio_radon.txt)

---

## 📚 Documentação e Links úteis

### 📦 Projeto

- [Página do Radon no PyPI](https://pypi.org/project/radon/)
- [Repositório oficial Radon no GitHub](https://github.com/rubik/radon)
- [Documentação oficial (Read the Docs)](https://radon.readthedocs.io/en/latest/)

### 🧠 API e Implementação

- [API Documentation (Read the Docs)](https://radon.readthedocs.io/en/latest/api.html)

#### 🔁 Complexidade Ciclomática

- [radon/complexity.py (GitHub)](https://github.com/rubik/radon/blob/master/radon/complexity.py)

#### 🧮 Métricas (Halstead, MI, etc.)

- [radon/metrics.py (GitHub)](https://github.com/rubik/radon/blob/master/radon/metrics.py)

#### 🧑‍💻 Visitantes (Visitors)

- [radon/visitors.py (GitHub)](https://github.com/rubik/radon/blob/master/radon/visitors.py)

#### 📏 Métricas Brutas

- [radon/raw.py (GitHub)](https://github.com/rubik/radon/blob/master/radon/raw.py)

---

## ⚖️ Licença

Este projeto está licenciado sob a **MIT License**.
