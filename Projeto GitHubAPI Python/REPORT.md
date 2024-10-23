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
- **Coleta de dados:** Foi utilizada a GitHub API para obter informações detalhadas dos repositórios que incluem a palavra-chave "microservices" em seus tópicos ou descrições. Como restrição do experimento, a coleta não inclui repositórios que implementam microsserviços, mas que não mencionam explicitamente a palavra-chave microservices em nenhum lugar.
- **Filtragem e paginação:** A coleta de dados envolveu a utilização da paginação da API do GitHub devido ao grande número de informações nos repositórios mais relevantes. Esse processo pode levar em média 30 minutos para terminar devido à necessidade de lidar com múltiplas requisições e alto volume de dados.
- **Normalização de dados:** Os dados foram normalizados usando a técnica de min-max scaling, garantindo que todos os valores estivessem na mesma escala para o cálculo da pontuação composta.
- **Cálculo da pontuação composta:** Foi utilizado um método de combinação linear ponderada (scores) para calcular uma pontuação composta para cada repositório, levando em consideração tanto as estrelas quanto os forks.
- **Ordenação dos Repositórios:** Os repositórios foram ordenados em ordem decrescente com base na pontuação composta calculada.

## Busca de repositórios no GitHub com a palavra-chave "microservices"

Esta funcionalidade utiliza a API do GitHub para buscar repositórios que tenham relação com a palavra-chave `microservices`. A busca é feita de acordo com diferentes critérios, como nome do repositório, descrição, README, e tópicos associados. Abaixo estão os detalhes de como cada critério é utilizado:

### URL da API

A busca é realizada através do seguinte endpoint da API do GitHub:

https://api.github.com/search/repositories?q={keyword}&sort=stars&order=desc&per_page={num_repos}

- **keyword**: palavra-chave usada na busca (neste caso, `"microservices"`).
- **num_repos**: número de repositórios a serem retornados.

### Critérios de busca

1. **Nome do repositório**: 
   - Repositórios cujo nome contém a palavra-chave `microservices`.

2. **Descrição do repositório**: 
   - Repositórios cuja descrição menciona a palavra-chave `microservices`.

3. **README**:
   - Repositórios cujo arquivo `README` contém a palavra-chave `microservices`.

4. **Tópicos do repositório**:
   - Repositórios que possuem tópicos (tags) associadas que contêm a palavra-chave `microservices`.

### Exemplo de uso

Para buscar os 10 repositórios mais populares relacionados a microservices:

https://api.github.com/search/repositories?q=microservices&sort=stars&order=desc&per_page=10

Essa consulta retornará os repositórios ordenados por número de estrelas em ordem decrescente.

## Análise

### Top 10 repositórios com microsserviços (ordenados por Stars)

Resultado bruto:

| Ranking | Repositório                  | Stars |
|---------|------------------------------|-------|
| 1       | [nodebestpractices](https://github.com/goldbergyoni/nodebestpractices) | 97090 |
| 2       | [nest](https://github.com/nestjs/nest)                              | 65393 |
| 3       | [dubbo](https://github.com/apache/dubbo)                            | 40191 |
| 4       | [kong](https://github.com/Kong/kong)                                 | 38213 |
| 5       | [awesome-design-patterns](https://github.com/DovAmir/awesome-design-patterns) | 37357 |
| 6       | [istio](https://github.com/istio/istio)                              | 35312 |
| 7       | [system-design](https://github.com/madd86/awesome-system-design)     | 30105 |
| 8       | [nacos](https://github.com/alibaba/nacos)                            | 29396 |
| 9       | [apollo](https://github.com/apolloconfig/apollo)                     | 28908 |
| 10      | [go-zero](https://github.com/zeromicro/go-zero)                      | 28063 |

### Stars + Forks
Para realizar uma análise mais completa que considere tanto o número de estrelas (stars) quanto o número de forks, podemos aplicar um teste estatístico que combine ambas as variáveis. Podemos usar uma pontuação composta que pondera ambos os fatores.

Vamos considerar repositórios mais populares como:

Stars + Forks

• 1) Normalização dos dados: Primeiro, normalizamos os dados para que as duas variáveis estejam na mesma escala.
• 2) Cálculo da pontuação composta: Em seguida, calculamos uma pontuação composta para cada repositório.
• 3) Ordenação dos repositórios: Finalmente, ordenamos os repositórios com base na pontuação composta.

1) Normalização dos dados: A normalização pode ser feita utilizando a técnica de min-max scaling:

   $$
   X' = \frac{X - X_{min}}{X_{max} - X_{min}}
   $$
   
   onde 𝑋′ é o valor normalizado, 𝑋 é o valor original, 𝑋𝑚𝑖𝑛 é o valor mínimo do conjunto de dados e 𝑋𝑚𝑎𝑥 é o valor máximo do conjunto de dados.

2) Cálculo da pontuação composta:
• Vamos atribuir pesos iguais para ambas as variáveis (estrelas e forks) para simplificar:
• Combinação linear ponderada: scores = 0.5 × normalized_stars + 0.5 × normalized_forks

3) Ordenação dos repositórios: Os repositórios serão ordenados de acordo com a pontuação composta.

## Resultados
Considerando stars e forks, os seguintes repositórios foram ranqueados como os mais populares que utilizam a arquitetura de microsserviços:

| Ranking | Repositório                  | Stars | Forks | Score  | Novo ranking | Movimentação     |
|---------|------------------------------|-------|-------|--------|--------------|------------------|
| 1       | [nodebestpractices](https://github.com/goldbergyoni/nodebestpractices) | 97090 | 9864  | 0.6508 | 1            | -                |
| 2       | [dubbo](https://github.com/apache/dubbo)                            | 40191 | 26331 | 0.5878 | 3 → 2        | ⬆                |
| 3       | [nest](https://github.com/nestjs/nest)                              | 65393 | 7447  | 0.3700 | 2 → 3        | ⬇                |
| 4       | [nacos](https://github.com/alibaba/nacos)                            | 29396 | 12650 | 0.2195 | 8 → 4        | ⬆                |
| 5       | [apollo](https://github.com/apolloconfig/apollo)                     | 28908 | 10186 | 0.1638 | 9 → 5        | ⬆                |
| 6       | [istio](https://github.com/istio/istio)                              | 35312 | 7618  | 0.1557 | 6            | -                |
| 7       | [kong](https://github.com/Kong/kong)                                 | 38213 | 4747  | 0.1158 | 4 → 7        | ⬇                |
| 8       | [awesome-design-patterns](https://github.com/DovAmir/awesome-design-patterns) | 37357 | 2752  | 0.0673 | 5 → 8        | ⬇                |
| 9       | [go-zero](https://github.com/zeromicro/go-zero)                      | 28063 | 3826  | 0.0228 | 10 → 9       | ⬆                |
| 10      | [system-design](https://github.com/madd86/awesome-system-design)     | 30105 | 3095  | 0.0221 | 7 → 10       | ⬇                |

### Tempo médio de execução

Devido à paginação dos resultados retornados pela API do GitHub, o script tem um **tempo médio de execução de aproximadamente 30 minutos**. Esse tempo pode variar conforme o número de repositórios processados e o limite de resultados por página.

## Conclusão
Este experimento demonstrou a viabilidade de coletar e analisar dados de repositórios populares no GitHub que implementam microsserviços. A metodologia utilizada permitiu identificar e ranquear os principais repositórios com base em critérios objetivos como estrelas e forks, apesar da limitação de apenas considerar repositórios que explicitamente mencionam "microservices" em seus metadados. O algoritmo de ranqueamento leva em média 30 minutos para rodar devido à necessidade de lidar com a paginação da API do GitHub, enquanto o algoritmo de cálculos estatísticos é instantâneo, pois os repositórios são fixos no código.
