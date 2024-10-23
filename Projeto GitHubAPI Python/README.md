# Coleta de dados dos Top 10 repositórios mais popular que utilizam microsserviços

Este projeto tem como objetivo coletar dados e métricas dos 10 repositórios mais populares no GitHub que utilizam microsserviços. As informações coletadas incluem número de estrelas, forks, pull requests, issues, último release e linguagens utilizadas. Além disso, as métricas serão normalizadas e uma pontuação composta será calculada para cada repositório.

## Funcionalidades

- Coleta de dados dos 10 repositórios mais populares que mencionam o termo "microservices".
- Utilização da API REST do GitHub para obter detalhes dos repositórios.
- Normalização das métricas coletadas.
- Cálculo de uma pontuação composta baseada em stars e forks.

## Requisitos

- Python 3.8 ou superior
- Token de autenticação GitHub
- Pacotes Python: `requests`, `python-dotenv`, `pandas`

## Preparação do Ambiente

1. **Instalação do Python 3**
   - Certifique-se de ter o Python 3 instalado em sua máquina.

2. **(Virtual env) Criação do ambiente virtual**
   ```bash
   python3 -m venv .venv
   ```

3. **(Virtual env) Ativação do ambiente virtual**
   ```bash
   source .venv/bin/activate  # Para usuários de Linux/macOS
   .venv\Scripts\activate  # Para usuários de Windows
   ```

4. **(Dependências) Instalação da biblioteca requests**
   ```bash
   pip3 install requests
   ```

5. **Geração de token de acesso**
   - Crie um token de acesso pessoal no GitHub nas configurações de desenvolvedor: [GitHub Tokens](https://github.com/settings/tokens)

6. **Apresentação da documentação da API REST do GitHub**
   - Consulte a documentação da API REST do GitHub para mais informações: [Documentação da API GitHub](https://docs.github.com/pt/rest?apiVersion=2022-11-28)

## Uso

Para iniciar a coleta de dados, basta rodar o script principal:

```bash
python3 main.py
```

## Top 10 Repositórios com microsserviços (ordenados por Stars)

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

## Top 10 Repositórios com microsserviços (ordenados por Stars + Forks usando score)

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

## Licença

Este projeto está licenciado sob a MIT License.

