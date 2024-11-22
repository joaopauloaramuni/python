# Projeto API Football

Este projeto utiliza a API Football para acessar dados sobre as ligas de futebol brasileiras, filtrando especificamente pelas ligas desejadas: "Serie A", "Serie B", "Copa Do Brasil" e "Mineiro - 1". A API permite acessar informações sobre os próximos jogos de cada uma dessas ligas.

## Request

- GET : https://v3.football.api-sports.io

## Exemplo de saída no terminal

### Liga: Serie A (2024)
#### Próximos jogos:
  - 2024-11-21T23:00:00+00:00: Vasco DA Gama vs Internacional
  - 2024-11-23T00:30:00+00:00: Fluminense vs Fortaleza EC
  - 2024-11-23T22:30:00+00:00: Botafogo vs Vitoria
  - 2024-11-23T22:30:00+00:00: Atletico Goianiense vs Palmeiras
  - 2024-11-23T22:30:00+00:00: Juventude vs Cuiaba
  - 2024-11-24T00:30:00+00:00: Sao Paulo vs Atletico-MG
  - 2024-11-24T19:00:00+00:00: Internacional vs RB Bragantino
  - 2024-11-24T19:00:00+00:00: Bahia vs Atletico Paranaense
  - 2024-11-24T19:00:00+00:00: Corinthians vs Vasco DA Gama
  - 2024-11-26T22:00:00+00:00: Fluminense vs Criciuma

### Liga: Serie B (2024)
#### Próximos jogos:
  - 2024-11-22T22:00:00+00:00: Coritiba vs Botafogo SP
  - 2024-11-22T23:00:00+00:00: Avai vs Ponte Preta
  - 2024-11-23T00:30:00+00:00: Ituano vs Amazonas
  - 2024-11-24T19:00:00+00:00: CRB vs Operario-PR
  - 2024-11-24T19:00:00+00:00: Paysandu vs Vila Nova
  - 2024-11-24T21:30:00+00:00: Goias vs Novorizontino
  - 2024-11-24T21:30:00+00:00: Guarani Campinas vs Ceara
  - 2024-11-24T21:30:00+00:00: Mirassol vs Chapecoense-sc
  - 2024-11-24T21:30:00+00:00: America Mineiro vs Brusque
  - 2024-11-24T21:30:00+00:00: Sport Recife vs Santos

### Liga: Copa Do Brasil (2024)
#### Próximos jogos:
  - (Nenhum jogo disponível)

### Liga: Mineiro - 1 (2024)
#### Próximos jogos:
  - (Nenhum jogo disponível)

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

- **Filtro de ligas brasileiras**: O projeto é configurado para filtrar as ligas do Brasil, selecionando apenas as ligas "Serie A", "Serie B", "Copa Do Brasil" e "Mineiro - 1".
  
- **Limitação aos 10 próximos jogos**: O código limita a consulta para retornar apenas os 10 próximos jogos de cada liga selecionada.

## Código

### Função `get_brazilian_leagues()`

Essa função faz uma requisição à API para obter as ligas do Brasil e filtra as ligas de acordo com a lista `DESIRED_LEAGUES`.

### Função `get_upcoming_fixtures(league_id)`

Essa função consulta os próximos jogos para a liga informada, limitando-se aos 10 próximos jogos.

### Função `main()`

A função principal faz a chamada das funções anteriores para listar as ligas e seus respectivos próximos jogos.

## Obter a chave da API

Para utilizar a API do Projeto API Football, é necessário criar uma conta no site [API-Football](https://www.api-football.com/). Após se cadastrar, você poderá acessar o painel de controle e obter o seu **API Key** (chave da API), que será usada para autenticar as requisições feitas à API. Insira essa chave no código, substituindo a variável `API_KEY` pelo seu token pessoal. A chave é essencial para garantir que você tenha acesso aos dados da API de forma segura e exclusiva para sua conta.

## Limitação diária de requisições

Ao utilizar a API do Projeto API Football, é importante estar ciente da limitação diária de requisições imposta pelo serviço. Cada conta possui um número máximo de requisições que podem ser feitas por dia, dependendo do plano escolhido. Para garantir o funcionamento contínuo da aplicação, é recomendável monitorar o número de requisições realizadas e, caso necessário, ajustar a frequência de chamadas para não exceder o limite. Mais informações sobre as limitações de requisições podem ser consultadas na [documentação oficial](https://www.api-football.com/documentation-v3#section/Introduction).

## Documentação e Links Úteis

- [Documentação da API](https://www.api-football.com/documentation-v3#section/Introduction)
- [API Tester](https://dashboard.api-football.com/soccer/tester)

## Licença

Este projeto está licenciado sob a Licença MIT.
