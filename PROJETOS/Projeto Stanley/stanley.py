"""
Raspagem didática - Stanley 1913 Brasil
=======================================
Objetivo: extrair modelo, cor, capacidade, preço, parcelamento, link
e TODAS as opções de cor dos cards de produto da home (ou de qualquer
página de coleção).

Instalação (com a .venv ativada):
    pip install requests beautifulsoup4 lxml playwright
    python -m playwright install chromium

Uso:
    python raspagem_stanley.py --navegador
    python raspagem_stanley.py https://www.stanley1913.com.br/collections/quencher --navegador

    Por padrão raspa a coleção "Últimos lançamentos" INTEIRA: o script
    segue o botão "Carregar mais" (?page=2, ?page=3...) até a última página.

    Sem --navegador o script usa só requests: é mais rápido, mas as
    bolinhas de cor não vêm (são montadas por JavaScript). Nesse caso a
    cor e o modelo são deduzidos comparando os títulos entre produtos.

Saídas:
    produtos_stanley.csv  -> uma linha por produto
    cores_stanley.csv     -> uma linha por combinação produto x cor

Boas práticas para mostrar aos alunos:
  - Consultar /robots.txt antes de raspar
  - Identificar-se com um User-Agent honesto
  - Colocar pausas entre requisições (time.sleep)
  - Não sobrecarregar o servidor nem coletar dados pessoais
"""

import csv
import re
import sys
import time
from urllib.parse import urljoin, urlparse
from pathlib import PurePosixPath

import requests
from bs4 import BeautifulSoup

VERSAO = "v6 (paginação automática)"
BASE = "https://www.stanley1913.com.br"
URL_PADRAO = BASE + "/collections/ultimos-lancamentos"
MAX_PAGINAS = 20  # trava de segurança
HEADERS = {"User-Agent": "Mozilla/5.0 (aula de raspagem de dados - uso educacional)"}


# ---------------------------------------------------------------------------
# 1) Baixar o HTML
# ---------------------------------------------------------------------------
def baixar_html(url: str) -> str:
    resp = requests.get(url, headers=HEADERS, timeout=20)
    resp.raise_for_status()
    return resp.text


class Navegador:
    """Abre o Chrome UMA vez e reaproveita para todas as páginas
    (abrir e fechar o navegador a cada página seria bem mais lento).

    Por que não usar wait_until="networkidle"?
    O site tem dezenas de rastreadores que nunca param de fazer
    requisições, então a rede nunca fica 'ociosa' -> timeout.
    Em vez disso: carregamos o DOM e esperamos o elemento que importa.
    """
    # Domínios de rastreamento/anúncio: bloquear deixa a página MUITO mais rápida
    BLOQUEAR = ("googletagmanager", "google-analytics", "doubleclick", "facebook",
                "tiktok", "clarity.ms", "klaviyo", "yotpo", "yimg", "navdmp",
                "tailtarget", "voxus", "lomadee", "cartstack", "edrone",
                "northbeam", "stackadapt", "signifyd", "smct", "omappapi", "getblue")

    def __enter__(self):
        from playwright.sync_api import sync_playwright
        self._pw = sync_playwright().start()
        self._nav = self._pw.chromium.launch()
        self._pagina = self._nav.new_page(user_agent=HEADERS["User-Agent"])
        self._pagina.route("**/*", self._filtro)
        return self

    def _filtro(self, route):
        if any(d in route.request.url for d in self.BLOQUEAR):
            return route.abort()
        return route.continue_()

    def baixar(self, url: str) -> str:
        self._pagina.goto(url, wait_until="domcontentloaded", timeout=60000)
        try:
            self._pagina.wait_for_selector("color-swatch", state="attached", timeout=30000)
            self._pagina.wait_for_timeout(2000)  # folga para todos os cards terminarem
        except Exception:
            print("  Aviso: as bolinhas de cor não apareceram a tempo.")
        return self._pagina.content()

    def __exit__(self, *erro):
        self._nav.close()
        self._pw.stop()


def baixar_html_navegador(url: str) -> str:
    """Atalho para baixar UMA página só com o navegador."""
    with Navegador() as nav:
        return nav.baixar(url)

# ---------------------------------------------------------------------------
# 2) O problema da COR
# ---------------------------------------------------------------------------
# Na Stanley BR cada cor é um PRODUTO separado (a variante é sempre
# "Default Title"), então a cor não aparece em nenhum campo próprio.
# Ela está "escondida" em dois lugares:
#
#   a) no título:  "Mug Térmica Café To Go Twilight Stanley 1913 | 236ml"
#      -> difícil, porque o nome do modelo tem tamanho variável
#
#   b) na imagem da bolinha (swatch) selecionada:
#      <color-swatch data-selected="true"
#                    data-image=".../files/twilight.png">
#      -> o NOME DO ARQUIVO é a cor! "twilight.png" -> "Twilight"
#
# Usamos (b) como fonte principal e (a) como plano B.

def cor_pelo_swatch(card) -> str | None:
    swatch = card.select_one('color-swatch[data-selected="true"]')
    if not swatch or not swatch.get("data-image"):
        return None
    arquivo = PurePosixPath(urlparse(swatch["data-image"]).path).stem  # "blue-dream-stone"
    return arquivo.replace("-", " ").title()                           # "Blue Dream Stone"


def todas_as_cores(card) -> list[dict]:
    """Lê TODAS as bolinhas do card (só existem com --navegador).
    Cada bolinha vira: {cor, titulo, esgotado, selecionada}"""
    cores = []
    for s in card.select("color-swatch"):
        img = s.get("data-image", "")
        nome_arquivo = PurePosixPath(urlparse(img).path).stem if img else ""
        cores.append({
            "cor": nome_arquivo.replace("-", " ").title() or None,
            "titulo": s.get("data-title"),
            "esgotado": s.get("data-sold-out") == "true",
            "selecionada": s.get("data-selected") == "true",
        })
    return cores


def _palavras(titulo: str) -> list[str]:
    """'Copo Quencher Cream Stanley 1913 | 887ML' -> ['Copo','Quencher','Cream']"""
    t = (titulo or "").split("|")[0]
    return re.sub(r"\bStanley 1913\b", "", t).split()


def modelo_pelos_swatches(card) -> str | None:
    """O começo que se repete em TODOS os títulos das bolinhas é o modelo.
       Mug Térmica Café To Go Twilight
       Mug Térmica Café To Go Toast      ->  'Mug Térmica Café To Go'
    """
    listas = [_palavras(s.get("data-title")) for s in card.select("color-swatch")]
    listas = [l for l in listas if l]
    if len(listas) < 2:
        return None
    k = 0
    while all(len(l) > k for l in listas) and len({l[k] for l in listas}) == 1:
        k += 1
    return " ".join(listas[0][:k]) or None


def cor_pelo_titulo(card) -> str | None:
    """Plano B: compara os títulos de todas as bolinhas do card.
    A parte que é IGUAL em todos é o nome do modelo; o que sobra é a cor."""
    titulos = [s.get("data-title", "") for s in card.select("color-swatch")]
    selecionado = card.select_one('color-swatch[data-selected="true"]')
    if len(titulos) < 2 or not selecionado:
        return None

    def limpar(t):  # tira "Stanley 1913" e "| 887ml"
        t = t.split("|")[0]
        return re.sub(r"\bStanley 1913\b", "", t).split()

    listas = [limpar(t) for t in titulos]
    prefixo = 0
    while all(len(l) > prefixo for l in listas) and len({l[prefixo] for l in listas}) == 1:
        prefixo += 1
    return " ".join(limpar(selecionado["data-title"])[prefixo:]) or None


def cor_por_familia(produtos: list[dict]) -> None:
    """Plano C (funciona SEM JavaScript): compara o título de cada produto
    com os OUTROS produtos da lista. Ex.:
        Garrafa Térmica Flowstate™ Spring Ash
        Garrafa Térmica Flowstate™ Spring Cream
    O começo em comum é o modelo; o resto é a cor.
    Limitação: produto sozinho na página (sem 'irmãos') fica sem cor."""
    def palavras(nome):
        return re.sub(r"\bStanley 1913\b", "", nome or "").split()

    nomes = [palavras(p["nome"]) for p in produtos]
    for i, p in enumerate(produtos):
        if p["cor"] and p["modelo"]:
            continue
        # tem cor mas não tem modelo: se o nome termina com a cor, o resto é o modelo
        if p["cor"] and not p["modelo"]:
            cor = p["cor"].split()
            if [w.lower() for w in nomes[i][-len(cor):]] == [w.lower() for w in cor]:
                p["modelo"] = " ".join(nomes[i][:-len(cor)]) or None
            continue
        melhor = 0
        for j, outro in enumerate(nomes):
            if i == j:
                continue
            k = 0
            while k < min(len(nomes[i]), len(outro)) and nomes[i][k] == outro[k]:
                k += 1
            melhor = max(melhor, k)
        if melhor >= 2 and melhor < len(nomes[i]):   # exige pelo menos 2 palavras de modelo
            p["modelo"] = " ".join(nomes[i][:melhor])
            p["cor"] = " ".join(nomes[i][melhor:])


# ---------------------------------------------------------------------------
# 3) Extrair os dados de cada card
# ---------------------------------------------------------------------------
def texto(el) -> str | None:
    return el.get_text(strip=True) if el else None


def preco_para_float(s: str | None) -> float | None:
    if not s:
        return None
    s = re.sub(r"[^\d,]", "", s).replace(",", ".")  # "R$ 219,00" -> "219.00"
    return float(s) if s else None


def extrair_produtos(html: str, aplicar_familia: bool = True) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")
    produtos, vistos = [], set()

    for card in soup.select("product-card"):
        pid = card.get("data-id")
        if pid in vistos:        # o mesmo produto pode aparecer em 2 carrosséis
            continue
        vistos.add(pid)

        # Os atributos data-* são o "ouro" da raspagem: dados limpos, sem CSS.
        titulo_completo = card.get("data-product-title", "")
        capacidade = titulo_completo.split("|")[-1].strip() if "|" in titulo_completo else None

        cores = todas_as_cores(card)
        link = card.select_one("a.productCard__titleLink")
        parcela = card.select_one(".c-installment__value")
        n_parcelas = card.select_one(".c-installment__count")

        produtos.append({
            "id": pid,
            "sku": card.get("data-product-sku"),
            "nome": texto(card.select_one(".productCard__title")),
            "modelo": modelo_pelos_swatches(card),
            "cor": cor_pelo_swatch(card) or cor_pelo_titulo(card),
            "capacidade": capacidade,
            "preco": float(card["data-product-price"]) if card.get("data-product-price")
                     else preco_para_float(texto(card.select_one(".productCard__price"))),
            "parcelas": texto(n_parcelas),
            "valor_parcela": preco_para_float(texto(parcela)),
            "cores_disponiveis": len(cores),
            "outras_cores": ", ".join(c["cor"] for c in cores if not c["selecionada"] and c["cor"]),
            "cores_esgotadas": ", ".join(c["cor"] for c in cores if c["esgotado"] and c["cor"]) or "0",
            "selo": texto(card.select_one(".c-promoBadge__text")),
            "url": urljoin(BASE, link["href"]) if link else None,
            "_cores": cores,   # lista completa (não vai pro CSV principal)
        })
    if aplicar_familia:
        cor_por_familia(produtos)
    return produtos


# ---------------------------------------------------------------------------
# 3b) Paginação: o botão "Carregar mais"
# ---------------------------------------------------------------------------
# No HTML, o botão é só um link comum:
#   <load-more><a data-load-more href="/collections/ultimos-lancamentos?page=2">
# Então não precisamos "clicar": basta visitar ?page=2, ?page=3... até o
# link sumir (última página).

def proxima_pagina(html: str) -> str | None:
    soup = BeautifulSoup(html, "lxml")
    link = soup.select_one("a[data-load-more]")
    if link and link.get("href"):
        return urljoin(BASE, link["href"])
    grade = soup.select_one("#product-grid[data-next-url]")   # plano B
    if grade and grade["data-next-url"]:
        return urljoin(BASE, grade["data-next-url"])
    return None


def raspar_colecao(url: str, baixar) -> list[dict]:
    """Percorre todas as páginas da coleção.
    'baixar' é a função que transforma URL em HTML (requests ou navegador)."""
    todos, vistos, pagina = [], set(), 1
    while url and pagina <= MAX_PAGINAS:
        print(f"Página {pagina}: {url}")
        html = baixar(url)
        novos = [p for p in extrair_produtos(html, aplicar_familia=False) if p["id"] not in vistos]
        if not novos:                       # nada novo -> acabou
            break
        vistos.update(p["id"] for p in novos)
        todos.extend(novos)
        print(f"  +{len(novos)} produtos (total: {len(todos)})")
        url = proxima_pagina(html)
        pagina += 1
        time.sleep(1.5)                     # educação com o servidor entre páginas
    cor_por_familia(todos)                  # compara títulos usando TODAS as páginas
    return todos


# ---------------------------------------------------------------------------
# 4) Salvar em CSV
# ---------------------------------------------------------------------------
def salvar_csv(produtos: list[dict], arquivo="produtos_stanley.csv"):
    if not produtos:
        print("Nenhum produto encontrado.")
        return
    for p in produtos:                       # garantia: nunca deixar vazio
        if not p.get("cores_esgotadas"):
            p["cores_esgotadas"] = "0"
    campos = [k for k in produtos[0] if not k.startswith("_")]
    with open(arquivo, "w", newline="", encoding="utf-8-sig") as f:  # utf-8-sig abre bem no Excel
        w = csv.DictWriter(f, fieldnames=campos, delimiter=";", extrasaction="ignore")
        w.writeheader()
        w.writerows(produtos)
    print(f"{len(produtos)} produtos salvos em {arquivo}")


def salvar_csv_cores(produtos: list[dict], arquivo="cores_stanley.csv"):
    """Formato 'longo': UMA LINHA POR COR de cada produto.
    Bom para ensinar dados 'tidy' e fazer tabela dinâmica no Excel."""
    linhas = []
    for p in produtos:
        for c in p["_cores"]:
            linhas.append({
                "produto_id": p["id"],
                "produto": p["nome"],
                "capacidade": p["capacidade"],
                "cor": c["cor"],
                "titulo_da_cor": c["titulo"],
                "esgotado": c["esgotado"],
                "e_a_cor_do_card": c["selecionada"],
            })
    if not linhas:
        print("Nenhuma bolinha de cor encontrada (rode com --navegador).")
        return
    with open(arquivo, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=linhas[0].keys(), delimiter=";")
        w.writeheader()
        w.writerows(linhas)
    print(f"{len(linhas)} combinações produto x cor salvas em {arquivo}")


if __name__ == "__main__":
    # python raspagem_stanley.py [url] [--navegador]
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    usar_navegador = "--navegador" in sys.argv
    url = args[0] if args else URL_PADRAO
    print(f"Raspagem Stanley - {VERSAO}")

    if usar_navegador:
        with Navegador() as nav:
            produtos = raspar_colecao(url, nav.baixar)
    else:
        produtos = raspar_colecao(url, baixar_html)

    print()
    for p in produtos:
        print(f"{(p['nome'] or '')[:50]:50} | {p['cor'] or '?':22} | {p['capacidade'] or '':7} | R$ {p['preco']:.2f}")
    sem_cor = sum(1 for p in produtos if not p["cor"])
    if sem_cor and not usar_navegador:
        print(f"\n{sem_cor} produto(s) sem cor. Tente de novo com --navegador")
    salvar_csv(produtos)
    salvar_csv_cores(produtos)