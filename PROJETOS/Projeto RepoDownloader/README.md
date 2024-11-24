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

Antes de executar o script principal do projeto, você precisa configurar algumas variáveis. 

1. Substitua os valores das seguintes variáveis no script:

```
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

O script irá acessar a API do GitHub, listar os repositórios do usuário configurado e fazer o download deles, seja via `git clone` ou como arquivos ZIP.

Por padrão, o script efetua o download como arquivos ZIP.

```
# download_repo(repo_url, repo_name)
download_repo_zip(repo_url, repo_name)
```

## Exemplo de como recuperar os repositórios usando a API do GitHub

Para recuperar os repositórios públicos de um usuário no GitHub, você pode usar uma URL da API semelhante a esta:

GET <a href="https://api.github.com/users/joaopauloaramuni/repos">https://api.github.com/users/joaopauloaramuni/repos</a>

### Resultado esperado (exemplo de um repo)

```json
[
  {
    "id": 882503612,
    "node_id": "R_kgDONJnvvA",
    "name": "actionscript",
    "full_name": "joaopauloaramuni/actionscript",
    "private": false,
    "owner": {
      "login": "joaopauloaramuni",
      "id": 58268075,
      "node_id": "MDQ6VXNlcjU4MjY4MDc1",
      "avatar_url": "https://avatars.githubusercontent.com/u/58268075?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/joaopauloaramuni",
      "html_url": "https://github.com/joaopauloaramuni",
      "followers_url": "https://api.github.com/users/joaopauloaramuni/followers",
      "following_url": "https://api.github.com/users/joaopauloaramuni/following{/other_user}",
      "gists_url": "https://api.github.com/users/joaopauloaramuni/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/joaopauloaramuni/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/joaopauloaramuni/subscriptions",
      "organizations_url": "https://api.github.com/users/joaopauloaramuni/orgs",
      "repos_url": "https://api.github.com/users/joaopauloaramuni/repos",
      "events_url": "https://api.github.com/users/joaopauloaramuni/events{/privacy}",
      "received_events_url": "https://api.github.com/users/joaopauloaramuni/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "html_url": "https://github.com/joaopauloaramuni/actionscript",
    "description": "Repo ActionScript",
    "fork": false,
    "url": "https://api.github.com/repos/joaopauloaramuni/actionscript",
    "forks_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/forks",
    "keys_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/teams",
    "hooks_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/hooks",
    "issue_events_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/issues/events{/number}",
    "events_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/events",
    "assignees_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/assignees{/user}",
    "branches_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/branches{/branch}",
    "tags_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/tags",
    "blobs_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/languages",
    "stargazers_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/stargazers",
    "contributors_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/contributors",
    "subscribers_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/subscribers",
    "subscription_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/subscription",
    "commits_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/contents/{+path}",
    "compare_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/merges",
    "archive_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/downloads",
    "issues_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/issues{/number}",
    "pulls_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/labels{/name}",
    "releases_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/releases{/id}",
    "deployments_url": "https://api.github.com/repos/joaopauloaramuni/actionscript/deployments",
    "created_at": "2024-11-03T00:16:19Z",
    "updated_at": "2024-11-21T23:00:45Z",
    "pushed_at": "2024-11-21T16:11:53Z",
    "git_url": "git://github.com/joaopauloaramuni/actionscript.git",
    "ssh_url": "git@github.com:joaopauloaramuni/actionscript.git",
    "clone_url": "https://github.com/joaopauloaramuni/actionscript.git",
    "svn_url": "https://github.com/joaopauloaramuni/actionscript",
    "homepage": "",
    "size": 87543,
    "stargazers_count": 7,
    "watchers_count": 7,
    "language": "ActionScript",
    "has_issues": true,
    "has_projects": true,
    "has_downloads": true,
    "has_wiki": true,
    "has_pages": false,
    "has_discussions": false,
    "forks_count": 0,
    "mirror_url": null,
    "archived": false,
    "disabled": false,
    "open_issues_count": 0,
    "license": {
      "key": "mit",
      "name": "MIT License",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit",
      "node_id": "MDc6TGljZW5zZTEz"
    },
    "allow_forking": true,
    "is_template": false,
    "web_commit_signoff_required": false,
    "topics": [
      "actionscript"
    ],
    "visibility": "public",
    "forks": 0,
    "open_issues": 0,
    "watchers": 7,
    "default_branch": "main"
  }
```

## Links úteis

- [GitHub API Documentation](https://docs.github.com/pt/rest/about-the-rest-api)
- [GitHub Personal Access Tokens](https://github.com/settings/tokens)
- [Requests no PyPI](https://pypi.org/project/requests/)

## Licença

Este projeto está licenciado sob a **Licença MIT**.
