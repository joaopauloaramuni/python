# 🤖 Projeto Selenium Bot

Este projeto realiza a raspagem de dados do curso de **Engenharia de Software** da PUC Minas 🌐 utilizando **Selenium** com **ChromeDriver**.

🔗 Site alvo: [PUC Minas - Engenharia de Software](https://www.pucminas.br/campus/coracao-eucaristico/ensino/graduacao/Paginas/Engenharia-de-Software.aspx?curso=267)

---

## 🖼️ Captura de tela

| ![EngSoft](https://joaopauloaramuni.github.io/python-imgs/Selenium_Bot/imgs/engsoft.png) |
|:----------------------:|
|         EngSoft        |

---

## 🚀 O que é o Selenium?

O **Selenium** é uma poderosa ferramenta de automação para navegadores web.  
Ela permite que programas controlem navegadores automaticamente, simulando interações humanas como clicar em botões, preencher formulários, navegar entre páginas e extrair dados de sites.  
Isso é muito útil para testes automatizados de aplicações web, raspagem de dados (web scraping) e qualquer tarefa repetitiva que envolva navegação na internet.

O Selenium suporta vários navegadores, como Chrome, Firefox, Edge e Safari,  
e pode ser usado com várias linguagens de programação, como Python, Java, C# e JavaScript.

Para controlar um navegador específico, como o Google Chrome, o Selenium utiliza um componente chamado **ChromeDriver**.  
Esse driver atua como uma ponte entre o código automatizado e o navegador, permitindo que o Selenium envie comandos e receba respostas do Chrome de forma programática.

---

## 🧠 O que cada função faz?

### [`log(msg)`](log.txt)
Registra mensagens de log no arquivo [`log.txt`](log.txt) para monitorar o fluxo de execução e ajudar na depuração.

> 💡 A função pode ser facilmente ajustada para também imprimir no console, se desejado (basta descomentar a linha `print(msg)`).

### `fechar_banner_cookies(driver)`
Detecta e clica no botão de aceitação do banner de cookies da página, garantindo que o conteúdo da página fique acessível para o scraper, evitando bloqueios ou sobreposições.

### `extrair_nome_disciplina(td_element)`
Extrai o nome da disciplina a partir de uma célula `<td>` da tabela. A função busca primeiro um elemento `<h5>` com a classe `modal-title` e, se não encontrar, procura por links `<a>` que contenham o nome da disciplina, ignorando links que indiquem requisitos.

### `extrair_ementa(td_element)`
Obtém a ementa da disciplina a partir de um campo oculto do tipo `input` dentro da célula `<td>`. A ementa é uma descrição textual do conteúdo programático da disciplina.

### `extrair_carga_horaria(td_element)`
Extrai a carga horária da disciplina, normalmente um texto que indica a quantidade de horas dedicadas à disciplina, a partir do texto da célula da tabela.

### `extrair_requisitos(td_element)`
Coleta os pré-requisitos da disciplina, que indicam quais outras disciplinas são necessárias para cursá-la. A função tenta encontrar um campo `input` contendo a lista em HTML, extrai os itens `<li>`, e monta uma lista de pré-requisitos; caso contrário, tenta capturar texto simples.

### `limpar_texto(texto)`
Função utilitária para padronizar e limpar textos extraídos:
- Remove múltiplos espaços substituindo-os por um único espaço.
- Remove espaços antes e depois da barra `/`.
- Remove espaços em excesso no início e fim da string.
Esta função é usada para garantir que os textos fiquem legíveis e sem espaçamentos estranhos.

### `extrair_docentes(td_element)`
Extrai informações detalhadas sobre o corpo docente responsável pela disciplina. Ela organiza os docentes por seções (ex.: TEÓRICA, PRÁTICA), identificadas em elementos `<strong>`, e coleta os nomes e qualificações que aparecem em listas `<li>`. O texto é limpo e formatado para remoção de espaços indesejados.

### `expandir_painel_noite(driver)`
Verifica se o painel referente ao turno **NOITE** está colapsado na página. Caso esteja, tenta expandi-lo clicando no cabeçalho correspondente para garantir que os dados das disciplinas do período noturno sejam carregados e acessíveis para extração.

### `log_inicio_execucao()`
Registra no arquivo de log a data, hora e uma mensagem inicial indicando o começo da execução do scraper.

### `abrir_navegador_com_user_agent()`
Configura e abre uma instância do navegador Chrome via Selenium, definindo um user-agent personalizado para simular um navegador real e evitar possíveis bloqueios.

### `abrir_navegador()`
Função auxiliar que chama `abrir_navegador_com_user_agent()` e registra no log a abertura do navegador.

### `acessar_pagina(driver)`
Carrega a URL da página de Engenharia de Software da PUC Minas no navegador e registra essa ação no log.

### `localizar_painel_noite(driver)`
Tenta localizar o painel de disciplinas do turno **NOITE**. Primeiro procura pelo modo colapsável (via ID), se não encontrar, busca por um cabeçalho `<h3>` com o texto "NOITE" e seu respectivo conteúdo. Retorna o elemento painel encontrado ou `None` caso não ache.

### `processar_painel(painel)`
Percorre cada período dentro do painel NOITE, obtendo as tabelas e os títulos dos períodos. Para cada período, extrai e imprime as informações das disciplinas.

### `processar_linha_disciplina(linha)`
Recebe uma linha da tabela com dados da disciplina e extrai: nome, ementa, carga horária, requisitos e corpo docente, imprimindo essas informações formatadas no console.

### `abrir_pagina()`
Função principal que gerencia todo o fluxo de execução do scraper, seguindo estas etapas:
- Registra o início da execução no arquivo de log.
- Inicializa o navegador Chrome com configurações específicas.
- Acessa a página da graduação em Engenharia de Software da PUC Minas.
- Fecha o banner de cookies, se ele estiver presente, para liberar o acesso ao conteúdo.
- Garante que o painel do turno **NOITE** esteja expandido, caso esteja colapsado.
- Localiza o painel de disciplinas do turno **NOITE** (modo colapsável ou estático).
- Se o painel não for encontrado, encerra a execução e fecha o navegador.
- Caso contrário, processa o painel extraindo e exibindo as informações de todas as disciplinas de todos os períodos.
- Após a extração, aguarda que o usuário pressione Enter para encerrar a execução e fechar o navegador.
- Registra no log o fechamento do navegador, finalizando o processo.

---

## 📦 Instalação de dependências

Certifique-se de ter o **Python** instalado. Depois, execute:

```bash
pip install selenium
```

Se estiver usando Mac e Homebrew, instale o **ChromeDriver** com:

```bash
brew install chromedriver
```

---

## 🧪 Ambiente Virtual (Recomendado)

### Passo 1: Criar e ativar o ambiente virtual

É recomendado criar um ambiente virtual para isolar as dependências do projeto. Para configurar o ambiente virtual:

1. **Criar o ambiente virtual**:
   ```bash
   python -m venv venv
   ```

2. **Ativar o ambiente virtual**:
   - No Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Passo 2: Instalar as dependências

Após ativar o ambiente virtual, instale as dependências:
```bash
pip install selenium
```

---

## ▶️ Como executar

```bash
python selenium_bot.py
```

---

## 💻 Resultado no terminal

<details>
  <summary>Clique para exibir a saída do terminal</summary>

```
(.venv) (3.9.9) (base) joaopauloaramuni@MacBook-Pro-de-Joao Projeto Selenium Bot % python selenium_bot.py


============================================================ 1° período ============================================================

Disciplina: ALGORITMOS E ESTRUTURAS DE DADOS I
Ementa: Representação e armazenamento de dados. Manipulação e movimentação de dados em memória principal e secundária. Abstração de dados. Estruturas e abstração de controle. Modularização, encapsulamento e herança. Recursividade. Documentação e testes. Implementação em linguagem de programação. Contagem de operações.
Carga Horária: 120
Requisitos: --
Corpo Docente:
PRÁTICA:

PROFESSOR(A):ANTÔNIO GERMINEO LIMA ESTEVES
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 7 DIA(S)

PROFESSOR(A):IVAN LUIZ VIEIRA DE ARAÚJO
QUALIFICAÇÃO:SISTEMA DE INFORMAÇÃO
ÁREA DE CONHECIMENTO:ENGENHARIA MECÂNICA
TITULAÇÃO:MESTRE
TEMPO DE CASA:11 ANO(S) 4 MES(ES) 15 DIA(S)

TEÓRICA:

PROFESSOR(A):ANTÔNIO GERMINEO LIMA ESTEVES
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 7 DIA(S)

PROFESSOR(A):IVAN LUIZ VIEIRA DE ARAÚJO
QUALIFICAÇÃO:SISTEMA DE INFORMAÇÃO
ÁREA DE CONHECIMENTO:ENGENHARIA MECÂNICA
TITULAÇÃO:MESTRE
TEMPO DE CASA:11 ANO(S) 4 MES(ES) 15 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: CÁLCULO I
Ementa: Funções: polinomiais, racionais, algébricas, exponenciais, logarítmicas e trigonométricas. Aplicações de funções nas Ciências Exatas e Engenharias. Limites. Continuidade. Derivada: definição e interpretações. Regras de derivação. Derivação implícita. Aplicações de derivada: taxas relacionadas, regra de L’Hospital, estudo do comportamento de funções, esboço de gráficos e otimização. Aplicações de derivadas nas Ciências Exatas e Engenharias.
Carga Horária: 80
Requisitos: --
Corpo Docente:
TEÓRICA:

PROFESSOR(A):CLEIDE PERÔNICO DE ALMEIDA
QUALIFICAÇÃO:MATEMÁTICA
ÁREA DE CONHECIMENTO:ESTATÍSTICA
TITULAÇÃO:MESTRE
TEMPO DE CASA:1 MES(ES) 11 DIA(S)

PROFESSOR(A):ELENICE DE SOUZA LODRON ZUIN
QUALIFICAÇÃO:MATEMÁTICA
ÁREA DE CONHECIMENTO:MATEMÁTICA
TITULAÇÃO:DOUTOR
TEMPO DE CASA:35 ANO(S) 10 MES(ES) 11 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: DESENVOLVIMENTO DE INTERFACES WEB
Ementa: Evolução e tendências. W3C. Aquitetura, linguagens e padrões da Web. Fundamentos e técnicas de construção de interfaces. Ambientes de desenvolvimento e frameworks de front end.
Carga Horária: 80
Requisitos: --
Corpo Docente:
PRÁTICA:

PROFESSOR(A):DIEGO AUGUSTO DE FARIA BARROS
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:1 ANO(S) 4 MES(ES) 17 DIA(S)

TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: FUNDAMENTOS DE ENGENHARIA DE SOFTWARE
Ementa: Conceitos de sistemas de software. Componentes e relacionamento de sistemas de software. Fundamentos e classificação de sistemas de software. Conceitos básicos de Engenharia de Software. Processo de desenvolvimento de software. Métodos e técnicas para Engenharia de Software.
Carga Horária: 80
Requisitos: --
Corpo Docente:
TEÓRICA:

PROFESSOR(A):DANILO DE QUADROS MAIA FILHO
ÁREA DE CONHECIMENTO:ENGENHARIA ELETRICA
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 11 DIA(S)

PROFESSOR(A):JOSE LAERTE PIRES XAVIER JUNIOR
QUALIFICAÇÃO:CIÊNCIA DA COMPUTAÇÃO
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:DOUTOR
TEMPO DE CASA:4 ANO(S) 10 MES(ES) 14 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: INTRODUÇÃO À COMPUTAÇÃO
Ementa: Pesquisa, Ensino, Extensão, Inovação e Mercado. História da computação. Fundamentos de Computabilidade. Linguagens de programação. Principais áreas da Computação. Computação Verde. Práticas de extensão. Atividades de extensão com integração entre academia e saberes da sociedade.
Carga Horária: 70
Requisitos: --
Corpo Docente:
PRÁTICA:

PROFESSOR(A):DANIEL MACHADO OSÓRIO PEREIRA
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 15 DIA(S)

PROFESSOR(A):JOÃO PEDRO OLIVEIRA BATISTELI
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:3 MES(ES) 29 DIA(S)

TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: TRABALHO INTERDISCIPLINAR: APLICAÇÕES WEB
Ementa: Desenvolvimento de uma aplicação web front end usando um processo incremental e iterativo. Trabalho e avaliação em equipe.
Carga Horária: 50
Requisitos: DESENVOLVIMENTO DE INTERFACES WEB; ALGORITMOS E ESTRUTURAS DE DADOS I
Corpo Docente:
PRÁTICA:

PROFESSOR(A):DANIEL MACHADO OSÓRIO PEREIRA
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 15 DIA(S)

PROFESSOR(A):DANILO DE QUADROS MAIA FILHO
ÁREA DE CONHECIMENTO:ENGENHARIA ELETRICA
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 11 DIA(S)

PROFESSOR(A):DIEGO AUGUSTO DE FARIA BARROS
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:1 ANO(S) 4 MES(ES) 17 DIA(S)

PROFESSOR(A):MICHELLE HANNE SOARES DE ANDRADE
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:1 ANO(S) 4 MES(ES) 13 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------


============================================================ 2° período ============================================================

Disciplina: ARQUITETURA DE COMPUTADORES
Ementa: Modelos para representação de dados e aritmética computacional em nível de máquina. Introdução às funções e aos sistemas lógicos. Organização de sistemas de computação e dos subsistemas (processador, memória, entrada e saída, barramentos). Linguagem de montagem, conjunto de instruções e modos de endereçamento. Avaliação de desempenho. Hierarquia de memória. Modelos de arquiteturas sequenciais e paralelas.
Carga Horária: 40
Requisitos: --
Corpo Docente:
TEÓRICA:

PROFESSOR(A):ROMANELLI LODRON ZUIM
QUALIFICAÇÃO:ENGENHARIA ELÉTRICA/MATEMÁTICA
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:DOUTOR
TEMPO DE CASA:27 ANO(S) 7 MES(ES) 24 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: BANCOS DE DADOS
Ementa: Conceitos de gerenciamento de bancos de dados. Arquitetura de um SGBD. Modelos de dados. Modelo de bancos de dados. Linguagens de definição, manipulação e controle de dados. Normalização e projeto físico de bancos de dados. Aspectos de segurança em banco de dados.
Carga Horária: 80
Requisitos: ALGORITMOS E ESTRUTURAS DE DADOS I
Corpo Docente:
PRÁTICA:

PROFESSOR(A):ILO AMY SALDANHA RIVERO
QUALIFICAÇÃO:ADMINISTRAÇÃO
ÁREA DE CONHECIMENTO:INFORMÁTICA
TITULAÇÃO:MESTRE
TEMPO DE CASA:3 ANO(S) 4 MES(ES) 16 DIA(S)

TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: CÁLCULO II
Ementa: Integral indefinida. Técnicas de Integração: substituição, por partes, trigonométricas, substituição trigonométrica e frações parciais. Integral definida: conceitos e Teorema Fundamental do Cálculo. Integrais impróprias. Aplicações de integrais nas Ciências Exatas e Engenharias. Superfícies. Funções de várias variáveis. Derivadas parciais. Aproximações lineares. Regra da cadeia. Derivadas direcionais e vetor gradiente. Valores máximos e mínimos. Aplicações de funções de várias variáveis nas Ciências Exatas e Engenharias.
Carga Horária: 80
Requisitos: CÁLCULO I
Corpo Docente:
TEÓRICA:

PROFESSOR(A):LUIZ OTÁVIO RODRIGUES ALVES SERENO
QUALIFICAÇÃO:MATEMÁTICA
ÁREA DE CONHECIMENTO:MATEMÁTICA APLICADA
TITULAÇÃO:DOUTOR
TEMPO DE CASA:11 ANO(S) 4 MES(ES) 15 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: FILOSOFIA: RAZÃO E MODERNIDADE
Ementa: As origens da Filosofia.  A Filosofia como busca do conhecimento.  Ciência e Filosofia: o  surgimento  da modernidade,  a  racionalidade  instrumental  e  o  impacto  das  novas  tecnologias.  A questão  do  saber  e  da linguagem  nas sociedades contemporâneas.
Carga Horária: 40
Requisitos: --
Corpo Docente:
TEÓRICA:

PROFESSOR(A):PAULO ANDRADE VITORIA
QUALIFICAÇÃO:FILOSOFIA
ÁREA DE CONHECIMENTO:FILOSOFIA
TITULAÇÃO:DOUTOR
TEMPO DE CASA:7 ANO(S) 10 MES(ES) 17 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: LABORATÓRIO DE PROGRAMAÇÃO MODULAR
Ementa: Teste unitário. Projeto e desenvolvimento de software orientado para objetos. Implementação de sistemas utilizando padrões de projeto. Uso de recursos funcionais no desenvolvimento de sistemas.
Carga Horária: 40
Requisitos: PROGRAMAÇÃO MODULAR
Corpo Docente:
PRÁTICA:

PROFESSOR(A):DANIEL PIMENTEL KANSAON
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:1 MES(ES) 13 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: MODELAGEM DE PROCESSOS DE NEGÓCIOS
Ementa: Conceitos de processos. Tipos de processos. Elementos do Processo. Gesta?o orientada a processos. Mapeamento e modelagem de processos. Metodologia para modelagem de processos de nego?cios. Definic?a?o de objetivos, metas e indicadores de desempenho. Tecnologias para gesta?o de processos. Metodologias para gesta?o e avaliac?a?o de processos dos nego?cios.
Carga Horária: 60
Requisitos: FUNDAMENTOS DE ENGENHARIA DE SOFTWARE
Corpo Docente:
PRÁTICA:

PROFESSOR(A):MICHELLE HANNE SOARES DE ANDRADE
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:1 ANO(S) 4 MES(ES) 13 DIA(S)

TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: PROGRAMAÇÃO MODULAR
Ementa: Fatores de qualidade de software. Modularidade. Projeto Orientado para Objetos. Polimorfismos de Inclusão e Paramétrico. Tipos enumeráveis e opcionais. Coleções. Tratamento de exceções. Programação Orientada a Eventos. Princípios SOLID. Padrões de projeto. Aspectos funcionais. Teste unitário. Serialização.
Carga Horária: 80
Requisitos: ALGORITMOS E ESTRUTURAS DE DADOS I
Corpo Docente:
TEÓRICA:

PROFESSOR(A):DANIEL PIMENTEL KANSAON
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:1 MES(ES) 13 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: TRABALHO INTERDISCIPLINAR: APLICAÇÕES PARA PROCESSOS DE NEGÓCIOS
Ementa: Conceitos de programação modular aplicados na automação de processos de negócio. Avaliac?a?o do processo e do produto.
Carga Horária: 50
Requisitos: MODELAGEM DE PROCESSOS DE NEGÓCIOS; PROGRAMAÇÃO MODULAR; LABORATÓRIO DE PROGRAMAÇÃO MODULAR
Corpo Docente:
PRÁTICA:

PROFESSOR(A):DANILO DE QUADROS MAIA FILHO
ÁREA DE CONHECIMENTO:ENGENHARIA ELETRICA
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 11 DIA(S)

PROFESSOR(A):JOANA GABRIELA RIBEIRO DE SOUZA
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:10 MES(ES) 17 DIA(S)

PROFESSOR(A):MICHELLE HANNE SOARES DE ANDRADE
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:1 ANO(S) 4 MES(ES) 13 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------


============================================================ 3° período ============================================================

Disciplina: ALGORITMOS E ESTRUTURAS DE DADOS II
Ementa: Somatórios. Fundamentos de análise de algoritmos. Ordenação e pesquisa em memória principal. Tipos abstratos de dados lineares e flexíveis. Árvores. Balanceamento de árvores. Tabelas e Dicionários.
Carga Horária: 120
Requisitos: ALGORITMOS E ESTRUTURAS DE DADOS I
Corpo Docente:
PRÁTICA:

PROFESSOR(A):ARIANE CARLA BARBOSA DA SILVA
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 15 DIA(S)

PROFESSOR(A):PEDRO HENRIQUE RAMOS COSTA
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 15 DIA(S)

TEÓRICA:

PROFESSOR(A):ARIANE CARLA BARBOSA DA SILVA
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 15 DIA(S)

PROFESSOR(A):PEDRO HENRIQUE RAMOS COSTA
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 15 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: CULTURA RELIGIOSA: FENÔMENO RELIGIOSO
Ementa: O fenômeno religioso: experiência e linguagem. O fenômeno religioso como experiência específica: limites e possibilidades da experiência de Deus. As categorias fundamentais de interpretação e de linguagem do fenômeno religioso. Narrativas sagradas. A Bíblia em sua formação histórica, cultural e literária; os critérios de interpretação, os temas e as perspectivas de estudo e da experiência mística e de abertura que o livro sagrado propicia. O cristianismo e os desafios do diálogo ecumênico e inter-religioso no contexto de um mundo globalizado. História e fundamentos da cultura e tradições religiosas Afro Brasileira e Indígenas.
Carga Horária: 40
Requisitos: --
Corpo Docente:
TEÓRICA:

PROFESSOR(A):WELLINGTON TEODORO DA SILVA
QUALIFICAÇÃO:HISTÓRIA
ÁREA DE CONHECIMENTO:FILOSOFIA
TITULAÇÃO:DOUTOR
TEMPO DE CASA:23 ANO(S) 10 MES(ES) 17 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: ENGENHARIA DE REQUISITOS DE SOFTWARE
Ementa: Conceitos de Engenharia de software. Conceitos e tipos de Processos de Software. Engenharia de requisitos. Métodos e técnicas para análise e especificação de softwares. Introdução às estimativas de software. Atividades de extensão com integração entre academia e saberes da sociedade.
Carga Horária: 80
Requisitos: FUNDAMENTOS DE ENGENHARIA DE SOFTWARE
Corpo Docente:
TEÓRICA:

PROFESSOR(A):RAMON LACERDA MARQUES
ÁREA DE CONHECIMENTO:ENGENHARIA ELETRICA
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 15 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: INTRODUÇÃO À PESQUISA EM INFORMÁTICA
Ementa: Função da metodologia científica. Técnicas de pesquisa bibliográfica. Normalização do trabalho científico. Pesquisa bibliográfica como fundamentação teórica. Metodologias qualitativas de pesquisa em Informática. Metodologias quantitativas de pesquisa em Informática (métodos, descritivos, experimentais e estatísticos). Elaboração e execução de trabalhos científicos. Comunicação científica e resenhas.
Carga Horária: 40
Requisitos: --
Corpo Docente:
TEÓRICA:

PROFESSOR(A):DANILO DE QUADROS MAIA FILHO
ÁREA DE CONHECIMENTO:ENGENHARIA ELETRICA
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 11 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: SISTEMAS OPERACIONAIS
Ementa: Estrutura de um sistema operacional. Gerência de processos: processos, comunicação, escalonamento, multiprocessamento, programação concorrente. Sincronização de processos. Deadlock. Gerência de memória: memória virtual, paginação, segmentação, mudança de contexto, proteção. Gerenciamento de arquivos. Gerenciamento de dispositivos de entrada/saída. Sistemas Operacionais Atuais. Virtualização de Armazenamento. Simulação de Sistemas. Escalabilidade.
Carga Horária: 80
Requisitos: ARQUITETURA DE COMPUTADORES
Corpo Docente:
TEÓRICA:

PROFESSOR(A):LESANDRO PONCIANO DOS SANTOS
QUALIFICAÇÃO:SISTEMAS DE INFORMAÇÃO
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:DOUTOR
TEMPO DE CASA:6 ANO(S) 10 MES(ES) 18 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: TRABALHO INTERDISCIPLINAR: APLICAÇÕES PARA CENÁRIOS REAIS
Ementa: Descrição dos requisitos funcionais e não funcionais de um software. Atividades de extensão com integração entre academia e saberes da sociedade na finalidade do desenvolvimento dos requisitos de um software de um cliente. Avaliação do artefato de requisitos.
Carga Horária: 45
Requisitos: ALGORITMOS E ESTRUTURAS DE DADOS II; ENGENHARIA DE REQUISITOS DE SOFTWARE
Corpo Docente:
PRÁTICA:

PROFESSOR(A):DANILO DE QUADROS MAIA FILHO
ÁREA DE CONHECIMENTO:ENGENHARIA ELETRICA
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 11 DIA(S)

PROFESSOR(A):JOÃO PAULO CARNEIRO ARAMUNI
ÁREA DE CONHECIMENTO:SISTEMAS DE COMPUTAÇÃO
TITULAÇÃO:DOUTOR
TEMPO DE CASA:10 MES(ES) 17 DIA(S)

PROFESSOR(A):RAMON LACERDA MARQUES
ÁREA DE CONHECIMENTO:ENGENHARIA ELETRICA
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 15 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------


============================================================ 4° período ============================================================

Disciplina: INTERAÇÃO HUMANO-COMPUTADOR
Ementa: Conceitos básicos de Interação Humano-Computador. Engenharia cognitiva e abordagens semióticas. Fatores humanos em software interativo: teorias, princípios e regras básicas. Ciclo de vida na Engenharia da Usabilidade. Estilos de interface. Projeto e prototipação de interface e interação para diversos dispositivos. Definição e métodos para avaliação de usabilidade e acessibilidade. Atividades de extensão com integração entre academia e saberes da sociedade.
Carga Horária: 90
Requisitos: ENGENHARIA DE REQUISITOS DE SOFTWARE
Corpo Docente:
TEÓRICA:

PROFESSOR(A):LESANDRO PONCIANO DOS SANTOS
QUALIFICAÇÃO:SISTEMAS DE INFORMAÇÃO
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:DOUTOR
TEMPO DE CASA:6 ANO(S) 10 MES(ES) 18 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: LABORATÓRIO DE DESENVOLVIMENTO DE SOFTWARE
Ementa: Elaboração de um projeto de um software dividido em camadas. Construção da camada de apresentação (interfaces reais). Construção da camada de aplicação. Construção da camada de domínio. Construção da camada de persistência/acesso a dados (Implementação de Bancos de Dados). Desenvolvimento do sistema projetado.
Carga Horária: 40
Requisitos: PROJETO DE SOFTWARE
Corpo Docente:
PRÁTICA:

PROFESSOR(A):JOÃO PAULO CARNEIRO ARAMUNI
ÁREA DE CONHECIMENTO:SISTEMAS DE COMPUTAÇÃO
TITULAÇÃO:DOUTOR
TEMPO DE CASA:10 MES(ES) 17 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: OPTATIVA I
Ementa: Disciplina de natureza estratégica que permite ao aluno escolher, entre um conjunto de disciplinas previamente definidas, diferentes conteúdos complementares à sua formação.
Carga Horária: 80
Requisitos: --
Corpo Docente:
TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: PROJETO DE SOFTWARE
Ementa: Conceituação de projeto de software. Introdução à Arquitetura de Software. Organização e projeto das camadas de negócios, serviços e dados. Modelagem estrutural e comportamental. Padrões de Projeto. Qualidade de projeto.
Carga Horária: 80
Requisitos: PROGRAMAÇÃO MODULAR; ENGENHARIA DE REQUISITOS DE SOFTWARE
Corpo Docente:
TEÓRICA:

PROFESSOR(A):JOÃO PAULO CARNEIRO ARAMUNI
ÁREA DE CONHECIMENTO:SISTEMAS DE COMPUTAÇÃO
TITULAÇÃO:DOUTOR
TEMPO DE CASA:10 MES(ES) 17 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: REDES DE COMPUTADORES
Ementa: Conceitos básicos de redes de computadores. Redes sem fio e cabeadas. Protocolo IP e endereçamento. Protocolos de transporte: TCP e UDP. Aplicações. Redes Multimídia. Arquitetura de Infraestrutura de TI. Virtualização. Computação em Nuvem. Comunicação entre dispositivos inteligentes.
Carga Horária: 80
Requisitos: SISTEMAS OPERACIONAIS
Corpo Docente:
TEÓRICA:

PROFESSOR(A):RAFAEL BAMBIRRA PEREIRA
ÁREA DE CONHECIMENTO:ENGENHARIA ELETRICA
TITULAÇÃO:DOUTOR
TEMPO DE CASA:4 MES(ES) 8 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: TEORIA DOS GRAFOS E COMPUTABILIDADE
Ementa: Lógica, relações de equivalência, funções e conjuntos. Prova e demonstração de teoremas. Estruturas de dados para grafos, caminhos, busca, árvores, conectividade, isomorfismo, planaridade, coloração, particionamento, modelagem de problemas e fluxo em redes.
Carga Horária: 120
Requisitos: ALGORITMOS E ESTRUTURAS DE DADOS II
Corpo Docente:
PRÁTICA:

PROFESSOR(A):LEONARDO VILELA CARDOSO
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:2 ANO(S) 10 MES(ES) 17 DIA(S)

TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: TRABALHO INTERDISCIPLINAR: APLICAÇÕES PARA SUSTENTABILIDADE
Ementa: Planejamento do projeto de software. Detalhamento dos requisitos de um software. Produc?a?o de artefatos de projeto e desenvolvimento de software. Atividades de extensão com integração entre academia e saberes da sociedade na finalidade do desenvolvimento dos artefatos de software aplicados a? projetos para sustentabilidade.
Carga Horária: 50
Requisitos: PROJETO DE SOFTWARE
Corpo Docente:
PRÁTICA:

PROFESSOR(A):JOANA GABRIELA RIBEIRO DE SOUZA
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:10 MES(ES) 17 DIA(S)

PROFESSOR(A):RAMON LACERDA MARQUES
ÁREA DE CONHECIMENTO:ENGENHARIA ELETRICA
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 15 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------


============================================================ 5° período ============================================================

Disciplina: ARQUITETURA DE SOFTWARE
Ementa: Conceitos de Arquiteturas de Software. Requisitos Arquiteturais. Padro?es arquiteturais. Modelos Baseados em Camadas, Componentes e Agentes. Arquiteturas: orientadas a mensagens, orientadas a servic?os, para persiste?ncia de dados, de objetos distribui?dos, para aplicac?o?es Web, para dispositivos mo?veis, para aplicac?o?es ubi?quas.
Carga Horária: 80
Requisitos: PROJETO DE SOFTWARE
Corpo Docente:
TEÓRICA:

PROFESSOR(A):DANIEL MACHADO OSÓRIO PEREIRA
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:4 MES(ES) 15 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: CULTURA RELIGIOSA: PESSOA E SOCIEDADE
Ementa: Fundamentação da práxis cristã. A categoria Pessoa em diálogo com categorias antropológicas contemporâneas. Temas atuais à luz do Humanismo Cristão: a família e a dimensão afetivo-sexual; o mundo do trabalho; ordem social e política, e a cidadania. O compromisso com o cuidado e a defesa da vida humana e ecológica, e as perspectivas de construção de uma nova ordem mundial, centrada na sustentabilidade, na justiça, no amor e na paz.
Carga Horária: 40
Requisitos: --
Corpo Docente:
TEÓRICA:

PROFESSOR(A):JOSE MARTINS DOS SANTOS NETO
QUALIFICAÇÃO:LETRAS/FILOSOFIA
ÁREA DE CONHECIMENTO:FILOSOFIA
TITULAÇÃO:DOUTOR
TEMPO DE CASA:27 ANO(S) 5 MES(ES) 19 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: DESENVOLVIMENTO DE APLICAÇÕES MÓVEIS E DISTRIBUÍDAS
Ementa: Fundamentos de sistemas distribuídos e computação móvel. Comunicação entre processos. Middlewares. Ambientes e ferramentas para o desenvolvimento de aplicações móveis e distribuídas. Problemas e limitações relacionados à mobilidade e à modalidade de comunicação. Coordenação e consenso. Transações distribuídas e controle de concorrência. Consistência, replicação e tolerância à falha. Computação ubíqua e pervasiva. Sistemas cientes de contexto.
Carga Horária: 80
Requisitos: PROGRAMAÇÃO MODULAR; REDES DE COMPUTADORES
Corpo Docente:
TEÓRICA:

PROFESSOR(A):CRISTIANO NEVES RODRIGUES
ÁREA DE CONHECIMENTO:ENGENHARIA ELETRICA
TITULAÇÃO:MESTRE
TEMPO DE CASA:1 ANO(S) 4 MES(ES) 12 DIA(S)

PROFESSOR(A):DANIEL EUGÊNIO NEVES
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:DOUTOR
TEMPO DE CASA:2 MES(ES) 16 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: ESTATÍSTICA E PROBABILIDADE
Ementa: Estatística descritiva. Probabilidade. Variáveis aleatórias. Distribuições discretas. Distribuições contínuas. Inferência estatística: estimação, intervalos de confiança e testes de hipóteses. Regressão linear.
Carga Horária: 80
Requisitos: CÁLCULO I
Corpo Docente:
PRÁTICA:

Professor(es) a definir

TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: FUNDAMENTOS DE PROJETO E ANÁLISE DE ALGORITMOS
Ementa: Fundamentos de análise de algoritmos. Análise de algoritmos. Técnicas de Projeto de Algoritmos. Teoria da Complexidade.
Carga Horária: 40
Requisitos: TEORIA DOS GRAFOS E COMPUTABILIDADE
Corpo Docente:
TEÓRICA:

PROFESSOR(A):FELIPE DE CASTRO BELÉM
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:DOUTOR
TEMPO DE CASA:1 ANO(S) 4 MES(ES) 17 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: GERÊNCIA DE PROJETOS DE SOFTWARE
Ementa: Conceito de gerência de projeto de software. Planejamento de projeto. Gerência de recursos. Controle de projetos. Processo de gerência de projetos. Modelos para gerencia de projetos. Utilização de softwares para planejamento e acompanhamento de projetos.
Carga Horária: 60
Requisitos: ENGENHARIA DE REQUISITOS DE SOFTWARE
Corpo Docente:
PRÁTICA:

PROFESSOR(A):MATHEUS LUIZ PONTELO DE SOUZA
QUALIFICAÇÃO:ENGENHARIA DE PRODUÇÃO
ÁREA DE CONHECIMENTO:FARMACOLOGIA
TITULAÇÃO:DOUTOR
TEMPO DE CASA:6 ANO(S) 4 MES(ES) 14 DIA(S)

TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: LABORATÓRIO DE DESENVOLVIMENTO DE APLICAÇÕES MÓVEIS E DISTRIBUÍDAS
Ementa: Elaboração da arquitetura de um sistema de software distribuído com clientes móveis e web. Desenvolvimento utilizando middlewares de comunicação. Comunicação indireta. Programação de sistemas baseados em nuvem. Construção de software utilizando funções como serviço.
Carga Horária: 40
Requisitos: DESENVOLVIMENTO DE APLICAÇÕES MÓVEIS E DISTRIBUÍDAS
Corpo Docente:
PRÁTICA:

PROFESSOR(A):ARTUR MARTINS MOL
QUALIFICAÇÃO:CIÊNCIA DA COMPUTAÇÃO
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:DOUTOR
TEMPO DE CASA:17 ANO(S) 8 MES(ES) 26 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: OPTATIVA II
Ementa: Disciplina de natureza estratégica que permite ao aluno escolher, entre um conjunto de disciplinas previamente definidas, diferentes conteúdos complementares à sua formação.
Carga Horária: 80
Requisitos: --
Corpo Docente:
TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: TRABALHO INTERDISCIPLINAR: APLICAÇÕES DISTRIBUÍDAS
Ementa: Planejamento e detalhamento do projeto de arquitetura de um software. Produção de artefatos de arquitetura de software e gerência de projetos. Implementação de um software distribuído de acordo com a arquitetura projetada. Avaliação da arquitetura do sistema.
Carga Horária: 45
Requisitos: ARQUITETURA DE SOFTWARE
Corpo Docente:
PRÁTICA:

PROFESSOR(A):ARTUR MARTINS MOL
QUALIFICAÇÃO:CIÊNCIA DA COMPUTAÇÃO
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:DOUTOR
TEMPO DE CASA:17 ANO(S) 8 MES(ES) 26 DIA(S)

PROFESSOR(A):LEONARDO VILELA CARDOSO
ÁREA DE CONHECIMENTO:CIÊNCIA DA COMPUTAÇÃO
TITULAÇÃO:MESTRE
TEMPO DE CASA:2 ANO(S) 10 MES(ES) 17 DIA(S)
----------------------------------------------------------------------------------------------------------------------------------


============================================================ 6° período ============================================================

Disciplina: ENGENHARIA ECONÔMICA PARA SOFTWARE
Ementa: Estimativa por pontos de função; Estimativa por dados históricos; Modelo COCOMO; Modelos empíricos de estimativa de software. Proposta técnica. Contratos de aquisição de software e serviços. Analise de viabilidade técnica e econômica. Retorno sobre investimento (ROI). Licença, Patente e propriedade intelectual ou industrial.
Carga Horária: 80
Requisitos: --
Corpo Docente:
TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: GERÊNCIA DE CONFIGURAÇÃO E EVOLUÇÃO DE SOFTWARE
Ementa: Conceitos. Papéis, Artefatos e Atividades de Gerência de Configuração. Princípios de entrega contínua. Integração contínua. A cultura DevOps. Definição e projeto de Build. Ferramentas. Provisionamento de ambientes de desenvolvimento, produção, integração e testes. Princípios e técnicas de manutenção de software. Tipos de manutenções. Reengenharia.
Carga Horária: 80
Requisitos: PROJETO DE SOFTWARE
Corpo Docente:
TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: LABORATÓRIO DE EXPERIMENTAÇÃO DE SOFTWARE
Ementa: Aplicação prática, em um projeto, de técnicas de medição e experimentação em Engenharia de Software e processos de software.
Carga Horária: 40
Requisitos: MEDIÇÃO E EXPERIMENTAÇÃO EM ENGENHARIA DE SOFTWARE
Corpo Docente:
PRÁTICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: MEDIÇÃO E EXPERIMENTAÇÃO EM ENGENHARIA DE SOFTWARE
Ementa: Métricas de software: conceito. Métricas objetivas e subjetivas; Métricas para processo, projeto e produto. Processo e Técnicas de medição e análise. Noções de confiabilidade metrológica. Controle estatístico de qualidade. Aplicação de técnicas estatísticas para análise de dados: análise fatorial, análise multivariada e testes de hipóteses. Estabilidade de processos. Princípios e técnicas para experimentação em Engenharia de Software. Planejamento e condução de experimentos.
Carga Horária: 80
Requisitos: ESTATÍSTICA E PROBABILIDADE
Corpo Docente:
TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: OPTATIVA III
Ementa: Disciplina de natureza estratégica que permite ao aluno escolher, entre um conjunto de disciplinas previamente definidas, diferentes conteúdos complementares à sua formação.
Carga Horária: 80
Requisitos: --
Corpo Docente:
TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: TESTE DE SOFTWARE
Ementa: Fundamentos de testes. Níveis de testes. Tipos de testes. Técnicas de projeto de testes. Ferramentas de suporte a testes. Automatização de testes. Projeto de casos de teste. Planos de testes. Gerenciamento do processo de testes. Registro e acompanhamento de problemas. Técnicas de verificação e validação de sistemas.
Carga Horária: 80
Requisitos: ENGENHARIA DE REQUISITOS DE SOFTWARE
Corpo Docente:
TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: TRABALHO INTERDISCIPLINAR: PESQUISA EM ENGENHARIA DE SOFTWARE
Ementa: Planejamento e execução de um experimento de Engenharia de Software.
Carga Horária: 45
Requisitos: MEDIÇÃO E EXPERIMENTAÇÃO EM ENGENHARIA DE SOFTWARE
Corpo Docente:
PRÁTICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------


============================================================ 7° período ============================================================

Disciplina: COMPUTADORES E SOCIEDADE
Ementa: A evolução tecnológica e os distintos contextos sociais. Consequências da informatização na sociedade: aspectos culturais, sociais e de sociabilidade.
Carga Horária: 40
Requisitos: --
Corpo Docente:
TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: ENGENHARIA DE PROCESSOS E QUALIDADE DE SOFTWARE
Ementa: Conceitos de processos e produtos. Modelos de processos de software.  Definição, personalização, institucionalização e avaliação de processos de desenvolvimento de software. Qualidade de Software: Normas e modelos de maturidade de processo de desenvolvimento de software. Avaliação de Qualidade e Certificação. Melhoria continua. Processos críticos.
Carga Horária: 80
Requisitos: ENGENHARIA DE REQUISITOS DE SOFTWARE
Corpo Docente:
TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: FILOSOFIA: ANTROPOLOGIA E ÉTICA
Ementa: Concepções filosófico-antropológicas. O ser humano como ser no mundo e sua dimensão simbólico-cultural. A condição ética da ação humana. Questões éticas fundamentais e atuais, sociedade de consumo, diversidade étnica e desafios ecológicos.
Carga Horária: 80
Requisitos: --
Corpo Docente:
TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: GESTÃO DA PRODUÇÃO DE SOFTWARE
Ementa: Caracterização da função planejamento da produção nas organizações. O PCP (Planejamento e Controle da Produção) na empresa. Conciliação entre suprimento e demanda. Parâmetros de Controle de Produção. Fundamentos da qualidade. Produção Enxuta (Lean Manufacturing).
Carga Horária: 40
Requisitos: GERÊNCIA DE PROJETOS DE SOFTWARE
Corpo Docente:
TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: TECNOLOGIAS DA INFORMAÇÃO E DO CONHECIMENTO
Ementa: Sociedade do Conhecimento. Estratégia e Inteligência Competitiva. Processos de Gestão da Informação. Processos de Gestão do Conhecimento. Sistema de Inteligência Competitiva. Integração da Inteligência Competitiva com a Gestão do Conhecimento. Tecnologia da Informação aplicada à Gestão da Informação. Tecnologia da Informação aplicada à Gestão do Conhecimento.
Carga Horária: 40
Requisitos: MODELAGEM DE PROCESSOS DE NEGÓCIOS
Corpo Docente:
TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: TÓPICOS EM COMPUTAÇÃO I
Ementa: Tema atual na área de Computação.
Carga Horária: 40
Requisitos: FUNDAMENTOS DE PROJETO E ANÁLISE DE ALGORITMOS
Corpo Docente:
PRÁTICA:

Professor(es) a definir

TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: TÓPICOS EM COMPUTAÇÃO II
Ementa: Tema atual na área de Computação.
Carga Horária: 40
Requisitos: FUNDAMENTOS DE PROJETO E ANÁLISE DE ALGORITMOS
Corpo Docente:
PRÁTICA:

Professor(es) a definir

TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: TRABALHO DE CONCLUSÃO DE CURSO I
Ementa: Elaboração de um projeto de trabalho que contribua para a melhoria da automação, do desempenho, da eficiência e da racionalização dos recursos no desenvolvimento, experimentação, manutenção e operação de software. Caracterização da natureza e objetivos do Trabalho de Conclusão de Curso. Elaboração do projeto de desenvolvimento, com metodologia, cronograma e descrição dos resultados esperados. Elaboração de resenhas e construção do estado da arte da área relacionada ao projeto.
Carga Horária: 60
Requisitos: INTRODUÇÃO À PESQUISA EM INFORMÁTICA
Corpo Docente:
PRÁTICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------


============================================================ 8° período ============================================================

Disciplina: MODELAGEM E AVALIAÇÃO DE DESEMPENHO
Ementa: Ciclo de vida, avaliação, modelagem e otimização de sistemas computacionais. Planejamento de capacidade. Curvas de desempenho teóricas e experimentais. Técnicas para avaliação de desempenho. Previsão de carga futura. Paradigmas de modelagem. Modelos de Markov e Teoria das filas. Modelos de sistemas computacionais. Simulação de modelos.
Carga Horária: 80
Requisitos: TEORIA DOS GRAFOS E COMPUTABILIDADE; ESTATÍSTICA E PROBABILIDADE
Corpo Docente:
TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: OPTATIVA IV
Ementa: Disciplina de natureza estratégica que permite ao aluno escolher, entre um conjunto de disciplinas previamente definidas, diferentes conteúdos complementares à sua formação.
Carga Horária: 80
Requisitos: --
Corpo Docente:
TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: SEGURANÇA E AUDITORIA DE SISTEMAS
Ementa: Auditoria de sistemas de informação. Ambiente de auditoria. Pirâmide da tecnologia de auditagem, conceitos básicos. Posicionamento na organização. Descrição das fases. Análise e desenvolvimento do processo. Segurança física e segurança lógica da informação. Contribuição do software em elementos de prevenção e combate a incêndios e desastres. Atividades de extensão com integração entre academia e saberes da sociedade.
Carga Horária: 60
Requisitos: PROJETO DE SOFTWARE; REDES DE COMPUTADORES
Corpo Docente:
PRÁTICA:

Professor(es) a definir

TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: TÓPICOS EM ENGENHARIA DE SOFTWARE
Ementa: Tema atual na área de Engenharia de Software.
Carga Horária: 40
Requisitos: PROJETO DE SOFTWARE
Corpo Docente:
PRÁTICA:

Professor(es) a definir

TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: TÓPICOS EM SISTEMAS DE SOFTWARE
Ementa: Tema atual na área de Sistemas de Informação e Engenharia de Software.
Carga Horária: 40
Requisitos: --
Corpo Docente:
PRÁTICA:

Professor(es) a definir

TEÓRICA:

Professor(es) a definir
----------------------------------------------------------------------------------------------------------------------------------

Disciplina: TRABALHO DE CONCLUSÃO DE CURSO II
Ementa: Execução e acompanhamento do projeto de trabalho elaborado na disciplina Trabalho de Conclusão de Curso I. Elaboração de artigo no padrão estabelecido pela PUC Minas. Apresentação do Trabalho de Conclusão de Curso perante professores avaliadores.
Carga Horária: 75
Requisitos: TRABALHO DE CONCLUSÃO DE CURSO I
```
</details>

---

## 📚 Documentação e links úteis

- 🌍 [Site oficial do Selenium](https://www.selenium.dev/)
- 📘 [Documentação do Selenium](https://www.selenium.dev/documentation/)
- 🐙 [Repositório GitHub do Selenium](https://github.com/SeleniumHQ/selenium)
- 🧪 [Pacote Selenium no PyPI](https://pypi.org/project/selenium/)

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Sinta-se à vontade para usar, modificar e distribuir. 🤝
