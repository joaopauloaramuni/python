# ⚙️ Projeto SQL SchemaGen

## 🚀 O que é o projeto
Este projeto é um **Gerador de Esquema e Massa de Dados SQL** que automatiza a criação de comandos SQL (`CREATE TABLE` e `INSERT INTO`) a partir de uma definição de estrutura em Python.

Em vez de escrever a sintaxe SQL repetidamente, o desenvolvedor foca na **lógica do modelo de dados** (colunas, tipos e restrições) usando dicionários Python. O script interpreta essas regras, abstrai o SQL e, através da integração com a biblioteca **Faker**, gera um arquivo SQL final pronto para ser executado em um ambiente de desenvolvimento ou teste.

---

## 🧩 O que é a técnica de Abstração de Schema
A técnica consiste em usar estruturas de dados Python (`Dict` e `List`) para representar as tabelas e suas colunas. O código é responsável por:

1.  **Formatar a Sintaxe:** Traduzir propriedades simples (como `primary_key: True` ou `nullable: False`) para a sintaxe SQL correta (`PRIMARY KEY`, `NOT NULL`).
2.  **Gerar Chaves Estrangeiras (FK):** Identificar as referências e criar as linhas de `FOREIGN KEY` no comando `CREATE TABLE`.
3.  **Gerar Dados (Seeding):** Usar o mapeamento para **Faker** na definição da coluna para criar comandos `INSERT INTO` com massa de dados de teste coerente.

Essa abordagem melhora a **legibilidade** e **manutenção** do modelo de dados.

---

## 🧠 Utilidades e Vantagens
- **Alta Produtividade:** Define um esquema completo em Python de forma concisa.
- **Geração Automática de Seeds:** Cria automaticamente comandos `INSERT INTO` com dados falsos realistas (`pt_BR`) para popular o banco de dados de desenvolvimento.
- **Abstração SQL:** Você escreve a lógica do BD, o script escreve o SQL.
- **Arquivo Único:** Gera um único arquivo SQL contendo a **estrutura** (`CREATE TABLE`) e os **dados** (`INSERT INTO`), simplificando o *setup*.

---

## 📦 Dependências do projeto
- Python 3.8 ou superior
- Biblioteca principal: **Faker**

Instalação (exemplo):
```bash
pip install faker
```

---

## 🛠️ Pré-requisitos
- Python 3.8+ instalado.
- Recomenda-se criar e ativar um ambiente virtual antes de instalar dependências.

---

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

---

## 🔎 O que cada função faz
Abaixo seguem as assinaturas das funções presentes no script e uma explicação curta do propósito de cada uma.

- `format_column_definition(col: ColumnDefinition) -> str`
  Gera a linha de definição de uma coluna (nome, tipo, `NOT NULL`, `DEFAULT`, `PRIMARY KEY`).

- `get_foreign_key_constraints(columns: List[ColumnDefinition]) -> List[str]`
  Identifica e retorna as linhas SQL de `FOREIGN KEY` baseadas na propriedade `references` da coluna.

- `generate_create_table_script(table_name: str, columns: List[ColumnDefinition]) -> str`
  Combina as definições de coluna e as FKs para montar o comando `CREATE TABLE` completo para uma única tabela.

- `generate_all_create_scripts(schema: Dict[str, List[ColumnDefinition]]) -> List[str]`
  Itera sobre o `DATABASE_SCHEMA` e chama `generate_create_table_script` para todas as tabelas.

- `generate_seed_script(table_name: str, columns: List[ColumnDefinition], num_records: int) -> str`
  Utiliza o mapeamento **Faker** em cada coluna para gerar e formatar o comando `INSERT INTO` com N registros.

- `write_sql_file(scripts: List[str], filename: str)`
  Salva a lista final de comandos SQL (`CREATE` + `INSERT`) em um único arquivo `.sql`.

- `main()`
  Função principal que coordena a geração do Schema, a geração dos Seeds e a escrita do arquivo final.

---

## ⚙️ Execução (exemplo)
1. Ative o ambiente virtual e instale dependências:
```bash
python -m venv .venv
source .venv/bin/activate   # ou .venv\Scripts\activate no Windows
pip install faker
```

2. Edite o dicionário `DATABASE_SCHEMA` no script Python (`sql_schemagen.py`, por exemplo) com a sua estrutura desejada.

3. Execute o script principal:
```bash
python sql_schemagen.py
```

4. Ao terminar, você terá o arquivo gerado:
- `database_schema_and_seed.sql`

---

## 🖥️ Exemplo de saída no terminal
```
(.venv) joaopaulo@MacBook-Pro-de-Joao Projeto SQL SchemaGen % python sql_schemagen.py
Iniciando a Geração de Schemas e Dados de Exemplo...

[SUCESSO] Scripts SQL gerados e salvos em: /Users/joaopauloaramuni/Documents/WORKSPACE-VSCODE/python-main/PROJETOS/Projeto SQL SchemaGen/database_schema_and_seed.sql

Processo concluído.
```

---

## 📝 Boas práticas e sugestões rápidas
- **Ordem de Geração:** Ao definir o `DATABASE_SCHEMA`, coloque as tabelas sem dependências de FK primeiro. O script gera os comandos na ordem em que estão no dicionário, o que é crucial para evitar erros de referência de FK durante a execução do script SQL no BD.
- **Customização Faker:** Aproveite ao máximo os métodos com argumentos, como `faker: "pydecimal(left_digits=3, right_digits=2, positive=True)"` para gerar dados numéricos com maior precisão.
- **Auto Incremento:** Atualmente, as colunas PK não recebem dados `INSERT INTO`. Se seu SGBD (como MySQL ou SQL Server) precisar de sintaxe específica para auto-incremento (ex: `AUTO_INCREMENT`), você precisará adicioná-la manualmente na definição do `type` da coluna: `{"name": "cliente_id", "type": "INT AUTO_INCREMENT", "primary_key": True}`.

---

## 📚 Documentação e Links Úteis

- 🧠 [Documentação oficial do módulo `typing`]([https://docs.python.org/3/library/typing.html](https://docs.python.org/3/library/typing.html))  
  → Tipagem estática opcional em Python (`TypedDict`, `List`, `Dict`, etc).  

- 🧑‍💻 [Documentação oficial do Faker](https://faker.readthedocs.io/en/master/)  
  → Geração de dados falsos realistas (nomes, endereços, CPFs, empresas, etc).  

- 🗂️ [Documentação oficial do módulo `os`]([https://docs.python.org/3/library/os.html](https://docs.python.org/3/library/os.html))  
  → Funções para interação com o sistema operacional (arquivos, diretórios, paths, etc).

---

## 🧾 Licença
Este projeto é disponibilizado sob a licença **MIT**.
