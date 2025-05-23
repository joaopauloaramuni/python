# 🤖 Projeto SentimentExplain

## 🎯 O que é o projeto SentimentExplain?

SentimentExplain é uma ferramenta em Python para análise de sentimento que não só classifica textos como positivos ou negativos, mas também explica **por que** o modelo tomou aquela decisão.  
Ela utiliza técnicas de interpretabilidade baseadas na biblioteca **LIME** para destacar as palavras que mais impactaram a predição, tornando o processo de análise transparente e educativo.

---

## Sobre o modelo e tecnologias usadas

O projeto usa o modelo pré-treinado **distilbert-base-uncased-finetuned-sst-2-english** da Hugging Face.  
Esse modelo é uma versão leve do BERT (DistilBERT), treinada especificamente no dataset SST-2, um benchmark padrão para análise de sentimento em inglês. Ele classifica frases como POSITIVE ou NEGATIVE com alta precisão e rapidez.

Para facilitar o uso do modelo, o projeto utiliza o **pipeline** da biblioteca **transformers** da Hugging Face, que abstrai todo o pré-processamento, inferência e pós-processamento, entregando um resultado simples e direto.

A explicação das decisões do modelo é feita com a biblioteca **LIME (Local Interpretable Model-agnostic Explanations)**, que cria explicações locais interpretáveis ao identificar quais palavras da frase mais influenciaram a classificação.  

O projeto gera um arquivo HTML interativo (`explanation.html`) que mostra a influência de cada palavra, além de imprimir no terminal o score (peso) dessas palavras — indicando se elas contribuem positivamente ou negativamente para o sentimento previsto.

---

## 🔍 Conceitos Importantes

### 📘 O que é BERT?

BERT (Bidirectional Encoder Representations from Transformers) é um modelo de **linguagem natural bidirecional** desenvolvido pelo Google em 2018. Ele entende o **contexto completo** de uma palavra observando as palavras anteriores e posteriores. É a base de muitos modelos de NLP atuais.

### 🔄 O que é `transformers`?

A biblioteca `transformers` da Hugging Face oferece **modelos pré-treinados de NLP** com desempenho de ponta. Ela permite o uso fácil de modelos como BERT, RoBERTa, GPT, etc., com apenas poucas linhas de código.

### 🔌 O que é `pipeline`?

`pipeline` é uma **interface de alto nível** da Hugging Face para executar tarefas como análise de sentimentos, tradução, resumo, etc., com o mínimo de configuração.

### 🟢 O que é `LIME`?

`LIME` (*Local Interpretable Model-agnostic Explanations*) é uma técnica de **interpretação de modelos de machine learning**. Ela ajuda a entender **por que** um modelo tomou determinada decisão, destacando quais partes da entrada (como palavras em um texto) mais influenciaram o resultado.

No contexto deste projeto, o LIME mostra **as palavras que mais contribuíram** para que o modelo previsse sentimento positivo ou negativo, tornando a IA **mais transparente e explicável**. 🔍

> LIME é particularmente útil para modelos complexos (como redes neurais), que normalmente são tratados como "caixas-pretas". Ele faz isso ao perturbar a entrada original e treinar modelos simples (como regressão linear) para simular o comportamento do modelo ao redor daquele exemplo.

---

## 🖼️ Captura de tela

| <img src="https://joaopauloaramuni.github.io/python-imgs/SentimentExplain/imgs/html.png" alt="HTML" width="1000"/> |
|:---------------------------------------------------------------:|
|                        HTML explicativo                         |

---

## 📦 Dependências

Para executar este projeto, você precisará instalar as seguintes bibliotecas:

```bash
pip install transformers torch lime
```

> ⚠️ **Importante**: a biblioteca `transformers` requer um backend de deep learning para funcionar corretamente.  
Você pode escolher entre **PyTorch** ou **TensorFlow**, dependendo da sua preferência ou do modelo utilizado.

### ✅ Instalar PyTorch (mais comum)

Para a maioria dos projetos e modelos, recomenda-se o uso do PyTorch:

```bash
pip install torch
```

Para opções com suporte a GPU/CUDA, consulte o site oficial:  
👉 https://pytorch.org/get-started/locally/

### 🔁 Alternativa: TensorFlow

Caso prefira usar TensorFlow como backend:

```bash
pip install tensorflow
```

Certifique-se de que o código ou modelo que você está utilizando seja compatível com o backend escolhido.

---

Se você tentar rodar um pipeline do `transformers` sem ter o PyTorch ou TensorFlow instalados, um erro será exibido informando que um backend é necessário.

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
(.venv) (base) joaopauloaramuni@MacBook-Pro-de-Joao Projeto SentimentExplain % python3 sentiment_explain.py
No model was supplied, defaulted to distilbert/distilbert-base-uncased-finetuned-sst-2-english and revision 714eb0f (https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english).
Using a pipeline without specifying a model name and revision in production is not recommended.
Device set to use mps:0
******************************************************************************************************************************************************
Digite uma frase para analisar: The food was good.
Texto: The food was good.

Sentimento previsto: POSITIVE (confiança 1.00)

Explicação das palavras que mais impactaram a decisão:

good: 0.0405
food: 0.0393
was: -0.0020
The: 0.0008
******************************************************************************************************************************************************
```

## 📚 Documentação e Links Úteis

### 🔧 Bibliotecas e Ferramentas


- [PyTorch (Documentação Oficial)](https://pytorch.org/docs/) — Biblioteca de aprendizado profundo amplamente usada como backend para `transformers`.
- [TensorFlow (Documentação Oficial)](https://www.tensorflow.org/learn) — Alternativa ao PyTorch, também compatível com `transformers`.

- [Transformers (Hugging Face)](https://huggingface.co/transformers/) — Documentação oficial da biblioteca `transformers`, usada para criar pipelines como `sentiment-analysis`.  
  > ⚠️ Requer que **PyTorch** ou **TensorFlow** esteja instalado como backend para execução dos modelos.

### 🤗 Modelo Pré-Treinado para Análise de Sentimentos

- [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) - Modelo baseado no DistilBERT, treinado especificamente para análise de sentimentos usando o dataset SST-2 (Stanford Sentiment Treebank). Ele é uma versão mais leve e rápida do BERT, ideal para tarefas de NLP com bom desempenho e eficiência.

### 📄 Artigos Relevantes

- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (Google)](https://arxiv.org/abs/1810.04805) — Artigo fundamental que introduz o modelo BERT, base para muitos modelos de NLP, incluindo os listados acima.

---

## 📚 Sugestão de Leitura

**Título:** *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*

**Autores:** Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova

**Tipo:** Artigo Científico (Google AI)

**Link original:** [BERT Paper (arXiv)](https://arxiv.org/abs/1810.04805)

**Link local:** [BERT Paper (PDF)](Artigo_BERT/1810.04805v2.pdf)

**Resumo:** O BERT (Bidirectional Encoder Representations from Transformers) é um modelo de linguagem pré-treinado profundamente bidirecional baseado na arquitetura Transformer. Ele foi projetado para compreender o contexto de uma palavra com base em todas as palavras em uma sentença (tanto à esquerda quanto à direita). O BERT foi treinado em tarefas de modelagem de linguagem e previsão de frases, e depois ajustado em tarefas específicas como perguntas e respostas, classificação de sentimentos e NER. Este artigo teve grande impacto no NLP moderno, redefinindo benchmarks em várias tarefas.

**Palavras-chave:** NLP, Transformers, BERT, Google AI, Modelos de Linguagem

---

**Título:** *Mineração de Emoções em Textos: Um Estudo Aplicado Sobre as Interações de Programadores em Comunidade On-line de Perguntas e Respostas*  

**Autor:** [Lucas Romualdo Fernandes de Sá](https://www.linkedin.com/in/lrfsa/)

**Tipo:** Dissertação de Mestrado em Sistemas de Informação e Gestão do Conhecimento

**Link:** [Dissertação (PDF)](Dissertação_Lucas_Romualdo_Fernandes_de_Sá/DISSERTAÇÃO_VERSAO_FINAL_REVISADA_LUCAS.pdf)

**Resumo:** O Stack Overflow é a maior comunidade on-line de Perguntas-Respostas sobre Linguagem de Programação na Web, e sua importância tem crescidopor causa do acumulo de tópicos relevantes para solução de problemas de Tecnologia da Informação (TI), disso a comunidade Stack Overflow tornou-se um repositório de conhecimento, resultado de muitas interações sociais entre programadores e usuários comuns. O Stack Overflow se tornou objeto de estudo e pesquisa em diferentes domínios de conhecimento, em paralelo, o campo de pesquisa de Análise de Sentimentos (AS) também esteve em desenvolvimento e ascensão. Uma parte dos estudos realizados no campo de AS teve o Stack Overflow como objeto de pesquisa com intuito de entender se existe uma relação dos sentimentos, emoções e opiniões dos usuários com as características e aspectos dessa comunidade on-line. O objetivo da pesquisa foi aplicar a análise de sentimentos em posts de uma comunidade on-line de programação. A metodologia do trabalho adotou a realização de uma Revisao Sistemática da Literatura sobre o Stack Overflow e a aplicação de recursos para AS fornecida pela linguagem R e seu pacote tidytext com os dicionários léxicos NRC e AFINN em cima de comentários de usuários de diferentes linguagens de programação. Os resultados apresentaram a importância de AS nas comunidades on-line e evidenciou como as tecnologias usadas pelo usuário influenciam na padronização do comportamento e tendência emocional dos usuários. A conclusão apontou à importância de se apronfundar em estudos mais focados e estender também o estudo a outras comunidades do Stack Exchange.

**Palavras-chaves:** Análise de Sentimentos, Mineração de Emoção, Stack Overflow.

---

## 📄 Licença

Este projeto é distribuído sob a licença **MIT**. Você pode utilizá-lo, modificá-lo e distribuí-lo livremente. 🧑‍🏫
