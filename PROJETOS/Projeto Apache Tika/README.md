# 📄 PDF Security Analyzer (Apache Tika)

Projeto em Python para análise de segurança de arquivos PDF utilizando o **Apache Tika**.

---

## 🚀 Funcionalidades

- Detecção de JavaScript suspeito
- Identificação de objetos embutidos
- Análise de encodings suspeitos
- Verificação de URLs maliciosas
- Inspeção de metadados
- Cálculo de score de risco (Baixo, Médio, Alto, Crítico)
- Exportação de relatório em JSON

---

## 🧰 Dependências

Instale o Apache Tika:

```bash
pip install tika
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

```bash
python pdf_scanner.py
```

---

## 📊 Exemplo de execução

```bash
(.venv) (base) joaopauloaramuni@MacBook-Pro-de-Joao Projeto Apache Tika % python3 pdf_scanner.py
Digite o caminho do PDF (ou glob, ex: docs/*.pdf): teste.pdf
16:29:11 [INFO] Analisando: /Users/joaopauloaramuni/Documents/.../teste.pdf

────────────────────────────────────────────────────────────
  Arquivo : teste.pdf
  Tamanho : 10,045,390 bytes (normal)
────────────────────────────────────────────────────────────
  JavaScript suspeito: nenhum
  Objetos embutidos: nenhum
  Encoding suspeito: nenhum
  URLs suspeitas:
    • [encurtador] https://goo.gl/pp2T6r
    • [encurtador] https://goo.gl/pp2T6r
    • [tld-suspeito] http://lattes.cnpq.br/1208427665892059
  Metadados suspeitos: nenhum
────────────────────────────────────────────────────────────
  Score   : 6
  Risco   : Alto
────────────────────────────────────────────────────────────

Exportar relatório JSON? [s/N] s
Nome do arquivo [relatorio.json]: relatorio.json
16:29:24 [INFO] Relatório exportado: relatorio.json
```

---

## 📁 Exemplo de `relatorio.json`

```json
[
  {
    "arquivo": "/Users/.../teste.pdf",
    "tamanho_bytes": 10045390,
    "tamanho_status": "normal",
    "javascript": [],
    "embedded_objects": [],
    "encoding_suspeito": [],
    "urls_suspeitas": [
      "[encurtador] https://goo.gl/pp2T6r",
      "[encurtador] https://goo.gl/pp2T6r",
      "[tld-suspeito] http://lattes.cnpq.br/1208427665892059"
    ],
    "metadados_suspeitos": [],
    "score": 6,
    "risco": "Alto",
    "erro": null,
    "timestamp": "2026-03-27T16:29:11.259862"
  }
]
```

---

## 🔗 Documentação e links úteis

- https://tika.apache.org/
- https://tika.apache.org/download.html
- https://github.com/apache/tika

---

## 📜 Licença

MIT
