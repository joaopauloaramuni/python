from PIL import Image

# Caminho da imagem (no macOS na pasta Documents)
image_path = '/Users/joaopauloaramuni/Documents/imagem.jpg'

# Caracteres ASCII para representar diferentes níveis de brilho
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# Escolha o modo de saída: 'multi' para vários caracteres ou 'single' para apenas '#'
output_mode = 'single'  # ou 'single'

# Redimensionar a imagem mantendo a proporção
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # Ajuste de altura
    return image.resize((new_width, new_height))

# Converter a imagem para tons de cinza
def grayify(image):
    return image.convert('L')

# Mapeia pixels escuros para diferentes caracteres ASCII
def pixels_to_ascii(image, threshold=128):
    pixels = image.getdata()

    if output_mode == 'multi':
        # Usar múltiplos caracteres ASCII
        ascii_str = ''.join([ASCII_CHARS[pixel // (255 // (len(ASCII_CHARS) - 1))] for pixel in pixels])
    else:
        # Usar apenas o caractere '#'
        ascii_str = ''.join(['#' if pixel < threshold else ' ' for pixel in pixels])

    return ascii_str 

# Exibir a arte ASCII
def display_ascii(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return
    
    # Processar a imagem
    image = resize_image(image)
    image = grayify(image)
    
    # Converter para ASCII
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    
    # Formatar a arte com caracteres apropriados
    ascii_img = '\n'.join([ascii_str[i:(i+img_width)] for i in range(0, len(ascii_str), img_width)])
    
    # Imprimir a arte ASCII
    print(ascii_img)

# Exemplo de uso
display_ascii(image_path)
