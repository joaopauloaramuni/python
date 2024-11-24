# Projeto RepoDownloader

Este projeto tem como objetivo baixar os repositórios de um usuário do GitHub, seja através do clone do repositório ou no formato ZIP. O código utiliza a API REST do GitHub para listar os repositórios de um usuário e realiza o download dos mesmos.

## Dependências

- `requests` - Para fazer requisições HTTP para a API do GitHub.

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
pip install requests
```

### Passo 3: Executar o script

1. Execute o script principal do projeto:

    ```bash
    python main.py
    ```

O script irá acessar a API do GitHub, listar os repositórios do usuário configurado e fazer o download deles, seja via `git clone` ou como arquivos ZIP.

## Exemplo de como eecuperar os repositórios usando a API do GitHub

Para recuperar os repositórios públicos de um usuário no GitHub, você pode usar uma URL da API semelhante a esta:

```
GET https://api.github.com/users/joaopauloaramuni/repos
```

## Links úteis

- [GitHub API Documentation](https://docs.github.com/pt/rest/about-the-rest-api)
- [GitHub Personal Access Tokens](https://github.com/settings/tokens)
- [Requests no PyPI](https://pypi.org/project/requests/)

## Licença

Este projeto está licenciado sob a **Licença MIT**.
