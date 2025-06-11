import subprocess
import os
import shutil
from fpdf import FPDF

# -----------------------------------
# Configurações principais
# -----------------------------------

PMD_CMD = "pmd-bin-7.14.0/bin/pmd"  # Caminho relativo para o executável PMD
REPO_URL = "https://github.com/arieslab/jnose.git"  # Repositório Java a ser analisado
CLONE_DIR = os.path.basename(REPO_URL).removesuffix(".git") # Pasta onde o repositório será clonado localmente
RULESET = "category/java/bestpractices.xml"  # Ruleset padrão para análise Java do PMD 7
REPORT_FORMAT = "text"  # Formato do relatório: pode ser 'text', 'xml', 'json', etc.

# -----------------------------------
# Função para clonar o repositório
# -----------------------------------
def clone_repo():
    # Se já existir a pasta do repositório, remove para evitar conflitos
    if os.path.exists(CLONE_DIR):
        print(f"🗑️ Removendo pasta existente '{CLONE_DIR}' para re-clonar...")
        shutil.rmtree(CLONE_DIR)
    
    # Clona o repositório do GitHub localmente
    print(f"📥 Clonando repositório {REPO_URL}...")
    subprocess.run(["git", "clone", REPO_URL], check=True)

# -----------------------------------
# Função para executar o PMD via CLI
# -----------------------------------
def run_pmd():
    # PMD espera o caminho para os arquivos-fonte via -d ou --dir
    source_dir = os.path.join(CLONE_DIR, "src")
    
    # Verifica se a pasta de código-fonte existe
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"⚠️ Pasta do código-fonte não encontrada: {source_dir}")

    print("🔍 Executando análise PMD...")

    # Monta o comando conforme documentação:
    # pmd check -d <diretório> -R <ruleset> -f <formato do relatório>
    command = [
        PMD_CMD,
        "check",             # Subcomando para rodar a análise
        "-d", source_dir,    # Diretório com código fonte Java
        "-R", RULESET,       # Ruleset que define quais regras rodar
        "-f", REPORT_FORMAT  # Formato do relatório de saída
    ]

    # Executa o comando, capturando stdout e stderr como texto
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Exibe o relatório gerado pelo PMD
    if process.stdout:
        print("== 📄 Relatório PMD ==\n")
        print(process.stdout)
        # Exporta o relatório para PDF
        export_report_to_pdf(process.stdout, output_pdf_path="pmd_report.pdf")

    # Exibe possíveis erros do PMD
    if process.stderr:
        print("== 🚨 Erros PMD (stderr) ==\n")
        print(process.stderr)

# -----------------------------------
# Função para limpar o repositório clonado
# -----------------------------------
def cleanup_repo():
    if os.path.exists(CLONE_DIR):
        print(f"🧹 Limpando pasta '{CLONE_DIR}' após análise...")
        shutil.rmtree(CLONE_DIR)

# -----------------------------------
# Função para exportar o relatório PMD para PDF
# -----------------------------------
def export_report_to_pdf(report_text, output_pdf_path="pmd_report.pdf"):
    """
    Gera um PDF simples contendo o texto do relatório PMD.
    Usa a biblioteca fpdf para criar o arquivo PDF.
    """
    print("📄 Exportando relatório para PDF...\n")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=8)

    # Quebra o texto em linhas para não ultrapassar a largura da página
    for line in report_text.splitlines():
        pdf.multi_cell(0, 10, txt=line)

    pdf.output(output_pdf_path)
    print(f"📑 Relatório exportado para PDF: {output_pdf_path}\n")

# -----------------------------------
# Fluxo principal do script
# -----------------------------------
if __name__ == "__main__":
    print("*" * 150)
    print("🚀 Iniciando análise estática com PMD...")
    print("*" * 150)
            
    # No Linux/macOS: garante que o executável do PMD tem permissão de execução
    if os.name != "nt":
        subprocess.run(["chmod", "+x", PMD_CMD])

    # Passo 1: clona o repositório Java para analisar
    print("*" * 150)
    clone_repo()
    print("*" * 150)
            
    # Passo 2: executa o PMD para rodar as análises estáticas
    print("*" * 150)
    run_pmd()
    print("*" * 150)
    
    # Passo 3: remove o repositório clonado para manter a pasta limpa
    print("*" * 150)
    cleanup_repo()
    print("*" * 150)
    
    print("*" * 150)
    print("✅ Análise finalizada com sucesso!")
    print("*" * 150)