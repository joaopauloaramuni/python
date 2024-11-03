import requests
import io
from PIL import Image
from tkinter import messagebox

# URL e headers para a API
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer hf_seutoken"}


# Função para consultar a API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        messagebox.showerror("Erro", f"Erro na API: {response.status_code}")
        return None


# Função para processar a imagem
def gerar_imagem(prompt):
    image_bytes = query({"inputs": prompt})
    if image_bytes:
        img = Image.open(io.BytesIO(image_bytes))
        return img
    else:
        return None