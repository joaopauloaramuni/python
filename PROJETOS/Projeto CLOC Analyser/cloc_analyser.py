import subprocess
import shutil
import os
from urllib.parse import urlparse

# 🧩 Função que clona um repositório Git no caminho de destino.
# Se o diretório de destino já existir, ele é removido antes de fazer o clone.
def clonar_repositorio(git_url, destino):
    if os.path.exists(destino):
        print("🧹 Diretório de destino já existe, removendo...")
        shutil.rmtree(destino)
    print(f"🔄 Clonando repositório de {git_url}...")
    subprocess.run(["git", "clone", git_url, destino], check=True)

# 📊 Função que executa o comando 'cloc' no diretório especificado
# e imprime o resultado da análise de contagem de linhas de código.
def rodar_cloc(caminho_repo):
    print(f"📊 Executando cloc em {caminho_repo}...\n")
    resultado = subprocess.run(["cloc", caminho_repo], capture_output=True, text=True)
    print("📋 Resultado:\n")
    print(resultado.stdout)

# 🚀 Função principal: solicita a URL do repositório,
# extrai seu nome, define o caminho de destino, clona e analisa com cloc.
def main():
    # Exemplo de URL: https://github.com/apache/commons-lang
    repositorio = input("📥 Informe a URL do repositório Git que deseja analisar com cloc: ").strip()

    # 🧠 Extrai o caminho da URL (ex: '/apache/commons-lang') e pega apenas o nome final ('commons-lang')
    caminho = urlparse(repositorio).path
    nome_repositorio = os.path.basename(caminho)

    # 🗂️ Define o caminho local onde o repositório será clonado
    caminho_destino = os.path.join(os.getcwd(), nome_repositorio)

    try:
        clonar_repositorio(repositorio, caminho_destino)
        rodar_cloc(caminho_destino)
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar subprocesso: {e}")
    except Exception as ex:
        print(f"⚠️ Erro inesperado: {ex}")

# ✅ Executa a função principal se o script for rodado diretamente
if __name__ == "__main__":
    print("🚀 Analisador de Código com CLOC\n")
    main()

# 💡 Observação:
# - Para usar este script, certifique-se de ter o 'cloc' instalado:
#     sudo apt install cloc        # Linux (Debian/Ubuntu)
#     brew install cloc            # macOS (Homebrew)