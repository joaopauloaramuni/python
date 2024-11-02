import requests

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer hf_seutoken"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
    # "inputs": "Astronaut riding a horse",
	"inputs": "Bearded software engineering professor",
})

import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

if image_bytes:
    print("Recebido conteúdo da imagem.")
    image = Image.open(io.BytesIO(image_bytes))
    image.show()  # Para exibir a imagem
    
    # Salvar a imagem na pasta raiz do projeto como 'imagem_gerada2.png'
    image.save("imagem_gerada2.png")
    print("Imagem salva como 'imagem_gerada2.png'.")