# 🚀 Projeto Stanley Web Scraping

O **Stanley Web Scraping** é uma ferramenta Python didática que faz a **raspagem de dados** das coleções do site da [Stanley 1913 Brasil](https://www.stanley1913.com.br). O script coleta **nome, modelo, cor, capacidade, preço, parcelamento, link e todas as opções de cor** de cada produto. Ele percorre automaticamente todas as páginas da coleção (botão **"Carregar mais"**) e usa um navegador real (**Playwright**) para capturar os dados montados por JavaScript.

### 🎯 Objetivo

O objetivo principal é ensinar, com um caso real, os desafios mais comuns da raspagem de dados:

- **Dados escondidos:** a cor do produto não existe em nenhum campo próprio e precisa ser deduzida do **nome do arquivo da imagem** da bolinha de cor.
- **Conteúdo gerado por JavaScript:** as bolinhas de cor não vêm no HTML baixado pelo `requests`, só aparecem no navegador.
- **Paginação:** a coleção tem **112 produtos**, carregados de **24 em 24**.
- **Qualidade de dados:** o próprio site tem inconsistências de cadastro que aparecem no resultado.

O resultado é exportado para **dois arquivos CSV** de fácil consumo no Excel ou no Pandas.

---

## 🖼️ Site da Stanley

| ![Stanley](https://joaopauloaramuni.github.io/python-imgs/Stanley/imgs/stanley.png) |
|:------------------------:|
|         Stanley          |

---

## 🛠️ Pré-requisitos

- **Python 3.10+** instalado (o código usa a sintaxe `str | None`).
- **Google Chrome** ou o Chromium do Playwright (instalado no passo abaixo).
- Conexão com a internet.

---

## 🐍 Ambiente virtual (recomendado)
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

3. **Instale as dependências:**
```bash
pip install requests beautifulsoup4 lxml playwright
```

4. **Baixe o navegador usado pelo Playwright:**
```bash
python -m playwright install chromium
```

> ⚠️ Use `python -m playwright` (e não só `playwright`). Assim o navegador baixado é o da versão do Playwright instalada na `.venv`. Isso evita conflito com outras instalações, como o `(base)` do Conda.

---

## ⚙️ Execução

### 1. Comando Principal

Execute o script com a opção `--navegador` (recomendado). Por padrão ele raspa a coleção **Últimos Lançamentos**:

```bash
python stanley.py --navegador
```

### 2. Outras coleções

Passe a URL de qualquer coleção como argumento:

```bash
python stanley.py https://www.stanley1913.com.br/collections/quencher --navegador
```

### 3. Modo sem navegador

Sem `--navegador`, o script usa apenas o `requests`. É mais rápido, mas as **bolinhas de cor não vêm** no HTML. Nesse modo, a cor e o modelo são deduzidos comparando os títulos entre produtos (plano C), e as colunas de outras cores ficam vazias.

```bash
python stanley.py
```

### 4. Exemplo de Saída no Terminal

A ferramenta exibe o progresso da paginação e, ao final, lista os produtos com cor, capacidade e preço:

```
(.venv) (base) joaopauloaramuni@MacBook-Pro-de-Joao Projeto Stanley % python stanley.py --navegador
Raspagem Stanley - v6 (paginação automática)
Página 1: https://www.stanley1913.com.br/collections/ultimos-lancamentos
  +24 produtos (total: 24)
Página 2: https://www.stanley1913.com.br/collections/ultimos-lancamentos?page=2
  +24 produtos (total: 48)
Página 3: https://www.stanley1913.com.br/collections/ultimos-lancamentos?page=3
  +24 produtos (total: 72)
Página 4: https://www.stanley1913.com.br/collections/ultimos-lancamentos?page=4
  +24 produtos (total: 96)
Página 5: https://www.stanley1913.com.br/collections/ultimos-lancamentos?page=5
  +16 produtos (total: 112)

Mug Térmica Café To Go Twilight Stanley 1913       | Twilight               | 236ml   | R$ 219.00
Mug Térmica Café To Go Blue Dream Stone            | Blue Dream Stone       | 236ml   | R$ 219.00
Quencher Protour Blue Dream                        | Blue Dream             | 1.18L   | R$ 359.00
Copo Quencher Blue Dream Wildflower                | Blue Dream Wildflower  | 887ML   | R$ 319.00
Quencher Protour Sorbet Wildflower                 | Sorbet Wildflower      | 1.18L   | R$ 359.00
Garrafa Vitalize Tempo Blue Dream                  | Blue Dream             | 710ml   | R$ 349.00
Garrafa Térmica Flowstate™ Spring Blue Dream Stone | Blue Dream Stone       | 591ml   | R$ 329.00
Jug Térmica Fast flow Ash Stanley 1913             | Ash                    | 1.9L    | R$ 439.00
Cooler  Térmico Sage Grey Stanley 1913             | Sage Grey              | 15L     | R$ 1180.00
Mochila Térmica Madeleine Mini Ash Stanley 1913    | Ash                    | 13.2L   | R$ 1499.00
Copo Prismático Alto Black Eclipse Stanley 1913    | Black Eclipse          | 381ml   | R$ 215.00
Camp Mug Rose Quartz Stanley 1913                  | Rose Quartz            | 236ml   | R$ 199.00
Pote Térmico com Garfolher Blue Sky Stanley 1913   | Blue Sky               | 414ml   | R$ 285.00
...
Garrafa Térmica Twist Flip Stanley 1913 Black 2.0  | Black 2.0              | 710ML   | R$ 335.00
Tulipa Térmica Pink Mesa Sunset Gloss Stanley 1913 | Pink Mesa Sunset Gloss | 414ml   | R$ 345.00
Beer Tumbler Happy Hour Pink Mesa Sunset Gloss Sta | Pink Mesa Sunset Gloss | 354ml   | R$ 189.00
112 produtos salvos em produtos_stanley.csv
931 combinações produto x cor salvas em cores_stanley.csv
```

---

## 📁 Arquivos Gerados

Os arquivos usam **ponto e vírgula (`;`)** como delimitador e codificação **UTF-8 com BOM**, para abrir corretamente no Excel.

### `produtos_stanley.csv`: uma linha por produto

| Coluna | Descrição | Exemplo |
| :--- | :--- | :--- |
| `id` | ID interno do produto no Shopify | 14973637427560 |
| `sku` | Código de estoque da Stanley | 08944 |
| `nome` | Título exibido no card | Mug Térmica Café To Go Twilight Stanley 1913 |
| `modelo` | Parte do título que se repete entre as cores | Mug Térmica Café To Go |
| `cor` | Cor do produto (nome do arquivo da bolinha) | Twilight |
| `capacidade` | Tamanho do produto | 236ml |
| `preco` | Preço em reais | 219.0 |
| `parcelas` | Número máximo de parcelas | 12x |
| `valor_parcela` | Valor de cada parcela | 18.25 |
| `cores_disponiveis` | Total de bolinhas de cor do card | 7 |
| `outras_cores` | Demais cores do mesmo modelo | Cream Gloss, Black 2.0, Toast... |
| `cores_esgotadas` | Cores esgotadas (ou `0` se nenhuma) | 0 |
| `selo` | Etiqueta do card | Novidade |
| `url` | Link do produto | https://www.stanley1913.com.br/products/... |

### `cores_stanley.csv`: uma linha por combinação produto × cor

| Coluna | Descrição | Exemplo |
| :--- | :--- | :--- |
| `produto_id` | ID do produto do card | 14973637427560 |
| `produto` | Nome do produto do card | Mug Térmica Café To Go Twilight Stanley 1913 |
| `capacidade` | Tamanho | 236ml |
| `cor` | Cor da bolinha | Toast |
| `titulo_da_cor` | Título do produto daquela cor | Mug Térmica Café To Go Toast Stanley 1913 \| 236ml |
| `esgotado` | Se aquela cor está esgotada | False |
| `e_a_cor_do_card` | `True` se for a cor do próprio produto do card | False |

> 💡 Para obter a lista única de modelo × cor (sem repetições), filtre `e_a_cor_do_card = True`.

---

## 📊 O que cada função faz

Abaixo seguem as assinaturas das funções presentes no script e uma explicação curta do propósito de cada uma:

| Função | Assinatura | Propósito |
| :--- | :--- | :--- |
| **`baixar_html`** | `(url: str) -> str` | Baixa o HTML da página com `requests` (sem JavaScript). |
| **`Navegador`** | `class` (usada com `with`) | Abre o Chrome **uma única vez**, bloqueia rastreadores e espera as bolinhas de cor aparecerem antes de devolver o HTML. |
| **`baixar_html_navegador`** | `(url: str) -> str` | Atalho para baixar uma única página com o navegador. |
| **`cor_pelo_swatch`** | `(card) -> str \| None` | Extrai a cor a partir do **nome do arquivo da imagem** da bolinha selecionada (`twilight.png` vira **Twilight**). |
| **`todas_as_cores`** | `(card) -> list[dict]` | Lê todas as bolinhas do card: cor, título, se está esgotada e se é a cor selecionada. |
| **`modelo_pelos_swatches`** | `(card) -> str \| None` | Descobre o **modelo** pelo começo que se repete em todos os títulos das bolinhas. |
| **`cor_pelo_titulo`** | `(card) -> str \| None` | Plano B: deduz a cor pelo que **sobra** do título depois do nome do modelo. |
| **`cor_por_familia`** | `(produtos: list[dict]) -> None` | Plano C (sem navegador): compara os títulos **entre produtos** para separar modelo e cor. |
| **`preco_para_float`** | `(s: str \| None) -> float \| None` | Converte textos como `R$ 219,00` em número (`219.0`). |
| **`extrair_produtos`** | `(html: str, aplicar_familia: bool = True) -> list[dict]` | Lê todos os cards de produto do HTML e monta o dicionário com os dados de cada um. |
| **`proxima_pagina`** | `(html: str) -> str \| None` | Encontra o link do botão **"Carregar mais"** (`?page=2`, `?page=3`...). |
| **`raspar_colecao`** | `(url: str, baixar) -> list[dict]` | Percorre **todas as páginas** da coleção, remove duplicados e faz pausas entre as requisições. |
| **`salvar_csv`** | `(produtos: list[dict], arquivo="produtos_stanley.csv")` | Exporta uma linha por produto. |
| **`salvar_csv_cores`** | `(produtos: list[dict], arquivo="cores_stanley.csv")` | Exporta uma linha por combinação produto × cor (formato "longo"). |

---

## 🧠 Lições da Raspagem

- 🔍 **O que você vê no "Inspecionar" não é o que o `requests` recebe.** As bolinhas de cor são montadas por JavaScript, por isso é necessário o `--navegador`.
- ⏳ **Evite `networkidle` em sites com muitos rastreadores.** A rede nunca fica ociosa, e o resultado é timeout. O melhor é esperar pelo elemento que interessa (`color-swatch`).
- 🔗 **Antes de simular cliques, inspecione o botão.** O "Carregar mais" é só um link com `?page=N`.
- 🖼️ **Às vezes o dado está onde menos se espera.** A cor estava no nome do arquivo da imagem.
- 🧹 **Dado raspado precisa de conferência.** O próprio site tem inconsistências, como a *Slim Bottle Purple Dust* com a cor selecionada *Ash Gloss*, cores duplicadas no mesmo card e nomes comerciais diferentes do nome do arquivo.

---

## ⚖️ Boas Práticas

- Consultar o [`/robots.txt`](https://www.stanley1913.com.br/robots.txt) antes de raspar.
- Identificar-se com um **User-Agent** honesto.
- Colocar **pausas entre requisições** (`time.sleep`).
- Não sobrecarregar o servidor nem coletar **dados pessoais**.
- Usar os dados apenas para fins **educacionais**.

---

## 📚 Documentação e Links Úteis

- 🛒 **Site da Stanley 1913 Brasil:** [stanley1913.com.br](https://www.stanley1913.com.br)
- 🎭 **Documentação oficial do Playwright para Python:** [playwright.dev/python](https://playwright.dev/python/docs/intro)
- 🍲 **Documentação oficial do Beautiful Soup:** [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- 🐍 **Documentação oficial do módulo `requests`:** [Python Requests](https://docs.python-requests.org/en/latest/)
- 📄 **Documentação oficial do módulo `csv`:** [csv — CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)

---

## 🧾 Licença

Este projeto é disponibilizado sob a licença **MIT**.

---