# 📊 CK Metrics Extractor

Este projeto automatiza a análise de **métricas de código-fonte Java** usando a ferramenta [CK (Chidamber & Kemerer)](https://github.com/mauricioaniche/ck). A aplicação clona um repositório Java do GitHub, executa o CK Tool e exibe métricas por **classe**, **método**, **campo** e **variável**.

---

## 🧠 O que é CK?

**CK** significa *Chidamber & Kemerer* – os autores de um dos primeiros conjuntos de métricas orientadas a objetos. A ferramenta **CK** implementa e estende essas métricas para projetos Java. Ela analisa o código-fonte estático e gera arquivos `.csv` com as métricas detalhadas.

---

## 📈 Métricas extraídas

Abaixo estão as métricas extraídas e analisadas pelo script:

### class.csv

Esta tabela contém métricas extraídas em nível de classe, sendo fundamentais para entender o **design estrutural** de um sistema. Métricas como `cbo` (Coupling Between Objects), `rfc` (Response For a Class), `wmc` (Weighted Methods per Class) e `lcom` (Lack of Cohesion of Methods) são amplamente utilizadas na **engenharia de software orientada a objetos** para avaliar **acoplamento**, **coesão**, **complexidade** e **tamanho** das classes. Por exemplo, um alto valor de `cbo` pode indicar que a classe está muito dependente de outras, dificultando a manutenção. Já `lcom` ajuda a identificar se os métodos da classe estão bem relacionados entre si. Além disso, métricas como `loc`, `loopQty`, `assignmentsQty` e `logStatementsQty` ajudam a estimar o tamanho e a complexidade da lógica implementada na classe.


| Coluna                   | Descrição                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| file                     | Caminho do arquivo Java analisado.                                       |
| class                    | Nome totalmente qualificado da classe.                                   |
| type                     | Tipo da classe (ex: class, interface, enum).                             |
| cbo                      | Coupling Between Objects — acoplamento entre objetos.                    |
| cboModified              | Variante de CBO considerando chamadas indiretas.                         |
| fanin                    | Número de métodos que chamam esta classe.                                |
| fanout                   | Número de métodos chamados por esta classe.                              |
| wmc                      | Weighted Methods per Class — soma da complexidade dos métodos.           |
| dit                      | Depth of Inheritance Tree — profundidade na hierarquia de herança.       |
| noc                      | Number of Children — número de subclasses diretas.                       |
| rfc                      | Response for a Class — número de métodos que podem ser executados.       |
| lcom                     | Lack of Cohesion of Methods — coesão entre métodos da classe.            |
| lcom*                    | Variante refinada de LCOM.                                                |
| tcc                      | Tight Class Cohesion.                                                    |
| lcc                      | Loose Class Cohesion.                                                    |
| totalMethodsQty          | Total de métodos na classe.                                              |
| staticMethodsQty         | Quantidade de métodos estáticos.                                         |
| publicMethodsQty         | Quantidade de métodos públicos.                                          |
| privateMethodsQty        | Quantidade de métodos privados.                                          |
| protectedMethodsQty      | Quantidade de métodos protegidos.                                        |
| defaultMethodsQty        | Quantidade de métodos com visibilidade default.                          |
| visibleMethodsQty        | Métodos visíveis externamente.                                           |
| abstractMethodsQty       | Quantidade de métodos abstratos.                                         |
| finalMethodsQty          | Quantidade de métodos final.                                             |
| synchronizedMethodsQty   | Quantidade de métodos sincronizados.                                     |
| totalFieldsQty           | Total de atributos na classe.                                            |
| staticFieldsQty          | Quantidade de atributos estáticos.                                       |
| publicFieldsQty          | Atributos públicos.                                                      |
| privateFieldsQty         | Atributos privados.                                                      |
| protectedFieldsQty       | Atributos protegidos.                                                    |
| defaultFieldsQty         | Atributos com visibilidade default.                                      |
| finalFieldsQty           | Atributos final.                                                         |
| synchronizedFieldsQty    | Atributos sincronizados.                                                 |
| nosi                     | Number of Static Invocations — chamadas estáticas realizadas.            |
| loc                      | Lines of Code — linhas de código da classe.                              |
| returnQty                | Número de instruções `return`.                                           |
| loopQty                  | Número de laços (for, while, etc).                                       |
| comparisonsQty           | Quantidade de comparações (`==`, `<`, etc).                              |
| tryCatchQty              | Blocos try-catch.                                                        |
| parenthesizedExpsQty     | Expressões com parênteses.                                               |
| stringLiteralsQty        | Literais de string.                                                      |
| numbersQty               | Literais numéricos.                                                      |
| assignmentsQty           | Atribuições.                                                             |
| mathOperationsQty        | Operações matemáticas.                                                   |
| variablesQty             | Quantidade de variáveis utilizadas.                                      |
| maxNestedBlocksQty       | Máxima profundidade de blocos aninhados.                                 |
| anonymousClassesQty      | Número de classes anônimas.                                              |
| innerClassesQty          | Número de inner classes.                                                 |
| lambdasQty               | Quantidade de expressões lambda.                                         |
| uniqueWordsQty           | Palavras únicas usadas no código.                                        |
| modifiers                | Modificadores da classe (ex: public, abstract).                          |
| logStatementsQty         | Número de chamadas de log (ex: `logger.info()`).                         |

### method.csv

Esta tabela detalha as métricas em nível de **método**, sendo útil para análises mais finas, como identificação de **métodos complexos**, **code smells** e oportunidades de **refatoração**. Métricas como `wmc` (Weighted Method Count) e `cc` (complexidade ciclomática, quando disponível) são essenciais para verificar a dificuldade de leitura e testes do método. A quantidade de `returnsQty`, `loopQty`, `comparisonsQty` e `tryCatchQty` indicam o **nível de ramificação e controle de fluxo**, o que impacta diretamente na **manutenibilidade**. Métricas como `methodsInvokedQty` e `parametersQty` ajudam a identificar **alta responsabilidade** ou **métodos longos**, que podem violar princípios como o **SRP (Single Responsibility Principle)**.


| Coluna                          | Descrição                                                               |
|---------------------------------|-------------------------------------------------------------------------|
| file                            | Caminho do arquivo Java analisado.                                     |
| class                           | Classe à qual o método pertence.                                       |
| method                          | Nome do método.                                                        |
| constructor                     | Indica se é um construtor (`true`/`false`).                            |
| line                            | Linha onde o método começa.                                            |
| cbo                             | Coupling Between Objects para o método.                                |
| cboModified                     | Variante de CBO.                                                       |
| fanin                           | Quantidade de métodos que chamam este.                                 |
| fanout                          | Quantidade de métodos chamados por este.                               |
| wmc                             | Weighted Method Count — complexidade do método.                        |
| rfc                             | Métodos que podem ser executados como resposta a uma chamada.          |
| loc                             | Linhas de código do método.                                            |
| returnsQty                      | Número de instruções `return` no método.                               |
| variablesQty                    | Número de variáveis utilizadas.                                        |
| parametersQty                   | Quantidade de parâmetros do método.                                    |
| methodsInvokedQty               | Total de métodos invocados.                                            |
| methodsInvokedLocalQty          | Métodos locais invocados.                                              |
| methodsInvokedIndirectLocalQty  | Métodos indiretamente locais invocados.                                |
| loopQty                         | Laços de repetição (`for`, `while`, etc).                              |
| comparisonsQty                  | Comparações.                                                           |
| tryCatchQty                     | Blocos try-catch.                                                      |
| parenthesizedExpsQty            | Expressões entre parênteses.                                           |
| stringLiteralsQty               | Literais de string.                                                    |
| numbersQty                      | Literais numéricos.                                                    |
| assignmentsQty                  | Atribuições.                                                           |
| mathOperationsQty               | Operações matemáticas.                                                |
| maxNestedBlocksQty              | Profundidade máxima de blocos aninhados.                               |
| anonymousClassesQty             | Classes anônimas no método.                                            |
| innerClassesQty                 | Inner classes no método.                                               |
| lambdasQty                      | Lambdas no método.                                                     |
| uniqueWordsQty                  | Palavras únicas utilizadas.                                            |
| modifiers                       | Modificadores aplicados (ex: public, static).                          |
| logStatementsQty                | Chamadas de logging.                                                   |
| hasJavaDoc                      | Indica se o método possui Javadoc (`true`/`false`).                    |

### field.csv e variable.csv

Essas duas tabelas mostram o uso de **variáveis e campos** ao longo do código, detalhando sua presença por classe e método. São úteis para identificar padrões de **uso excessivo de variáveis globais**, **reutilização inadequada**, ou **baixo encapsulamento**. A métrica `usage` indica se a variável foi **lida, escrita ou ambos**, ajudando em análises sobre **imutabilidade** ou **uso excessivo de estados mutáveis**. Essas informações são valiosas em auditorias de código, na busca por melhores práticas de encapsulamento e design limpo.

| Coluna    | Descrição                                              |
|-----------|--------------------------------------------------------|
| file      | Caminho do arquivo Java analisado.                     |
| class     | Classe em que a variável ou campo aparece.             |
| method    | Método em que a variável é usada (se aplicável).       |
| variable  | Nome da variável ou campo.                             |
| usage     | Tipo de uso (leitura, escrita, etc).                   |

---

## 📦 Dependências

- [Python 3.8+](https://www.python.org/)
- [GitPython](https://gitpython.readthedocs.io/)
- [pandas](https://pandas.pydata.org/)
- [Java JDK 17](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)
- [Apache Maven](https://maven.apache.org/) — necessário para compilar o JAR do CK
- [CK Tool JAR](https://github.com/mauricioaniche/ck)

Instale as dependências Python:

```bash
pip install gitpython pandas
```

---

## ⚙️ Ambiente virtual

Para usar este projeto, recomendamos criar e ativar um ambiente virtual Python:

```bash
# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente virtual

# Windows:
.venv\Scripts\activate

# Linux/macOS:
source .venv/bin/activate
```

---

## 🚀 Executando o projeto

### 1️⃣ Obter o JAR do CK Tool

Você tem três opções para obter o **JAR do CK Tool**:

---

#### ⚙️ Opção 1: Compilar manualmente (Java 17 + Maven)

```bash
git clone https://github.com/mauricioaniche/ck.git
cd ck
mvn clean package
```

O JAR será gerado em:  
`ck/target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar`

> 💡 É necessário ter o **Java 17** e o **Maven** instalados na sua máquina.

---

#### ⬇️ Opção 2: Baixar o JAR já compilado

Você pode baixar diretamente o JAR já gerado [nesta pasta](https://github.com/joaopauloaramuni/laboratorio-de-experimentacao-de-software/tree/main/PROJETOS/Projeto%20CK%20Metrics%20Extractor/ck/target).

Após o download, lembre-se de colocá-lo no diretório:  
`ck/target/`

---

#### 🐳 Opção 3: Gerar o JAR usando Docker (sem instalar Java/Maven)

Se não quiser instalar o **Java 17** e o **Maven**, você pode usar Docker:

```bash
⁠ docker run --rm -v "$PWD":/work -w /work maven:3.9.6-eclipse-temurin-17 \
            cp target/*-jar-with-dependencies.jar /work/ck.jarecommends git && \
            rm -rf /var/lib/apt/lists/* && \
            git clone https://github.com/mauricioaniche/ck.git && \
            cd ck && mvn -B -DskipTests clean package && \
            cp target/*-jar-with-dependencies.jar /work/ck.jar'
```

Após a execução, o arquivo `ck.jar` estará disponível no diretório atual (`$PWD`).

---

### 2️⃣ Rodar o script Python

```bash
python ck_metrics_extractor.py
```

Informe a URL do repositório Java no prompt:

```bash
Informe a URL do repositório GitHub: https://github.com/spring-projects/spring-petclinic
```

---

## 📄 Arquivos gerados

Após a execução, os seguintes arquivos `.csv` serão gerados:

- `ck_output/class.csv`
- `ck_output/method.csv`
- `ck_output/field.csv`
- `ck_output/variable.csv`

O script exibirá na tela os principais dados de cada métrica.

---

## 🖥️ Exemplo de saída no terminal, com visualização de até 5 linhas por tabela

```
(.venv) (base) joaopauloaramuni@MacBook-Pro-de-Joao Projeto CK Metrics Extractor % python ck_metrics_extractor.py
== CK Metrics Extractor ==
Informe a URL do repositório GitHub: https://github.com/spring-projects/spring-petclinic
[+] Clonando repositório de https://github.com/spring-projects/spring-petclinic ...
[+] Executando CK Tool nas fontes em repo ...
log4j:WARN No appenders could be found for logger (com.github.mauricioaniche.ck.CK).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.
Metrics extracted!!!

[+] Lendo métricas por CLASSE ...
                                                file                                              class  ... modifiers  logStatementsQty
0  /Users/joaopauloaramuni/Downloads/Projeto CK M...  org.springframework.samples.petclinic.PetClini...  ...         1                 0
1  /Users/joaopauloaramuni/Downloads/Projeto CK M...    org.springframework.samples.petclinic.owner.Pet  ...         1                 0
2  /Users/joaopauloaramuni/Downloads/Projeto CK M...  org.springframework.samples.petclinic.owner.Pe...  ...         1                 0
3  /Users/joaopauloaramuni/Downloads/Projeto CK M...  org.springframework.samples.petclinic.system.W...  ...         1                 0
4  /Users/joaopauloaramuni/Downloads/Projeto CK M...  org.springframework.samples.petclinic.system.C...  ...         0                 0

[5 rows x 52 columns]

[+] Lendo métricas por MÉTODO ...
                                                file                                              class  ... logStatementsQty  hasJavaDoc
0  /Users/joaopauloaramuni/Downloads/Projeto CK M...  org.springframework.samples.petclinic.PetClini...  ...                0       False
1  /Users/joaopauloaramuni/Downloads/Projeto CK M...  org.springframework.samples.petclinic.PetClini...  ...                0       False
2  /Users/joaopauloaramuni/Downloads/Projeto CK M...  org.springframework.samples.petclinic.PetClini...  ...                0       False
3  /Users/joaopauloaramuni/Downloads/Projeto CK M...    org.springframework.samples.petclinic.owner.Pet  ...                0       False
4  /Users/joaopauloaramuni/Downloads/Projeto CK M...    org.springframework.samples.petclinic.owner.Pet  ...                0       False

[5 rows x 34 columns]

[+] Lendo métricas por CAMPO ...
                                                file                                              class  ... variable usage
0  /Users/joaopauloaramuni/Downloads/Projeto CK M...  org.springframework.samples.petclinic.PetClini...  ...     port     1
1  /Users/joaopauloaramuni/Downloads/Projeto CK M...  org.springframework.samples.petclinic.PetClini...  ...  builder     1
2  /Users/joaopauloaramuni/Downloads/Projeto CK M...  org.springframework.samples.petclinic.PetClini...  ...     vets     2
3  /Users/joaopauloaramuni/Downloads/Projeto CK M...    org.springframework.samples.petclinic.owner.Pet  ...     type     1
4  /Users/joaopauloaramuni/Downloads/Projeto CK M...    org.springframework.samples.petclinic.owner.Pet  ...     type     3

[5 rows x 5 columns]

[+] Lendo métricas por VARIÁVEL ...
                                                file                                              class  ...  variable usage
0  /Users/joaopauloaramuni/Downloads/Projeto CK M...  org.springframework.samples.petclinic.PetClini...  ...  template     1
1  /Users/joaopauloaramuni/Downloads/Projeto CK M...  org.springframework.samples.petclinic.PetClini...  ...    result     1
2  /Users/joaopauloaramuni/Downloads/Projeto CK M...  org.springframework.samples.petclinic.PetClini...  ...      args     1
3  /Users/joaopauloaramuni/Downloads/Projeto CK M...    org.springframework.samples.petclinic.owner.Pet  ...      type     2
4  /Users/joaopauloaramuni/Downloads/Projeto CK M...    org.springframework.samples.petclinic.owner.Pet  ...     visit     1

[5 rows x 5 columns]
```

---

## 🌿 Sobre a *default branch* do repositório

Nem todo repositório no GitHub usa `main` ou `master` como branch padrão. Alguns podem ter nomes diferentes, como `develop`, `trunk` ou `release`. Saber a branch principal é importante, pois o CK Metrics Extractor precisa dela para clonar e analisar o código corretamente.

#### Como o script trata a default branch

O script Python utiliza a **GitHub GraphQL API** para identificar a branch padrão de cada repositório, consultando o campo `defaultBranchRef`:

```graphql
defaultBranchRef {
  name
}
```

No código, isso é feito assim:

```python
default_branch = 'main'
if repo.get('defaultBranchRef') and repo['defaultBranchRef']:
    default_branch = repo['defaultBranchRef']['name']
```

Dessa forma:
- O script **não depende de comandos Git locais** como `git remote show origin`.
- Ele obtém a default branch **diretamente do GitHub**, garantindo que mesmo repositórios com branches não padrão sejam analisados corretamente.
- O fallback `main` é usado apenas se o repositório não fornecer `defaultBranchRef`.

> 💡 Isso torna o processo de coleta de métricas mais confiável e automatizado.

---

## 💡 Sugestão: Download de repositórios via ZIP

Atualmente, o CK Metrics Extractor faz o **clone completo do repositório** usando Git, o que inclui a pasta `.git` com todo o histórico de commits.  
Em repositórios grandes ou antigos, isso pode deixar o download **mais pesado e lento**.

Como alternativa, você poderia baixar o código diretamente como um **arquivo ZIP** da *default branch*:

```python
zip_url = f"https://github.com/{repo_owner}/{repo_name}/archive/refs/heads/{default_branch}.zip"
```

### Vantagens do download via ZIP

- Mais rápido, pois não traz o histórico Git.
- Menos espaço em disco ocupado.
- Ideal para análises estáticas de código, quando você não precisa do histórico de commits.
- Ideal para quem precisa analisar **centenas de repositórios** rapidamente.

> ⚠️ Observação: esta é apenas uma sugestão de melhoria; o script atual ainda faz o clone completo via Git.

---

## 📚 Documentação e Links úteis

- 📘 [Repositório oficial do CK](https://github.com/mauricioaniche/ck)
- 📦 [CK no Maven Repository](https://mvnrepository.com/artifact/com.github.mauricioaniche/ck)
- 🐼 [Site oficial do pandas](https://pandas.pydata.org/)
- 📖 [Documentação do pandas](https://pandas.pydata.org/docs/)
- 📕 [Python para Análise de Dados (Wes McKinney, março de 2023)](https://www.amazon.com.br/Python-Para-An%C3%A1lise-Dados-Tratamento/dp/8575228412/)

---

## 📝 Licença

Este projeto está licenciado sob os termos da Licença MIT. Sinta-se livre para usar, modificar e distribuir!

---

Feito com ❤️ para análise estática de código em Engenharia de Software.
