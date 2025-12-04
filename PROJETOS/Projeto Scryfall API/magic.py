import io
import requests
import tkinter as tk
from PIL import Image, ImageTk

# Scryfall API
# Exemplo de ID: "4e3e3f3b-212f-4cd8-8f8d-16e8a6fd2e99"
# (cada carta tem um UUID único na Scryfall)
API_URL = "https://api.scryfall.com/cards/{}"


def get_card_data(card_id: str) -> dict:
    """Busca os dados de uma carta de Magic pelo ID da Scryfall."""
    url = API_URL.format(card_id)
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()


def get_card_image(card_data: dict):
    """Baixa a imagem da carta e retorna um objeto PIL.Image."""
    # Algumas cartas possuem várias faces (como cards dupla-face)
    if "image_uris" in card_data:
        img_url = card_data["image_uris"]["large"]
    else:
        # cartas dupla-face
        img_url = card_data["card_faces"][0]["image_uris"]["large"]

    resp = requests.get(img_url)
    resp.raise_for_status()
    return Image.open(io.BytesIO(resp.content))


def show_card(card_id: str):
    """Mostra a carta de Magic em uma janela Tkinter."""

    data = get_card_data(card_id)

    # Nome da carta (se dupla-face, pega da primeira face)
    if "name" in data:
        name = data["name"]
    else:
        name = data["card_faces"][0]["name"]

    print(f"Carta: {name} — {data.get('set_name', 'Sem Set')}")

    img = get_card_image(data)
    img = img.resize((400, 560))

    root = tk.Tk()
    root.title(f"{name} — {data.get('set_name', '')}")

    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.pack(padx=10, pady=10)

    # Montagem das informações
    info = f"Nome: {name}\n"
    info += f"Tipo: {data.get('type_line', '---')}\n"
    info += f"Raridade: {data.get('rarity', '---').title()}\n"
    info += f"Artista: {data.get('artist', '---')}\n"

    # Mana cost
    if "mana_cost" in data:
        info += f"Custo de Mana: {data['mana_cost']}\n"
    elif "card_faces" in data and "mana_cost" in data["card_faces"][0]:
        info += f"Custo de Mana: {data['card_faces'][0]['mana_cost']}\n"

    # Power/Toughness (criaturas)
    if data.get("power") and data.get("toughness"):
        info += f"P/T: {data['power']}/{data['toughness']}\n"
    elif "card_faces" in data:
        face = data["card_faces"][0]
        if face.get("power") and face.get("toughness"):
            info += f"P/T: {face['power']}/{face['toughness']}\n"

    # Oracle text
    if "oracle_text" in data:
        info += f"\nTexto:\n{data['oracle_text']}\n"
    elif "card_faces" in data:
        if "oracle_text" in data["card_faces"][0]:
            info += f"\nTexto:\n{data['card_faces'][0]['oracle_text']}\n"

    tk.Label(
        root,
        text=info,
        font=("Arial", 11),
        justify="left",
        wraplength=380
    ).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    # Exemplo de carta: A-The One Ring — The Lord of the Rings: Tales of Middle-earth
    # https://scryfall.com/card/ltr/A-246/a-the-one-ring
    # https://api.scryfall.com/cards/ltr/A-246
    show_card("ltr/A-246")

    # pip install requests pillow
    # python magic.py
