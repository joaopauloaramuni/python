from PIL import Image
import os


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
    caminho_imagem = "imgs/image.jpg"
    qualidade = 50  # Definindo a qualidade para 50 (em vez de 0,5)
    resultado = comprimir_imagem(caminho_imagem, qualidade)
    print(f"Imagem comprimida salva em: {resultado}")


if __name__ == "__main__":
    main()
