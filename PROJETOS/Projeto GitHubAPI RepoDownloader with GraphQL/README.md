# Projeto RepoDownloader with GraphQL

Este projeto tem como objetivo baixar os repositórios de um usuário do GitHub, seja através do clone do repositório ou no formato ZIP. O código utiliza a API REST e GraphQL do GitHub para listar os repositórios de um usuário e realiza o download dos mesmos.

## Dependências

- requests - Para fazer requisições HTTP para a API do GitHub.
- gql - Para interagir com a API GraphQL do GitHub.

### Como configurar o ambiente

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

### Instalando as dependências

Para instalar as dependências do projeto, use o seguinte comando:

```bash
pip install requests requests-toolbelt gql
```

### Passo 3: Executar o script

Antes de executar o script principal do projeto, você precisa configurar algumas variáveis. 

1. Substitua os valores das seguintes variáveis no script:

```python
# Seu token do GitHub (crie um token em https://github.com/settings/tokens)
GITHUB_TOKEN = 'seutokenaqui'

# Nome do usuário no GitHub
GITHUB_USERNAME = 'nomedousuarioaqui'
```

- **GITHUB_TOKEN**: Para gerar seu token, vá até [Configurações de Tokens do GitHub](https://github.com/settings/tokens) e crie um novo token com as permissões necessárias. Esse token será usado para autenticar as requisições à API do GitHub.

- **GITHUB_USERNAME**: Aqui você pode colocar seu próprio nome de usuário do GitHub ou o nome de usuário de outra pessoa. Esse valor é usado para buscar os repositórios desse usuário na plataforma.

2. Após configurar essas variáveis, execute o script principal do projeto com o seguinte comando:

```bash
python main.py
```

Isso iniciará a execução do script, que agora estará autenticado com o token fornecido e buscará os repositórios do usuário especificado.

O script irá acessar a API do GitHub, listar os repositórios do usuário configurado e fazer o download deles, seja via git clone ou como arquivos ZIP.

Por padrão, o script efetua o download como arquivos ZIP.

```python
# download_repo(repo_url, repo_name)
download_repo_zip(repo_url, repo_name)
```

## Uso do parâmetro "first" na API GraphQL

Na API GraphQL, o parâmetro "first" substitui o uso de "per_page" para controlar o número de itens retornados por requisição. O valor máximo permitido para esse parâmetro é 100.

Exemplo:

```python
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Query GraphQL para listar repositórios
query = gql("""
query ($username: String!, $first: Int!) {
  user(login: $username) {
    repositories(first: $first) {
      edges {
        node {
          name
          url
        }
      }
    }
  }
}
""")

# Função para configurar o cliente GraphQL
def configure_github_client():
    # Configuração do transporte HTTP com autenticação
    transport = RequestsHTTPTransport(
        url='https://api.github.com/graphql',
        headers={'Authorization': f'bearer {GITHUB_TOKEN}'},
        use_json=True,
    )
    # Criar o cliente GraphQL
    return Client(transport=transport, fetch_schema_from_transport=True)
```

## Exemplo de como recuperar os repositórios usando a API do GitHub

Para recuperar os repositórios públicos de um usuário no GitHub usando GraphQL, você pode usar a seguinte estrutura:

```graphql
{
  user(login: "joaopauloaramuni") {
    repositories(first: 100) {
      nodes {
        name
        url
      }
    }
  }
}
```

## Links úteis

### GraphQL
- [GraphQL.org](https://graphql.org/)
- [gql no PyPI](https://pypi.org/project/gql/)
- [Documentação GraphQL do GitHub](https://docs.github.com/pt/graphql)

### GitHub
- [GitHub API Documentation](https://docs.github.com/pt/rest/about-the-rest-api)
- [GitHub Repositories API](https://docs.github.com/pt/rest/repos/repos)
- [Usando paginação na API REST do GitHub](https://docs.github.com/pt/rest/using-the-rest-api/using-pagination-in-the-rest-api)
- [GitHub Personal Access Tokens](https://github.com/settings/tokens)

### Requests
- [Requests no PyPI](https://pypi.org/project/requests/)

## Licença

Este projeto está licenciado sob a **Licença MIT**.
