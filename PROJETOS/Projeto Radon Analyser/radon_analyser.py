import os
import shutil
import subprocess
from radon.complexity import cc_visit, cc_rank
from radon.raw import analyze as raw_analyze
from radon.metrics import h_visit, mi_visit, mi_rank


"""
Clona um repositório Git no caminho especificado.
"""
def clonar_repositorio(repo_url, local_path):
    print(f"[INFO] Clonando repositório: {repo_url}")
    subprocess.run(["git", "clone", repo_url, local_path], check=True)


"""
Busca todos os arquivos Python (.py) recursivamente a partir do caminho dado.
Retorna uma lista com os caminhos completos dos arquivos encontrados.
"""
def encontrar_arquivos_py(caminho):
    arquivos = []
    for raiz, _, arquivos_nome in os.walk(caminho):
        for nome in arquivos_nome:
            if nome.endswith(".py"):
                caminho_arquivo = os.path.join(raiz, nome)
                arquivos.append(caminho_arquivo)
                print(f"  [✓] Encontrado: {caminho_arquivo}")
    return arquivos


"""
Lê o conteúdo de um arquivo Python e executa as seguintes análises:
- Complexidade ciclomática
- Métricas brutas (LOC, comentários, etc.)
- Métricas Halstead
- Índice de Manutenibilidade (MI)
Retorna os resultados dessas análises.
"""
def analisar_arquivo(arquivo):
    with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
        codigo = f.read()
    try:
        blocos = cc_visit(codigo)
        raw = raw_analyze(codigo)
        halstead = h_visit(codigo)
        mi = mi_visit(codigo, multi=True)
        return blocos, raw, halstead.total, mi
    except Exception as e:
        print(f"[-] Erro ao analisar {arquivo}: {e}")
        return [], None, None, None


"""
Gera e imprime no console um relatório detalhado do arquivo analisado:
- Complexidade por função/método
- Métricas brutas
- Métricas Halstead
- Índice de Manutenibilidade
"""
def gerar_relatorio(blocos, raw, halstead, mi, arquivo):
    print(f"\n==== Relatório de Análise do Arquivo ====")
    print(f"\n  📄 [INFO] Arquivo: {arquivo}")

    for bloco in blocos:
        rank = cc_rank(bloco.complexity)
        print(f"  ↳ {bloco.name} (linha {bloco.lineno}): complexidade {bloco.complexity} - nota {rank}")

    if raw:
        print("\n  [Métricas Brutas]")
        print(f"    LOC: {raw.loc} | LLOC: {raw.lloc} | SLOC: {raw.sloc} | Comentários: {raw.comments} | Blanks: {raw.blank}")

    if halstead:
        print("\n  [Halstead]")
        print(f"    Volume: {halstead.volume:.2f} | Dificuldade: {halstead.difficulty:.2f} | Esforço: {halstead.effort:.2f} | Bugs estimados: {halstead.bugs:.2f}")

    if mi is not None:
        rank = mi_rank(mi)
        print("\n  [Maintainability Index]")
        print(f"    MI: {mi:.2f} - nota {rank}")


"""
Exporta o relatório de análise para um arquivo de texto, no mesmo formato do console.
Inclui: complexidade, métricas brutas, Halstead e MI.
"""
def exportar_relatorio_txt(blocos, raw, halstead, mi, arquivo, arquivo_saida):
    if not blocos and not raw:
        return
    with open(arquivo_saida, "a", encoding="utf-8") as f:
        f.write(f"\n  📄 Arquivo: {arquivo}\n")

        for bloco in blocos:
            rank = cc_rank(bloco.complexity)
            f.write(f"  ↳ {bloco.name} (linha {bloco.lineno}): complexidade {bloco.complexity} - nota {rank}\n")

        if raw:
            f.write("\n  [Métricas Brutas]\n")
            f.write(f"    LOC: {raw.loc} | LLOC: {raw.lloc} | SLOC: {raw.sloc} | Comentários: {raw.comments} | Blanks: {raw.blank}\n")

        if halstead:
            f.write("\n  [Halstead]\n")
            f.write(f"    Volume: {halstead.volume:.2f} | Dificuldade: {halstead.difficulty:.2f} | Esforço: {halstead.effort:.2f} | Bugs estimados: {halstead.bugs:.2f}\n")

        if mi is not None:
            rank = mi_rank(mi)
            f.write("\n  [Maintainability Index]\n")
            f.write(f"    MI: {mi:.2f} - nota {rank}\n")


"""
Função principal que realiza a análise do repositório.
- Encontra os arquivos Python.
- Para cada arquivo, analisa a complexidade e gera relatório tanto no console quanto no arquivo.
"""
def analisar_repositorio(caminho_repositorio, caminho_saida_txt):
    print("[+] Buscando arquivos Python...")
    arquivos_py = encontrar_arquivos_py(caminho_repositorio)

    for arquivo in arquivos_py:
        blocos, raw, halstead, mi = analisar_arquivo(arquivo)
        gerar_relatorio(blocos, raw, halstead, mi, arquivo)
        exportar_relatorio_txt(blocos, raw, halstead, mi, arquivo, caminho_saida_txt)


"""
Remove o diretório clonado após a análise.
"""
def limpar_repositorio(caminho):
    print(f"[INFO] Limpando repositório clonado em: {caminho}")
    shutil.rmtree(caminho)


"""
Função principal do script.
- Define a URL do repositório.
- Clona o repositório.
- Executa a análise.
- Salva os resultados.
- Remove os arquivos temporários.
"""
def main():
    url = "https://github.com/Textualize/rich.git"
    local_path = "./repo_temp"
    caminho_saida_txt = "./relatorio_radon.txt"

    if os.path.exists(caminho_saida_txt):
        os.remove(caminho_saida_txt)

    clonar_repositorio(url, local_path)
    analisar_repositorio(local_path, caminho_saida_txt)
    limpar_repositorio(local_path)

    print("\n✅ Análise concluída.")


if __name__ == "__main__":
    main()

# pip install radon