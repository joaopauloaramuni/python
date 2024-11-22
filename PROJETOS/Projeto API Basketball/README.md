# Projeto NBA Games API

Este projeto utiliza a **NBA API** para acessar dados sobre os próximos jogos da NBA, ordenados pela data mais próxima. A aplicação realiza requisições à API para listar os jogos de uma data específica, exibindo informações detalhadas como times, status do jogo, local e cidade.

## Request

- GET : https://v2.nba.api-sports.io

## Exemplo de saída no terminal

### Próximos jogos da NBA:

- 2024-11-22T00:00:00.000Z | Charlotte Hornets vs Detroit Pistons
  Status: In Play | Local: Spectrum Center, Charlotte

- 2024-11-22T00:30:00.000Z | Toronto Raptors vs Minnesota Timberwolves
  Status: In Play | Local: Scotiabank Arena, Toronto

- 2024-11-22T01:00:00.000Z | San Antonio Spurs vs Utah Jazz
  Status: In Play | Local: Frost Bank Center, San Antonio

- 2024-11-22T03:30:00.000Z | Los Angeles Lakers vs Orlando Magic
  Status: Scheduled | Local: crypto.com Arena, Los Angeles

## Dependências

Este projeto utiliza a biblioteca `requests` para fazer requisições HTTP à API.

### Para instalar a dependência:

Execute o seguinte comando:

```
pip install requests
```

## Ambiente Virtual (venv)

É recomendado criar um ambiente virtual para isolar as dependências do projeto. Para isso, siga os passos abaixo:

1. **Criar o ambiente virtual**:
   ```
   python -m venv venv
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

3. **Instalar as dependências**:
   Após ativar o ambiente virtual, instale as dependências com:
   ```
   pip install requests
   ```

## Funcionalidades

- **Próximos jogos da NBA**: O projeto retorna os jogos programados para a data especificada, ordenados pela data e hora do jogo.
- **Exibição detalhada**: Informações incluem times, status do jogo, local e cidade.

## Código

### Função `get_games(date)`

Essa função faz uma requisição à API para obter os jogos de uma data específica e retorna os dados processados.

### Função `display_games(games)`

Essa função exibe os jogos ordenados pela data mais próxima.

### Função `main()`

A função principal chama as funções anteriores para listar os jogos da NBA em uma data específica.

## Obter a chave da API

Para utilizar a API do Projeto NBA API, é necessário criar uma conta no site [API-Football](https://www.api-football.com/). Após se cadastrar, você poderá acessar o painel de controle e obter o seu **API Key** (chave da API), que será usada para autenticar as requisições feitas à API. Insira essa chave no código, substituindo a variável `API_KEY` pelo seu token pessoal.

## Limitação diária de requisições

Ao utilizar a API do Projeto NBA API, é importante estar ciente da limitação diária de requisições imposta pelo serviço. Cada conta possui um número máximo de requisições que podem ser feitas por dia, dependendo do plano escolhido. Para garantir o funcionamento contínuo da aplicação, é recomendável monitorar o número de requisições realizadas e, caso necessário, ajustar a frequência de chamadas para não exceder o limite. Mais informações sobre as limitações de requisições podem ser consultadas na [documentação oficial](https://api-sports.io/documentation/nba/v2#section/Introduction).

## Documentação e Links Úteis

- [Documentação da NBA API](https://api-sports.io/documentation/nba/v2#section/Introduction)
- [API Tester](https://dashboard.api-football.com/nba/tester)

## Licença

Este projeto está licenciado sob a Licença MIT.
