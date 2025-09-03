# Projeto SGA Spider

Este projeto, dividido em duas versões, realiza uma raspagem de dados para extrair as informações de notas e faltas dos alunos de graduação da PUC Minas, diretamente da página do Sistema de Gestão Acadêmica [SGA](https://www.sistemas.pucminas.br/sgaaluno4/SilverStream/Pages/pgAln_LoginSSL.html).

## Captura de Tela

| <img src="https://joaopauloaramuni.github.io/python-imgs/SGA_Spider/imgs/sga.png" width="1000px" alt="SGA"> |
|:--------------------------------------------:|
| **Sistema de Gestão Acadêmica (SGA)** |

## Como funciona

Este projeto é uma aplicação Python que automatiza a consulta de informações acadêmicas para estudantes de graduação da PUC Minas. Ele utiliza web scraping para acessar o SGA e processar dados de frequência, notas e credenciais, facilitando a visualização do desempenho e o acesso a serviços institucionais.

---

## Funcionalidades da versão 1 - **Faltas**

- **Login Automático**: Realiza login no portal do estudante da PUC Minas.
- **Extração de dados**:
  - Navega até a página de notas e frequência.
  - Extrai informações de faltas.
- **Exportação**:
  - Gera um arquivo `faltas.json` com informações de frequência.

**Exemplo de Faltas**:

| Disciplina | Carga Horária | Faltas | Observação |
|------------|---------------|--------|------------|
| DESENVOLVIMENTO WEB FULL STACK - 4139.1.01 | 40 aula(s) | 0 falta(s) (0.00%) |  |
| INTERAÇÃO HUMANO-COMPUTADOR - 3172.1.00 | 80 aula(s) | 2 falta(s) (2.50%) |  |
| LABORATÓRIO DE DESENVOLVIMENTO DE SOFTWARE - 3134.1.01 | 40 aula(s) | 0 falta(s) (0.00%) |  |
| PROJETO DE SOFTWARE - 3133.1.00 | 80 aula(s) | 0 falta(s) (0.00%) |  |
| REDES DE COMPUTADORES - 3138.1.00 | 80 aula(s) | 2 falta(s) (2.50%) |  |
| TEORIA DOS GRAFOS E COMPUTABILIDADE - 3132.1.01 | 80 aula(s) | 0 falta(s) (0.00%) |  |
| TRABALHO INTERDISCIPLINAR: APLICAÇÕES PARA SUSTENTABILIDADE - 3170.1.02 | 40 aula(s) | 0 falta(s) (0.00%) |  |

---

## Funcionalidades da versão 2 - **Faltas e Notas**

- **Login Automático**: Realiza login no portal do estudante da PUC Minas.
- **Extração de Dados**:
  - Navega até a página de notas e frequência.
  - Extrai informações de disciplinas, faltas e notas.
- **Cálculo Automático**:
  - Soma as notas de cada disciplina, facilitando a visualização do desempenho total.
- **Exportação**:
  - Gera arquivos `faltas.json` e `notas.json` com informações de frequência e notas.

**Exemplo de Notas**:

| Disciplina | Data | Descrição | Valor Máximo | Valor Obtido |
|------------|------|-----------|--------------|--------------|
| DESENVOLVIMENTO WEB FULL STACK - 4139.1.01 | 03/09/2025 | Somatório das Avaliações | 98.00 | 0.00 (0%) |
| INTERAÇÃO HUMANO-COMPUTADOR - 3172.1.00 | 03/09/2025 | Somatório das Avaliações | 100.00 | 17.00 (17%) |
| LABORATÓRIO DE DESENVOLVIMENTO DE SOFTWARE - 3134.1.01 | 03/09/2025 | Somatório das Avaliações | 95.00 | 0.00 (0%) |
| PROJETO DE SOFTWARE - 3133.1.00 | 03/09/2025 | Somatório das Avaliações | 35.00 | 0.00 (0%) |
| REDES DE COMPUTADORES - 3138.1.00 | 03/09/2025 | Somatório das Avaliações | 5.00 | 0.00 (0%) |
| TEORIA DOS GRAFOS E COMPUTABILIDADE - 3132.1.01 | 03/09/2025 | Somatório das Avaliações | 75.00 | 0.00 (0%) |
| TRABALHO INTERDISCIPLINAR: APLICAÇÕES PARA SUSTENTABILIDADE - 3170.1.02 | 03/09/2025 | Somatório das Avaliações | 100.00 | 0.00 (0%) |

---

## Funcionalidades da versão 3 - **Faltas, Notas e Credenciais**

- **Login Automático**: Realiza login no portal do estudante da PUC Minas.
- **Extração de Dados**:
  - Navega até a página de notas, frequência e credenciais.
  - Extrai informações de disciplinas, faltas, notas e credenciais de serviços institucionais.
- **Cálculo Automático**:
  - Soma as notas de cada disciplina, facilitando a visualização do desempenho total.
- **Exportação**:
  - Gera arquivos `faltas.json`, `notas.json` e `credenciais.json` com todas as informações.
- **Credenciais de Serviços**:
  - Permite visualizar facilmente os logins de diversos serviços da PUC Minas, como:

| Título | Credencial |
|--------|------------|
| PUC Mail | Login: matricula@sga.pucminas.br |
| Office 365/Teams | Login: matricula@sga.pucminas.br |
| Canvas | Login Microsoft: matricula@sga.pucminas.br |
| Rede Wifi | Login: matricula@pucminas.br |
| Portal CAPES | Login: matricula |
| Laboratórios acadêmicos | Login: matricula |
| Microsoft Azure Dev Tools For Teaching | Login: Usuário de e-mail@sga.pucminas.br. Em caso de problemas acesse: [http://icei.pucminas.br/microsoft-azure/](http://icei.pucminas.br/microsoft-azure/) |

## Requisitos

- Python 3.8 ou superior
- Bibliotecas necessárias:
  - `requests`
  - `beautifulsoup4`
  - `lxml`
  
Você pode instalar as dependências com o comando:
```bash
pip install requests beautifulsoup4 lxml
```

## Como utilizar

### 1. Configuração Inicial

Substitua SUA MATRICULA e SUA SENHA na variável formdata com as credenciais do SGA.

### 2. Execução do código

Para executar o código e gerar a imagem a partir do texto especificado, basta utilizar o seguinte comando no terminal:

```bash
python3 sga_v3.py
```

Certifique-se de que você esteja no diretório onde o arquivo sga.py está localizado e que o ambiente virtual esteja ativado, caso você esteja usando um.

### 3. Saídas

Os arquivos `faltas.json`, `notas.json` e `credenciais.json` serão gerados na pasta do projeto contendo as informações do SGA.

## Ambiente Virtual

É recomendável usar um ambiente virtual para gerenciar suas dependências. Siga os passos abaixo para configurar um ambiente virtual:

1. Crie um ambiente virtual usando o seguinte comando:
    ```bash
    python3 -m venv .venv
    ```
2. Ative o ambiente virtual:
    - No macOS e Linux:
        ```bash
        source .venv/bin/activate
        ```
    - No Windows:
        ```bash
        .venv\Scripts\activate
        ```

## Documentação e links úteis

- [Requests - PyPI](https://pypi.org/project/requests/)
- [Beautiful Soup 4 - PyPI](https://pypi.org/project/beautifulsoup4/)
- [Documentação oficial do Beautiful Soup 4](https://beautiful-soup-4.readthedocs.io/en/latest/)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto é distribuído sob a MIT License.
