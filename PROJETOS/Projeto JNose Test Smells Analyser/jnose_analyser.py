import shutil
import os
import subprocess
import stat
from datetime import datetime
from urllib.parse import urlparse

# ========== CONFIGURAÇÕES ==========
REPO_URL = "https://github.com/apache/commons-lang" # Maven
# REPO_URL = "https://github.com/mockito/mockito"   # Gradle
BASE_DIR = os.path.abspath(".")                     # Diretório base onde o script está localizado  
JNOSE_DIR = os.path.join(BASE_DIR, "jnose")         # Caminho local do projeto JNose
OUTPUT_DIR = os.path.join(BASE_DIR, "output")       # Pasta onde será salvo o CSV de saída
caminho = urlparse(REPO_URL).path                   # Extrai o caminho da URL (ex: /apache/commons-lang)
NOME_REPO = os.path.basename(caminho)               # Extrai o nome do repositório (último segmento do caminho)           
CLONE_DIR = os.path.join(BASE_DIR, NOME_REPO)       # Caminho onde o repositório será clonado
TIMEOUT = 300                                       # Tempo limite (em segundos) para operações demoradas

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
    print("🔧 Compilando projeto Java clonado...")
    start_time = datetime.now()
    try:
        if os.path.exists(os.path.join(repo_path, "pom.xml")):
            print("🛠️ Projeto Maven detectado.")
            resultado = subprocess.run(
                ["mvn", "compile"],
                cwd=repo_path,
                capture_output=True,
                text=True,
                timeout=TIMEOUT
            )
            print("[Maven][STDOUT]:", resultado.stdout)
            print("[Maven][STDERR]:", resultado.stderr)

            if resultado.returncode != 0:
                print("❌ [Maven] Falha na compilação do JNose.")
                return False
            print("✅ [Maven] Compilação JNose concluída com sucesso.")

        elif os.path.exists(os.path.join(repo_path, "build.gradle")) or os.path.exists(os.path.join(repo_path, "build.gradle.kts")):
            print("🛠️ Projeto Gradle detectado.")
            gradlew = os.path.join(repo_path, "gradlew")
            if os.path.exists(gradlew):
                os.chmod(gradlew, os.stat(gradlew).st_mode | stat.S_IEXEC)
                cmd = ["./gradlew", "compileJava", "--no-daemon", "--info"]
            else:
                cmd = ["gradle", "compileJava", "--no-daemon", "--info"]

            resultado = subprocess.run(
                cmd,
                cwd=repo_path,
                capture_output=True,
                text=True,
                timeout=TIMEOUT
            )
            print("[Gradle][STDOUT]:", resultado.stdout)
            print("[Gradle][STDERR]:", resultado.stderr)

            if resultado.returncode != 0:
                print("❌ [Gradle] Falha na compilação do JNose.")
                return False
            print("✅ [Gradle] Compilação JNose concluída com sucesso.")
        else:
            print("❌ Nenhum build tool detectado.")
            return False

        # Verifica se o build gerou classes
        build_dirs = [
            "target/classes",
            "build/classes/java/main",
            "buildSrc/build/classes/kotlin/main"
        ]
        if not any(os.path.exists(os.path.join(repo_path, d)) for d in build_dirs):
            print("⚠️ Projeto compilado, mas diretórios de classes não encontrados.")
            return False

        return True

    except subprocess.TimeoutExpired:
        print("⏱️ Timeout durante a compilação.")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado na compilação: {e}")
        return False
    finally:
        print(f"⏰ Duração: {datetime.now() - start_time}")

def rodar_jnose(projeto_java, output_csv):
    """
    Executa o JNose com o caminho do projeto Java e o destino do arquivo CSV de saída.
    """
    print("🚀 Rodando JNose...")
    start_time = datetime.now()
    args = f'"{projeto_java}" "{output_csv}"'

    comando = [
        "mvn", "exec:java",
        "-Dexec.mainClass=br.ufba.jnose.JNoseCLI",
        f"-Dexec.args={args}",
        "-Dexec.jvmArgs=-Xmx512m",
        "--batch-mode"
    ]
    
    print(f"[DEBUG] Comando: {' '.join(comando)}")
    try:
        print("▶️ Executando Maven subprocess...")
        # Executa o JNose via Maven no diretório do projeto JNose
        resultado = subprocess.run(
            comando, 
            cwd=JNOSE_DIR, 
            timeout=TIMEOUT,
            check=True  # levanta exceções se retornar código de erro
        )
        
        if resultado.returncode != 0:
            raise RuntimeError("❌ Erro ao executar JNose.")
        
        print("✅ Subprocesso finalizado.")
        
        print("[Maven][STDOUT]:", resultado.stdout)
        print("[Maven][STDERR]:", resultado.stderr)
        
        if os.path.exists(output_csv):
            if os.path.getsize(output_csv) > 0:
                status = "Concluído"
            else:
                print(f"⚠️ Arquivo CSV gerado mas está vazio: {output_csv}")
                status = "Falhou"
        else:
            status = "Falhou"
        
        print(f"✅ JNose Concluído {projeto_java}: {status}")
        
    except subprocess.TimeoutExpired:
        print(f"⏱️ Timeout ao rodar em {projeto_java}")
        print([projeto_java, "Timeout", datetime.now().isoformat()])
    except Exception as e:
        print(f"❌ Erro ao rodar em {projeto_java}: {e}")
        print([projeto_java, f"Erro: {str(e)}", datetime.now().isoformat()])
    finally:
        print(f"⏰ Duração: {datetime.now() - start_time}")

# ========== EXECUÇÃO ==========
def main():
    try:
        # 1. Clona o repositório do projeto Java
        clone_repo(REPO_URL, CLONE_DIR)

        # 2. Compila o projeto Java clonado (Maven ou Gradle)
        if not compilar_projeto_java(CLONE_DIR):
            raise RuntimeError("❌ Falha na compilação do projeto. Abortando execução de JNose.")

        # 3. Cria a pasta de saída (se ainda não existir)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # 4. Define o caminho do CSV de saída com timestamp no nome
        output_csv = os.path.join(OUTPUT_DIR, f"resultado_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

        # 5. Executa o JNose para gerar o CSV de métricas
        rodar_jnose(CLONE_DIR, output_csv)

        # 6. Informa o caminho final do arquivo gerado
        print(f"📁 Resultado salvo em: {output_csv}")

    except RuntimeError as re:
        # Captura erros de execução previstos, como falhas na compilação
        print(f"❌ Erro de execução: {re}")
    except Exception as e:
        # Captura e exibe qualquer erro que ocorrer no processo
        print(f"❌ Erro geral inesperado: {e}")

# Executa o programa
if __name__ == "__main__":
    main()
