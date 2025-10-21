import requests

# ==========================================
# CONFIGURAÇÕES
# ==========================================
# O seu token de acesso (mantido aqui, mas deve ser armazenado com segurança)
ACCESS_TOKEN = "#################"
PHONE_NUMBER_ID = "#################"
API_URL = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"


# ==========================================
# FUNÇÃO: Montar payload de template
# ==========================================
# Esta nova função cria o payload para enviar um template
def criar_payload_template(nome_template: str, codigo_idioma: str, numero_destino: str) -> dict:
    """
    Cria o corpo da requisição (payload) para enviar uma mensagem de template.
    """
    return {
        "messaging_product": "whatsapp",
        "to": numero_destino,
        "type": "template",
        "template": {
            "name": nome_template,
            "language": {
                "code": codigo_idioma
            }
        }
    }


# ==========================================
# FUNÇÃO: Enviar requisição à API (inalterada)
# ==========================================
def enviar_requisicao(payload: dict) -> dict:
    """
    Envia o payload para a API oficial do WhatsApp.
    """
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


# ==========================================
# FUNÇÃO PRINCIPAL: Enviar template
# ==========================================
def enviar_template(numero_destino: str, nome_template: str, codigo_idioma: str):
    """
    Envia uma mensagem de template via API do WhatsApp da Meta.
    """
    payload = criar_payload_template(nome_template, codigo_idioma, numero_destino)
    resposta = enviar_requisicao(payload)

    if "messages" in resposta:
        print(f"✅ Template '{nome_template}' enviado com sucesso!")
    else:
        print("⚠️ Erro ao enviar template:", resposta)


# ==========================================
# EXEMPLO DE USO
# ==========================================
if __name__ == "__main__":
    # Número: +55 31 98040-2103
    numero_destino = "5531980402103" 
    
    # Detalhes do template
    template_name = "hello_world"
    language_code = "en_US" # Ou "pt_BR" se o template for em português
    
    enviar_template(numero_destino, template_name, language_code)

# pip install requests