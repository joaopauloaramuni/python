<p align="center"><img src="https://github.com/tassiovirginio/jnose/blob/master/src/main/webapp/logo.png?raw=true" width="70"></p>

# JNose - Tutorial
Java TestSmells Detection

O JNose Test é uma ferramenta desenvolvida para detectar automaticamente test smells no código de teste e coletar métricas de cobertura. 
O JNose Test foi baseado no tsDetect. Além de apresentar o número de test smells detectados por classe, nossa ferramenta mostra a coleção de métricas de código e cobertura de teste usando a biblioteca JaCoCo; 
um resultado unificado para todos os projetos em análise; e uma interface gráfica. 
Além disso, o projeto usa o Apache Maven para gerenciar todas as dependências da biblioteca e oferecer suporte à compilação e execução da ferramenta JNose Test.

## Pré-requisitos

<a target="_blank" href="https://github.com/arieslab/jnose">
  Dependence on Project (JNose-Core)
</a>

It is necessary to install the "jnose-core" dependency for JNose to work. Below is the step by step to install, before installing Jnose.

```shell
git clone https://github.com/arieslab/jnose-core
cd jnose-core
mvn install
```

 - JDK 11
 - Maven 3 
 - GIT

## Download e Executar
 - git clone https://github.com/arieslab/jnose
 - cd jnose
 - mvn jetty:run
 - acessar: http://127.0.0.1:8080

## Tela inicial
<p align="center">
  <img src="https://github.com/tassiovirginio/jnose/blob/master/docs/tela_01.png?raw=true" width="800">
</p>

Na tela inicial temos a descrição de cada opção de busca e a opção de configuração:
 - by ClassTest: Realiza a busca com base na classe de teste, retornando a quantidade de cada tipo de test smells encontrados em cada classe.
 - by TestSmells: realiza a busca com base no test smell, dizendo em qual classe ele foi encontrado e a linha que foi encontrado.
 - Evolution: Faz uma busca no repositório do projeto (git) em busca de test smells em cada commit/tag realizado.
 - Configuration: Temos a opção de escolher quais os test smells que queremos realizar a busca, por padrão todos estão selecionados.
 
## By ClassTest
<p align="center">
  <img src="https://github.com/tassiovirginio/jnose/blob/master/docs/tela_02.png?raw=true" width="800">
</p>
Inicialmente "colamos" o endereço da pasta onde se encontra os projetos "Folders with projects".

Ex:
 - Linux: /home/nome/projetos
 - Windows: C:\users\name\projetos
<p align="center">
 <img src="docs/screenshot.png" width="800">
</p>

Depois de "colar" o endereço da pasta dos projetos que se encontra na sua maquina, clicamos em "Select Directory". Na caixa que se encontra logo a baixo serão mostrados todos os projetos dentro da pasta selecionada.

<p align="center">
  <img src="https://github.com/tassiovirginio/jnose/blob/master/docs/tela_02_01.png?raw=true" width="800">
</p>

Poderemos selecionar todos os projetos que se encontram na lista, ou selecionar somente alguns deles, com a opção do checkbox que cada projeto tem na frente do seu nome.

Depois mandaremos executar a busca por test smells clicando no botão "Process".

A Busca será iniciada e poderemos acompanar atraves da barra de progresso em cada projeto e na barra de progresso geral.

Ao Final será gerado um CSV com os resultados obtidos.

Retorno(CSV): Nome do Projeto, Classe de Teste, Classe de Produção, LOC, Número de Métodos e a quantidade de cada um dos 21 test_smells encontrados por classe de teste.

## By TestSmells
<p align="center">
  <img src="https://github.com/tassiovirginio/jnose/blob/master/docs/tela_03.png?raw=true" width="800">
</p>
Nesta opção, podemos passar no final da pasta "projeto", que será pesquisada por cheiros de teste. Com o seguinte retorno: Nome do Projeto, Classe de Teste, Classe de Produção, nome dos cheiros de teste, nome do método, linha de ocorrência, linha de ocorrência inicial, linha de ocorrência final.

## Evolution
<p align="center">
  <img src="https://github.com/tassiovirginio/jnose/blob/master/docs/tela_04.png?raw=true" width="800">
</p>
Usando o controle de versão GIT, podemos realizar uma pesquisa por odores de teste em cada confirmação executada ou tag existente no histórico do projeto. O retorno é o mesmo que o ByClassTest, com informações adicionais de confirmação: ID de confirmação, nome de quem confirmou, data de confirmação e mensagem de confirmação. Para funcionar, o projeto deve ser clonado: git clone https: //address.do.project

## Configuration
<p align="center">
  <img src="https://github.com/tassiovirginio/jnose/blob/master/docs/tela_05.png?raw=true" width="800">
</p>

### Email para contato:
- tassiovirginio@gmail.com
