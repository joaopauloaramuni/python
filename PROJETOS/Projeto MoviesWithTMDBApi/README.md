# Projeto MoviesWithTMDBApi

Este projeto utiliza a API do The Movie Database (TMDb) para buscar informações sobre filmes populares e sugerir filmes semelhantes com base nos gêneros dos filmes pesquisados.

## Dependências

- requests: Biblioteca para fazer requisições HTTP.

## Como Criar o Ambiente Virtual

### No macOS / Linux:
1. Crie o ambiente virtual:
   ```bash
   python3 -m venv venv
   ```
2. **Ativar o ambiente virtual**:
   - No Windows:
     ```
     .venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```
     source venv/bin/activate
     ```
3. Instale as dependências:
   ```bash
   pip install requests
   ```

## Funções

### `fetch_movie_details(api_key, movie_name)`
Esta função busca as informações de um filme com base no nome fornecido, retornando os dados do primeiro filme encontrado na busca.

- **Parâmetros**:
  - `api_key`: A chave da API TMDb.
  - `movie_name`: O nome do filme a ser pesquisado.

- **Retorno**:
  - Um dicionário com os detalhes do filme, incluindo título, ID e gêneros.

### `fetch_similar_movies(api_key, genre_ids)`
Esta função busca filmes populares e bem avaliados com base no(s) gênero(s) fornecido(s).

- **Parâmetros**:
  - `api_key`: A chave da API TMDb.
  - `genre_ids`: Uma lista com os IDs dos gêneros dos filmes.

- **Retorno**:
  - Uma lista com os 10 filmes mais populares e bem avaliados do mesmo gênero.

## Exemplo de Chamadas para a API

1. Buscar filmes populares:
   ```bash
   https://api.themoviedb.org/3/movie/popular?api_key=suaapitokenaqui
   ```

2. Buscar filmes por nome (exemplo: Harry Potter):
   ```bash
   https://api.themoviedb.org/3/search/movie?api_key=suaapitokenaqui&query=Harry+Potter&language=pt-BR
   ```

## Documentação e Links Úteis

- [TMDb](https://www.themoviedb.org/)
- [Configuração da API TMDb](https://www.themoviedb.org/settings/api)
- [Documentação da API TMDb](https://api.themoviedb.org/3/)

## Licença

Este projeto está licenciado sob a Licença MIT.
