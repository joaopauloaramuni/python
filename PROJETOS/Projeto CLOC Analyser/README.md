# 📊 Projeto CLOC Analyser

O **CLOC Analyser** é uma ferramenta simples e eficiente para analisar a contagem de linhas de código (LoC) em projetos hospedados no GitHub. Utilizando o utilitário `cloc`, este script Python automatiza o processo de clonagem de repositórios Git e execução da análise de código-fonte.

---

## 🚀 Funcionalidades

- Clona automaticamente um repositório Git informado pelo usuário.
- Executa o `cloc` no repositório clonado.
- Exibe um resumo com número de arquivos, linhas em branco, linhas de comentário e linhas de código, por linguagem.

---

## 🔍 O que é o `cloc`?

> **cloc** (Count Lines of Code) é uma ferramenta que conta linhas em branco, linhas de comentários e linhas físicas de código fonte em diversos idiomas de programação.

📦 Última versão: **v2.04 (31 de janeiro de 2025)**

---

## 📦 Dependências

- Python 3.x
- Git
- [cloc v2.04](https://github.com/AlDanial/cloc/releases/tag/v2.04)

### 💻 Instalação do `cloc`:

- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt install cloc
  ```
- **macOS (Homebrew):**
  ```bash
  brew install cloc
  ```

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

## 🧪 Exemplo de Execução

```bash
(.venv) (base) joaopauloaramuni@MacBook-Pro-de-Joao Projeto CLOC Analyser % python cloc_analyser.py
🚀 Analisador de Código com CLOC

📥 Informe a URL do repositório Git que deseja analisar com cloc: https://github.com/apache/commons-lang
🔄 Clonando repositório de https://github.com/apache/commons-lang...
Cloning into '/Users/joaopauloaramuni/Downloads/Projeto CLOC Analyser/commons-lang'...
remote: Enumerating objects: 102696, done.
remote: Counting objects: 100% (2655/2655), done.
remote: Compressing objects: 100% (998/998), done.
remote: Total 102696 (delta 1921), reused 1796 (delta 1417), pack-reused 100041 (from 3)
Receiving objects: 100% (102696/102696), 28.25 MiB | 9.74 MiB/s, done.
Resolving deltas: 100% (48069/48069), done.
📊 Executando cloc em /Users/joaopauloaramuni/Downloads/Projeto CLOC Analyser/commons-lang...

📋 Resultado:

github.com/AlDanial/cloc v 2.04  T=2.17 s (269.8 files/s, 96274.4 lines/s)
----------------------------------------------------------------------------------------
Language                              files          blank        comment           code
----------------------------------------------------------------------------------------
Java                                    512          18106          71724          97366
Text                                     30           1959              0          12492
XML                                      28            402            583           4409
Maven                                     1             17             41            942
HTML                                      1             13             16            236
YAML                                      6             36            109            151
Markdown                                  5             52            122            131
Velocity Template Language                1             22             31             88
Properties                                1              3             19              3
Bourne Shell                              1              0              2              2
----------------------------------------------------------------------------------------
SUM:                                    586          20610          72647         115820
----------------------------------------------------------------------------------------

```

---

## 📚 Documentação e Links Úteis

- 🔗 [Repositório oficial do cloc](https://github.com/AlDanial/cloc)
- 📝 [Release v2.04](https://github.com/AlDanial/cloc/releases/tag/v2.04)

---

## ⚖️ Licença

Este projeto está licenciado sob a **MIT License**. Sinta-se livre para usar, modificar e compartilhar!
