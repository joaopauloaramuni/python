# Projeto JNose Test Smells Analyser

## Sobre o projeto

Este projeto automatiza o processo de análise de **Test Smells** em projetos Java usando a ferramenta **JNose**. Ele realiza o clone de um repositório público, compila o projeto (suportando Maven e Gradle) e executa o JNose para gerar um arquivo CSV contendo métricas relacionadas aos testes do projeto.

<p align="center"><img src="https://joaopauloaramuni.github.io/python-imgs/JNose_Test_Smells_Analyser/imgs/logo_jnose.png?raw=true" width="70"></p>

---

## 👃 O que é o JNose?

O **JNose** é uma ferramenta de análise estática para identificar *Test Smells* em testes automatizados escritos em Java. Ele avalia a qualidade dos testes para detectar padrões que podem indicar problemas, como testes frágeis, repetitivos ou difíceis de manter.

O JNose Test é uma ferramenta desenvolvida para detectar automaticamente test smells no código de teste e coletar métricas de cobertura. O JNose Test foi baseado no tsDetect. Além de apresentar o número de test smells detectados por classe, a ferramenta mostra a coleção de métricas de código e cobertura de teste usando a biblioteca JaCoCo; um resultado unificado para todos os projetos em análise; e uma interface gráfica. Além disso, o projeto usa o Apache Maven para gerenciar todas as dependências da biblioteca e oferecer suporte à compilação e execução da ferramenta JNose Test.

O JNose foi apresentado na `CBSoft’20 — Congresso Brasileiro de Software`, na trilha `SBES Tools Track`, onde recebeu o prêmio `Best Paper` 🏆.

Autores: Tássio Virgínio (Federal Institute of Tocantins), Luana Martins, Railana Santana, Larissa Rocha, Ivan Machado (Federal University of Bahia), Adriana Cruz, Heitor Costa (Federal University of Lavras)

### 📚 Referências

**2021** — `On the test smells detection: an empirical study on the JNose Test accuracy`  
*Journal of Software Engineering Research and Development*  
https://doi.org/10.5753/jserd.2021.1893  

**2020** — `JNose: Java Test Smell Detector`  
*Congresso Brasileiro de Software: Teoria e Prática (CBSoft - 2020) — Trilha de Ferramentas*  
http://cbsoft2020.imd.ufrn.br/artigos.php?evento=sbes-ferramentas  

**2020** — `An Empirical Study of Automatically-Generated Tests from the Perspective of Test Smells`  
*Congresso Brasileiro de Software: Teoria e Prática (CBSoft - 2020) — Trilha de Pesquisa*  
http://cbsoft2020.imd.ufrn.br/artigos.php?evento=sbes-pesquisa  

**2019** — `On the influence of Test Smells on Test Coverage`  
*33º Simpósio Brasileiro de Engenharia de Software (SBES - 2019)*  
Proceedings of the XXXIII Brazilian Symposium on Software Engineering  
[https://dl.acm.org/doi/10.1145/3350768.3350775](https://dl.acm.org/doi/10.1145/3350768.3350775)

---

## 🧪 O que são Test Smells?

*Test Smells* são sinais ou padrões em testes automatizados que indicam possíveis problemas de qualidade, dificultando a manutenção, legibilidade ou confiabilidade dos testes. Assim como *code smells* apontam problemas no código de produção, *test smells* indicam que os testes podem estar mal escritos ou estruturalmente problemáticos.

### Exemplos comuns de Test Smells:

- **Test Frágil:** Testes que falham frequentemente devido a pequenas mudanças no código ou no ambiente, não necessariamente por bugs reais.
- **Teste Dependente:** Quando um teste depende do resultado ou da execução de outro teste, criando dependências ocultas que dificultam a execução isolada.
- **Teste Lento:** Testes que demoram muito para rodar, prejudicando ciclos rápidos de desenvolvimento.
- **Teste Repetitivo:** Código duplicado nos testes, que torna a manutenção mais trabalhosa e aumenta o risco de erros.
- **Setup Complexo:** Quando o cenário necessário para rodar o teste é muito complexo, tornando o teste difícil de entender e manter.

### Por que se preocupar com Test Smells?

Além de dificultarem manutenção e legibilidade, *test smells* podem:

- Levar a **falsos positivos ou falsos negativos** nos testes.
- Diminuir a **confiabilidade** da suíte de testes.
- Tornar a identificação de **regressões reais** mais difícil.
- Impactar a **confiança da equipe** nos testes automatizados, levando ao seu abandono.

### Outros exemplos comuns de Test Smells:

- **Eager Test:** Quando um único teste verifica comportamentos demais, violando o princípio de que cada teste deve ter um foco específico.
- **Assertion Roulette:** Muitos `asserts` num mesmo teste sem mensagens claras, dificultando identificar qual falhou.
- **Mystery Guest:** Uso de recursos externos (como arquivos ou bancos de dados) sem transparência no teste, tornando o comportamento imprevisível.
- **Conditional Test Logic:** Lógica condicional (`if`, `switch`, etc.) dentro dos testes, que pode esconder comportamentos inesperados.
- **Resource Optimism:** Quando o teste assume que recursos externos (ex: conexões, arquivos) estarão sempre disponíveis, causando falhas intermitentes.

Detectar e corrigir *Test Smells* ajuda a garantir uma suíte de testes mais confiável, eficiente e fácil de evoluir.

---

## 📚 Diferenças entre JNose e JNose-Core

O **JNose** e o **JNose-Core** são projetos relacionados, mas com focos e funcionalidades diferentes dentro do ecossistema de detecção de *Test Smells* em Java.

### JNose

- É a ferramenta principal com interface e funcionalidades completas.
- Inclui a interface gráfica para visualização dos resultados.
- Gerencia a análise de projetos Java completos, integrando detecção de *test smells*, métricas de cobertura (via JaCoCo) e métricas de código.
- Facilita o uso para usuários finais, oferecendo uma experiência “pronta para uso”.
- Normalmente usado para execução direta e análise de projetos.

#### 🖼️ Interface Gráfica

| ![Interface](https://joaopauloaramuni.github.io/python-imgs/JNose_Test_Smells_Analyser/imgs/home.png) |
|:------------------------:|
|         Interface        |

### JNose-Core

- É o núcleo da ferramenta, ou seja, a biblioteca principal que contém as regras e algoritmos para a detecção de *test smells*.
- Focado em fornecer a lógica central, sem interface gráfica.
- Pode ser usado como uma dependência em outras ferramentas ou para integrar a análise de *test smells* em projetos personalizados.
- Projetado para ser uma base reutilizável, modular e leve.
- Ideal para desenvolvedores que querem incorporar a análise do JNose em outras aplicações ou realizar customizações avançadas.

---

**Resumindo:**  
O **JNose-Core** é a “engine” de análise, enquanto o **JNose** é a aplicação completa, com interface e integração para facilitar a utilização da análise em projetos Java.

---

Links úteis:

- [Repositório JNose](https://github.com/arieslab/jnose)  
- [Repositório JNose-Core](https://github.com/arieslab/jnose-core)

---

## 📂 Estrutura das pastas necessárias

Para que o projeto funcione corretamente, é necessário ter duas pastas específicas no diretório principal do projeto:

- **`jnose/`**  
  Esta pasta deve conter o código-fonte do projeto **JNose**. É nela que a ferramenta principal é executada para realizar a análise dos *Test Smells*.

- **`jnose-core/`**  
  Esta pasta contém o núcleo da ferramenta, ou seja, a biblioteca **JNose-Core** que inclui as regras e algoritmos para a detecção dos *Test Smells*.  

Ambas as pastas são essenciais:  
- A pasta `jnose` é onde a execução do JNose acontece.  
- A pasta `jnose-core` é uma dependência interna usada pelo JNose para realizar as análises.

Certifique-se de clonar ou copiar esses dois diretórios para o local correto antes de executar o projeto para evitar erros de compilação ou execução.

---

## 🛠️ Explicação das Funções do Script

Este script automatiza o processo de análise de projetos Java utilizando a ferramenta JNose. Abaixo, uma descrição das principais funções:

### `clone_repo(repo_url, local_path)`

- **Objetivo:** Clonar um repositório Git em um diretório local.  
- **Detalhes:**  
  - Remove a pasta local anterior, caso exista, para garantir um clone limpo.  
  - Clona o repositório a partir da URL fornecida para o caminho local especificado.  
- **Uso no script:** Baixa o projeto Java que será analisado.

---

### `compilar_projeto_java(repo_path)`

- **Objetivo:** Detectar e compilar o projeto Java clonado usando Maven ou Gradle.  
- **Detalhes:**  
  - Verifica se o projeto possui arquivo `pom.xml` (Maven) ou `build.gradle`/`build.gradle.kts` (Gradle).  
  - Executa o comando de compilação adequado para cada build tool.  
  - Exibe os logs da compilação para auxiliar na identificação de erros.  
  - Confirma se a compilação gerou os diretórios comuns com as classes compiladas.  
- **Uso no script:** Prepara o projeto para ser analisado pelo JNose.

---

### `rodar_jnose(projeto_java, output_csv)`

- **Objetivo:** Executar o JNose para analisar o projeto Java compilado e gerar um relatório CSV.  
- **Detalhes:**  
  - Chama o Maven para executar a classe principal do JNose (`br.ufba.jnose.JNoseCLI`).  
  - Passa como argumentos o caminho do projeto Java e o caminho do arquivo CSV onde o resultado será salvo.  
  - Limita a memória da JVM para evitar problemas durante a execução.  
- **Uso no script:** Realiza a análise de *Test Smells* e gera os dados para consulta.

---

### `main()`

- Função principal que orquestra o fluxo:  
  1. Clona o repositório do projeto Java.  
  2. Compila o projeto clonado.  
  3. Cria a pasta para salvar o resultado, se necessário.  
  4. Define o nome do arquivo CSV com timestamp para evitar sobrescrever resultados anteriores.  
  5. Executa o JNose para gerar o relatório.  
  6. Exibe o caminho do arquivo CSV gerado.  
  7. Captura e mostra qualquer erro que ocorrer durante o processo.

---

Esse conjunto de funções permite automatizar desde a obtenção do código até a geração do relatório de análise de *Test Smells*, facilitando o uso do JNose em múltiplos projetos.

---

## 📦 Dependências

Para rodar este projeto, você precisa das seguintes dependências instaladas e configuradas no seu ambiente:

- **Python 3.x** — Para executar o script automatizado.  
- **Git** — Para clonar repositórios remotamente.  
- **Java JDK (11 ou superior)** — Necessário para compilar e executar projetos Java.  
- **Apache Maven** — Usado para gerenciar dependências, compilar e executar o JNose e projetos Maven.  
- **Gradle** (opcional) — Caso o projeto Java use Gradle como build tool.  
- **Pacote `shutil`, `os`, `subprocess`, `stat`, `datetime`** — Módulos padrão do Python usados no script.  

---

### 🔭 Observação importante

- Certifique-se que o comando `mvn` e `gradle` estejam disponíveis no PATH do seu sistema.  
- O projeto JNose (pasta `jnose`) e sua dependência `jnose-core` devem estar presentes na mesma pasta do script para a execução correta.

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

## 📚 Documentação e Links úteis

### :octocat: GitHub

- [Site oficial do JNose](https://jnosetest.github.io/)
- [Repositório GitHub do JNose Core](https://github.com/arieslab/jnose-core)
- [Repositório GitHub do JNose](https://github.com/arieslab/jnose)
- [Tutorial em Português do JNose](https://github.com/arieslab/jnose/blob/main/TUTORIAL_pt-br.md)

### ▶️ Vídeos

- [Apresentação do JNose Test por Luana Martins](https://www.youtube.com/watch?v=6qrglBetOSc&ab_channel=LuanaMartins)
- [Demonstração do JNose Test por Tássio Virgínio](https://www.youtube.com/watch?v=BfYtwqQeqHc&ab_channel=T%C3%A1ssioVirg%C3%ADnio)

### 📄 Publicações

**2021** — `On the test smells detection: an empirical study on the JNose Test accuracy`  
*Journal of Software Engineering Research and Development*  
🔗 [Versão SBC](https://journals-sol.sbc.org.br/index.php/jserd/article/view/1893)  
🔗 [Versão online (PDF SBC)](https://journals-sol.sbc.org.br/index.php/jserd/article/view/1893/1798)  
📁 [Versão local (PDF)](https://github.com/joaopauloaramuni/python/tree/main/PROJETOS/Projeto%20JNose%20Test%20Smells%20Analyser/artigo/1893-Article-7403-2-10-20220214.pdf)  
🔗 [DOI](https://doi.org/10.5753/jserd.2021.1893)  

**2020** — `JNose: Java Test Smell Detector`  
*Congresso Brasileiro de Software: Teoria e Prática (CBSoft - 2020) — Trilha de Ferramentas*  
🔗 [http://cbsoft2020.imd.ufrn.br/artigos.php?evento=sbes-ferramentas](http://cbsoft2020.imd.ufrn.br/artigos.php?evento=sbes-ferramentas)  

**2020** — `An Empirical Study of Automatically-Generated Tests from the Perspective of Test Smells`  
*Congresso Brasileiro de Software: Teoria e Prática (CBSoft - 2020) — Trilha de Pesquisa*  
🔗 [http://cbsoft2020.imd.ufrn.br/artigos.php?evento=sbes-pesquisa](http://cbsoft2020.imd.ufrn.br/artigos.php?evento=sbes-pesquisa)  

**2019** — `On the influence of Test Smells on Test Coverage`  
*33º Simpósio Brasileiro de Engenharia de Software (SBES - 2019)*  
Proceedings of the XXXIII Brazilian Symposium on Software Engineering  
🔗 [https://dl.acm.org/doi/10.1145/3350768.3350775](https://dl.acm.org/doi/10.1145/3350768.3350775)  

---

## ⚖️ Licença

Este projeto está licenciado sob a **MIT License**.
