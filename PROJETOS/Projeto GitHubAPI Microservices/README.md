# Coleta de dados dos Top 10 repositórios mais populares que utilizam microsserviços

Este projeto tem como objetivo coletar dados e métricas dos 10 repositórios mais populares no GitHub que utilizam microsserviços. As informações coletadas incluem número de estrelas, forks, pull requests, issues, último release e linguagens utilizadas. Além disso, as métricas serão normalizadas e uma pontuação composta será calculada para cada repositório.

## Funcionalidades

- Coleta de dados dos 10 repositórios mais populares que mencionam o termo "microservices".
- Utilização da API REST do GitHub para obter detalhes dos repositórios.
- Normalização das métricas coletadas.
- Cálculo de uma pontuação composta baseada em stars e forks.

## Requisitos do projeto

- Python 3.11.0 ou superior
- Token de autenticação GitHub
- Pacotes Python: `requests` e `numpy`

### Versões
- Python==3.11.0
- requests==2.32.3
- numpy==2.1.2

## Preparação do ambiente

1. **Clone o repositório** (se ainda não o fez):
   ```bash
   git clone https://github.com/joaopauloaramuni/python.git
   cd python/Projeto GitHubAPI Python
   ```
   
2. **Instalação do Python 3**
   - Certifique-se de ter o Python 3 instalado em sua máquina.

3. **(Virtual env) Criação do ambiente virtual**
   ```bash
   python3 -m venv .venv
   ```

4. **(Virtual env) Ativação do ambiente virtual**
   ```bash
   source .venv/bin/activate  # Para usuários de Linux/macOS
   .venv\Scripts\activate  # Para usuários de Windows
   ```

5. **(Dependências) Instalação da biblioteca requests**
   ```bash
   pip3 install requests
   pip3 install numpy
   ```
   ou
   ```bash
   pip3 install -r requirements.txt
   ```

6. **Geração de token de acesso**
   - Crie um token de acesso pessoal no GitHub nas configurações de desenvolvedor: [GitHub Tokens](https://github.com/settings/tokens)

7. **Adicione o token ao código**
   - Adicione o token gerado em main.py:
   
   ```python
   # Adicione seu token de acesso pessoal aqui
   token = "token"
   ```

8. **Documentação da API REST do GitHub**
   - Consulte a documentação da API REST do GitHub para mais informações: [Documentação da API GitHub](https://docs.github.com/pt/rest?apiVersion=2022-11-28)

## Uso

Para iniciar a coleta de dados, basta rodar o script principal:

```bash
python3 main.py
```

Em seguida, copie os resultados e cole para o array em stats.py. Feito isso, basta rodar o script de apoio (estatísticas):
```bash
python3 stats.py
```

## Top 10 repositórios com microsserviços (ordenados por Stars)

Resultado bruto:
1. [https://github.com/goldbergyoni/nodebestpractices](https://github.com/goldbergyoni/nodebestpractices)
2. [https://github.com/nestjs/nest](https://github.com/nestjs/nest)
3. [https://github.com/apache/dubbo](https://github.com/apache/dubbo)
4. [https://github.com/Kong/kong](https://github.com/Kong/kong)
5. [https://github.com/DovAmir/awesome-design-patterns](https://github.com/DovAmir/awesome-design-patterns)
6. [https://github.com/istio/istio](https://github.com/istio/istio)
7. [https://github.com/karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design)
8. [https://github.com/alibaba/nacos](https://github.com/alibaba/nacos)
9. [https://github.com/apolloconfig/apollo](https://github.com/apolloconfig/apollo)
10. [https://github.com/zeromicro/go-zero](https://github.com/zeromicro/go-zero)

## Top 10 repositórios com microsserviços (ordenados por Stars + Forks usando score)

1. [https://github.com/goldbergyoni/nodebestpractices](https://github.com/goldbergyoni/nodebestpractices)
2. [https://github.com/apache/dubbo](https://github.com/apache/dubbo)
3. [https://github.com/nestjs/nest](https://github.com/nestjs/nest)
4. [https://github.com/alibaba/nacos](https://github.com/alibaba/nacos)
5. [https://github.com/apolloconfig/apollo](https://github.com/apolloconfig/apollo)
6. [https://github.com/istio/istio](https://github.com/istio/istio)
7. [https://github.com/Kong/kong](https://github.com/Kong/kong)
8. [https://github.com/DovAmir/awesome-design-patterns](https://github.com/DovAmir/awesome-design-patterns)
9. [https://github.com/zeromicro/go-zero](https://github.com/zeromicro/go-zero)
10. [https://github.com/karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design)

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

## Código

## Descrição das funções

## main.py

### `get_popular_repos(keyword, num_repos)`
Esta função busca os repositórios mais populares do GitHub que contêm uma palavra-chave específica, neste caso, "microservices". Utiliza a API do GitHub para realizar a pesquisa e retorna uma lista de repositórios, ordenados por número de estrelas. Os parâmetros incluem a palavra-chave e o número máximo de repositórios a serem retornados.

### `get_repo_details(owner, repo)`
Esta função coleta detalhes específicos sobre um repositório. Recebe o nome do proprietário e o nome do repositório como parâmetros e retorna informações detalhadas, como URL, número de estrelas, forks, linguagem principal, licença, entre outros.

### `get_pull_requests(owner, repo)`
Esta função obtém o número total de pull requests de um repositório, utilizando paginação para garantir que todos os pull requests sejam contados. Recebe o nome do proprietário e o nome do repositório como parâmetros e retorna a contagem total de pull requests.

### `get_releases(owner, repo)`
Semelhante à função anterior, esta função coleta o número total de releases de um repositório. Utiliza paginação para contabilizar corretamente todas as releases. Os parâmetros são o nome do proprietário e o nome do repositório, e a função retorna a contagem total de releases.

### `get_closed_issues(owner, repo)`
Esta função retorna o número de issues fechadas de um repositório, utilizando também paginação para garantir a precisão na contagem. Recebe como parâmetros o nome do proprietário e o nome do repositório e retorna a contagem total de issues fechadas.

### `collect_and_print_repo_info(repos)`
Esta função coleta informações detalhadas sobre cada repositório em uma lista de repositórios e imprime essas informações no console. Para cada repositório, ela chama as funções de detalhes, pull requests, releases e issues fechadas, formatando a saída de maneira legível.

### `__main__`
A seção principal do `main.py` realiza as seguintes funções:

1. **Definição de variáveis**: Define a palavra-chave a ser pesquisada (`keyword`) como "microservices" e o número de repositórios a serem coletados (`num_repos`) como 10.
2. **Chamada de funções**: Tenta obter os repositórios mais populares com a palavra-chave especificada, utilizando a função `get_popular_repos`. Em seguida, chama a função `collect_and_print_repo_info` para exibir as informações coletadas dos repositórios.
3. **Tratamento de exceções**: Caso ocorra uma falha na coleta de dados, captura a exceção e imprime uma mensagem de erro.

## stats.py

## Descrição das funções

### `calculate_scores(repos)`
Esta função calcula uma pontuação composta para uma lista de repositórios com base no número de estrelas e forks.

1. **Extração de dados**: Os dados dos repositórios, como estrelas e forks, são inseridos manualmente em um array no stats.py para análise.
2. **Normalização**: Normaliza os valores de estrelas e forks para uma escala de 0 a 1, utilizando a fórmula de normalização padrão.
3. **Cálculo da pontuação composta**: Calcula a pontuação composta usando uma média ponderada (50% para estrelas e 50% para forks).
4. **Atualização dos repositórios**: Adiciona a pontuação calculada a cada repositório no dicionário.
5. **Ordenação dos repositórios**: Ordena a lista de repositórios com base na pontuação composta, do maior para o menor.

A função retorna a lista de repositórios ordenados.

> **Nota:** Os resultados coletados por `main.py` foram inseridos manualmente no array em `stats.py`.

### `__main__`
A seção principal do `stats.py` executa as seguintes operações:

1. **Definição de dados**: Insere manualmente dados de repositórios em um array, contendo informações sobre o nome, número de estrelas e forks de cada repositório.
2. **Cálculo das pontuações**: Chama a função `calculate_scores` para calcular e ordenar as pontuações dos repositórios com base nas estrelas e forks fornecidos.
3. **Exibição dos resultados**: Itera sobre a lista de repositórios ordenados e imprime informações sobre cada um, incluindo nome, estrelas, forks e a pontuação calculada.

## Relatório técnico

Para uma análise detalhada dos repositórios populares que utilizam microsserviços no GitHub, consulte o [relatório técnico](REPORT.md).

## Licença

Este projeto está licenciado sob a MIT License.

