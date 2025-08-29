import io
import requests
import tkinter as tk
from PIL import Image, ImageTk

# https://dev.pokemontcg.io/dashboard
API_KEY = "SUA_API_KEY_AQUI"
API_URL = "https://api.pokemontcg.io/v2/cards/{}"

def get_card_data(card_id: str) -> dict:
    """Busca os dados de uma carta pelo ID"""
    url = API_URL.format(card_id)
    headers = {"X-Api-Key": API_KEY}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()["data"]

def get_card_image(card_data: dict):
    """Baixa a imagem da carta e retorna um objeto PIL.Image"""
    img_url = card_data["images"]["large"]  # pode trocar por "small"
    resp = requests.get(img_url)
    resp.raise_for_status()
    return Image.open(io.BytesIO(resp.content))

def show_card(card_id: str):
    """Mostra a carta em uma janela Tkinter"""
    data = get_card_data(card_id)
    print(f"Carta: {data['name']} — {data['supertype']} ({data['set']['name']})")

    img = get_card_image(data)
    img = img.resize((400, 560))  # redimensiona para caber na janela

    root = tk.Tk()
    root.title(f"{data['name']} — {data['set']['name']}")

    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.pack(padx=10, pady=10)

    # exibir também algumas infos básicas
    info = f"HP: {data.get('hp', '?')} | Tipo: {', '.join(data.get('types', []))}\n"
    info += f"Artista: {data.get('artist', 'Desconhecido')} | Raridade: {data.get('rarity', 'N/A')}\n"

    # flavor text
    if "flavorText" in data:
        info += f"Descrição: {data['flavorText']}\n"

    # ataques
    if "attacks" in data:
        ataques = []
        for atk in data["attacks"]:
            nome = atk.get("name", "?")
            dano = atk.get("damage", "")
            custo = ", ".join(atk.get("cost", []))
            texto = atk.get("text", "")
            ataques.append(f"- {nome} ({dano}) | Custo: {custo} | {texto}")
        info += "Ataques:\n" + "\n".join(ataques) + "\n"

    # habilidades
    if "abilities" in data:
        habs = []
        for hab in data["abilities"]:
            habs.append(f"- {hab.get('name', '')}: {hab.get('text', '')}")
        info += "Habilidades:\n" + "\n".join(habs) + "\n"

    # fraquezas
    if "weaknesses" in data:
        fraqs = [f"{w['type']} {w['value']}" for w in data["weaknesses"]]
        info += "Fraquezas: " + ", ".join(fraqs) + "\n"

    # resistências
    if "resistances" in data:
        resists = [f"{r['type']} {r['value']}" for r in data["resistances"]]
        info += "Resistências: " + ", ".join(resists) + "\n"

    # custo de retirada
    if "retreatCost" in data:
        info += "Custo de Retirada: " + ", ".join(data["retreatCost"]) + "\n"

    tk.Label(root, text=info, font=("Arial", 11), justify="left", wraplength=380).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    # Exemplo: Charizard de Vivid Voltage
    # https://api.pokemontcg.io/v2/cards?q=name:Charizard
    show_card("swsh4-25")

# pip install requests pillow
# python pokemon.py
