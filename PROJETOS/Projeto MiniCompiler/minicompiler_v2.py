import re
 
# === 1. ANALISADOR LÉXICO ===
def lexer(source_code):
    token_specification = [
        ('IF',      r'if\b'),
        ('ELSE',    r'else\b'),
        ('WHILE',   r'while\b'),
        ('INT',     r'int\b'),
        ('FLOAT',   r'float\b'),
        ('ID',      r'[a-zA-Z_]\w*'),
        ('ASSIGN',  r'='),
        ('EQ',      r'=='),
        ('LT',      r'<'),
        ('GT',      r'>'),
        ('NUMBER',  r'\d+(\.\d+)?'),
        ('SEMICOLON', r';'),
        ('LBRACE',  r'\{'),
        ('RBRACE',  r'\}'),
        ('LPAREN',  r'\('),
        ('RPAREN',  r'\)'),
        ('SKIP',    r'[ \t]+'),
        ('NEWLINE', r'\n'),
        ('MISMATCH', r'.'),
    ]
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    tokens = []
    for match in re.finditer(token_regex, source_code):
        kind = match.lastgroup
        value = match.group()
        if kind in ('SKIP', 'NEWLINE'):
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f"Caractere inesperado: {value}")
        else:
            tokens.append((kind, value))
    return tokens
 
# === 2. ANALISADOR SINTÁTICO ===
def parser(tokens):
    pos = 0
 
    def expect(expected_type):
        nonlocal pos
        if pos < len(tokens) and tokens[pos][0] == expected_type:
            pos += 1
        else:
            raise SyntaxError(f"Esperado {expected_type}, mas encontrei {tokens[pos] if pos < len(tokens) else 'EOF'}")
 
    def parse_program():
        while pos < len(tokens):
            parse_statement()
 
    def parse_statement():
        if tokens[pos][0] in ('INT', 'FLOAT'):
            parse_declaration()
        elif tokens[pos][0] == 'IF':
            parse_if()
        elif tokens[pos][0] == 'WHILE':
            parse_while()
        else:
            raise SyntaxError(f"Comando inválido: {tokens[pos]}")
 
    def parse_declaration():
        nonlocal pos
        expect(tokens[pos][0])  # INT ou FLOAT
        expect('ID')
        expect('ASSIGN')
        expect('NUMBER')
        expect('SEMICOLON')
 
    def parse_expression():
        nonlocal pos
        if tokens[pos][0] in ('ID', 'NUMBER'):
            pos += 1
            if pos < len(tokens) and tokens[pos][0] in ('EQ', 'LT', 'GT'):
                pos += 1
                if pos < len(tokens) and tokens[pos][0] in ('ID', 'NUMBER'):
                    pos += 1
                else:
                    raise SyntaxError("Expressão incompleta após operador")
        else:
            raise SyntaxError("Expressão inválida")
 
 
    def parse_block():
        expect('LBRACE')
        while tokens[pos][0] != 'RBRACE':
            parse_statement()
        expect('RBRACE')
 
    def parse_if():
        expect('IF')
        expect('LPAREN')
        parse_expression()
        expect('RPAREN')
        parse_block()
 
    def parse_while():
        expect('WHILE')
        expect('LPAREN')
        parse_expression()
        expect('RPAREN')
        parse_block()
 
    parse_program()
    print("Código válido!")
 
# === 3. MAIN ===
def main():
    source_code = """
    int x = 5;
    if (x > 0) {
        float y = 3.14;
    }
    """
 
    print(">>> Código fonte:")
    print(source_code.strip())
 
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
        print(f"Erro sintático: {e.args}")
 
 
if __name__ == "__main__":
    main()