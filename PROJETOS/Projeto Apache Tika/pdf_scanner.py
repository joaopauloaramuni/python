import re
import os
import sys
import json
import logging
import glob
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Optional

from tika import parser as tika_parser
from tika import tika

# ── Configuração do Tika ───────────────────────────────────────────────────────
tika.TikaClientOnly = True
tika.TikaServerEndpoint = os.getenv("TIKA_ENDPOINT", "http://localhost:9998")

# ── Logging ────────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("pdf_analyzer")


# ── Estrutura de resultado ─────────────────────────────────────────────────────
@dataclass
class AnalysisResult:
    arquivo: str
    tamanho_bytes: int
    tamanho_status: str
    javascript: list[str] = field(default_factory=list)
    embedded_objects: list[str] = field(default_factory=list)
    encoding_suspeito: list[str] = field(default_factory=list)
    urls_suspeitas: list[str] = field(default_factory=list)
    metadados_suspeitos: list[str] = field(default_factory=list)
    score: int = 0
    risco: str = "Baixo"
    erro: Optional[str] = None
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


# ── Padrões de detecção ────────────────────────────────────────────────────────
PADROES_JS = [
    r"/JavaScript",
    r"/JS\b",
    r"\beval\s*\(",
    r"app\.launchURL",
    r"this\.exportDataObject",
    r"util\.printf",          # exploits de format string
    r"media\.newPlayer",      # CVE-2009-4324
    r"collab\.collectEmailInfo",
]

TLDS_SUSPEITOS = [
    ".ru", ".cn", ".tk", ".pw", ".cc", ".xyz",
    ".top", ".gq", ".ml", ".cf", ".ga",
]

ENCURTADORES = [
    "bit.ly", "tinyurl.com", "t.co", "goo.gl",
    "ow.ly", "is.gd", "buff.ly", "rebrand.ly",
]

FERRAMENTAS_MALICIOSAS = [
    "metasploit", "msfvenom", "exploit",
    "cobalt strike", "pypdf2 exploit",
]

FERRAMENTAS_NEUTRAS_SUSPEITAS = [
    "unknown",          # criador desconhecido
    "ilovepdf",         # frequente em phishing
]

PADROES_EMBEDDED = [
    r"/EmbeddedFile",
    r"/Launch",
    r"/SubmitForm",
    r"/ImportData",
    r"/RichMedia",
    r"/3D",             # modelos 3D podem conter shellcode
    r"/Sound",
    r"/Movie",
]

PADROES_ENCODING = [
    r"/ASCIIHexDecode",
    r"/ASCII85Decode",
    r"/LZWDecode",      # raro em PDFs modernos
]


# ── Classe principal ───────────────────────────────────────────────────────────
class PDFAnalyzer:
    """Pipeline de análise de segurança para arquivos PDF."""

    # Pesos para o score de risco
    PESOS = {
        "javascript": 4,
        "embedded_objects": 3,
        "encoding_suspeito": 2,
        "urls_suspeitas": 2,
        "metadados_suspeitos": 2,
        "tamanho_anormal": 1,
    }

    def __init__(self, caminho: str):
        self.caminho = os.path.abspath(caminho)

    # ── Extração ───────────────────────────────────────────────────────────────
    def _extrair(self) -> tuple[str, dict]:
        try:
            parsed = tika_parser.from_file(self.caminho)
            texto = parsed.get("content") or ""
            meta = parsed.get("metadata") or {}
            return texto, meta
        except Exception as exc:
            log.error("Falha ao processar %s: %s", self.caminho, exc)
            raise

    # ── Verificações individuais ───────────────────────────────────────────────
    @staticmethod
    def _verificar_js(texto: str) -> list[str]:
        return [p for p in PADROES_JS if re.search(p, texto, re.IGNORECASE)]

    @staticmethod
    def _verificar_embedded(texto: str) -> list[str]:
        return [p for p in PADROES_EMBEDDED if re.search(p, texto, re.IGNORECASE)]

    @staticmethod
    def _verificar_encoding(texto: str) -> list[str]:
        encontrados = [p for p in PADROES_ENCODING if re.search(p, texto, re.IGNORECASE)]
        # Muitos streams FlateDecode pode indicar ofuscação em camadas
        count_flat = len(re.findall(r"/FlateDecode", texto, re.IGNORECASE))
        if count_flat > 20:
            encontrados.append(f"/FlateDecode ×{count_flat} (possível ofuscação)")
        return encontrados

    @staticmethod
    def _verificar_urls(texto: str) -> list[str]:
        urls = re.findall(r'https?://[^\s<>"\'\\]+', texto)
        suspeitas = []
        for url in urls:
            url_lower = url.lower()
            if any(enc in url_lower for enc in ENCURTADORES):
                suspeitas.append(f"[encurtador] {url}")
            elif any(tld in url_lower for tld in TLDS_SUSPEITOS):
                suspeitas.append(f"[tld-suspeito] {url}")
            elif re.search(r"\d{1,3}(\.\d{1,3}){3}", url):
                suspeitas.append(f"[ip-direto] {url}")
        return suspeitas

    @staticmethod
    def _verificar_metadados(meta: dict) -> list[str]:
        suspeitos = []
        campos = {
            "producer": meta.get("producer", "") or "",
            "creator": meta.get("creator", "") or "",
            "author": meta.get("author", "") or "",
        }
        texto_meta = " ".join(campos.values()).lower()

        for ferr in FERRAMENTAS_MALICIOSAS:
            if ferr in texto_meta:
                suspeitos.append(f"ferramenta maliciosa: {ferr}")

        for ferr in FERRAMENTAS_NEUTRAS_SUSPEITAS:
            if ferr in texto_meta:
                suspeitos.append(f"produtor suspeito: {ferr}")

        # Datas de criação vs modificação muito divergentes podem indicar falsificação
        criado = meta.get("Creation-Date") or meta.get("created") or ""
        modificado = meta.get("Last-Modified") or meta.get("modified") or ""
        if criado and modificado and criado[:4] != modificado[:4]:
            suspeitos.append(f"datas divergentes: criado={criado[:10]} modificado={modificado[:10]}")

        return suspeitos

    @staticmethod
    def _verificar_tamanho(caminho: str) -> tuple[int, str]:
        tamanho = os.path.getsize(caminho)
        if tamanho < 1_024:
            return tamanho, "muito pequeno (<1 KB)"
        if tamanho > 50 * 1_024 * 1_024:
            return tamanho, "muito grande (>50 MB)"
        return tamanho, "normal"

    # ── Score e classificação ──────────────────────────────────────────────────
    def _calcular_score(self, resultado: AnalysisResult) -> int:
        score = 0
        score += len(resultado.javascript)       * self.PESOS["javascript"]
        score += len(resultado.embedded_objects) * self.PESOS["embedded_objects"]
        score += len(resultado.encoding_suspeito)* self.PESOS["encoding_suspeito"]
        score += len(resultado.urls_suspeitas)   * self.PESOS["urls_suspeitas"]
        score += len(resultado.metadados_suspeitos) * self.PESOS["metadados_suspeitos"]
        if resultado.tamanho_status != "normal":
            score += self.PESOS["tamanho_anormal"]
        return score

    @staticmethod
    def _classificar(score: int) -> str:
        if score == 0:
            return "Baixo"
        if score <= 5:
            return "Médio"
        if score <= 12:
            return "Alto"
        return "Crítico"

    # ── Pipeline principal ─────────────────────────────────────────────────────
    def analisar(self) -> AnalysisResult:
        log.info("Analisando: %s", self.caminho)
        tamanho, tamanho_status = self._verificar_tamanho(self.caminho)

        resultado = AnalysisResult(
            arquivo=self.caminho,
            tamanho_bytes=tamanho,
            tamanho_status=tamanho_status,
        )

        try:
            texto, meta = self._extrair()
        except Exception as exc:
            resultado.erro = str(exc)
            resultado.risco = "Indeterminado"
            return resultado

        resultado.javascript        = self._verificar_js(texto)
        resultado.embedded_objects  = self._verificar_embedded(texto)
        resultado.encoding_suspeito = self._verificar_encoding(texto)
        resultado.urls_suspeitas    = self._verificar_urls(texto)
        resultado.metadados_suspeitos = self._verificar_metadados(meta)

        resultado.score = self._calcular_score(resultado)
        resultado.risco = self._classificar(resultado.score)

        return resultado


# ── Formatação do relatório ────────────────────────────────────────────────────
CORES = {
    "Baixo":         "\033[92m",   # verde
    "Médio":         "\033[93m",   # amarelo
    "Alto":          "\033[91m",   # vermelho
    "Crítico":       "\033[95m",   # magenta
    "Indeterminado": "\033[90m",   # cinza
    "reset":         "\033[0m",
}


def _cor(nivel: str, texto: str) -> str:
    """Aplica cor ANSI se o terminal suportar."""
    if not sys.stdout.isatty():
        return texto
    return f"{CORES.get(nivel, '')}{texto}{CORES['reset']}"


def imprimir_relatorio(r: AnalysisResult) -> None:
    sep = "─" * 60
    print(f"\n{sep}")
    print(f"  Arquivo : {os.path.basename(r.arquivo)}")
    print(f"  Tamanho : {r.tamanho_bytes:,} bytes ({r.tamanho_status})")
    if r.erro:
        print(f"  Erro    : {r.erro}")
    print(sep)

    def _linha(label: str, items: list) -> None:
        if items:
            print(f"  {label}:")
            for it in items:
                print(f"    • {it}")
        else:
            print(f"  {label}: nenhum")

    _linha("JavaScript suspeito",   r.javascript)
    _linha("Objetos embutidos",     r.embedded_objects)
    _linha("Encoding suspeito",     r.encoding_suspeito)
    _linha("URLs suspeitas",        r.urls_suspeitas)
    _linha("Metadados suspeitos",   r.metadados_suspeitos)

    print(sep)
    print(f"  Score   : {r.score}")
    print(f"  Risco   : {_cor(r.risco, r.risco)}")
    print(sep)


def exportar_json(resultados: list[AnalysisResult], saida: str = "relatorio.json") -> None:
    dados = [asdict(r) for r in resultados]
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    log.info("Relatório exportado: %s", saida)


# ── Entrada ────────────────────────────────────────────────────────────────────
def resolver_caminhos(args: list[str]) -> list[str]:
    """Expande globs e valida existência dos arquivos."""
    caminhos = []
    for arg in args:
        expandido = glob.glob(arg)
        if expandido:
            caminhos.extend(expandido)
        elif os.path.exists(arg):
            caminhos.append(arg)
        else:
            log.warning("Arquivo não encontrado: %s", arg)
    return [c for c in caminhos if c.lower().endswith(".pdf")]


def main() -> None:
    if len(sys.argv) > 1:
        caminhos = resolver_caminhos(sys.argv[1:])
    else:
        entrada = input("Digite o caminho do PDF (ou glob, ex: docs/*.pdf): ").strip()
        caminhos = resolver_caminhos([entrada])

    if not caminhos:
        log.error("Nenhum PDF válido encontrado.")
        sys.exit(1)

    resultados = []
    for caminho in caminhos:
        analisador = PDFAnalyzer(caminho)
        resultado = analisador.analisar()
        imprimir_relatorio(resultado)
        resultados.append(resultado)

    if len(resultados) > 1:
        criticos = [r for r in resultados if r.risco in ("Alto", "Crítico")]
        print(f"\nResumo: {len(resultados)} arquivo(s) analisado(s), "
              f"{len(criticos)} com risco alto/crítico.")

    exportar = input("\nExportar relatório JSON? [s/N] ").strip().lower()
    if exportar == "s":
        nome = input("Nome do arquivo [relatorio.json]: ").strip() or "relatorio.json"
        exportar_json(resultados, nome)


if __name__ == "__main__":
    main()