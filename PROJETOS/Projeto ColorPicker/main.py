import pyautogui
import time

# Função para converter RGB em hexadecimal
def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

# Função principal
def track_mouse():
    last_position = None
    print("Movimente o mouse para capturar as cores. Pressione Ctrl+C para sair.")

    while True:
        try:
            # Obtém a posição atual do mouse
            current_position = pyautogui.position()

            # Verifica se o mouse se moveu
            if current_position != last_position:
                last_position = current_position

                # Captura a cor do pixel na posição atual
                rgb = pyautogui.pixel(current_position.x, current_position.y)
                hex_color = rgb_to_hex(rgb)

                # Exibe os resultados
                print(f"Posição: {current_position} | RGB: {rgb} | Hex: {hex_color}")

            # Aguarda um pouco para reduzir o uso de CPU
            time.sleep(0.1)

        except KeyboardInterrupt:
            print("\nPrograma encerrado.")
            break

if __name__ == "__main__":
    track_mouse()


# pip install Pillow pyautogui