from PIL import Image
import os


# Função para comprimir a imagem JPEG
def comprimir_imagem_jpeg(caminho_imagem, qualidade):
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


# Função para comprimir a imagem PNG
def comprimir_imagem_png(caminho_imagem):
    try:
        img = Image.open(caminho_imagem)
        img = img.convert("P", palette=Image.ADAPTIVE, colors=128)  # Reduz para 128 cores

        caminho_comprimido = os.path.join(
            os.path.dirname(caminho_imagem),
            "comprimido_" + os.path.basename(caminho_imagem),
        )
        img.save(caminho_comprimido, "PNG", optimize=True)
        return caminho_comprimido
    except Exception as e:
        return f"Erro: {e}"


# Função para comprimir a imagem WebP sem alterar a extensão
def comprimir_imagem_webp(caminho_imagem, qualidade):
    try:
        img = Image.open(caminho_imagem)
        caminho_comprimido = os.path.join(
            os.path.dirname(caminho_imagem),
            "comprimido_" + os.path.basename(caminho_imagem),  # Mantém a extensão original
        )
        img.save(caminho_comprimido, "WEBP", quality=qualidade, optimize=True)
        return caminho_comprimido
    except Exception as e:
        return f"Erro: {e}"


# Função principal
def main():
    caminho_imagem = "imgs/image.jpg"
    qualidade = 50  # Define a qualidade da compressão (1 a 100)
    resultado = comprimir_imagem_jpeg(caminho_imagem, qualidade)
    # resultado = comprimir_imagem_png(caminho_imagem)
    # resultado = comprimir_imagem_webp(caminho_imagem, qualidade)
    print(f"Imagem comprimida salva em: {resultado}")


if __name__ == "__main__":
    main()
