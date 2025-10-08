# 🧪 Projeto Faker Generator

## 🚀 O que é o projeto
Este projeto é um gerador simples de **dados falsos** para testes de software, usando a biblioteca **Faker**. Ele produz registros realistas (nomes, CPFs, e-mails, endereços, cargos, salários etc.) e salva em arquivos CSV e JSON. O objetivo é facilitar a criação de massa de dados para testes locais, demonstrações e prototipagem.

## 🧠 O que é a lib Faker
**Faker** é uma biblioteca Python que gera dados falsos realistas para diversas localidades (ex.: `pt_BR`, `en_US`). Em vez de criar dados manualmente ou copiar listas, o Faker permite produzir rapidamente grandes quantidades de entradas plausíveis (nomes, endereços, empresas, documentos) que parecem reais, mas são fictícias. Isso é útil para testar pipelines de ingestão, interfaces, validações e cargas de dados sem expor informações reais de usuários.

## 📦 Dependências do projeto
- Python 3.7 ou superior
- Biblioteca principal: **Faker**

Instalação (exemplo):
```bash
pip install faker
```

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

2. Execute o script principal:
```bash
python faker_generator.py
```

3. Ao terminar, você terá os arquivos gerados, por exemplo:
- `dados_falsos.csv`
- `dados_falsos.json`

## 🖥️ Exemplo de saída no terminal
```
(.venv) (base) joaopauloaramuni@MacBook-Pro-de-Joao Projeto Faker Generator % python faker_generator.py 
Iniciando o Gerador de Dados Falsos (CSV e JSON)...

Gerando 100 registros...
Progresso: 10/100...
Progresso: 20/100...
Progresso: 30/100...
Progresso: 40/100...
Progresso: 50/100...
Progresso: 60/100...
Progresso: 70/100...
Progresso: 80/100...
Progresso: 90/100...
Progresso: 100/100...

--- Processo de Salvamento ---
-> CSV criado com sucesso: /Users/joaopauloaramuni/Documents/WORKSPACE-VSCODE/python/Projeto Faker Generator/dados_falsos.csv
-> JSON criado com sucesso: /Users/joaopauloaramuni/Documents/WORKSPACE-VSCODE/python/Projeto Faker Generator/dados_falsos.json

--- FIM ---
Total de 100 registros criados com sucesso.
```

## 📝 Boas práticas e sugestões rápidas
- Se for gerar grandes volumes, considere desabilitar `fake.unique` para evitar exceções por esgotamento de valores únicos.  
- Para reprodutibilidade durante desenvolvimento, adicione suporte a uma `seed` (semente) e use `random.seed(seed)` / `Faker.seed(seed)`.  
- Se precisar de tipos brasileiros adicionais (ex.: CNPJ, telefone formatado), é possível estender a função `gerar_dados_usuario` ou adicionar novos campos no script.

## 🧾 Licença
Este projeto é disponibilizado sob a licença **MIT**.

---
