# 📊 Projeto SentimentAnalyzer

Este projeto tem como objetivo analisar o **sentimento** de um texto utilizando **modelos de aprendizado profundo** baseados em **transformers**, por meio da biblioteca 🤗 `transformers` da Hugging Face.

O usuário pode escolher entre **três modelos distintos** de análise de sentimentos, todos treinados com bases de dados diferentes e voltados para contextos específicos, como multilíngue, espanhol e inglês informal (tweets).

---

## 🎯 Objetivo do Projeto

O `SentimentAnalyzer` permite que você:

- Escolha entre 3 modelos de análise de sentimentos.
- Analise textos em diferentes idiomas ou estilos (formal/informal).
- Interprete o sentimento com **ícones emoji** para facilitar a compreensão.
- Visualize o modelo utilizado, a saída bruta, a confiança e a interpretação do sentimento.

---

## 🧠 Modelos Disponíveis

### 1️⃣ `nlptown/bert-base-multilingual-uncased-sentiment`

- 📅 Ano: Lançado em 2020.
- 🌐 Multilíngue: funciona com textos em **vários idiomas** (inclusive português).
- 🤖 Baseado no **BERT-base**.
- 📚 Treinado com avaliações de lugares como restaurantes e hotéis (Yelp, Amazon, TripAdvisor).
- 🔢 Classificação de 1 a 5 estrelas.
- 🗃️ Base de dados: aproximadamente 150 mil avaliações.
- ⚙️ Ideal para reviews e feedbacks de usuários.

### 2️⃣ `pysentimiento/robertuito-sentiment-analysis`

- 📅 Ano: 2021.
- 🇪🇸 Focado em textos em **espanhol**.
- 🧱 Baseado no **RoBERTuito** (variação do RoBERTa para espanhol).
- 📚 Treinado com milhões de tweets em espanhol.
- 🔤 Labels: `POS` (positivo), `NEG` (negativo), `NEU` (neutro).
- 🤝 Ótimo para redes sociais e comunicação informal em espanhol.

### 3️⃣ `finiteautomata/bertweet-base-sentiment-analysis`

- 📅 Ano: 2020.
- 🌐 Focado em **inglês informal**, especialmente **tweets**.
- 🐦 Baseado no **BERTweet**, um modelo treinado com **850 milhões de tweets**.
- 📊 Labels: `POS`, `NEG`, `NEU`.
- 🚀 Excelente para conteúdo de redes sociais em inglês.

---

## 🔍 Conceitos Importantes

### 📘 O que é BERT?

BERT (Bidirectional Encoder Representations from Transformers) é um modelo de **linguagem natural bidirecional** desenvolvido pelo Google em 2018. Ele entende o **contexto completo** de uma palavra observando as palavras anteriores e posteriores. É a base de muitos modelos de NLP atuais.

### 🔄 O que é `transformers`?

A biblioteca `transformers` da Hugging Face oferece **modelos pré-treinados de NLP** com desempenho de ponta. Ela permite o uso fácil de modelos como BERT, RoBERTa, GPT, etc., com apenas poucas linhas de código.

### 🔌 O que é `pipeline`?

`pipeline` é uma **interface de alto nível** da Hugging Face para executar tarefas como análise de sentimentos, tradução, resumo, etc., com o mínimo de configuração.

---

## 📦 Dependências

Para executar este projeto, instale os seguintes pacotes:

```bash
pip install transformers emoji
```

---

## 🧪 Ambiente Virtual

É recomendável usar um **ambiente virtual** para evitar conflitos entre dependências. Siga os passos:

### 1. Crie um ambiente virtual

```bash
python3 -m venv .venv
```

### 2. Ative o ambiente virtual

- **macOS e Linux**:

```bash
source .venv/bin/activate
```

- **Windows**:

```bash
.venv\Scripts\activate
```

---

## 🖥️ Exemplo de uso no terminal

### ✅ Modelo 1:

```bash
python3 sentiment_analyzer.py
Modelos disponíveis:
1 - nlptown/bert-base-multilingual-uncased-sentiment
2 - pysentimiento/robertuito-sentiment-analysis
3 - finiteautomata/bertweet-base-sentiment-analysis
****************************************************************************************************
Escolha o modelo (número): 1
Device set to use mps:0
Digite o texto a ser analisado: A comida estava boa.
****************************************************************************************************
Texto: A comida estava boa.
Modelo usado: nlptown/bert-base-multilingual-uncased-sentiment
Classificação bruta: 4 stars
Score de confiança: 0.38
Sentimento interpretado: positivo 🙂
****************************************************************************************************
```

### ✅ Modelo 2:

```bash
Escolha o modelo (número): 2
Device set to use mps:0
Digite o texto a ser analisado: A comida estava boa.
****************************************************************************************************
Texto: A comida estava boa.
Modelo usado: pysentimiento/robertuito-sentiment-analysis
Classificação bruta: POS
Score de confiança: 0.78
Sentimento interpretado: positivo 🙂
****************************************************************************************************
```

### ✅ Modelo 3:

```bash
Escolha o modelo (número): 3
Device set to use mps:0
Digite o texto a ser analisado: The food was good.
****************************************************************************************************
Texto: The food was good.
Modelo usado: finiteautomata/bertweet-base-sentiment-analysis
Classificação bruta: POS
Score de confiança: 0.99
Sentimento interpretado: positivo 🙂
****************************************************************************************************
```

---

## 📚 Documentação e Links Úteis

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [nlptown/bert-base-multilingual-uncased-sentiment](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)
- [pysentimiento/robertuito-sentiment-analysis](https://huggingface.co/pysentimiento/robertuito-sentiment-analysis)
- [finiteautomata/bertweet-base-sentiment-analysis](https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis)
- [BERT Paper (Google)](https://arxiv.org/abs/1810.04805)

---

## 📄 Licença

Este projeto é distribuído sob a licença **MIT**. Você pode utilizá-lo, modificá-lo e distribuí-lo livremente. 🧑‍🏫

---
