# 🧠 Projeto: Análise Automática de Repositórios Java com SonarQube

Este projeto tem como objetivo facilitar a análise de qualidade de código em repositórios Java hospedados no GitHub. Ao informar uma URL de repositório, o script clona o projeto, compila o código (via Maven, Gradle ou manualmente), executa uma análise com o `sonar-scanner` e consulta as métricas diretamente do SonarQube Server. Tudo isso é feito automaticamente, e ao final o usuário recebe as principais métricas de qualidade do projeto analisado. 💡

Ideal para desenvolvedores, analistas e professores que desejam obter uma visão rápida da saúde do código-fonte, sem precisar configurar projetos manualmente no painel web do SonarQube. É uma forma prática de incorporar práticas de qualidade de software em ciclos de desenvolvimento, revisão ou ensino. 🚀

---

## 🛠️ O que é o SonarQube?

O SonarQube é uma plataforma open-source para inspeção contínua da qualidade de código-fonte. Ele realiza análise estática e identifica bugs, code smells, vulnerabilidades, duplicações e outros problemas relacionados à manutenibilidade, segurança e cobertura de testes.

---

## 📏 O que são as métricas do SonarQube?

Métricas do SonarQube representam indicadores quantitativos e qualitativos sobre o código analisado. Exemplos incluem: `coverage` (cobertura de testes), `code_smells`, `bugs`, `complexity`, `duplicated_lines`, entre outros. Essas métricas ajudam equipes a monitorar e melhorar continuamente a qualidade de seus projetos.

A seguir, temos uma tabela com as principais métricas utilizadas para análise de qualidade de código em ferramentas como SonarQube. Essas métricas estão divididas em categorias como cobertura de testes, duplicações, tamanho do código e complexidade, ajudando a avaliar diversos aspectos do software, desde a eficácia dos testes até a manutenção e riscos potenciais.


| Categoria   | Métrica              | Descrição                           |
|-------------|----------------------|-----------------------------------|
| Coverage    | coverage             | Percentual total de linhas cobertas por testes |
| Coverage    | new_coverage         | Cobertura de linhas novas          |
| Coverage    | lines_to_cover       | Linhas que devem ser cobertas      |
| Coverage    | new_lines_to_cover   | Linhas novas que devem ser cobertas|
| Coverage    | uncovered_lines      | Linhas não cobertas por testes     |
| Coverage    | new_uncovered_lines  | Novas linhas não cobertas          |
| Coverage    | line_coverage        | Percentual de cobertura por linha  |
| Coverage    | new_line_coverage    | Percentual de cobertura por linha nas linhas novas |
| Coverage    | branch_coverage      | Percentual de cobertura de ramos/condições |
| Coverage    | new_branch_coverage  | Cobertura de ramos em código novo  |
| Coverage    | uncovered_conditions | Condições não cobertas por testes  |
| Coverage    | new_uncovered_conditions | Condições não cobertas em código novo |
| Coverage    | tests                | Total de testes executados         |
| Coverage    | test_errors          | Erros nos testes                   |
| Coverage    | test_failures        | Falhas nos testes                  |
| Coverage    | skipped_tests        | Testes ignorados                   |
| Coverage    | test_execution_time  | Tempo de execução dos testes       |
| Coverage    | test_success_density | Percentual de sucesso nos testes   |
| Duplications| duplicated_lines_density | Densidade de linhas duplicadas    |
| Duplications| new_duplicated_lines_density | Densidade de linhas duplicadas novas |
| Duplications| duplicated_lines     | Número de linhas duplicadas        |
| Duplications| new_duplicated_lines | Número de linhas duplicadas novas  |
| Duplications| duplicated_blocks    | Número de blocos duplicados        |
| Duplications| new_duplicated_blocks| Número de blocos duplicados novos  |
| Duplications| duplicated_files     | Número de arquivos duplicados      |
| Size        | new_lines            | Novas linhas adicionadas           |
| Size        | ncloc                | Número de linhas de código não comentadas |
| Size        | lines                | Total de linhas                   |
| Size        | statements           | Número de statements (instruções) |
| Size        | functions            | Número de funções                 |
| Size        | classes              | Número de classes                 |
| Size        | files                | Número de arquivos                |
| Size        | comment_lines        | Linhas de comentários            |
| Size        | comment_lines_density| Densidade de linhas de comentário |
| Size        | ncloc_language_distribution | Distribuição por linguagem       |
| Size        | projects             | Número de projetos                |
| Complexity  | complexity           | Complexidade ciclomatica          |
| Complexity  | cognitive_complexity | Complexidade cognitiva            |
| Complexity  | sqale_index          | Índice de qualidade técnica       |
| Complexity  | code_smells          | Número de code smells             |
| Complexity  | bugs                 | Número de bugs                   |
| Complexity  | vulnerabilities      | Número de vulnerabilidades       |

---

## 🔄 Diferença entre `sonar-scanner` e `sonar-server`

- `sonar-server` é o backend que armazena e processa os dados dos projetos analisados. Ele roda em um servidor web (por exemplo, `http://localhost:9000`) e possui uma interface gráfica.
- `sonar-scanner` é o cliente que executa localmente a análise estática do código-fonte e envia os dados ao `sonar-server`.

---

## 🔐 Como gerar um token no SonarQube

Para que o script se conecte ao SonarQube com segurança e consiga enviar os dados de análise, você precisará de um **token de autenticação**. Siga o passo a passo abaixo:

1. 🖥️ Acesse o SonarQube localmente pelo navegador:

- `http://localhost:9000`

2. 🔑 Faça login (por padrão, o usuário e senha iniciais são `admin` / `admin`).

3. Clique no seu avatar ou nome de usuário no canto superior direito e selecione **"My Account"** (ou **"Minha Conta"**, dependendo do idioma).

4. Vá até a aba **"Security"** (ou **"Segurança"**).

5. Na seção **"Generate Tokens"**, digite um nome para o token (ex: `meu-token-sonarqube`) e clique em **"Generate"**.

6. 📋 Copie o token gerado e salve em um local seguro! **Você só verá esse token uma vez!**

7. 🔁 Use esse token em seu código Python, por exemplo:

```python
SONAR_TOKEN = "seu_token_aqui" # squ_0a771d466672b12431951af497d79e**********
```

### 🖼️ Captura de Tela

| ![SonarQube](https://joaopauloaramuni.github.io/python-imgs/SonarQube_API/imgs/sonarqube.png) |
|:-------------------------:|
|         SonarQube         |

---

## 🧩 Explicação das funções do código

- `compilar_java(caminho_repo)`: Compila automaticamente o projeto Java utilizando Maven, Gradle ou `javac` puro. Retorna o caminho para os arquivos `.class`.
- `get_sonar_metrics(project_key)`: Consulta a API do SonarQube e extrai métricas de qualidade com base na chave do projeto.
- `aguardar_processamento(task_id)`: Aguarda o término da análise assíncrona no SonarQube antes de buscar as métricas.
- `run_sonar_scanner(repo_path, project_key)`: Cria o arquivo de configuração `sonar-project.properties` e executa o `sonar-scanner`.
- `clone_repo(github_url)`: Clona o repositório GitHub em uma pasta temporária.
- `analisar_repositorio(github_url)`: Coordena todo o processo de análise (clone, build, scanner, consulta).

---

## ⚙️ Configuração do SonarQube com arquivo properties

Os arquivos de configuração do SonarQube são arquivos de propriedades (`.properties`) que definem parâmetros essenciais para a análise do código-fonte. Eles configuram detalhes como o projeto, servidor, autenticação e regras de qualidade.

Esses arquivos seguem o formato chave=valor e são usados para integrar o SonarQube em processos automatizados ou na análise local via Sonar Scanner.

Exemplo básico do arquivo `sonar-project.properties`:

```
# Identificação do projeto no SonarQube
sonar.projectKey=my_project_key
sonar.projectName=Meu Projeto Exemplo
sonar.projectVersion=1.0

# Diretórios contendo os arquivos fonte
sonar.sources=src

# URL do servidor SonarQube
sonar.host.url=https://meu-sonarqube-servidor.com

# Token de autenticação
sonar.login=seu_token_de_acesso

# Linguagem da análise (opcional)
sonar.language=java

# Exclusão de arquivos ou pastas da análise
sonar.exclusions=**/test/**,**/*.spec.js

# Codificação dos arquivos fonte
sonar.sourceEncoding=UTF-8
```

### Principais propriedades

- `sonar.projectKey`: identificador único do projeto.
- `sonar.projectName`: nome legível do projeto.
- `sonar.projectVersion`: versão do projeto.
- `sonar.sources`: diretórios com o código-fonte.
- `sonar.host.url`: endereço do servidor SonarQube.
- `sonar.login`: token para autenticação.
- `sonar.exclusions`: padrões de arquivos/pastas a ignorar.
- `sonar.sourceEncoding`: codificação dos arquivos, geralmente UTF-8.

Essas propriedades podem ser adaptadas e expandidas conforme a necessidade do seu projeto.

---

## 📦 Dependências

### Instalação via terminal

```bash
pip install requests
```

### Ferramentas necessárias

- **SonarQube Server** (baixe em: https://www.sonarsource.com/products/sonarqube/downloads/)
- **sonar-scanner**
  - MacOS: `brew install sonar-scanner`
  - Linux: via script ou `.zip`
  - Windows: baixe o zip no site oficial e adicione à `PATH`

- **Maven**:
  - MacOS: `brew install maven`
  - Linux: `sudo apt install maven`
  - Windows: baixar binário e adicionar à `PATH`

- **Gradle** (opcional, se projeto usar Gradle):
  - MacOS: `brew install gradle`
  - Linux: `sudo apt install gradle`
  - Windows: baixar e adicionar à `PATH`

- **Rodar o SonarQube**:
  ```bash
  ./sonar.sh start
  ```
  Acesse: http://localhost:9000

- **Token de autenticação**:
  Gere em: [http://localhost:9000/account/security](http://localhost:9000/account/security)

---

## ⚙️ Ambiente virtual

1. **Crie um ambiente virtual:**

```bash
python -m venv .venv
```

2. **Ative o ambiente virtual:**

- **Windows:**
  ```bash
  .venv\Scripts\activate
  ```

- **Linux/MacOS:**
  ```bash
  source .venv/bin/activate
  ```

---

## 💻 Resultado no terminal

- **Repositório analisado:** `arieslab/jnose`
- **URL**: `https://github.com/arieslab/jnose`

```
(venv) (base) joaopauloaramuni@MacBook-Pro-de-Joao Projeto SonarQube API % python3 sonar.py
************ Projeto de Análise de Repositórios Java com SonarQube ************
Informe a URL do repositório GitHub: https://github.com/arieslab/jnose
Cloning into '/Users/joaopauloaramuni/Downloads/Projeto SonarQube API/temp_clone_941885d2cf014d598fbc80e8102fad5d_jnose'...
remote: Enumerating objects: 4808, done.
remote: Counting objects: 100% (1133/1133), done.
remote: Compressing objects: 100% (346/346), done.
remote: Total 4808 (delta 529), reused 1084 (delta 488), pack-reused 3675 (from 1)
Receiving objects: 100% (4808/4808), 2.45 MiB | 3.68 MiB/s, done.
Resolving deltas: 100% (2199/2199), done.
******************************************************************************************************************************************************
[+] Rodando análise com SonarQube...
[+] Encontrado pom.xml, compilando com Maven...
******************************************************************************************************************************************************
[DEBUG Maven STDOUT]: [INFO] Scanning for projects...
[INFO] 
[INFO] ------------------------< br.ufba.jnose:jnose >-------------------------
[INFO] Building jnose 2.2.0
[INFO]   from pom.xml
[INFO] --------------------------------[ war ]---------------------------------
[WARNING] 1 problem was encountered while building the effective model for org.javassist:javassist:jar:3.18.1-GA during dependency collection step for project (use -X to see details)
[INFO] 
[INFO] --- clean:3.2.0:clean (default-clean) @ jnose ---
[INFO] 
[INFO] --- resources:3.3.1:resources (default-resources) @ jnose ---
[INFO] Copying 3 resources from src/main/resources to target/classes
[INFO] Copying 17 resources from src/main/java to target/classes
[INFO] 
[INFO] --- compiler:3.6.1:compile (default-compile) @ jnose ---
[INFO] Changes detected - recompiling the module!
[INFO] Compiling 39 source files to /Users/joaopauloaramuni/Downloads/Projeto SonarQube API/temp_clone_941885d2cf014d598fbc80e8102fad5d_jnose/target/classes
[WARNING] location of system modules is not set in conjunction with -source 11
  not setting the location of system modules may lead to class files that cannot run on JDK 11
    --release 11 is recommended instead of -source 11 -target 11 because it sets the location of system modules automatically
[WARNING] /Users/joaopauloaramuni/Downloads/Projeto SonarQube API/temp_clone_941885d2cf014d598fbc80e8102fad5d_jnose/src/main/java/br/ufba/jnose/base/Util.java:[40,45] exec(java.lang.String,java.lang.String[],java.io.File) in java.lang.Runtime has been deprecated
[WARNING] /Users/joaopauloaramuni/Downloads/Projeto SonarQube API/temp_clone_941885d2cf014d598fbc80e8102fad5d_jnose/src/main/java/br/ufba/jnose/base/GitCore.java:[144,52] peel(org.eclipse.jgit.lib.Ref) in org.eclipse.jgit.lib.Repository has been deprecated
[INFO] /Users/joaopauloaramuni/Downloads/Projeto SonarQube API/temp_clone_941885d2cf014d598fbc80e8102fad5d_jnose/src/main/java/br/ufba/jnose/pages/EvolutionPage.java: Some input files use unchecked or unsafe operations.
[INFO] /Users/joaopauloaramuni/Downloads/Projeto SonarQube API/temp_clone_941885d2cf014d598fbc80e8102fad5d_jnose/src/main/java/br/ufba/jnose/pages/EvolutionPage.java: Recompile with -Xlint:unchecked for details.
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  1.828 s
[INFO] Finished at: 2025-06-10T22:42:44-03:00
[INFO] ------------------------------------------------------------------------

[DEBUG Maven STDERR]: WARNING: A restricted method in java.lang.System has been called
WARNING: java.lang.System::load has been called by org.fusesource.jansi.internal.JansiLoader in an unnamed module (file:/opt/homebrew/Cellar/maven/3.9.9/libexec/lib/jansi-2.4.1.jar)
WARNING: Use --enable-native-access=ALL-UNNAMED to avoid a warning for callers in this module
WARNING: Restricted methods will be blocked in a future release unless native access is enabled

WARNING: A terminally deprecated method in sun.misc.Unsafe has been called
WARNING: sun.misc.Unsafe::objectFieldOffset has been called by com.google.common.util.concurrent.AbstractFuture$UnsafeAtomicHelper (file:/opt/homebrew/Cellar/maven/3.9.9/libexec/lib/guava-33.2.1-jre.jar)
WARNING: Please consider reporting this to the maintainers of class com.google.common.util.concurrent.AbstractFuture$UnsafeAtomicHelper
WARNING: sun.misc.Unsafe::objectFieldOffset will be removed in a future release

******************************************************************************************************************************************************
[DEBUG] Diretório de classes Maven encontrado: /Users/joaopauloaramuni/Downloads/Projeto SonarQube API/temp_clone_941885d2cf014d598fbc80e8102fad5d_jnose/target/classes/br/ufba/jnose
******************************************************************************************************************************************************
[+] Executando sonar-scanner...
******************************************************************************************************************************************************
[DEBUG] STDOUT:
 22:42:44.556 INFO  Scanner configuration file: /opt/homebrew/Cellar/sonar-scanner/7.1.0.4889/libexec/conf/sonar-scanner.properties
22:42:44.558 INFO  Project root configuration file: /Users/joaopauloaramuni/Downloads/Projeto SonarQube API/temp_clone_941885d2cf014d598fbc80e8102fad5d_jnose/sonar-project.properties
22:42:44.567 INFO  SonarScanner CLI 7.1.0.4889
22:42:44.568 INFO  Java 24.0.1 Homebrew (64-bit)
22:42:44.569 INFO  Mac OS X 15.5 aarch64
22:42:44.594 INFO  User cache: /Users/joaopauloaramuni/.sonar/cache
22:42:46.417 INFO  Communicating with SonarQube Community Build 25.6.0.109173
22:42:46.418 WARN  Use of 'sonar.login' property has been deprecated in favor of 'sonar.token' (or the env variable alternative 'SONAR_TOKEN'). Please use the latter when passing a token.
22:42:46.418 INFO  JRE provisioning: os[macos], arch[arm64]
22:42:46.712 INFO  Starting SonarScanner Engine...
22:42:46.712 INFO  Java 17.0.13 Eclipse Adoptium (64-bit)
22:42:48.670 INFO  Load global settings
22:42:48.725 INFO  Load global settings (done) | time=55ms
22:42:48.727 INFO  Server id: 147B411E-AZdahJhDKBwSzFA01poK
22:42:48.735 INFO  Loading required plugins
22:42:48.736 INFO  Load plugins index
22:42:48.753 INFO  Load plugins index (done) | time=18ms
22:42:48.753 INFO  Load/download plugins
22:42:48.785 INFO  Load/download plugins (done) | time=31ms
22:42:48.950 INFO  Process project properties
22:42:48.957 INFO  Process project properties (done) | time=7ms
22:42:48.961 INFO  Project key: jnose
22:42:48.961 INFO  Base dir: /Users/joaopauloaramuni/Downloads/Projeto SonarQube API/temp_clone_941885d2cf014d598fbc80e8102fad5d_jnose
22:42:48.961 INFO  Working dir: /Users/joaopauloaramuni/Downloads/Projeto SonarQube API/temp_clone_941885d2cf014d598fbc80e8102fad5d_jnose/.scannerwork
22:42:48.966 INFO  Load project settings for component key: 'jnose'
22:42:48.981 INFO  Load project settings for component key: 'jnose' (done) | time=14ms
22:42:48.994 INFO  Load quality profiles
22:42:49.080 INFO  Load quality profiles (done) | time=86ms
22:42:49.100 INFO  Load active rules
22:42:49.334 INFO  Load active rules (done) | time=233ms
22:42:49.338 INFO  Load analysis cache
22:42:49.351 INFO  Load analysis cache (4.2 kB) | time=14ms
22:42:49.371 WARN  The property 'sonar.login' is deprecated and will be removed in the future. Please use the 'sonar.token' property instead when passing a token.
22:42:49.378 INFO  Preprocessing files...
22:42:50.190 INFO  7 languages detected in 115 preprocessed files (done) | time=811ms
22:42:50.190 INFO  160 files ignored because of scm ignore settings
22:42:50.191 INFO  Loading plugins for detected languages
22:42:50.191 INFO  Load/download plugins
22:42:50.202 INFO  Load/download plugins (done) | time=11ms
22:42:50.316 INFO  Load project repositories
22:42:50.365 INFO  Load project repositories (done) | time=49ms
22:42:50.377 INFO  Indexing files...
22:42:50.377 INFO  Project configuration:
22:42:50.471 INFO  Some of the project files were automatically excluded because they looked like generated code. Enable debug logging to see which files were excluded. You can disable bundle detection by setting sonar.javascript.detectBundles=false
22:42:50.482 INFO  108 files indexed (done) | time=105ms
22:42:50.483 INFO  Quality profile for css: Sonar way
22:42:50.483 INFO  Quality profile for docker: Sonar way
22:42:50.483 INFO  Quality profile for java: Sonar way
22:42:50.483 INFO  Quality profile for web: Sonar way
22:42:50.484 INFO  Quality profile for xml: Sonar way
22:42:50.484 INFO  Quality profile for yaml: Sonar way
22:42:50.484 INFO  ------------- Run sensors on module jnose
22:42:50.526 INFO  Load metrics repository
22:42:50.543 INFO  Load metrics repository (done) | time=17ms
22:42:50.927 INFO  Sensor JavaSensor [java]
22:42:50.937 INFO  Server-side caching is enabled. The Java analyzer will not try to leverage data from a previous analysis.
22:42:50.939 INFO  Using ECJ batch to parse 39 Main java source files with batch size 107 KB.
22:42:51.124 INFO  Starting batch processing.
22:42:51.359 INFO  The Java analyzer cannot skip unchanged files in this context. A full analysis is performed for all files.
22:42:53.406 INFO  100% analyzed
22:42:53.407 INFO  Batch processing: Done.
22:42:53.407 INFO  Did not optimize analysis for any files, performed a full analysis for all 39 files.
22:42:53.407 WARN  Dependencies/libraries were not provided for analysis of SOURCE files. The 'sonar.java.libraries' property is empty. Verify your configuration, as you might end up with less precise results.
22:42:53.407 WARN  Unresolved imports/types have been detected during analysis. Enable DEBUG mode to see them.
22:42:53.408 WARN  Use of preview features have been detected during analysis. Enable DEBUG mode to see them.
22:42:53.408 INFO  No "Test" source files to scan.
22:42:53.408 INFO  No "Generated" source files to scan.
22:42:53.408 INFO  Sensor JavaSensor [java] (done) | time=2473ms
22:42:53.408 INFO  Sensor SurefireSensor [java]
22:42:53.408 INFO  parsing [/Users/joaopauloaramuni/Downloads/Projeto SonarQube API/temp_clone_941885d2cf014d598fbc80e8102fad5d_jnose/target/surefire-reports]
22:42:53.409 INFO  Sensor SurefireSensor [java] (done) | time=1ms
22:42:53.409 INFO  Sensor HTML [web]
22:42:53.544 INFO  Sensor HTML [web] (done) | time=142ms
22:42:53.544 INFO  Sensor XML Sensor [xml]
22:42:53.547 INFO  3 source files to be analyzed
22:42:53.667 INFO  3/3 source files have been analyzed
22:42:53.667 INFO  Sensor XML Sensor [xml] (done) | time=123ms
22:42:53.667 INFO  Sensor JaCoCo XML Report Importer [jacoco]
22:42:53.667 INFO  'sonar.coverage.jacoco.xmlReportPaths' is not defined. Using default locations: target/site/jacoco/jacoco.xml,target/site/jacoco-it/jacoco.xml,build/reports/jacoco/test/jacocoTestReport.xml
22:42:53.668 INFO  No report imported, no coverage information will be imported by JaCoCo XML Report Importer
22:42:53.668 INFO  Sensor JaCoCo XML Report Importer [jacoco] (done) | time=2ms
22:42:53.668 INFO  Sensor Java Config Sensor [iac]
22:42:53.680 INFO  1 source file to be analyzed
22:42:53.709 INFO  1/1 source file has been analyzed
22:42:53.709 INFO  Sensor Java Config Sensor [iac] (done) | time=41ms
22:42:53.709 INFO  Sensor JavaScript inside HTML analysis [javascript]
22:42:53.846 INFO  Detected os: Mac OS X arch: aarch64 alpine: false. Platform: DARWIN_ARM64
22:42:53.847 INFO  Deploy location /Users/joaopauloaramuni/.sonar/js/node-runtime, tagetRuntime: /Users/joaopauloaramuni/.sonar/js/node-runtime/node,  version: /Users/joaopauloaramuni/.sonar/js/node-runtime/version.txt
22:42:53.948 INFO  Using embedded Node.js runtime.
22:42:53.948 INFO  Using Node.js executable: '/Users/joaopauloaramuni/.sonar/js/node-runtime/node'.
22:42:54.981 INFO  Memory configuration: OS (8192 MB), Node.js (2096 MB).
22:42:55.093 INFO  18 source files to be analyzed
22:42:55.934 INFO  18/18 source files have been analyzed
22:42:55.934 INFO  Hit the cache for 0 out of 18
22:42:55.934 INFO  Miss the cache for 18 out of 18: ANALYSIS_MODE_INELIGIBLE [18/18]
22:42:55.934 INFO  Sensor JavaScript inside HTML analysis [javascript] (done) | time=2225ms
22:42:55.934 INFO  Sensor CSS Rules [javascript]
22:42:55.938 INFO  23 source files to be analyzed
22:42:56.399 INFO  23/23 source files have been analyzed
22:42:56.399 INFO  Hit the cache for 0 out of 0
22:42:56.399 INFO  Miss the cache for 0 out of 0
22:42:56.399 INFO  Sensor CSS Rules [javascript] (done) | time=465ms
22:42:56.399 INFO  Sensor CSS Metrics [javascript]
22:42:56.661 INFO  Sensor CSS Metrics [javascript] (done) | time=262ms
22:42:56.662 INFO  Sensor IaC Docker Sensor [iac]
22:42:56.710 INFO  1 source file to be analyzed
22:42:56.739 INFO  1/1 source file has been analyzed
22:42:56.739 INFO  Sensor IaC Docker Sensor [iac] (done) | time=78ms
22:42:56.739 INFO  Sensor TextAndSecretsSensor [text]
22:42:56.750 INFO  Available processors: 8
22:42:56.750 INFO  Using 8 threads for analysis.
22:42:56.753 INFO  The property "sonar.tests" is not set. To improve the analysis accuracy, we categorize a file as a test file if any of the following is true:
  * The filename starts with "test"
  * The filename contains "test." or "tests."
  * Any directory in the file path is named: "doc", "docs", "test" or "tests"
  * Any directory in the file path has a name ending in "test" or "tests"

22:42:56.961 INFO  Start fetching files for the text and secrets analysis
22:42:56.977 INFO  Using Git CLI to retrieve untracked files
22:42:56.999 INFO  Retrieving language associated files and files included via "sonar.text.inclusions" that are tracked by git
22:42:57.009 INFO  Starting the text and secrets analysis
22:42:57.011 INFO  73 source files to be analyzed for the text and secrets analysis
22:42:57.173 INFO  73/73 source files have been analyzed for the text and secrets analysis
22:42:57.175 INFO  2 files are ignored because they are untracked by git
22:42:57.176 INFO  Sensor TextAndSecretsSensor [text] (done) | time=437ms
22:42:57.179 INFO  ------------- Run sensors on project
22:42:57.247 INFO  Sensor Zero Coverage Sensor
22:42:57.258 INFO  Sensor Zero Coverage Sensor (done) | time=10ms
22:42:57.258 INFO  Sensor Java CPD Block Indexer
22:42:57.298 INFO  Sensor Java CPD Block Indexer (done) | time=41ms
22:42:57.298 INFO  ------------- Gather SCA dependencies on project
22:42:57.299 INFO  Dependency analysis skipped
22:42:57.313 INFO  CPD Executor 17 files had no CPD blocks
22:42:57.313 INFO  CPD Executor Calculating CPD for 40 files
22:42:57.328 INFO  CPD Executor CPD calculation finished (done) | time=14ms
22:42:57.333 INFO  SCM revision ID '5d52ed62c30f3a0012692f4eea889ef7770daeae'
22:42:57.411 INFO  Analysis report generated in 74ms, dir size=1.7 MB
22:42:57.559 INFO  Analysis report compressed in 148ms, zip size=473.2 kB
22:42:57.694 INFO  Analysis report uploaded in 134ms
22:42:57.696 INFO  ANALYSIS SUCCESSFUL, you can find the results at: http://localhost:9000/dashboard?id=jnose
22:42:57.696 INFO  Note that you will be able to access the updated dashboard once the server has processed the submitted analysis report
22:42:57.697 INFO  More about the report processing at http://localhost:9000/api/ce/task?id=125b99b9-c6eb-4c01-b1fb-ae71aab44ef5
22:42:57.782 INFO  Analysis total time: 8.970 s
22:42:57.782 INFO  SonarScanner Engine completed successfully
22:42:58.171 INFO  EXECUTION SUCCESS
22:42:58.173 INFO  Total time: 13.618s

[DEBUG] STDERR:
 
******************************************************************************************************************************************************
[+] Aguardando processamento da análise no SonarQube...
******************************************************************************************************************************************************
[+] Obtendo métricas...
[DEBUG] Consultando métricas para project_key: 'jnose'
******************************************************************************************************************************************************
[+] Resultado:
complexity: 511
duplicated_lines_density: 0.6
duplicated_lines: 197
functions: 200
classes: 33
statements: 1842
sqale_index: 2836
bugs: 25
lines_to_cover: 2097
duplicated_files: 6
ncloc: 27359
line_coverage: 0.0
lines: 31516
coverage: 0.0
code_smells: 364
ncloc_language_distribution: <null>=18;css=22312;docker=8;java=3499;web=1030;xml=492
comment_lines_density: 1.6
comment_lines: 454
uncovered_lines: 2097
cognitive_complexity: 347
duplicated_blocks: 11
files: 67
vulnerabilities: 0
******************************************************************************************************************************************************
[+] Limpando repositório clonado.
******************************************************************************************************************************************************
************ Análise concluída! ************
(venv) (base) joaopauloaramuni@MacBook-Pro-de-Joao Projeto SonarQube API % 
```

---

## 📊 Resumo dos resultados

| Métrica                      | Valor             | Explicação                                                                                  |
|-----------------------------|-------------------|--------------------------------------------------------------------------------------------|
| **Complexity**               | 511               | Soma da complexidade ciclomática das funções/métodos, indica complexidade do código.        |
| **Duplicated Lines Density** | 0.6               | Percentual de linhas duplicadas em relação ao total de linhas do código.                    |
| **Duplicated Lines**         | 197               | Número total de linhas duplicadas no código.                                               |
| **Functions**                | 200               | Quantidade de funções/métodos presentes no projeto.                                        |
| **Classes**                  | 33                | Quantidade de classes definidas no código.                                                |
| **Statements**               | 1842              | Total de comandos ou instruções executáveis no código.                                    |
| **SQALE Index**              | 2836              | Índice que indica a dívida técnica do código (quanto maior, pior).                        |
| **Bugs**                    | 25                | Número estimado de defeitos ou erros no código.                                           |
| **Lines to Cover**           | 2097              | Quantidade de linhas de código que deveriam ser cobertas por testes.                       |
| **Duplicated Files**         | 6                 | Número de arquivos que possuem código duplicado.                                          |
| **NCLOC (Non-Comment Lines of Code)** | 27,359    | Número de linhas de código sem contar comentários.                                       |
| **Line Coverage**            | 0.0%              | Percentual de linhas efetivamente cobertas por testes automatizados.                      |
| **Total Lines**              | 31,516            | Total de linhas presentes no projeto, incluindo código e comentários.                     |
| **Coverage**                 | 0.0%              | Percentual geral de cobertura de testes (linhas, branches, etc.).                        |
| **Code Smells**              | 364               | Número de “code smells” ou problemas de qualidade no código que podem indicar refatoração.|
| **NCLOC Language Distribution** | `<null>`=18; CSS=22,312; Docker=8; Java=3,499; Web=1,030; XML=492 | Distribuição das linhas de código por linguagem/tecnologia.                          |
| **Comment Lines Density**    | 1.6               | Percentual de linhas de comentário em relação ao total de linhas de código.                |
| **Comment Lines**            | 454               | Quantidade total de linhas contendo comentários.                                          |
| **Uncovered Lines**          | 2,097             | Linhas de código que não foram cobertas por testes.                                       |
| **Cognitive Complexity**     | 347               | Medida da complexidade mental para entender o código, levando em conta estruturas e lógica.|
| **Duplicated Blocks**        | 11                | Número de blocos de código duplicado identificados.                                       |
| **Files**                   | 67                | Quantidade total de arquivos analisados.                                                  |
| **Vulnerabilities**          | 0                 | Número de vulnerabilidades de segurança encontradas.                                     |

---

## 📚 Documentação e links úteis

- [📘 SonarQube Docs](https://docs.sonarsource.com/sonarqube-server/latest/)
- [📘 SonarQube Docs - Generating and using tokens](https://docs.sonarsource.com/sonarqube-server/10.0/user-guide/user-account/generating-and-using-tokens/)
- [🧪 Gerar Token de Acesso](http://localhost:9000/account/security)
- [📏 Métricas no SonarQube](https://docs.sonarsource.com/sonarqube-server/latest/user-guide/code-metrics/metrics-definition/)
- [🎥 What is SonarQube (YouTube)](https://www.youtube.com/watch?v=xeTwG9XFFTE)
- [🔗 SonarQube Downloads](https://www.sonarsource.com/products/sonarqube/downloads/)

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.
