from fastapi import FastAPI, Request, HTTPException, Response, status
from fastapi.responses import JSONResponse
import uvicorn
import requests
 
app = FastAPI()

# -------------------------------
# CONFIGURAÇÕES
# -------------------------------
VERIFY_TOKEN = "#################"
ACCESS_TOKEN = "#################"
PHONE_NUMBER_ID = "#################"
API_URL = f"https://graph.facebook.com/v24.0/{PHONE_NUMBER_ID}/messages"
 
# -------------------------------
# FUNÇÃO: Enviar template hello_world
# -------------------------------
def enviar_hello_world(numero_destino: str):
    payload = {
        "messaging_product": "whatsapp",
        "to": numero_destino,
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {"code": "en_US"}
        }
    }
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"✅ Hello World enviado para {numero_destino}")
    else:
        print(f"⚠️ Erro ao enviar Hello World: {response.text}")
 
# -------------------------------
# ROTA DE VERIFICAÇÃO DO WEBHOOK
# -------------------------------
@app.get("/webhook")
async def verify_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")
 
    if mode == "subscribe" and token == VERIFY_TOKEN:
        return Response(content=challenge, media_type="text/plain", status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token inválido")
 
# -------------------------------
# ROTA PARA RECEBER MENSAGENS
# -------------------------------
@app.post("/webhook")
async def handle_webhook(request: Request):
    data = await request.json()
    print("📩 Payload recebido:", data)
 
    try:
        for entry in data.get("entry", []):
            for change in entry.get("changes", []):
                value = change.get("value", {})
                messages = value.get("messages", [])
                for message in messages:
                    phone = message["from"]
                    text = message.get("text", {}).get("body", "").strip()
                    print(f"Mensagem recebida de {phone}: {text}")
 
    except Exception as e:
        print("Erro processando webhook:", e)
 
    return JSONResponse(content={"status": "ok"})
 
# -------------------------------
# INÍCIO DO SERVIDOR
# -------------------------------
if __name__ == "__main__":
    print("Servidor iniciado!")
    numero_destino = "5531980402103"  # Seu número no WhatsApp
    enviar_hello_world(numero_destino)
    uvicorn.run(app, host="127.0.0.1", port=8000)

# pip install fastapi uvicorn requests