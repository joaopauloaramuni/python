import subprocess
import os
import shutil
import csv
from fpdf import FPDF

# -----------------------------------
# Configurações principais
# -----------------------------------
PMD_CMD = "pmd-bin-7.14.0/bin/pmd"  # Caminho relativo para o executável PMD
RULESET = "category/java/bestpractices.xml"  # Ruleset padrão para análise Java do PMD 7
REPORT_FORMAT = "text"  # Formato do relatório: pode ser 'text', 'xml', 'json', etc.
CSV_PATH = "repos.csv"  # Caminho para o CSV com URLs dos repositórios

# -----------------------------------
# Função para clonar o repositório
# -----------------------------------
def clone_repo(repo_url, clone_dir):
    if os.path.exists(clone_dir):
        print(f"🗑️ Removendo pasta existente '{clone_dir}' para re-clonar...")
        shutil.rmtree(clone_dir)
    
    print(f"📥 Clonando repositório {repo_url}...")
    subprocess.run(["git", "clone", repo_url], check=True)

# -----------------------------------
# Função para executar o PMD via CLI
# -----------------------------------
def run_pmd(clone_dir, pdf_name):
    source_dir = os.path.join(clone_dir, "src")
    
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"⚠️ Pasta do código-fonte não encontrada: {source_dir}")

    print("🔍 Executando análise PMD...")
    
    command = [
        PMD_CMD,
        "check",
        "-d", source_dir,
        "-R", RULESET,
        "-f", REPORT_FORMAT
    ]

    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if process.stdout:
        print("== 📄 Relatório PMD ==\n")
        print(process.stdout)
        export_report_to_pdf(process.stdout, output_pdf_path=pdf_name)

    if process.stderr:
        print("== 🚨 Erros PMD (stderr) ==\n")
        print(process.stderr)

# -----------------------------------
# Função para limpar o repositório clonado
# -----------------------------------
def cleanup_repo(clone_dir):
    if os.path.exists(clone_dir):
        print(f"🧹 Limpando pasta '{clone_dir}' após análise...")
        shutil.rmtree(clone_dir)

# -----------------------------------
# Função para exportar o relatório PMD para PDF
# -----------------------------------
def export_report_to_pdf(report_text, output_pdf_path="reports/pmd_report.pdf"):
    print("📄 Exportando relatório para PDF...\n")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=8)

    for line in report_text.splitlines():
        pdf.multi_cell(0, 10, txt=line)

    pdf.output(output_pdf_path)
    print(f"📑 Relatório exportado para PDF: {output_pdf_path}\n")

# -----------------------------------
# Leitura do CSV com os repositórios
# -----------------------------------
def read_repositories(csv_path):
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row[0] for row in reader if row]

# -----------------------------------
# Fluxo principal do script
# -----------------------------------
if __name__ == "__main__":
    print("*" * 150)
    print("🚀 Iniciando análise estática com PMD para múltiplos repositórios...")
    print("*" * 150)

    if os.name != "nt":
        subprocess.run(["chmod", "+x", PMD_CMD])

    repos = read_repositories(CSV_PATH)

    for repo_url in repos:
        print("*" * 150)
        print(f"📦 Processando: {repo_url}")
        print("*" * 150)
        
        clone_dir = os.path.basename(repo_url).removesuffix(".git")
        pdf_name = os.path.join("reports", f"{clone_dir}_pmd_report.pdf")

        try:
            clone_repo(repo_url, clone_dir)
            run_pmd(clone_dir, pdf_name)
        except Exception as e:
            print(f"❌ Erro ao processar {repo_url}: {e}")
        finally:
            cleanup_repo(clone_dir)

    print("*" * 150)
    print("✅ Análise finalizada para todos os repositórios!")
    print("*" * 150)
