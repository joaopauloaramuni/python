from PIL import Image
import os
from interface import CompressorInterface


# Função para comprimir a imagem
def comprimir_imagem(caminho_imagem, qualidade):
    try:
        img = Image.open(caminho_imagem)
        caminho_comprimido = os.path.join(
            os.path.dirname(caminho_imagem),
            "comprimido_" + os.path.basename(caminho_imagem),
        )
        img.save(caminho_comprimido, "JPEG", quality=qualidade)
        return caminho_comprimido
    except Exception as e:
        return f"Erro: {e}"


# Função principal
def main():
    # Inicializa a interface gráfica
    interface = CompressorInterface(comprimir_imagem)
    interface.iniciar()


if __name__ == "__main__":
    main()
