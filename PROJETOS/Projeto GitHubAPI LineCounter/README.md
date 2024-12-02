# Projeto GitHubAPI LineCounter

Este projeto utiliza a API do GitHub para realizar uma análise detalhada dos repositórios de um usuário. Ele conta as linhas de código para uma ampla variedade de linguagens de programação, incluindo Java, Python e muitas outras, bem como as linhas de SQL e Markdown, que são contabilizadas separadamente.

O script mede o tempo necessário para processar cada repositório utilizando a biblioteca time, permitindo identificar a eficiência e o desempenho da execução. É importante destacar que as linhas de SQL e Markdown são reportadas individualmente e não somam ao total de linhas de código principal (code_lines). Isso garante uma classificação mais precisa dos dados analisados.

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

## Uso do parâmetro `per_page`

Ao fazer requisições à API do GitHub para coletar informações sobre repositórios, o parâmetro `per_page` controla o número de itens retornados por página. O valor máximo permitido para esse parâmetro é 100, o que significa que podemos retornar até 100 repositórios em uma única requisição.

Exemplo de código:

```python
# Definir o parâmetro per_page para 100, que é o máximo de repositórios retornados em uma requisição
response = requests.get(API_URL, headers=headers, params={'per_page': 100})
```

Neste exemplo, ao configurar o parâmetro per_page como 100, garantimos que a API retorne até 100 repositórios por vez, otimizando a coleta de dados e evitando múltiplas requisições em casos de grande volume de repositórios.

## Exemplo de como recuperar os repositórios usando a API do GitHub

Para recuperar os repositórios públicos de um usuário no GitHub, você pode usar uma URL da API semelhante a esta:

GET <a href="https://api.github.com/users/joaopauloaramuni/repos">https://api.github.com/users/joaopauloaramuni/repos</a>

# Exemplo de Saída

```
******************************************************************************************************************************
Obtendo a lista de repositórios...

Extensões consideradas para análise:
  Código: .cs, .kt, .java, .rs, .c, .css, .scala, .js, .pas, .rb, .cpp, .swift, .go, .vbs, .py, .sh, .php, .html, .ts, .dart
  SQL: .sql
  Markdown: .md

Total de repositórios encontrados: 37

******************************************************************************************************************************
Processando repositório: actionscript...
Arquivo processado: README.md, Linhas contadas: 42
Tempo para processar actionscript: 0.73 segundos
Linguagem fora da lista no repositório actionscript

******************************************************************************************************************************
Processando repositório: algoritmos-e-estruturas-de-dados-i...
Arquivo processado: PROJETOS/Prj_ASCII_Clock/src/Prj_ASCII_Clock.c, Linhas contadas: 70
Arquivo processado: PROJETOS/Prj_Aramuni_Recursivo/src/Prj_Aramuni_Recursivo.c, Linhas contadas: 248
Arquivo processado: PROJETOS/Prj_Array_Ex1/src/Prj_Array_Ex1.c, Linhas contadas: 35
Arquivo processado: PROJETOS/Prj_Array_Ex2/src/Prj_Array_Ex2.c, Linhas contadas: 43
Arquivo processado: PROJETOS/Prj_Array_Exer1/src/Prj_Array_Exer1.c, Linhas contadas: 33
Arquivo processado: PROJETOS/Prj_Array_Exer2/src/Prj_Array_Exer2.c, Linhas contadas: 28
Arquivo processado: PROJETOS/Prj_Array_Exer3/src/Prj_Array_Exer3.c, Linhas contadas: 34
Arquivo processado: PROJETOS/Prj_ByVal_ByRef/src/Prj_ByVal_ByRef.c, Linhas contadas: 34

...

Tempo para processar algoritmos-e-estruturas-de-dados-i: 50.89 segundos
Linhas encontradas no repositório algoritmos-e-estruturas-de-dados-i:
  Linhas de código: 5825
  Linhas de Markdown: 37

******************************************************************************************************************************

...

--- Resultado Final ---
  Total de linhas de código: 272575
  Total de linhas de Markdown: 26418
  Total de linhas de código Java: 116994
  Total de linhas de código Python: 7005
  Total de linhas de código SQL: 3787

```

## Links úteis

- [GitHub API Documentation](https://docs.github.com/pt/rest/about-the-rest-api)
- [GitHub Repositories API](https://docs.github.com/pt/rest/repos/repos)
- [Usando paginação na API REST do GitHub](https://docs.github.com/pt/rest/using-the-rest-api/using-pagination-in-the-rest-api)
- [GitHub Personal Access Tokens](https://github.com/settings/tokens)
- [Requests no PyPI](https://pypi.org/project/requests/)

## Licença

Este projeto está licenciado sob a **Licença MIT**.
