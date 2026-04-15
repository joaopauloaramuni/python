# 📄 Projeto PdfTranslator

Projeto em Python para tradução automática de artigos científicos em PDF do **inglês para o português**, utilizando **PyMuPDF (fitz)** e **Deep Translator**.

---

## 🔎 O que é o projeto?

O **PdfTranslator** é uma ferramenta em Python que extrai o texto de um PDF página a página, realiza limpeza dos artefatos comuns de documentos científicos e traduz o conteúdo utilizando a API do Google Translator.

O projeto oferece duas formas de uso:

- 🖥️ **Interface gráfica (Tkinter)** — uso simples com botões
- 🧪 **Modo script (CLI)** — execução direta via terminal

A saída é um arquivo `.txt` traduzido e organizado por páginas.

### 🧠 Conceito principal

O projeto resolve os principais problemas de tradução de PDFs científicos:

- Extração respeitando a **ordem visual de leitura**, inclusive em PDFs com duas colunas
- Correção de **hifenização de quebra de linha** (`hyp-\nhenation → hyphenation`)
- Divisão inteligente do texto em blocos, respeitando parágrafos e frases
- Retry automático com **backoff crescente** em caso de falha na API
- Saída com **separadores de página**, facilitando a conferência ao lado do PDF original

---

## 🚀 Funcionalidades

- Extração de texto via `blocks` (respeita colunas de artigos)
- Limpeza de artefatos comuns de PDFs científicos
- Divisão inteligente por parágrafos e frases (limite seguro de 4500 chars)
- Tradução com pausa entre chamadas (evita bloqueio da API gratuita)
- Retry automático com backoff em falhas temporárias
- Salvamento com separadores de página no `.txt` final

---

## 🧰 Dependências

```bash
pip install pymupdf deep-translator
```

---

## 🐍 Ambiente Virtual

É recomendável usar um ambiente virtual:

### Criar ambiente:

```bash
python3 -m venv .venv
```

### Ativar ambiente:

**macOS/Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

---

## ▶️ Execução

Coloque o PDF na mesma pasta do script com o nome `artigo.pdf` (ou edite a variável `caminho_pdf` no `main()`), depois execute:

```bash
python traduzir_artigo.py
```

---

## 📊 Exemplo de execução

```bash
(.venv) python traduzir_artigo.py

📄 Lendo PDF...
   8 página(s) encontrada(s).

── Página 1 ──────────────────────────────
   2 bloco(s) para traduzir.
  Traduzindo bloco 1/2 (3201 chars)...
  Traduzindo bloco 2/2 (1874 chars)...

── Página 2 ──────────────────────────────
   3 bloco(s) para traduzir.
  Traduzindo bloco 1/3 (4102 chars)...
  Traduzindo bloco 2/3 (2893 chars)...
  Traduzindo bloco 3/3 (987 chars)...

...

💾 Salvando resultado...

✅ Concluído! Arquivo salvo em: artigo_traduzido.txt
```

---

## 📁 Exemplo de saída (`artigo_traduzido.txt`)

```
════════════════════════════════════════════════════════════
  PÁGINA 1
════════════════════════════════════════════════════════════

Este artigo apresenta uma abordagem inovadora para o processamento
de linguagem natural aplicado a documentos científicos...

════════════════════════════════════════════════════════════
  PÁGINA 2
════════════════════════════════════════════════════════════

Os experimentos foram conduzidos utilizando um corpus de 10.000
artigos indexados nas bases Web of Science e Scopus...
```

---

## 📁 Estrutura do projeto

```
Projeto PdfTranslator/
├── traduzir_artigo.py   # Script principal
├── artigo.pdf           # PDF de entrada (você fornece)
├── artigo_traduzido.txt # Saída gerada automaticamente
└── README.md
```

---

## 🔗 Documentação e links úteis

- https://pymupdf.readthedocs.io/
- https://github.com/nidhaloff/deep-translator
- https://pypi.org/project/deep-translator/

---

## 📜 Licença

Este projeto está licenciado sob a MIT License.
