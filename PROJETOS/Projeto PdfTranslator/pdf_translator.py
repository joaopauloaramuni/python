import fitz  # PyMuPDF
import time
import re
from deep_translator import GoogleTranslator


# ─────────────────────────────────────────────
# 1. EXTRAÇÃO
# ─────────────────────────────────────────────

def ler_pdf(caminho_pdf: str) -> list[dict]:
    doc = fitz.open(caminho_pdf)
    paginas = []

    for num, pagina in enumerate(doc, start=1):
        raw = pagina.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)
        linhas_por_bloco = []

        for block in raw.get("blocks", []):
            if block.get("type") != 0:
                continue

            spans_do_bloco = [
                s["text"].strip()
                for line in block.get("lines", [])
                for s in line.get("spans", [])
                if s.get("text", "").strip()
            ]

            if spans_do_bloco:
                # Cada bloco vira um parágrafo separado
                linhas_por_bloco.append(" ".join(spans_do_bloco))

        texto_pagina = "\n\n".join(linhas_por_bloco)
        paginas.append({"pagina": num, "texto": texto_pagina})

    doc.close()
    return paginas


# ─────────────────────────────────────────────
# 2. LIMPEZA
# ─────────────────────────────────────────────

def limpar_texto(texto: str) -> str:
    # 1. Une palavras hifenizadas no fim da linha
    texto = re.sub(r"-\n(\w)", r"\1", texto)

    # 2. Corrige bullet quebrado
    texto = re.sub(r"•\s*\n\s*", "• ", texto)

    # 3. Une linhas do mesmo parágrafo
    texto = re.sub(
        r"(?<=[a-záéíóúãõàâêôçA-Z,;:])\n(?=[a-záéíóúãõàâêôç])",
        " ",
        texto
    )

    # 4. Normaliza múltiplas linhas em branco
    texto = re.sub(r"\n{3,}", "\n\n", texto)

    # 5. Remove espaços extras
    texto = re.sub(r"[ \t]{2,}", " ", texto)

    return texto.strip()


# ─────────────────────────────────────────────
# 3. DIVISÃO EM BLOCOS PARA A API
# ─────────────────────────────────────────────

def dividir_em_blocos(texto: str, max_chars: int = 4500) -> list[str]:
    """
    Divide o texto em blocos respeitando parágrafos primeiro,
    depois frases. Evita cortar no meio de uma palavra.

    max_chars=4500 deixa margem segura abaixo do limite de 5000
    da GoogleTranslator gratuita.
    """
    paragrafos = texto.split("\n\n")
    blocos: list[str] = []
    buffer = ""

    for paragrafo in paragrafos:
        # Se o parágrafo sozinho já passa do limite, divide por frases
        if len(paragrafo) > max_chars:
            frases = re.split(r"(?<=[.!?])\s+", paragrafo)
            for frase in frases:
                if len(buffer) + len(frase) + 2 <= max_chars:
                    buffer += ("" if not buffer else " ") + frase
                else:
                    if buffer:
                        blocos.append(buffer.strip())
                    buffer = frase
        else:
            if len(buffer) + len(paragrafo) + 2 <= max_chars:
                buffer += ("" if not buffer else "\n\n") + paragrafo
            else:
                if buffer:
                    blocos.append(buffer.strip())
                buffer = paragrafo

    if buffer:
        blocos.append(buffer.strip())

    return blocos


# ─────────────────────────────────────────────
# 4. TRADUÇÃO
# ─────────────────────────────────────────────

def traduzir_blocos(
    blocos: list[str],
    origem: str = "en",
    destino: str = "pt",
    pausa: float = 1.0,
    tentativas: int = 3,
) -> list[str]:
    """
    Traduz cada bloco com:
      - pausa entre chamadas (evita bloqueio da API gratuita)
      - retry automático em caso de falha temporária
    """
    tradutor = GoogleTranslator(source=origem, target=destino)
    traducoes: list[str] = []
    total = len(blocos)

    for i, bloco in enumerate(blocos, start=1):
        print(f"  Traduzindo bloco {i}/{total} ({len(bloco)} chars)...")

        for tentativa in range(1, tentativas + 1):
            try:
                traducao = tradutor.translate(bloco)
                traducoes.append(traducao or bloco)  # fallback: mantém original
                break
            except Exception as e:
                print(f"    ⚠ Tentativa {tentativa}/{tentativas} falhou: {e}")
                if tentativa < tentativas:
                    time.sleep(pausa * tentativa * 2)  # backoff crescente
                else:
                    print(f"    ✗ Bloco {i} não traduzido, mantendo original.")
                    traducoes.append(bloco)

        time.sleep(pausa)  # pausa padrão entre blocos

    return traducoes


# ─────────────────────────────────────────────
# 5. SALVAMENTO
# ─────────────────────────────────────────────

def salvar_resultado(
    paginas_traduzidas: list[dict],
    caminho_saida: str,
) -> None:
    """
    Salva o texto traduzido em .txt mantendo separadores de página,
    o que facilita conferir a tradução lado a lado com o PDF original.
    """
    with open(caminho_saida, "w", encoding="utf-8") as f:
        for item in paginas_traduzidas:
            f.write(f"\n{'═' * 60}\n")
            f.write(f"  PÁGINA {item['pagina']}\n")
            f.write(f"{'═' * 60}\n\n")
            f.write(item["texto_traduzido"])
            f.write("\n")


# ─────────────────────────────────────────────
# 6. MAIN
# ─────────────────────────────────────────────

def main():
    caminho_pdf = "artigo.pdf"
    caminho_saida = "artigo_traduzido.txt"

    # ── Extração ──────────────────────────────
    print("📄 Lendo PDF...")
    paginas = ler_pdf(caminho_pdf)
    print(f"   {len(paginas)} página(s) encontrada(s).")

    # ── Tradução página a página ──────────────
    resultado: list[dict] = []

    for pg in paginas:
        print(f"\n── Página {pg['pagina']} ──────────────────────────────")

        texto_limpo = limpar_texto(pg["texto"])

        if not texto_limpo:
            print("   (página sem texto — possivelmente imagem, pulando)")
            resultado.append({**pg, "texto_traduzido": "[imagem / sem texto]"})
            continue

        blocos = dividir_em_blocos(texto_limpo)
        print(f"   {len(blocos)} bloco(s) para traduzir.")

        traducoes = traduzir_blocos(blocos)
        texto_traduzido = "\n\n".join(traducoes)

        resultado.append({**pg, "texto_traduzido": texto_traduzido})

    # ── Salvamento ────────────────────────────
    print("\n💾 Salvando resultado...")
    salvar_resultado(resultado, caminho_saida)

    print(f"\n✅ Concluído! Arquivo salvo em: {caminho_saida}")


if __name__ == "__main__":
    main()

# ─────────────────────────────────────────────
# Instalação das dependências:
#   pip install pymupdf deep-translator
# ─────────────────────────────────────────────
