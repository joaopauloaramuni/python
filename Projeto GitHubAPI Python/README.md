# Coleta de dados dos Top 10 repositórios mais popular que utilizam microsserviços

Este projeto tem como objetivo coletar dados e métricas dos 10 repositórios mais populares no GitHub que utilizam microsserviços. As informações coletadas incluem número de estrelas, forks, pull requests, issues, último release e linguagens utilizadas. Além disso, as métricas serão normalizadas e uma pontuação composta será calculada para cada repositório.

## Funcionalidades

- Coleta de dados dos 10 repositórios mais populares que mencionam o termo "microservices".
- Utilização da API REST do GitHub para obter detalhes dos repositórios.
- Normalização das métricas coletadas.
- Cálculo de uma pontuação composta baseada em stars e forks.

## Requisitos

- Python 3.8 ou superior
- Token de autenticação GitHub
- Pacotes Python: `requests`, `python-dotenv`, `pandas`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/repositorio-microservices.git
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd repositorio-microservices
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Adicione seu Token GitHub no arquivo de configuração:
   ```bash
   echo "GITHUB_TOKEN=seu_token_aqui" > .env
   ```

## Uso

Para iniciar a coleta de dados dos 10 repositórios mais populares que utilizam microsserviços, execute o seguinte comando:

```bash
python3 main.py
```

O script irá acessar a API do GitHub e coletar as seguintes informações para cada repositório:
- **Nome do repositório**
- **Estrelas**
- **Forks**
- **Pull Requests abertos e fechados**
- **Issues abertas e fechadas**
- **Último release**
- **Linguagens utilizadas**

## Documentação da API REST do GitHub

O projeto faz uso das seguintes rotas da API REST do GitHub:
- `GET /repos/{owner}/{repo}`: Para obter informações detalhadas sobre o repositório.
- `GET /repos/{owner}/{repo}/pulls`: Para listar os pull requests.
- `GET /repos/{owner}/{repo}/issues`: Para listar as issues.
- `GET /repos/{owner}/{repo}/languages`: Para obter as linguagens mais utilizadas.

## Licença

Este projeto está licenciado sob a MIT License.

