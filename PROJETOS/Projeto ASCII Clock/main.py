import time

# Mapeamento de números para formato ASCII
ascii_digits = {
    '0': [' _ ', '| |', '|_|'],
    '1': ['   ', '  |', '  |'],
    '2': [' _ ', ' _|', '|_ '],
    '3': [' _ ', ' _|', ' _|'],
    '4': ['   ', '|_|', '  |'],
    '5': [' _ ', '|_ ', ' _|'],
    '6': [' _ ', '|_ ', '|_|'],
    '7': [' _ ', '  |', '  |'],
    '8': [' _ ', '|_|', '|_|'],
    '9': [' _ ', '|_|', ' _|']
}

# Função para colorir o texto de verde (Matrix)
def color_text(text):
    return f"\033[1;32m{text}\033[0m"  # 1 aplica o bold e 32 a cor verde

def print_time():
    # Obtém a hora atual
    current_time = time.strftime('%H%M%S')  # Formato HHMMSS
    lines = ['', '', '']
    
    for char in current_time:
        # Adiciona a representação ASCII do número à linha correspondente
        for i in range(3):
            colored_part = color_text(ascii_digits[char][i])
            lines[i] += colored_part + '  '  # Espaço entre cada dígito

    # Exibe o relógio digital com cor verde
    for line in lines:
        print(line)

if __name__ == "__main__":
    while True:
        print_time()
        time.sleep(1)  # Atualiza a hora a cada segundo
        print("\033[H\033[J", end='')  # Limpa a tela antes de mostrar a hora novamente
