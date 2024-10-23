# Relatório técnico: Análise de repositórios populares que utilizam microsserviços no GitHub

## Objetivo
O objetivo deste experimento é coletar e analisar características de repositórios populares no GitHub que implementam a arquitetura de microsserviços. Os principais parâmetros analisados incluem estrelas, forks, commits, watchers, pull requests, data do último commit, linguagem principal, licença, contribuidores, tamanho, ramo principal, releases, issues fechadas e tópicos.

## Linguagem de programação
Python 3 foi a linguagem escolhida para desenvolver o experimento.

## Dependências
Para executar este experimento, as seguintes dependências foram utilizadas:
- `requests` (para fazer requisições HTTP à API do GitHub)
- `numpy` (para realizar operações matemáticas, como normalização)

## API Utilizada
Foi utilizada a GitHub API para coletar os dados necessários dos repositórios. Mais detalhes sobre a API podem ser encontrados na documentação do GitHub REST API.
- [GitHub REST API Documentation](https://docs.github.com/pt/rest?apiVersion=2022-11-28)

## Metodologia
- **Coleta de Dados:** Foi utilizada a GitHub API para obter informações detalhadas dos repositórios que incluem a palavra-chave "microservices" em seus tópicos ou descrições. Como restrição do experimento, a coleta não inclui repositórios que implementam microsserviços, mas que não mencionam explicitamente a palavra-chave microservices em nenhum lugar.
- **Filtragem e Paginação:** A coleta de dados envolveu a utilização da paginação da API do GitHub devido ao grande número de informações nos repositórios mais relevantes. Esse processo pode levar em média 30 minutos para terminar devido à necessidade de lidar com múltiplas requisições e alto volume de dados.
- **Normalização de Dados:** Os dados foram normalizados usando a técnica de min-max scaling, garantindo que todos os valores estivessem na mesma escala para o cálculo da pontuação composta.
- **Cálculo da Pontuação Composta:** Foi utilizado um método de combinação linear ponderada (scores) para calcular uma pontuação composta para cada repositório, levando em consideração tanto as estrelas quanto os forks.
- **Ordenação dos Repositórios:** Os repositórios foram ordenados em ordem decrescente com base na pontuação composta calculada.

## Resultados
Considerando estrelas e forks, os seguintes repositórios foram ranqueados como os mais populares que utilizam a arquitetura de microsserviços:

| Ranking | Repositório                  | Stars | Forks | Score  | Novo Ranking |
|---------|------------------------------|-------|-------|--------|--------------|
| 1       | nodebestpractices            | 97090 | 9864  | 0.6508 | 1            |
| 2       | dubbo                        | 40191 | 26331 | 0.5878 | 3 → 2        |
| 3       | nest                         | 65393 | 7447  | 0.3700 | 2 → 3        |
| 4       | nacos                        | 29396 | 12650 | 0.2195 | 8 → 4        |
| 5       | apollo                       | 28908 | 10186 | 0.1638 | 9 → 5        |
| 6       | istio                        | 35312 | 7618  | 0.1557 | 6            |
| 7       | kong                         | 38213 | 4747  | 0.1158 | 4 → 7        |
| 8       | awesome-design-patterns      | 37357 | 2752  | 0.0673 | 5 → 8        |
| 9       | go-zero                      | 28063 | 3826  | 0.0228 | 10 → 9       |
| 10      | system-design                | 30105 | 3095  | 0.0221 | 7 → 10       |

## Conclusão
Este experimento demonstrou a viabilidade de coletar e analisar dados de repositórios populares no GitHub que implementam microsserviços. A metodologia utilizada permitiu identificar e ranquear os principais repositórios com base em critérios objetivos como estrelas e forks, apesar da limitação de apenas considerar repositórios que explicitamente mencionam "microservices" em seus metadados. O algoritmo de ranqueamento leva em média 30 minutos para rodar devido à necessidade de lidar com a paginação da API do GitHub, enquanto o algoritmo de cálculos estatísticos é instantâneo, pois os repositórios são fixos no código.
