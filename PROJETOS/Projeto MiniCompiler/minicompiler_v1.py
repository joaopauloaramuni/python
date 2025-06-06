import re

# === 1. ANALISADOR LÉXICO ===
def lexer(source_code):
    """
    Converte uma string de código-fonte em uma lista de tokens (tuplas: tipo, valor).
    """
    token_specification = [
        ('INT',     r'int\b'),        # palavra-chave 'int'
        ('FLOAT',   r'float\b'),      # palavra-chave 'float'
        ('ID',      r'[a-zA-Z_]\w*'), # identificador
        ('ASSIGN',  r'='),            # sinal de atribuição
        ('NUMBER',  r'\d+(\.\d+)?'),  # número inteiro ou float
        ('SEMICOLON', r';'),          # ponto e vírgula
        ('SKIP',    r'[ \t]+'),       # espaços e tabulações
        ('NEWLINE', r'\n'),           # quebras de linha
        ('MISMATCH', r'.'),           # qualquer outro caractere (erro)
    ]
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    tokens = []
    for match in re.finditer(token_regex, source_code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'SKIP' or kind == 'NEWLINE':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f"Caractere inesperado: {value}")
        else:
            tokens.append((kind, value))
    return tokens

# === 2. ANALISADOR SINTÁTICO ===
def parser(tokens):
    """
    Verifica se a lista de tokens forma uma declaração de variável válida.
    """
    pos = 0

    def expect(expected_type):
        nonlocal pos
        if pos < len(tokens) and tokens[pos][0] == expected_type:
            pos += 1
        else:
            raise SyntaxError(f"Esperado {expected_type}, mas encontrei {tokens[pos] if pos < len(tokens) else 'EOF'}")

    def parse_declaration():
        # tipo: int ou float
        if tokens[pos][0] in ('INT', 'FLOAT'):
            pos_type = tokens[pos][0]
            expect(pos_type)
        else:
            raise SyntaxError("Esperado tipo (int ou float)")

        # identificador
        expect('ID')

        # sinal de '='
        expect('ASSIGN')

        # número
        expect('NUMBER')

        # ponto e vírgula
        expect('SEMICOLON')

        print("Declaração válida!")

    parse_declaration()

# === 3. MAIN ===
def main():
    source_code = "int x = 42"  # Entrada com erro

    print(">>> Código fonte:")
    print(source_code)

    print("\n>>> Análise léxica (tokens):")
    try:
        tokens = lexer(source_code)
        for token in tokens:
            print(token)
    except SyntaxError as e:
        print(f"Erro léxico: {e}")
        return

    print("\n>>> Análise sintática:")
    try:
        parser(tokens)
    except SyntaxError as e:
        print(f"Erro sintático: {e}")

if __name__ == "__main__":
    main()
