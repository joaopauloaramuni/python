# 🧪 Projeto PMD Code Analyser

Este projeto realiza **análise estática de código Java** usando a ferramenta **PMD**, clonando repositórios GitHub, executando a análise e exportando o relatório em **PDF** 📄.

---

## 🔍 O que é o PMD?

**PMD** é um analisador estático de código **multilíngue e extensível**. Ele detecta falhas comuns de programação como:

- Variáveis não utilizadas
- Blocos `catch` vazios
- Criação desnecessária de objetos
- Problemas de estilo e complexidade

O PMD trabalha principalmente com **Java e Apex**, mas também oferece suporte para outras 16 linguagens. Ele inclui mais de **400 regras prontas**, e também permite a criação de **regras personalizadas** com Java ou expressões XPath.

Além disso, o PMD oferece o **CPD (Copy-Paste Detector)**, que identifica trechos duplicados em linguagens como Java, Python, PHP, C, C++, JavaScript, Ruby, entre outras.

🔗 Mais detalhes: [Documentação do PMD](https://docs.pmd-code.org/latest/)

---

## ⚖️ PMD vs SonarQube vs Qodana

| Ferramenta    | Tipo                | Interface        | Personalização | Uso comum                                 | Requer compilação (.class)? |
|---------------|---------------------|------------------|----------------|-------------------------------------------|------------------------------|
| **PMD**       | CLI / Analisador    | Terminal         | Alta (XPath)   | Análise rápida, pipelines, IDE            | ❌ Não                      |
| **SonarQube** | Plataforma Web      | Web Dashboard    | Alta           | Monitoramento contínuo, dashboards        | ✅ Sim                      |
| **Qodana**    | JetBrains + Docker  | Web + IDE        | Média          | Integração com IDEs JetBrains             | ✅ Sim                      |

**Resumo:**
- **PMD** é ótimo para scripts e análise local, sem necessidade de compilação.
- **SonarQube** é mais robusto e ideal para times que desejam rastrear evolução do código, mas requer `.class`.
- **Qodana** é voltado a usuários JetBrains, com foco em integração, e também precisa do projeto compilado.

---

## 🛠️ Criando conjuntos de regras (Rulesets) no PMD

Um **ruleset** é um arquivo de configuração que descreve um conjunto de regras a serem executadas durante a análise do PMD. O PMD já inclui conjuntos prontos para facilitar análises rápidas, mas é recomendado criar seus próprios conjuntos para maior personalização.

### O que é um conjunto de regras?

- Define quais regras o PMD irá rodar.
- Pode ser personalizado para atender necessidades específicas do projeto.
- É configurado em formato XML (mas essa configuração geralmente fica externa ao código).

### Como referenciar regras integradas?

Para usar regras já existentes no PMD, basta referenciá-las pela categoria e pelo nome da regra, por exemplo:

`category/java/errorprone.xml/EmptyCatchBlock`

Aqui:
- `category/java/errorprone.xml` é a categoria da regra para Java, na área “errorprone” (propenso a erros).
- `EmptyCatchBlock` é o nome da regra específica que detecta blocos catch vazios.

### Categorias padrão do PMD

Desde a versão 6.0.0, as regras internas do PMD estão organizadas em oito categorias principais, consistentes entre linguagens:

- **Melhores práticas**: Regras que incentivam boas práticas aceitas pela comunidade.
- **Estilo de código**: Regras que impõem um padrão de estilo de escrita do código.
- **Design**: Regras que ajudam a detectar problemas arquiteturais e de design.
- **Documentação**: Focadas em manter a documentação do código adequada.
- **Propenso a erros**: Detectam construções confusas ou que podem gerar erros de execução.
- **Multithreading**: Identificam problemas relacionados a concorrência e múltiplas threads.
- **Desempenho**: Alertam para trechos de código com potencial impacto negativo na performance.
- **Segurança**: Regras que detectam potenciais vulnerabilidades de segurança.

---

### 🔗 Onde descobrir e aprender mais sobre rulesets e regras do PMD?

- Guia oficial para criação de rulesets:  
  [https://pmd.github.io/pmd/pmd_userdocs_making_rulesets.html](https://pmd.github.io/pmd/pmd_userdocs_making_rulesets.html)

- Página oficial com referências às regras existentes:  
  [https://pmd.github.io/pmd/tag_rule_references.html](https://pmd.github.io/pmd/tag_rule_references.html)

---

## 🔧 Como funciona o script?

1. 🧬 **Clona** o repositório Java do GitHub
2. 🧪 **Executa** o PMD na pasta `src` do projeto
3. 📄 **Gera um relatório** com os resultados
4. 🖨️ **Exporta o relatório para PDF**
5. 🧹 **Remove** o repositório clonado

---

## 🧠 Explicação das funções

- `run_pmd`: Executa a ferramenta PMD na pasta `src` do repositório clonado, captura o relatório e exporta para PDF.
- `cleanup_repo`: Remove a pasta clonada após a análise, mantendo o ambiente limpo.
- `export_report_to_pdf`: Converte o texto do relatório gerado pelo PMD para um arquivo PDF usando a biblioteca `fpdf`.

---

## 📦 Dependências

- `fpdf`
- Python 3.9+
- PMD versão **7.14.0**

---

## ⬇️ Baixando o PMD

Você precisa baixar o PMD manualmente:

🔗 [Download PMD 7.14.0](https://github.com/pmd/pmd/releases/download/pmd_releases%2F7.14.0/pmd-dist-7.14.0-bin.zip)

Extraia e coloque o caminho do executável no script (`PMD_CMD`).

---

## ⚙️ Ambiente virtual

1. **Crie o ambiente virtual:**
```bash
python -m venv .venv
```

2. **Ative o ambiente virtual:**

- **Windows:**
```bash
.venv\Scripts\activate
```

- **Linux/macOS:**
```bash
source .venv/bin/activate
```

3. **Instale a dependência:**
```bash
pip install fpdf
```

---

## 💻 Resultado no terminal

- **Repositório analisado:** `arieslab/jnose`
- **URL**: `https://github.com/arieslab/jnose`

<details>
  <summary>Clique para exibir a saída do terminal</summary>

```
(.venv) (base) joaopauloaramuni@MacBook-Pro-de-Joao Projeto PMD Code Analyser % python3 pmd_analyser.py
******************************************************************************************************************************************************
🚀 Iniciando análise estática com PMD...
******************************************************************************************************************************************************
******************************************************************************************************************************************************
📥 Clonando repositório https://github.com/arieslab/jnose.git...
Cloning into 'jnose'...
remote: Enumerating objects: 4808, done.
remote: Counting objects: 100% (1133/1133), done.
remote: Compressing objects: 100% (346/346), done.
remote: Total 4808 (delta 529), reused 1084 (delta 488), pack-reused 3675 (from 1)
Receiving objects: 100% (4808/4808), 2.45 MiB | 7.64 MiB/s, done.
Resolving deltas: 100% (2199/2199), done.
******************************************************************************************************************************************************
******************************************************************************************************************************************************
🔍 Executando análise PMD...
== 📄 Relatório PMD ==

jnose/src/main/java/br/ufba/jnose/WicketApplication.java:54:    SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/WicketApplication.java:57:    SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/WicketApplication.java:62:    SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/WicketApplication.java:63:    SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/WicketApplication.java:64:    SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/WicketApplication.java:65:    SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/WicketApplication.java:66:    SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/WicketApplication.java:67:    SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/WicketApplication.java:68:    SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/WicketApplication.java:69:    SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/WicketApplication.java:70:    SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/WicketApplication.java:74:    SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/base/CSVCore.java:64: AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/CSVCore.java:91: AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/CoverageCore.java:17:    AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:48: AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:55: UnusedAssignment:       The initializer for variable 'owner_' is never used (overwritten on line 64)
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:57: AvoidReassigningParameters:     Avoid reassigning parameters such as 'path_'
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:71: UnusedAssignment:       The initializer for variable 'repoName' is never used (overwritten on lines 73, 79 and 81)
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:78: AvoidReassigningParameters:     Avoid reassigning parameters such as 'repoURL'
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:91: UnusedLocalVariable:    Avoid unused local variables such as 'git'.
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:107:        LooseCoupling:  Avoid using implementation types like 'ArrayList'; use the interface instead
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:109:        LooseCoupling:  Avoid using implementation types like 'ArrayList'; use the interface instead
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:115:        UnusedLocalVariable:    Avoid unused local variables such as 'authorTimeZone'.
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:125:        AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:131:        LooseCoupling:  Avoid using implementation types like 'ArrayList'; use the interface instead
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:133:        LooseCoupling:  Avoid using implementation types like 'ArrayList'; use the interface instead
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:140:        SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:155:        UnusedLocalVariable:    Avoid unused local variables such as 'authorTimeZone'.
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:156:        SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:169:        AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:180:        AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:190:        AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:201:        AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:211:        AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:221:        UnusedAssignment:       The initializer for variable 'git' is never used (overwritten on line 226)
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:240:        SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:249:        AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:257:        UnusedAssignment:       The initializer for variable 'git' is never used (overwritten on line 259)
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:260:        UnusedLocalVariable:    Avoid unused local variables such as 'lista'.
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:265:        AvoidReassigningParameters:     Avoid reassigning parameters such as 'filePath'
jnose/src/main/java/br/ufba/jnose/base/GitCore.java:269:        AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/JNose.java:111:  UnusedAssignment:       The initializer for variable 'columnValues' is never used (overwritten on line 112)
jnose/src/main/java/br/ufba/jnose/base/JNose.java:165:  SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/base/JNose.java:178:  UnusedAssignment:       The initializer for variable 'hash' is never used (overwritten on line 182)
jnose/src/main/java/br/ufba/jnose/base/JNose.java:186:  AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/JNose.java:196:  AvoidReassigningParameters:     Avoid reassigning parameters such as 'start'
jnose/src/main/java/br/ufba/jnose/base/JNose.java:197:  AvoidReassigningParameters:     Avoid reassigning parameters such as 'end'
jnose/src/main/java/br/ufba/jnose/base/JNose.java:206:  AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/JNose.java:211:  UseVarargs:     Consider using varargs for methods or constructors which take an array the last parameter.
jnose/src/main/java/br/ufba/jnose/base/JNose.java:223:  AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/JNose.java:262:  AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/JNose.java:312:  SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/base/JNose.java:335:  AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/JNose.java:349:  SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/base/JNose.java:354:  UnusedLocalVariable:    Avoid unused local variables such as 'valorSoma'.
jnose/src/main/java/br/ufba/jnose/base/JNose.java:356:  UnusedAssignment:       The value assigned to variable 'valorSoma' is never used
jnose/src/main/java/br/ufba/jnose/base/JNose.java:358:  UnusedAssignment:       The value assigned to variable 'valorSoma' is never used
jnose/src/main/java/br/ufba/jnose/base/JNose.java:370:  AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/JNose.java:389:  MissingOverride:        The method 'compare(Commit, Commit)' is missing an @Override annotation.
jnose/src/main/java/br/ufba/jnose/base/JNose.java:417:  UnusedLocalVariable:    Avoid unused local variables such as 'total'.
jnose/src/main/java/br/ufba/jnose/base/JNose.java:419:  UnusedAssignment:       The initializer for variable 'listTestClass' is never used (overwritten on line 425)
jnose/src/main/java/br/ufba/jnose/base/JNose.java:427:  UseCollectionIsEmpty:   Substitute calls to size() == 0 (or size() != 0, size() > 0, size() < 1) with calls to isEmpty()
jnose/src/main/java/br/ufba/jnose/base/JNose.java:494:  AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/Util.java:20:    UnusedLocalVariable:    Avoid unused local variables such as 'i'.
jnose/src/main/java/br/ufba/jnose/base/Util.java:38:    UnusedLocalVariable:    Avoid unused local variables such as 'r'.
jnose/src/main/java/br/ufba/jnose/base/Util.java:38:    UnusedAssignment:       The initializer for variable 'r' is never used (overwritten on line 47)
jnose/src/main/java/br/ufba/jnose/base/Util.java:44:    SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/base/Util.java:47:    UnusedAssignment:       The value assigned to variable 'r' is never used
jnose/src/main/java/br/ufba/jnose/base/Util.java:49:    AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/Util.java:92:    AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/Util.java:102:   UnusedAssignment:       The initializer for variable 'digest' is never used (overwritten on line 104)
jnose/src/main/java/br/ufba/jnose/base/Util.java:107:   AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/base/Util.java:115:   ForLoopCanBeForeach:    This for loop can be replaced by a foreach loop
jnose/src/main/java/br/ufba/jnose/base/cobertura/ReportGenerator.java:73:       AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/business/ProjetoBusiness.java:15:     LiteralsFirstInComparisons:     Position literals first in String comparisons
jnose/src/main/java/br/ufba/jnose/pages/AnalyzePage.java:59:    UnusedLocalVariable:    Avoid unused local variables such as 'clientAddress'.
jnose/src/main/java/br/ufba/jnose/pages/AnalyzePage.java:99:    AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/pages/AnalyzePage.java:106:   AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/pages/AnalyzePage.java:114:   AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/pages/AnalyzePage.java:142:   GuardLogStatement:      Logger calls should be surrounded by log level guards.
jnose/src/main/java/br/ufba/jnose/pages/AnalyzePage.java:145:   GuardLogStatement:      Logger calls should be surrounded by log level guards.
jnose/src/main/java/br/ufba/jnose/pages/ByClassTestPage.java:39:        UnusedPrivateField:     Avoid unused private fields such as 'pastaPath'.
jnose/src/main/java/br/ufba/jnose/pages/ByClassTestPage.java:48:        AvoidStringBufferField: StringBuffers can grow quite a lot, and so may become a source of memory leak (if the owning class has a long life time).
jnose/src/main/java/br/ufba/jnose/pages/ByClassTestPage.java:198:       UseCollectionIsEmpty:   Substitute calls to size() == 0 (or size() != 0, size() > 0, size() < 1) with calls to isEmpty()
jnose/src/main/java/br/ufba/jnose/pages/ByTestSmellsPage.java:44:       UnusedPrivateField:     Avoid unused private fields such as 'indicator'.
jnose/src/main/java/br/ufba/jnose/pages/ByTestSmellsPage.java:47:       UnusedPrivateField:     Avoid unused private fields such as 'totalProgressBar'.
jnose/src/main/java/br/ufba/jnose/pages/ByTestSmellsPage.java:52:       AvoidStringBufferField: StringBuffers can grow quite a lot, and so may become a source of memory leak (if the owning class has a long life time).
jnose/src/main/java/br/ufba/jnose/pages/ByTestSmellsPage.java:52:       UnusedPrivateField:     Avoid unused private fields such as 'logRetorno'.
jnose/src/main/java/br/ufba/jnose/pages/ByTestSmellsPage.java:157:      UseCollectionIsEmpty:   Substitute calls to size() == 0 (or size() != 0, size() > 0, size() < 1) with calls to isEmpty()
jnose/src/main/java/br/ufba/jnose/pages/CodePage.java:44:       AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/pages/EvolutionPage.java:35:  AvoidStringBufferField: StringBuffers can grow quite a lot, and so may become a source of memory leak (if the owning class has a long life time).
jnose/src/main/java/br/ufba/jnose/pages/EvolutionPage.java:220: UnusedLocalVariable:    Avoid unused local variables such as 'todasLinhas2'.
jnose/src/main/java/br/ufba/jnose/pages/EvolutionPage.java:234: UnusedLocalVariable:    Avoid unused local variables such as 'todasLinhas5'.
jnose/src/main/java/br/ufba/jnose/pages/EvolutionPage.java:248: SystemPrintln:  Usage of System.out/err
jnose/src/main/java/br/ufba/jnose/pages/ProjetosPage.java:72:   LooseCoupling:  Avoid using implementation types like 'ArrayList'; use the interface instead
jnose/src/main/java/br/ufba/jnose/pages/ProjetosPage.java:103:  LooseCoupling:  Avoid using implementation types like 'ArrayList'; use the interface instead
jnose/src/main/java/br/ufba/jnose/pages/ProjetosPage.java:111:  LooseCoupling:  Avoid using implementation types like 'ArrayList'; use the interface instead
jnose/src/main/java/br/ufba/jnose/pages/ProjetosPage.java:127:  AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/pages/ResultPage.java:26:     AvoidReassigningParameters:     Avoid reassigning parameters such as 'todasLinhas'
jnose/src/main/java/br/ufba/jnose/pages/SourcePage.java:26:     UnusedLocalVariable:    Avoid unused local variables such as 'fileSource'.
jnose/src/main/java/br/ufba/jnose/pages/SourcePage.java:39:     AvoidPrintStackTrace:   Avoid printStackTrace(); use a logger call instead.
jnose/src/main/java/br/ufba/jnose/pages/base/BasePage.java:35:  LiteralsFirstInComparisons:     Position literals first in String comparisons
jnose/src/main/java/br/ufba/jnose/pages/base/BasePage.java:45:  LiteralsFirstInComparisons:     Position literals first in String comparisons
jnose/src/main/java/br/ufba/jnose/pages/base/BasePage.java:55:  LiteralsFirstInComparisons:     Position literals first in String comparisons
jnose/src/main/java/br/ufba/jnose/pages/base/BasePage.java:65:  LiteralsFirstInComparisons:     Position literals first in String comparisons
jnose/src/main/java/br/ufba/jnose/pages/base/BasePage.java:75:  LiteralsFirstInComparisons:     Position literals first in String comparisons
jnose/src/main/java/br/ufba/jnose/pages/base/BasePage.java:85:  LiteralsFirstInComparisons:     Position literals first in String comparisons
jnose/src/main/java/br/ufba/jnose/pages/base/BasePage.java:95:  LiteralsFirstInComparisons:     Position literals first in String comparisons

📄 Exportando relatório para PDF...

📑 Relatório exportado para PDF: pmd_report.pdf

== 🚨 Erros PMD (stderr) ==

[WARN] Progressbar rendering conflicts with reporting to STDOUT. No progressbar will be shown. Try running with argument -r <file> to output the report to a file instead.
[WARN] This analysis could be faster, please consider using Incremental Analysis: https://docs.pmd-code.org/pmd-doc-7.14.0/pmd_userdocs_incremental_analysis.html

******************************************************************************************************************************************************
******************************************************************************************************************************************************
🧹 Limpando pasta 'jnose' após análise...
******************************************************************************************************************************************************
******************************************************************************************************************************************************
✅ Análise finalizada com sucesso!
******************************************************************************************************************************************************
```
</details>

---

## 📚 Documentação e links úteis

### 📘 PMD

- 🌐 [Site oficial do PMD](https://pmd.github.io/)
- 📖 [Documentação principal do PMD](https://docs.pmd-code.org/latest/)
- 🛠️ [Guia de uso via linha de comando](https://docs.pmd-code.org/latest/pmd_userdocs_installation.html#running-pmd-via-command-line)
- 📚 [Guia oficial para criação de rulesets no PMD](https://pmd.github.io/pmd/pmd_userdocs_making_rulesets.html)
- 📖 [Referências oficiais das regras disponíveis no PMD](https://pmd.github.io/pmd/tag_rule_references.html)
- 📦 [Download do PMD 7.14.0 (binário)](https://github.com/pmd/pmd/releases/download/pmd_releases%2F7.14.0/pmd-dist-7.14.0-bin.zip)

### 🧾 FPDF

- 📦 [Pacote FPDF no PyPI (pip install fpdf)](https://pypi.org/project/fpdf/)
- 📚 [Site oficial da biblioteca FPDF](https://www.fpdf.org/)

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.
