import os
import shutil
import subprocess
import sys
import pandas as pd
from git import Repo

def clone_repo(repo_url, dest_dir='repo'):
    """
    Clona o repositório GitHub informado para um diretório local.
    Se o diretório já existir, ele será removido antes de clonar novamente.
    """
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    print(f"[+] Clonando repositório de {repo_url} ...")
    Repo.clone_from(repo_url, dest_dir)
    return dest_dir

def run_ck(jar_path, repo_dir, output_dir='ck_output'):
    """
    Executa o CK Tool e retorna os caminhos para os arquivos .csv gerados.
    """
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    print(f"[+] Executando CK Tool nas fontes em {repo_dir} ...")
    
    cmd = [
        'java', '-jar', jar_path,
        repo_dir,
        'true',      # usar JARs
        '0',         # max files per partition = automático
        'true',      # extrair métricas de variáveis e campos
        output_dir + os.sep
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o CK:", e)
        sys.exit(1)

    # Caminhos para os arquivos gerados
    files = {
        'class': os.path.join(output_dir, 'class.csv'),
        'field': os.path.join(output_dir, 'field.csv'),
        'method': os.path.join(output_dir, 'method.csv'),
        'variable': os.path.join(output_dir, 'variable.csv'),
    }

    # Confirma se class.csv existe
    if not os.path.exists(files['class']):
        print("Erro: class.csv não encontrado.")
        sys.exit(1)

    # Confirma se field.csv existe (aviso)
    if not os.path.exists(files['field']):
        print("Aviso: field.csv não encontrado. Métricas de campos não estarão disponíveis.")

    # Confirma se method.csv existe (aviso)
    if not os.path.exists(files['method']):
        print("Aviso: method.csv não encontrado. Métricas por método não estarão disponíveis.")

    # Confirma se variable.csv existe (aviso)
    if not os.path.exists(files['variable']):
        print("Aviso: variable.csv não encontrado. Métricas de variáveis não estarão disponíveis.")

    return files


def load_and_print_class_metrics(class_csv_path):
    """
    Carrega métricas por classe do CSV, seleciona colunas importantes e imprime as primeiras linhas.
    """
    print("\n[+] Lendo métricas por CLASSE ...")
    df_class = pd.read_csv(class_csv_path)

    # Colunas baseadas no class.csv
    class_columns = [
        'file', 'class', 'type',

        # Acoplamento e dependência
        'cbo', 'cboModified', 'fanin', 'fanout',

        # Complexidade e herança
        'wmc', 'dit', 'noc', 'rfc',

        # Coesão
        'lcom', 'lcom*', 'tcc', 'lcc',

        # Quantidade de métodos e campos
        'totalMethodsQty', 'staticMethodsQty', 'publicMethodsQty', 'privateMethodsQty',
        'protectedMethodsQty', 'defaultMethodsQty', 'visibleMethodsQty', 'abstractMethodsQty',
        'finalMethodsQty', 'synchronizedMethodsQty', 'totalFieldsQty', 'staticFieldsQty',
        'publicFieldsQty', 'privateFieldsQty', 'protectedFieldsQty', 'defaultFieldsQty',
        'finalFieldsQty', 'synchronizedFieldsQty',

        # Uso e complexidade
        'nosi', 'loc', 'returnQty', 'loopQty', 'comparisonsQty', 'tryCatchQty', 'parenthesizedExpsQty',
        'stringLiteralsQty', 'numbersQty', 'assignmentsQty', 'mathOperationsQty', 'variablesQty',
        'maxNestedBlocksQty', 'anonymousClassesQty', 'innerClassesQty', 'lambdasQty',
        'uniqueWordsQty', 'modifiers', 'logStatementsQty'
    ]

    available_class_cols = [col for col in class_columns if col in df_class.columns]
    # print(df_class[available_class_cols].to_string(index=False))  # Sem índice numérico
    print(df_class[available_class_cols].head()) # Exibe as 5 primeiras linhas para visualização

def load_and_print_method_metrics(method_csv_path):
    """
    Carrega métricas por método do CSV, seleciona colunas importantes e imprime as primeiras linhas.
    """
    if not os.path.exists(method_csv_path):
        print("[!] method.csv não encontrado.")
        return

    print("\n[+] Lendo métricas por MÉTODO ...")
    df_method = pd.read_csv(method_csv_path)

    # Colunas baseadas no method.csv
    method_columns = [
        'file', 'class', 'method', 'constructor', 'line',

        # Acoplamento e dependência
        'cbo', 'cboModified', 'fanin', 'fanout',

        # Complexidade e herança
        'wmc', 'rfc', 'loc',

        # Uso e complexidade
        'returnsQty', 'variablesQty', 'parametersQty', 'methodsInvokedQty',
        'methodsInvokedLocalQty', 'methodsInvokedIndirectLocalQty',

        # Estruturas de controle
        'loopQty', 'comparisonsQty', 'tryCatchQty', 'parenthesizedExpsQty',

        # Literais, operadores e variáveis
        'stringLiteralsQty', 'numbersQty', 'assignmentsQty', 'mathOperationsQty',

        # Estruturas internas
        'maxNestedBlocksQty', 'anonymousClassesQty', 'innerClassesQty', 'lambdasQty',

        # Semântica e modificadores
        'uniqueWordsQty', 'modifiers', 'logStatementsQty', 'hasJavaDoc'
    ]

    available_method_cols = [col for col in method_columns if col in df_method.columns]
    # print(df_method[available_method_cols].to_string(index=False))  # Sem índice numérico
    print(df_method[available_method_cols].head()) # Exibe as 5 primeiras linhas para visualização

def load_and_print_field_metrics(field_csv_path):
    """
    Carrega métricas por campo do CSV e imprime as primeiras linhas.
    """
    if not os.path.exists(field_csv_path):
        print("[!] field.csv não encontrado.")
        return

    print("\n[+] Lendo métricas por CAMPO ...")
    df_field = pd.read_csv(field_csv_path)

    # Colunas conforme o field.csv
    field_columns = [
        'file', 'class', 'method', 'variable', 'usage'
    ]

    available_field_cols = [col for col in field_columns if col in df_field.columns]
    # print(df_field[available_field_cols].to_string(index=False))  # Sem índice numérico
    print(df_field[available_field_cols].head()) # Exibe as 5 primeiras linhas para visualização

def load_and_print_variable_metrics(variable_csv_path):
    """
    Carrega métricas por variável do CSV e imprime as primeiras linhas.
    """
    if not os.path.exists(variable_csv_path):
        print("[!] variable.csv não encontrado.")
        return

    print("\n[+] Lendo métricas por VARIÁVEL ...")
    df_variable = pd.read_csv(variable_csv_path)

    # Colunas conforme o variable.csv
    variable_columns = [
        'file', 'class', 'method', 'variable', 'usage'
    ]

    available_variable_cols = [col for col in variable_columns if col in df_variable.columns]
    # print(df_variable[available_variable_cols].to_string(index=False))  # Sem índice numérico
    print(df_variable[available_variable_cols].head()) # Exibe as 5 primeiras linhas para visualização 

def main():
    print("== CK Metrics Extractor ==")

    repo_url = input("Informe a URL do repositório GitHub: ").strip()
    ck_jar_path = os.path.join("ck", "target", "ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar")

    if not os.path.exists(ck_jar_path):
        print(f"Erro: {ck_jar_path} não encontrado.")
        sys.exit(1)

    # Clona o repositório e executa o CK
    repo_path = clone_repo(repo_url)
    csv_paths = run_ck(ck_jar_path, repo_path)

    # Processa métricas de classe e método
    load_and_print_class_metrics(csv_paths['class'])
    load_and_print_method_metrics(csv_paths['method'])

    # Processa métricas de campo e variável
    load_and_print_field_metrics(csv_paths['field'])
    load_and_print_variable_metrics(csv_paths['variable'])

if __name__ == "__main__":
    main()

# Baixe o CK Tool e monte o JAR file (ck/target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar):
# git clone https://github.com/mauricioaniche/ck.git
# cd ck
# mvn clean package
# Documentação: https://github.com/mauricioaniche/ck

# Instale as dependências necessárias deste projeto:
# pip install gitpython pandas

# Execute o script:
# python ck_metrics_extractor.py
# Repo de exemplo: https://github.com/spring-projects/spring-petclinic