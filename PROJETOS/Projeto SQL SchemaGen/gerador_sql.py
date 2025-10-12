import os
from typing import TypedDict, List, Dict, Any
from faker import Faker

# --- 1. Definição do Tipo (Para clareza) ---

class ColumnDefinition(TypedDict, total=False):
    """Define a estrutura esperada para a definição de uma coluna no esquema."""
    name: str
    type: str
    primary_key: bool
    nullable: bool
    unique: bool
    default: str
    references: str  # Formato: "tabela_referenciada(coluna_referenciada)"
    faker: str       # Nome do método Faker (ex: 'name', 'email', 'random_int(min=0, max=100)')

# --- 2. Configurações Globais e Esquema do BD ---

# Configuração
NUM_RECORDS = 20 # Número de registros de exemplo a serem gerados por tabela.
FAKE = Faker('pt_BR') # Inicializa o Faker com localização para dados brasileiros.
FILENAME = "database_schema_and_seed.sql"

# O SCHEMA ABSTRAÍDO: Defina a estrutura do seu banco de dados aqui.
# Você foca na lógica (o que é uma PK, o que referencia), não na sintaxe SQL.
DATABASE_SCHEMA = {
    "clientes": [
        {"name": "cliente_id", "type": "INT", "primary_key": True},
        {"name": "nome", "type": "VARCHAR(100)", "nullable": False, "faker": "name"},
        {"name": "email", "type": "VARCHAR(100)", "nullable": False, "unique": True, "faker": "unique.email"},
        {"name": "data_cadastro", "type": "DATE", "default": "CURRENT_DATE", "faker": "date_this_year"}
    ],
    "produtos": [
        {"name": "produto_id", "type": "INT", "primary_key": True},
        {"name": "nome", "type": "VARCHAR(100)", "nullable": False, "faker": "word"},
        {"name": "preco", "type": "DECIMAL(10, 2)", "nullable": False, "faker": "pydecimal(left_digits=3, right_digits=2, positive=True)"},
        {"name": "estoque", "type": "INT", "default": 0, "faker": "random_int(min=0, max=100)"}
    ],
    "pedidos": [
        {"name": "pedido_id", "type": "INT", "primary_key": True},
        # Chave estrangeira (FK)
        {"name": "cliente_id", "type": "INT", "nullable": False, "references": "clientes(cliente_id)"},
        {"name": "data_pedido", "type": "TIMESTAMP", "default": "CURRENT_TIMESTAMP", "faker": "past_datetime"},
        {"name": "status", "type": "VARCHAR(50)", "default": "'Pendente'", "faker": "random_element(elements=('Aprovado', 'Pendente', 'Cancelado'))"}
    ],
    # Para o SEED funcionar corretamente, certifique-se de que a ordem das tabelas
    # no dicionário respeite as dependências de chaves estrangeiras.
}

# --- 3. Funções de Geração de SQL (Estrutura) ---

def format_column_definition(col: ColumnDefinition) -> str:
    """
    Formata o dicionário de definição de coluna em uma linha SQL (CREATE TABLE).
    """
    parts = [f"{col['name']} {col['type']}"]

    # Adiciona restrições baseadas nas propriedades do dicionário
    if col.get("primary_key"):
        parts.append("PRIMARY KEY")
    elif col.get("nullable") == False:
        parts.append("NOT NULL")

    if col.get("unique"):
        parts.append("UNIQUE")

    if col.get("default") is not None:
        parts.append(f"DEFAULT {col['default']}")

    return " ".join(parts)

def get_foreign_key_constraints(columns: List[ColumnDefinition]) -> List[str]:
    """
    Extrai as restrições FOREIGN KEY das definições de coluna.
    """
    fk_constraints = []
    for col in columns:
        if "references" in col:
            fk_target = col["references"]
            source_column = col["name"]
            
            fk_constraint = f"FOREIGN KEY ({source_column}) REFERENCES {fk_target}"
            fk_constraints.append(fk_constraint)
            
    return fk_constraints

def generate_create_table_script(table_name: str, columns: List[ColumnDefinition]) -> str:
    """
    Gera o comando SQL CREATE TABLE a partir da definição da tabela.
    """
    column_lines = [format_column_definition(col) for col in columns]
    fk_lines = get_foreign_key_constraints(columns)
    
    all_definitions = column_lines + fk_lines
    columns_definition = ',\n    '.join(all_definitions)

    sql_script = f"""
-- Comando para criar a tabela: {table_name}
CREATE TABLE IF NOT EXISTS {table_name} (
    {columns_definition}
);
"""
    return sql_script.strip()

def generate_all_create_scripts(schema: Dict[str, List[ColumnDefinition]]) -> List[str]:
    """
    Gera uma lista de comandos SQL CREATE TABLE para todas as tabelas no esquema.
    """
    scripts = []
    for table_name, columns in schema.items():
        script = generate_create_table_script(table_name, columns)
        scripts.append(script)
    return scripts

# --- 4. Funções de Geração de Dados (Seed) ---

def generate_seed_script(table_name: str, columns: List[ColumnDefinition], num_records: int) -> str:
    """
    Gera comandos SQL INSERT INTO com dados fake para uma tabela.
    """
    insert_scripts = [f"\n-- Dados de exemplo para a tabela: {table_name}"]
    
    # Filtra colunas que têm mapeamento 'faker' e não são PK (pois o ID será gerado pelo BD)
    cols_to_fill = [
        col for col in columns 
        if col.get('faker') and not col.get('primary_key')
    ]

    if not cols_to_fill:
        return f"\n-- Nenhum dado de exemplo a ser gerado para {table_name}."

    # 1. Monta o cabeçalho INSERT INTO
    column_names = [col['name'] for col in cols_to_fill]
    insert_header = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES"
    insert_scripts.append(insert_header)
    
    value_lines = []
    for _ in range(num_records):
        values = []
        for col in cols_to_fill:
            faker_method = col['faker']
            value = None
            
            try:
                # Usa eval() para métodos Faker com argumentos (ex: pydecimal(...))
                if '(' in faker_method and ')' in faker_method:
                    value = eval(f"FAKE.{faker_method}")
                else:
                    value = getattr(FAKE, faker_method)()

                # 2. Formata o valor: strings, datas e timestamps precisam de aspas simples no SQL
                if col['type'].startswith('VARCHAR') or col['type'] in ('DATE', 'TIMESTAMP'):
                    values.append(f"'{value}'")
                else:
                    values.append(str(value))

            except Exception as e:
                # Fallback em caso de erro na geração
                values.append(f"'ERROR_FAKE_{col['name']}'")

        value_line = f"({', '.join(values)})"
        value_lines.append(value_line)

    # 3. Finaliza o comando SQL
    final_values = ',\n'.join(value_lines) + ';'
    insert_scripts.append(final_values)

    return '\n'.join(insert_scripts)

# --- 5. Função de Escrita e Principal ---

def write_sql_file(scripts: List[str], filename: str):
    """
    Escreve os comandos SQL gerados em um arquivo .sql.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            content = '\n\n'.join(scripts)
            f.write(content)
        print(f"\n[SUCESSO] Scripts SQL gerados e salvos em: {os.path.abspath(filename)}")
    except IOError as e:
        print(f"\n[ERRO] Não foi possível escrever no arquivo: {e}")

def main():
    """
    Função principal que orquestra a geração e salvamento dos scripts SQL.
    """
    print("Iniciando a Geração de Schemas e Dados de Exemplo...")

    # 1. Geração dos scripts CREATE TABLE (Estrutura)
    create_scripts = [
        "-- Comandos CREATE TABLE (Estrutura do BD)",
        *generate_all_create_scripts(DATABASE_SCHEMA)
    ]

    # 2. Geração dos scripts INSERT INTO (Dados)
    seed_scripts = [
        "\n-- Comandos INSERT INTO (Dados de Exemplo)",
    ]
    # Itera sobre as tabelas para gerar dados
    for table_name, columns in DATABASE_SCHEMA.items():
        seed_scripts.append(generate_seed_script(table_name, columns, NUM_RECORDS))

    # 3. Combina e Salva no arquivo final
    final_scripts = create_scripts + seed_scripts
    write_sql_file(final_scripts, FILENAME)

    print("\nProcesso concluído.")

if __name__ == "__main__":
    main()