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

# Variável para rastrear se a pergunta já foi enviada
# Em um ambiente de produção, isso seria um banco de dados
pergunta_enviada = {} 

# -------------------------------
# FUNÇÃO: Enviar template hello_world
# -------------------------------
def enviar_hello_world(numero_destino: str):
    # ... (código da função enviar_hello_world permanece o mesmo)
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
# FUNÇÃO: Enviar mensagem de texto
# -------------------------------
def enviar_mensagem_texto(numero_destino: str, texto: str):
    payload = {
        "messaging_product": "whatsapp",
        "to": numero_destino,
        "type": "text",
        "text": {
            "body": texto
        }
    }
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"✅ Mensagem de texto enviada para {numero_destino}")
    else:
        print(f"⚠️ Erro ao enviar mensagem de texto: {response.text}")

# -------------------------------
# FUNÇÃO: Enviar mensagem com botões de opinião
# -------------------------------
def enviar_pergunta_com_botoes(numero_destino: str):
    payload = {
        "messaging_product": "whatsapp",
        "to": numero_destino,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": "Olá! Me diga: o que você achou da oficina do DevLabs? Sua opinião é muito importante!"
            },
            "action": {
                "buttons": [
                    {"type": "reply", "reply": {"id": "opcao_otima", "title": "Ótima"}},
                    {"type": "reply", "reply": {"id": "opcao_boa", "title": "Boa"}},
                    {"type": "reply", "reply": {"id": "opcao_regular", "title": "Regular"}}
                ]
            }
        }
    }

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"✅ Pergunta com botões enviada para {numero_destino}")
    else:
        print(f"⚠️ Erro ao enviar pergunta com botões: {response.text}")

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
                
                # O payload de notificação de template pode vir aqui
                if value.get("statuses"):
                    print("Status de mensagem recebido (entregue, lido, etc.). Ignorando.")
                    continue

                messages = value.get("messages", [])
                for message in messages:
                    phone = message["from"]
                    text = message.get("text", {}).get("body", "").strip()
                    print(f"Mensagem recebida de {phone}: {text}")
                    
                    # --- Lógica de Resposta com Botões ---

                    # Verifica se é resposta de botão
                    interactive = message.get("interactive", {})
                    if interactive:
                        button_reply = interactive.get("button_reply", {})
                        if button_reply:
                            escolha = button_reply.get("title")  # Título do botão clicado
                            print(f"📌 {phone} clicou na opção: {escolha}")

                            # Responder de forma confirmatória
                            agradecer = f"Você escolheu: {escolha}. Agradeço muito seu feedback! 😊"
                            enviar_mensagem_texto(phone, agradecer)

                            continue  # pula o restante da lógica de texto
                    
                    # --- Lógica de Resposta com Texto ---
                    
                    # 1. Se a pergunta ainda não foi enviada para este número
                    if phone not in pergunta_enviada:
                        pergunta = "Olá! Já que iniciamos a conversa, me diga: de 0 a 10, o que você achou da oficina do DevLabs? Sua opinião é muito importante!"
                        enviar_mensagem_texto(phone, pergunta)
                        pergunta_enviada[phone] = True # Marca como enviada
                        
                    # 2. Se a pergunta JÁ foi enviada, processa a resposta
                    elif pergunta_enviada.get(phone) == True:
                        try:
                            nota = int(text)
                            if 0 <= nota <= 10:
                                # Aqui você faria o armazenamento da nota (ex: em um banco de dados)
                                print(f"⭐️ Nota recebida de {phone}: {nota}")
                                
                                # Resposta de confirmação
                                agradecer = f"Você escolheu: {nota}! Agradeço muito seu feedback. Qualquer coisa estou à disposição! 😊"
                                enviar_mensagem_texto(phone, agradecer)
                                
                                # Poderia marcar como "resposta_recebida" se fosse um sistema mais complexo
                                pergunta_enviada[phone] = "respondido"
                            else:
                                # Resposta para nota fora do range
                                erro_nota = "Por favor, responda com um número entre 0 e 10. 😉"
                                enviar_mensagem_texto(phone, erro_nota)
                                
                        except ValueError:
                            # Resposta para texto que não é número
                            nao_entendi = "Não entendi sua resposta. Você poderia me dizer a nota (de 0 a 10) para a oficina de Python?"
                            enviar_mensagem_texto(phone, nao_entendi)

    except Exception as e:
        print("Erro processando webhook:", e)
 
    return JSONResponse(content={"status": "ok"})
 
# -------------------------------
# INÍCIO DO SERVIDOR
# -------------------------------
if __name__ == "__main__":
    print("Servidor iniciado!")
    # É importante garantir que o número de destino seja o SEU número do WhatsApp 
    # para receber a mensagem inicial de template.
    numero_destino = "5531980402103"  # Seu número no WhatsApp (no formato internacional)
    # A linha abaixo inicia a conversa com o template "Hello World"
    enviar_hello_world(numero_destino)
    enviar_pergunta_com_botoes(numero_destino)
    # Note que se o template for enviado e você responder, a lógica de feedback será acionada.
    uvicorn.run(app, host="127.0.0.1", port=8000)

# pip install fastapi uvicorn requests
