# 🎬 AraMovies - Sistema de Análise Cinematográfica

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green)

**AraMovies** é um sistema educacional de análise e predição de dados cinematográficos desenvolvido em Python. O projeto demonstra conceitos fundamentais de programação orientada a objetos, estruturas de dados, visualização e aprendizado de máquina aplicados ao contexto da indústria cinematográfica.

## 📋 Sobre o Projeto

O AraMovies permite:

- ✅ Organizar dados de filmes usando programação orientada a objetos
- 📊 Analisar padrões de sucesso financeiro no cinema
- 📈 Visualizar relações entre orçamento, receita e gênero
- 🤖 Prever receitas usando regressão linear simples
- 🧪 Aplicar desenvolvimento orientado por testes (TDD)

### Objetivos Educacionais

Este projeto foi desenvolvido para ensinar:

1. **Estruturação de dados** com classes e objetos
2. **Organização** com listas, dicionários e conjuntos
3. **Visualização de dados** com matplotlib e seaborn
4. **Predição** com modelos de regressão linear
5. **Boas práticas** como TDD e documentação de código

## 🚀 Funcionalidades

### 1. Classe Filme
Representação estruturada de filmes com:
- Título, orçamento, receita e gênero
- Validação de dados numéricos
- Cálculo automático de lucro

### 2. Análise de Dados
- Agrupamento de filmes por gênero
- Cálculo de estatísticas (lucro médio, totais)
- Identificação de gêneros únicos

### 3. Visualizações Gráficas
- Gráfico de dispersão: Orçamento x Receita
- Análise por gênero
- Distribuição de frequências
- Gráfico de resíduos

### 4. Modelo Preditivo
- Regressão linear para prever receita
- Divisão treino/teste
- Métricas de avaliação (R², coeficientes)
- Análise de erros

## 📦 Dependências

O projeto utiliza as seguintes bibliotecas Python:

```
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=1.0.0
```

## 🔧 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo 1: Clone o repositório

```bash
git clone https://github.com/seu-usuario/aramovies.git
cd aramovies
```

### Passo 2: Crie um ambiente virtual

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

### Passo 3: Instale as dependências

```bash
pip install -r requirements.txt
```

## 💻 Como Usar

### Executar Testes

```bash
python test_filmes.py
```

Saída esperada:
```
=== Executando Testes da Classe Filme ===

✓ Teste de criação de filme passou
✓ Teste de valores numéricos passou
✓ Teste de cálculo de lucro passou
✓ Teste de representação string passou
✓ Teste de filme sem gênero passou

=== Todos os testes passaram! ===
```

### Executar Análise Completa

```bash
python main.py
```

Isso irá:
1. Carregar dados de exemplo
2. Exibir estatísticas básicas
3. Treinar modelo de regressão linear
4. Gerar predições
5. Criar visualizações gráficas

### Exemplo de Uso Programático

```python
from filme import Filme
from main import calcular_lucro_medio, agrupar_por_genero

# Criar filmes
filmes = [
    Filme("Matrix", 63000000, 465000000, "Ficção"),
    Filme("Titanic", 200000000, 2200000000, "Drama")
]

# Calcular lucro médio
lucro_medio = calcular_lucro_medio(filmes)
print(f"Lucro médio: R$ {lucro_medio:,.2f}")

# Agrupar por gênero
grupos = agrupar_por_genero(filmes)
for genero, lista in grupos.items():
    print(f"{genero}: {len(lista)} filme(s)")
```

## 📁 Estrutura do Projeto

```
aramovies/
│
├── filme.py              # Classe Filme (modelo de dados)
├── main.py               # Pipeline principal de análise
├── test_filmes.py        # Testes unitários (TDD)
├── requirements.txt      # Dependências do projeto
├── README.md            # Este arquivo
└── LICENSE              # Licença MIT
```

## 📊 Exemplo de Saída

### Estatísticas Básicas
```
=== Estatísticas Básicas ===
Total de filmes: 5
Gêneros únicos: {'Ficção', 'Drama'}
Lucro médio: R$ 1,354,000,000.00

Lucro médio por gênero:
  Ficção: R$ 1,294,666,666.67
  Drama: R$ 1,537,000,000.00
```

### Métricas do Modelo
```
=== Métricas do Modelo ===
Coeficiente (a): 11.54
Intercepto (b): 96,605,918.32
R² (coeficiente de determinação): 0.8234
```

### Predições
```
=== Comparação: Real vs Previsto ===
Real: R$ 220,000,000 | Previsto: R$ 327,376,749
Real: R$ 677,000,000 | Previsto: R$ 2,000,465,272
```

## 🧪 Desenvolvimento Orientado por Testes (TDD)

O projeto segue princípios de TDD:

1. **Red**: Escrever teste que falha
2. **Green**: Implementar código mínimo para passar
3. **Refactor**: Melhorar o código mantendo testes passando

Exemplo de teste:

```python
def test_calculo_lucro():
    """Testa se o cálculo de lucro está correto."""
    filme = Filme("Titanic", 200000000, 2200000000, "Drama")
    lucro_esperado = 2000000000
    
    assert filme.lucro() == lucro_esperado
    print("✓ Teste de cálculo de lucro passou")
```

## 📚 Conceitos Abordados

### Programação Orientada a Objetos
- Classes e objetos
- Encapsulamento
- Métodos e atributos

### Estruturas de Dados
- Listas para armazenamento sequencial
- Dicionários para agrupamentos
- Conjuntos para valores únicos

### Análise de Dados
- Estatísticas descritivas
- Agregações e filtragens
- Transformação de dados

### Visualização
- Gráficos de dispersão
- Gráficos de barras
- Análise de resíduos

### Aprendizado de Máquina
- Regressão linear simples
- Divisão treino/teste
- Avaliação de modelos

## 🔗 Links Úteis

### Documentação Oficial

- [Python](https://docs.python.org/3/) - Documentação oficial do Python
- [NumPy](https://numpy.org/doc/) - Documentação do NumPy
- [Pandas](https://pandas.pydata.org/docs/) - Documentação do Pandas
- [Matplotlib](https://matplotlib.org/stable/contents.html) - Documentação do Matplotlib
- [Seaborn](https://seaborn.pydata.org/) - Documentação do Seaborn
- [Scikit-learn](https://scikit-learn.org/stable/) - Documentação do Scikit-learn

### Tutoriais Recomendados

- [Real Python](https://realpython.com/) - Tutoriais Python de qualidade
- [Kaggle Learn](https://www.kaggle.com/learn) - Cursos de Data Science
- [Python for Data Analysis](https://wesmckinney.com/book/) - Livro de Wes McKinney
- [Introduction to Machine Learning with Python](https://github.com/amueller/introduction_to_ml_with_python) - Livro de Andreas Müller

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
