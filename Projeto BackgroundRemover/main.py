from rembg import remove
from PIL import Image
import io

def remove_background(input_path: str, output_path: str):
    # Abrir a imagem de entrada
    with open(input_path, 'rb') as input_file:
        input_data = input_file.read()

    # Remover o fundo
    output_data = remove(input_data)

    # Salvar a imagem sem fundo
    with open(output_path, 'wb') as output_file:
        output_file.write(output_data)

    # Opcional: Mostrar a imagem resultante
    output_image = Image.open(io.BytesIO(output_data))
    output_image.show()

if __name__ == "__main__":
    # Caminho para a imagem de entrada e saída
    input_image_path = 'imgs/Guido_van_Rossum.jpeg'  # Caminho para sua imagem
    output_image_path = 'imgs/fundoremovido.png'  # Caminho para a imagem de saída

    # Remover o fundo da imagem
    remove_background(input_image_path, output_image_path)

# python 3.7 a 3.10
# pip install Pillow
# pip install onnxruntime
# pip install rembg
# python main.py