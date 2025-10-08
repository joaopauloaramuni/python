
# 🧪 Projeto Faker Generator

## 🚀 O que é o projeto
Este projeto é um gerador simples de **dados falsos** para testes de software, usando a biblioteca **Faker**. Ele produz registros realistas (nomes, CPFs, e-mails, endereços, cargos, salários etc.) e salva em arquivos CSV e JSON. O objetivo é facilitar a criação de massa de dados para testes locais, demonstrações e prototipagem.

## 🧠 Técnica: o que é usar o Faker
**Faker** é uma biblioteca Python que gera dados falsos realistas para diversas localidades (ex.: `pt_BR`, `en_US`). Em vez de criar dados manualmente ou copiar listas, o Faker permite produzir rapidamente grandes quantidades de entradas plausíveis (nomes, endereços, empresas, documentos) que parecem reais, mas são fictícias. Isso é útil para testar pipelines de ingestão, interfaces, validações e cargas de dados sem expor informações reais de usuários.

## 📦 Dependências do projeto
- Python 3.7 ou superior
- Biblioteca principal: **Faker**

Instalação (exemplo):
```bash
pip install faker
```

> Observação: o repositório exemplo mostrava `tqdm` e uma wordlist (rockyou) — esses itens pertencem a outro tipo de projeto (ex.: ferramentas de auditoria). **Não incluímos instruções para uso de wordlists ou ataques**. Este repositório é somente para geração de dados de teste legítimos.

## 🛠️ Pré-requisitos
- Python 3.7+ instalado.
- Recomenda-se criar e ativar um ambiente virtual antes de instalar dependências (veja seção abaixo).

## 🐍 Ambiente virtual (recomendado)
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

3. **Instale as dependências:**
```bash
pip install faker
```

## 🔎 O que cada função faz
Abaixo seguem as assinaturas das funções presentes no script e uma explicação curta do propósito de cada uma — **sem** incluir o código.

- `configurar_faker(locale: str = 'pt_BR') -> Faker`  
  Inicializa e retorna uma instância da classe `Faker` com o locale informado (por padrão `pt_BR`), que será usada para gerar dados no formato local apropriado.

- `gerar_dados_usuario(fake_instance: Faker) -> Dict[str, Any]`  
  Gera e retorna um único registro (dicionário) contendo campos como ID, nome completo, e-mail, CPF, endereço, data de nascimento, cargo, empresa e salário. Usa métodos do objeto `Faker` passado como argumento.

- `salvar_dados_csv(dados_lista: List[Dict], nome_arquivo: str)`  
  Recebe uma lista de dicionários e salva em disco no formato CSV. A função obtém os campos a partir das chaves do primeiro registro e escreve o cabeçalho seguido das linhas.

- `salvar_dados_json(dados_lista: List[Dict], nome_arquivo: str)`  
  Recebe uma lista de dicionários e salva em disco no formato JSON, com formatação legível (`indent`) e suporte a caracteres UTF-8 (`ensure_ascii=False`).

- `main()`  
  Função principal que coordena o fluxo: configura o Faker, gera N registros (conforme constante ou configuração), exibe progresso simples, e chama as funções de persistência (CSV e JSON).

## ⚙️ Execução (exemplo)
1. Ative o ambiente virtual (opcional) e instale dependências:
```bash
python -m venv .venv
source .venv/bin/activate   # ou .venv\Scripts\activate no Windows
pip install faker
```

2. Execute o script principal (supondo que o arquivo se chame `main.py` ou `gerador.py`):
```bash
python main.py
```

3. Ao terminar, você terá os arquivos gerados, por exemplo:
- `dados_falsos.csv`
- `dados_falsos.json`

## 📝 Boas práticas e sugestões rápidas
- Se for gerar grandes volumes, considere desabilitar `fake.unique` para evitar exceções por esgotamento de valores únicos.  
- Para reprodutibilidade durante desenvolvimento, adicione suporte a uma `seed` (semente) e use `random.seed(seed)` / `Faker.seed(seed)`.  
- Se precisar de tipos brasileiros adicionais (ex.: CNPJ, telefone formatado), é possível estender a função `gerar_dados_usuario` ou adicionar novos campos no script.

## 🧾 Licença
Este projeto é disponibilizado sob a licença **MIT**.

---
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the \"Software\"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
