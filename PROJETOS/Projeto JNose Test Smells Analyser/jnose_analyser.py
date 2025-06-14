import shutil
import os
import subprocess
import stat
from datetime import datetime

# ========== CONFIGURAÇÕES ==========
REPO_URL = "https://github.com/apache/commons-lang" # Maven
# REPO_URL = "https://github.com/mockito/mockito" # Gradle
BASE_DIR = os.path.abspath(".")
JNose_DIR = os.path.join(BASE_DIR, "jnose")             # Caminho local do projeto JNose
OUTPUT_DIR = os.path.join(BASE_DIR, "output")           # Pasta onde será salvo o CSV de saída
CLONE_DIR = os.path.join(BASE_DIR, "repo_clonado")      # Caminho onde o repositório será clonado
TIMEOUT = 300                                           # Tempo limite (em segundos) para operações demoradas

# ========== FUNÇÕES ==========
def clone_repo(repo_url, local_path):
    """
    Clona um repositório Git para o caminho especificado. Remove o diretório anterior, se existir.
    """
    if os.path.exists(local_path):
        print("🗑️ Removendo clone antigo...")
        shutil.rmtree(local_path)  # Remove o diretório antigo antes de clonar novamente
    print(f"🔁 Clonando {repo_url} para {local_path}...")
    subprocess.run(["git", "clone", repo_url, local_path], check=True)  # Executa o comando git clone
    print("✅ Clone concluído.")

def compilar_projeto_java(repo_path):
    """
    Detecta se o projeto usa Maven ou Gradle e realiza a compilação Java correspondente.
    """
    print("🔧 Compilando projeto Java clonado...")

    if os.path.exists(os.path.join(repo_path, "pom.xml")):
        # Projeto usa Maven
        print("🛠️ Projeto Maven detectado.")
        resultado = subprocess.run(
            ["mvn", "compile"],
            cwd=repo_path,
            capture_output=True,
            text=True,
            timeout=TIMEOUT
        )
    elif os.path.exists(os.path.join(repo_path, "build.gradle")) or os.path.exists(os.path.join(repo_path, "build.gradle.kts")):
        # Projeto usa Gradle
        print("🛠️ Projeto Gradle detectado.")
        gradlew = os.path.join(repo_path, "gradlew")
        if os.path.exists(gradlew):
            # Torna o gradlew executável (caso esteja no projeto)
            os.chmod(gradlew, os.stat(gradlew).st_mode | stat.S_IEXEC)
            cmd = ["./gradlew", "compileJava", "--no-daemon", "--info"]
        else:
            # Usa o Gradle global do sistema
            cmd = ["gradle", "compileJava", "--no-daemon", "--info"]
        resultado = subprocess.run(
            cmd,
            cwd=repo_path,
            capture_output=True,
            text=True,
            timeout=TIMEOUT
        )
    else:
        raise RuntimeError("❌ Nenhum build tool detectado (pom.xml ou build.gradle).")

    # Exibe os logs de compilação
    print("🔍 STDOUT:")
    print(resultado.stdout)
    print("🔍 STDERR:")
    print(resultado.stderr)

    if resultado.returncode != 0:
        raise RuntimeError("❌ Falha ao compilar o projeto Java.")

    # Verifica se algum diretório comum de build foi gerado
    build_dirs = [
        "target/classes",                      # Diretório comum em projetos Maven
        "build/classes/java/main",             # Diretório comum em projetos Gradle
        "buildSrc/build/classes/kotlin/main"   # Caso especial usado por alguns projetos Gradle com Kotlin
    ]
    if not any(os.path.exists(os.path.join(repo_path, d)) for d in build_dirs):
        raise RuntimeError("⚠️ Projeto compilado, mas diretórios de classes não encontrados.")

def rodar_jnose(projeto_java, output_csv):
    """
    Executa o JNose com o caminho do projeto Java e o destino do arquivo CSV de saída.
    """
    print("🚀 Rodando JNose...")
    args = f'"{projeto_java}" "{output_csv}"'

    comando = [
        "mvn", "exec:java",
        "-Dexec.mainClass=br.ufba.jnose.JNoseCLI",
        f"-Dexec.args={args}",
        "-Dexec.jvmArgs=-Xmx512m"
    ]

    # Executa o JNose via Maven no diretório do projeto JNose
    resultado = subprocess.run(comando, cwd=JNose_DIR, timeout=TIMEOUT)
    if resultado.returncode != 0:
        raise RuntimeError("❌ Erro ao executar JNose.")
    print(resultado.stdout)
    print("✅ JNose finalizado.")

# ========== EXECUÇÃO ==========
def main():
    try:
        # 1. Clona o repositório do projeto Java
        clone_repo(REPO_URL, CLONE_DIR)

        # 2. Compila o projeto Java clonado (Maven ou Gradle)
        compilar_projeto_java(CLONE_DIR)

        # 3. Cria a pasta de saída (se ainda não existir)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # 4. Define o caminho do CSV de saída com timestamp no nome
        output_csv = os.path.join(OUTPUT_DIR, f"resultado_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

        # 5. Executa o JNose para gerar o CSV de métricas
        rodar_jnose(CLONE_DIR, output_csv)

        # 6. Informa o caminho final do arquivo gerado
        print(f"📁 Resultado salvo em: {output_csv}")

    except Exception as e:
        # Captura e exibe qualquer erro que ocorrer no processo
        print(f"❌ Erro geral: {e}")

# Executa o programa
if __name__ == "__main__":
    main()
