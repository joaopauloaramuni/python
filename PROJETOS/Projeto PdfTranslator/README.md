# 📄 Projeto PdfTranslator

Projeto em Python para tradução automática de artigos científicos em PDF do **inglês para o português**, utilizando **PyMuPDF (fitz)**, **Deep Translator** e **ttkbootstrap**.

---

## Captura de Tela 📸

<table align="center">
  <tr>
    <td align="center">
      <img src="https://joaopauloaramuni.github.io/python-imgs/PdfTranslator/imgs/home_v2.png" width="800px" alt="Home">
    </td>
  </tr>
  <tr>
    <td align="center">
      Pdf Translator
    </td>
  </tr>
</table>

---

## 🔎 O que é o projeto?

O **PdfTranslator** é uma ferramenta em Python que extrai o texto de um PDF página a página, realiza limpeza dos artefatos comuns de documentos científicos e traduz o conteúdo utilizando a API do Google Translator.

O projeto oferece duas formas de uso:

- 🖥️ **Interface gráfica (ttkbootstrap)** — uso simples com botões e visual moderno
- 🧪 **Modo script (CLI)** — execução direta via terminal

A saída é um arquivo `.txt` traduzido e organizado por páginas.

### 🧠 Conceito principal

O projeto resolve os principais problemas de tradução de PDFs científicos:

- Extração via `get_text("dict")`, que respeita automaticamente **colunas múltiplas** sem detecção manual de layout
- Correção de **hifenização de quebra de linha** (`hyp-\nhenation → hyphenation`)
- Divisão inteligente do texto em blocos, respeitando parágrafos e frases
- Retry automático com **backoff crescente** em caso de falha na API
- Saída com **separadores de página**, facilitando a conferência ao lado do PDF original

---

## 🚀 Funcionalidades

### 🎯 Funcionalidades Principais
- **Tradução Automática**: Tradução completa de PDFs com um clique
- **Interface Intuitiva**: GUI moderna com design responsivo
- **Múltiplos Idiomas**: Suporte a 26 idiomas diferentes
- **Detecção Automática**: Identificação automática do idioma de origem
- **Preservação de Estrutura**: Mantém formatação e separação por páginas
- **Extração de Texto Inteligente**: Uso de `get_text("dict")`, respeitando colunas e estrutura interna do PDF sem heurísticas de posição
- **Limpeza de Texto**: Remoção de artefatos comuns de PDFs científicos
- **Divisão Inteligente**: Separação por parágrafos e frases (limite seguro de 4500 caracteres)
- **Controle de Tradução**: Pausa entre chamadas para evitar bloqueio da API gratuita
- **Resiliência**: Retry automático com backoff em falhas temporárias
- **Exportação Estruturada**: Salvamento em `.txt` com separadores de página
- **Interface Moderna**: Construída com `ttkbootstrap`

### 🔧 Funcionalidades Técnicas
- **Processamento Assíncrono**: Interface não bloqueia durante a tradução
- **Gerenciamento de Erros**: Retry automático em falhas de API
- **Otimização de Blocos**: Divisão inteligente para maximizar eficiência
- **Log Detalhado**: Acompanhamento em tempo real do progresso
- **Tratamento de Imagens**: Identifica e ignora páginas baseadas em imagens

### 📊 Funcionalidades de Saída
- **Formato Estruturado**: Arquivo `.txt` com separadores de página
- **Preservação de Conteúdo**: Mantém texto original em caso de falha
- **Nomenclatura Automática**: Nome gerado automaticamente baseado no arquivo original

---

## 🌐 Idiomas Suportados

O projeto suporta 26 idiomas com detecção automática:

| Idioma | Código |
|--------|--------|
| Detectar automaticamente | auto |
| Afrikaans | af |
| Alemão | de |
| Árabe | ar |
| Chinês (simplificado) | zh-CN |
| Chinês (tradicional) | zh-TW |
| Coreano | ko |
| Dinamarquês | da |
| Espanhol | es |
| Finlandês | fi |
| Francês | fr |
| Grego | el |
| Hindi | hi |
| Holandês | nl |
| Húngaro | hu |
| Indonésio | id |
| Inglês | en |
| Italiano | it |
| Japonês | ja |
| Norueguês | no |
| Persa | fa |
| Polonês | pl |
| Português | pt |
| Romeno | ro |
| Russo | ru |
| Sueco | sv |
| Tailandês | th |
| Tcheco | cs |
| Turco | tr |
| Ucraniano | uk |
| Vietnamita | vi |

---

## 🧰 Dependências

```bash
pip install pymupdf deep-translator ttkbootstrap
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

## 🎨 Interface Gráfica (ttkbootstrap)

A interface utiliza `ttkbootstrap`, uma extensão moderna do Tkinter que oferece temas visuais inspirados no Bootstrap. O import utilizado é:

```python
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
```

Para alterar o tema visual, basta modificar o parâmetro `themename` ao instanciar a janela principal. Temas disponíveis incluem: `flatly`, `darkly`, `superhero`, `cosmo`, `journal`, entre outros.

---

## ▶️ Execução

Coloque o PDF na mesma pasta do script com o nome `artigo.pdf` (ou edite a variável `caminho_pdf` no `main()`), depois execute:

```bash
python gui.py  # ou
python pdf_translator.py
```

---

## 📊 Exemplo de execução

```
(.venv) python pdf_translator.py

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
├── pdf_translator.py    # Script principal
├── gui.py               # Interface com ttkbootstrap
├── artigo.pdf           # PDF de entrada (você fornece)
├── artigo_traduzido.txt # Saída gerada automaticamente
└── README.md
```

---

## 🔗 Documentação e links úteis

- https://pymupdf.readthedocs.io/
- https://github.com/nidhaloff/deep-translator
- https://pypi.org/project/deep-translator/
- https://ttkbootstrap.readthedocs.io/

---

## Contribuição 🤝

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

### Agradecimentos especiais pelas contribuições

* v1 -> Davi Nunes Carvalho - [https://github.com/Davii13/](https://github.com/Davii13/) e Artur Bomtempo [https://github.com/arturbomtempo-dev](https://github.com/arturbomtempo-dev)

---

## 📜 Licença

Este projeto está licenciado sob a MIT License.
