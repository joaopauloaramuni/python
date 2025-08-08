# 📊 Projeto Seaborn Samples

## 🚀 Sobre o Projeto

Este projeto é um exemplo prático para criação e salvamento de diversos gráficos utilizando bibliotecas poderosas do Python para análise e visualização de dados. Aqui, você vai gerar dados de vendas fictícios e explorar diferentes tipos de gráficos para entender melhor os dados.

---

## 📚 Bibliotecas Usadas

- **Pandas 🐼**  
  Biblioteca essencial para manipulação e análise de dados em Python. Facilita o trabalho com tabelas e séries temporais, tornando o processo de limpeza e organização dos dados muito mais simples.

- **Seaborn 🎨**  
  Biblioteca baseada no Matplotlib que oferece uma interface de alto nível para criar gráficos estatísticos bonitos e informativos de forma simples e elegante.

- **Matplotlib 📈**  
  Biblioteca fundamental para criação de gráficos em Python. Permite criar praticamente qualquer tipo de visualização, desde gráficos simples até complexas figuras personalizadas.

---

## 🖼️ Gráficos gerados

| <img src="https://joaopauloaramuni.github.io/python-imgs/SeabornSamples/imgs/grafico_barras.png" alt="grafico_barras" width="100"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/SeabornSamples/imgs/grafico_pizza.png" alt="grafico_pizza" width="100"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/SeabornSamples/imgs/grafico_linha.png" alt="grafico_linha" width="100"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/SeabornSamples/imgs/grafico_histograma.png" alt="grafico_histograma" width="100"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/SeabornSamples/imgs/grafico_dispersao.png" alt="grafico_dispersao" width="100"/> |
|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|
| grafico_barras.png | grafico_pizza.png | grafico_linha.png | grafico_histograma.png | grafico_dispersao.png |

| <img src="https://joaopauloaramuni.github.io/python-imgs/SeabornSamples/imgs/grafico_boxplot.png" alt="grafico_boxplot" width="100"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/SeabornSamples/imgs/grafico_heatmap.png" alt="grafico_heatmap" width="100"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/SeabornSamples/imgs/grafico_pairplot.png" alt="grafico_pairplot" width="100"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/SeabornSamples/imgs/grafico_violin.png" alt="grafico_violin" width="100"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/SeabornSamples/imgs/grafico_barras_empilhadas.png" alt="grafico_barras_empilhadas" width="100"/> |
|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|
| grafico_boxplot.png | grafico_heatmap.png | grafico_pairplot.png | grafico_violin.png | grafico_barras_empilhadas.png |

---

## 📦 Instalação das Dependências

Para rodar este projeto, instale as bibliotecas necessárias usando o comando:

```bash
pip install pandas seaborn matplotlib
````

---

## ⚙️ Ambiente virtual

Para usar este projeto, recomendamos criar e ativar um ambiente virtual Python:

```bash
# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente virtual

# Windows:
.venv\Scripts\activate

# Linux/macOS:
source .venv/bin/activate
```

---

## 📊 Quando usar cada tipo de gráfico: Guia rápido

Este guia explica, de forma genérica, os contextos mais comuns para usar cada um dos gráficos exemplificados no projeto.

---

### 1. Gráfico de Barras (Barplot)

- **O que mostra:** Comparação de valores categóricos (ex.: soma, média) entre diferentes grupos.
- **Quando usar:** Para comparar a magnitude de diferentes categorias de forma clara e visual, como vendas por produto, população por país, etc.

---

### 2. Gráfico de Pizza (Pie chart)

- **O que mostra:** Proporções relativas de um todo dividido em categorias.
- **Quando usar:** Quando quiser mostrar a participação percentual ou fração de cada categoria em relação ao total, como participação de mercado, porcentagem de respostas, etc.

---

### 3. Gráfico de Linha (Line plot)

- **O que mostra:** Tendência ou evolução de uma variável ao longo do tempo ou outra variável contínua.
- **Quando usar:** Para visualizar mudanças e tendências ao longo do tempo, como evolução de preços, temperaturas diárias, crescimento populacional.

---

### 4. Histograma (Histogram)

- **O que mostra:** Distribuição da frequência de valores em uma variável numérica.
- **Quando usar:** Para analisar a forma da distribuição dos dados (simetria, assimetria, dispersão), como notas de prova, idades, rendimentos.

---

### 5. Gráfico de Dispersão (Scatter plot)

- **O que mostra:** Relação entre duas variáveis numéricas, ponto a ponto.
- **Quando usar:** Para identificar correlações, tendências, agrupamentos e outliers entre variáveis quantitativas, como altura vs peso, preço vs demanda.

---

### 6. Boxplot (Caixa e Bigodes)

- **O que mostra:** Distribuição resumida de uma variável numérica por grupos, destacando mediana, quartis e outliers.
- **Quando usar:** Para comparar distribuições, variabilidade e identificar outliers entre categorias, como salários por setor, notas por turma.

---

### 7. Heatmap (Mapa de calor)

- **O que mostra:** Matriz de valores representados por cores, destacando padrões e variações.
- **Quando usar:** Para visualizar dados tabulares complexos e detectar tendências ou concentrações, como correlações entre variáveis, matrizes de confusão, vendas por região e mês.

---

### 8. Pairplot (Matriz de dispersão)

- **O que mostra:** Relações par a par entre múltiplas variáveis numéricas.
- **Quando usar:** Para explorar rapidamente correlações e distribuições entre várias variáveis numéricas simultaneamente, ideal para análise exploratória.

---

### 9. Violin Plot (Gráfico Violino)

- **O que mostra:** Distribuição completa dos dados com densidade e mediana, por categoria.
- **Quando usar:** Para analisar a forma da distribuição e comparar grupos, mostrando mais detalhes que um boxplot, útil para dados multimodais ou complexos.

---

### 10. Gráfico de Barras Empilhadas (Stacked Barplot)

- **O que mostra:** Composição de categorias dentro de cada grupo, empilhadas numa única barra.
- **Quando usar:** Para comparar o total e a composição interna das categorias ao mesmo tempo, como vendas totais divididas por região, ou população por faixa etária em diferentes países.

---

Esse conjunto de gráficos é essencial para análise visual de dados em múltiplos contextos, ajudando a transformar dados em insights claros e acionáveis.

---

## 📚 Documentação e Links Úteis

- **Seaborn**  
  Biblioteca Python para visualização estatística baseada no matplotlib, com interface de alto nível para criar gráficos atraentes e informativos.  
  Site oficial: [https://seaborn.pydata.org/](https://seaborn.pydata.org/)

- **Matplotlib**  
  Biblioteca fundamental para criação de gráficos em Python, flexível e poderosa para personalização.  
  Site oficial: [https://matplotlib.org/](https://matplotlib.org/)

- **Pandas**  
  Biblioteca para manipulação e análise de dados, oferecendo estruturas de dados rápidas e flexíveis.  
  Site oficial: [https://pandas.pydata.org/](https://pandas.pydata.org/)

- **Python**  
  Linguagem de programação usada neste projeto.  
  Site oficial: [https://www.python.org/](https://www.python.org/)

---

## 📝 Licença

Este projeto está licenciado sob a Licença MIT.

---
