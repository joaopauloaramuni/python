# 🤖 ZapSender: Envio e Recebimento de Mensagens via WhatsApp Cloud API

O **ZapSender** é um projeto em **Python** que demonstra, de forma prática, como integrar-se à **WhatsApp Cloud API** (Meta for Developers) para **enviar** e **receber** mensagens de forma automatizada.

Ele contém dois scripts independentes e complementares:

- 🟢 **`zapsender.py`** — envia mensagens de *template* pré-aprovadas (como `hello_world`) para contatos via API oficial da Meta.  
- 🟣 **`webhook.py`** — implementa um servidor **FastAPI** capaz de receber e processar notificações e mensagens enviadas pelo WhatsApp por meio de **Webhooks**.

O objetivo é fornecer uma base **simples**, **segura** e **reproduzível** para entender o fluxo completo de automação com a WhatsApp Cloud API — desde o envio de templates até o recebimento de mensagens e eventos em tempo real.

---

## 📖 Sumário

- [💬 Fluxo Interativo: Avaliação da Oficina](#-fluxo-interativo-avaliação-da-oficina)
- [💡 Estrutura do Projeto](#-estrutura-do-projeto)
- [📘 Meta for Developers e a Cloud API](#-meta-for-developers-e-a-cloud-api)
- [🚀 Passo a Passo para Criar o App no Meta for Developers](#-passo-a-passo-para-criar-o-app-no-meta-for-developers)
- [📝 Mensagens de Template (Message Templates)](#-mensagens-de-template-message-templates)
- [🌐 Criando e Configurando o Webhook](#-criando-e-configurando-o-webhook)
- [📝 Explicação do Código Python](#-explicação-do-código-python)
- [📌 Pré-requisitos](#-pré-requisitos)
- [🐍 Ambiente virtual (recomendado)](#-ambiente-virtual-recomendado)
- [⚡ Execução](#-execução)
- [📚 Documentação e Links Úteis](#-documentação-e-links-úteis)
- [🤝 Contribuição](#-contribuição)
- [🧾 Licença](#-licença)

---

## 💬 Fluxo Interativo: Avaliação da Oficina (WhatsApp + FastAPI)

O arquivo **`webhook.py`** implementa um bot automatizado via **WhatsApp Business API**, permitindo que o usuário avalie a oficina do DevLabs de forma **interativa** e **flexível**.

---

### 🧠 Lógica de Funcionamento

1. O bot envia automaticamente **o template “Hello World”** ao iniciar o fluxo.
2. Em seguida, envia uma **mensagem interativa com botões**:  
   > "Olá! Me diga: o que você achou da oficina do DevLabs? Sua opinião é muito importante!"  
   Botões disponíveis:  
   - 🟢 Ótima  
   - 🟡 Boa  
   - 🔵 Regular  
3. O usuário **responde clicando em um botão**, e o bot confirma:  
   > "Você escolheu: [opção]. Agradeço muito seu feedback! 😊"  
4. O usuário **pode iniciar uma nova conversa** a qualquer momento enviando “Oi” ou qualquer outra mensagem.
5. Ao iniciar uma nova conversa, o bot envia uma **pergunta de texto solicitando uma nota de 0 a 10**:  
   > "Olá! Já que iniciamos a conversa, me diga: de 0 a 10, o que você achou da oficina do DevLabs? Sua opinião é muito importante!"  
6. O usuário responde com **uma nota de 0 a 10**, e o bot confirma:  
   > "Você escolheu: [nota]! Agradeço muito seu feedback. Qualquer coisa estou à disposição! 😊"  
7. A resposta (opção de botão ou nota) é **registrada no terminal** e pode ser **armazenada em banco de dados** futuramente.

---

## 🖼️ Captura de Tela

| <img src="https://joaopauloaramuni.github.io/python-imgs/ZapSender/imgs/Chat.png" alt="ZapSender" width="1000"/> |
|:---------:|
| ZapSender |

🖥️ No terminal:

```bash
...
📩 Payload recebido: {'object': 'whatsapp_business_account', 'entry': [{'id': '788244184191501', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '15551438086', 'phone_number_id': '836567342875521'}, 'contacts': [{'profile': {'name': 'João Paulo Aramuni'}, 'wa_id': '553180402103'}], 'messages': [{'from': '553180402103', 'id': 'wamid.HBgMNTUzMTgwNDAyMTAzFQIAEhgUM0I2QkIzRTlGRTIyNUQyN0Q2RDcA', 'timestamp': '1761249588', 'text': {'body': 'Oi'}, 'type': 'text'}]}, 'field': 'messages'}]}]}
Mensagem recebida de 553180402103: Oi
✅ Mensagem de texto enviada para 553180402103
INFO:     2a03:2880:12ff:7:::0 - "POST /webhook HTTP/1.1" 200 OK
...
```

---

## 💡 Estrutura do Projeto

### 🟢 `zapsender.py`
Script responsável por **enviar mensagens de template** (pré-aprovadas pela Meta) para números de WhatsApp específicos.  
Ele realiza uma requisição **HTTP POST** diretamente para o endpoint oficial da Cloud API, autenticando-se via **Access Token**.

Ideal para testar o **envio automatizado de mensagens** sem precisar configurar um servidor.

### 🟣 `webhook.py`
Script que cria um **servidor FastAPI** para **receber mensagens e eventos** enviados pela Cloud API via **Webhook**.  
É usado para capturar mensagens de usuários, testar interações bidirecionais e depurar callbacks em tempo real.

Durante o desenvolvimento local, o servidor pode ser exposto à internet com o **ngrok**, que fornece uma **URL HTTPS temporária** para uso como “Callback URL” na **Meta for Developers**.

---

Esses scripts são **independentes**, ou seja, você pode:
- Executar apenas o `zapsender.py` para enviar mensagens, ou  
- Rodar o `webhook.py` para receber e inspecionar mensagens recebidas.

---

## 📘 Meta for Developers e a Cloud API

### O que é o Meta for Developers?
É a plataforma oficial da **Meta** que fornece APIs, SDKs e ferramentas para desenvolvedores criarem integrações com produtos como **Facebook**, **Instagram** e **WhatsApp**.

Para utilizar a **WhatsApp Cloud API**, é necessário:
1. Criar um aplicativo dentro do [Meta for Developers](https://developers.facebook.com/).  
2. Adicionar o **produto WhatsApp** ao seu app.  
3. Obter um **Access Token** e um **Phone Number ID**.  
4. (Opcional) Configurar um **Webhook** para receber mensagens e eventos automaticamente.

---

## 🚀 Passo a Passo para Criar o App no Meta for Developers

Antes de enviar mensagens com a **WhatsApp Cloud API**, é necessário criar um **aplicativo** e vinculá-lo a uma **Conta Comercial (Business Portfolio)**.  
Esse vínculo habilita o produto **WhatsApp** no seu app e permite gerar as credenciais necessárias (Access Token, ID do telefone e endpoint da API).

### 🧩 1. Criar o aplicativo

1. Acesse o portal [Meta for Developers](https://developers.facebook.com/apps/) e clique em **Criar aplicativo**.
2. Escolha o tipo de aplicativo:
   - **Negócios (Business)**: para empresas que enviarão mensagens de forma comercial.
   - **Outro (Other)**: para testes ou integrações simples.
3. Dê um **nome ao seu aplicativo** e finalize a criação.

---

### 💼 2. Vincular a Conta Comercial (Business Portfolio)

Para que o produto **WhatsApp** apareça como opção no seu app:

1. Certifique-se de ter uma **Conta Comercial ativa** no [Meta Business](https://business.facebook.com/).
2. No painel do app, vá em **Configurações > Informações do App**.
3. Vincule o seu **Business Portfolio** à conta do aplicativo.
4. Após o vínculo, o produto **WhatsApp** será exibido para integração.

> ⚠️ **Observação:** Sem essa etapa, você não conseguirá adicionar o WhatsApp ao app, nem enviar mensagens via Cloud API.

---

### ✅ 3. Próximos passos

- Adicione o produto **WhatsApp** no painel do seu app.
- Configure um número de telefone (sandbox ou oficial) para testes.
- Crie templates de mensagens para poder enviar notificações ou mensagens automatizadas.

---

## 📝 Mensagens de Template (Message Templates)

### O que é um Template?
Templates (ou Modelos de Mensagem) são mensagens pré-aprovadas que devem ser usadas para iniciar conversas ou enviar notificações fora da janela de 24 horas de atendimento.  
Para usar a Cloud API, a primeira mensagem para um novo contato deve ser um Template, como o `hello_world` usado neste projeto.

### Passo a passo para criar um Template
1.  Acesse o **Gerenciador do WhatsApp** através do link: [Gerenciador de Templates](https://business.facebook.com/latest/whatsapp_manager/message_templates).
2.  Certifique-se de que está na conta de Negócios correta.
3.  Clique em **"Criar Modelo de Mensagem"**.
4.  Defina o **Nome** (ex.: `hello_world`), **Categoria** (ex.: Utilidade) e **Idioma**.
5.  Crie o corpo da mensagem.
6.  Envie o template para aprovação (em ambientes de teste, templates básicos são aprovados instantaneamente).

### ⏳ Prazo de Aprovação
O prazo de aprovação de um novo modelo de mensagem pela **Meta** pode levar **até 24 horas**.  
Esse tempo é necessário para que a equipe da Meta analise o conteúdo e garanta que o template esteja em conformidade com as **políticas do WhatsApp Business API**.

---

## 🌐 Criando e Configurando o Webhook

O **Webhook** é o mecanismo usado pela Meta para **enviar notificações e mensagens recebidas** para o seu servidor.  
Quando alguém envia uma mensagem para o seu número do WhatsApp Business, a Meta faz uma requisição `POST` para a **URL de callback** configurada no seu app.

---

### ⚙️ 4. Criar o Webhook no Meta for Developers

1. No painel do seu aplicativo, vá em **Produtos → WhatsApp → Configurações**.  
2. Na seção **Webhook**, clique em **“Configurar Webhook”**.  
3. Você verá dois campos:
   - **Callback URL:** o endereço público do seu servidor que receberá os eventos.  
     Exemplo (usando ngrok): `https://1234abcd.ngrok.io/webhook`
   - **Verify Token:** uma senha personalizada que você escolhe (ex.: `joaopauloaramuni`).  
     Esse token deve **coincidir com o valor da variável `VERIFY_TOKEN`** no arquivo `webhook.py`.

4. Clique em **Verificar e Salvar**.  
   O Meta enviará uma requisição `GET` ao seu endpoint `/webhook` com parâmetros de verificação.  
   Se o seu servidor (`webhook.py`) estiver rodando corretamente, ele retornará o `hub.challenge` e a verificação será concluída com sucesso.

---

### 🔔 5. Assinar o Campo “messages”

Após configurar o Webhook:

1. Ainda no painel de **Webhooks**, clique em **“Gerenciar campos”**.  
2. Marque a opção **`messages`** para que seu servidor receba notificações sempre que novas mensagens forem enviadas ou recebidas.  
3. Clique em **Salvar alterações**.

> 💡 **Importante:** sem assinar o campo `messages`, o seu endpoint `/webhook` não receberá nenhum evento de mensagem.

---

### 🧪 Testando o Webhook

1. Execute o servidor diretamente com:
   python webhook.py

2. Configure seu ngrok com o token pessoal (somente na primeira execução):
   ngrok config add-authtoken SEU_TOKEN_AQUI

3. Inicie o túnel HTTPS para expor a porta local 8000:
   ngrok http 8000

4. Copie o link HTTPS gerado e adicione **`/webhook`** ao final.  
   Use esse endereço completo como **Callback URL** no painel da Meta.  
   Exemplo final: `https://1234abcd.ngrok.io/webhook`

5. Envie uma mensagem para o número de teste configurado.  
   Você verá o **payload JSON** aparecer no terminal, confirmando que o webhook está recebendo os dados corretamente.

---

## 📝 Explicação do Código Python

O projeto é dividido em **dois scripts independentes**, cada um com responsabilidades claras:

### 🟢 `zapsender.py` — Envio de Templates

Este script é responsável por **enviar mensagens de template pré-aprovadas** via API oficial da Meta.  
Ele é estruturado em funções que organizam o fluxo de criação do payload e envio da requisição:

| Assinatura da Função | Descrição |
| :--- | :--- |
| `criar_payload_template(nome_template: str, codigo_idioma: str, numero_destino: str) -> dict` | Monta o corpo JSON da requisição, garantindo que o nome do template, o código do idioma e o número de destino estejam no formato exigido pela API. |
| `enviar_requisicao(payload: dict) -> dict` | Realiza a chamada `POST` para a API da Meta, incluindo o **ACCESS_TOKEN** nos headers e o payload JSON no corpo da requisição. Retorna a resposta da API. |
| `enviar_template(numero_destino: str, nome_template: str, codigo_idioma: str)` | Função de orquestração. Cria o payload e envia a requisição, exibindo no terminal uma mensagem de sucesso ou erro, de acordo com a resposta da API. |

> 💡 Ideal para testar o envio automatizado de mensagens sem precisar de um servidor web.

---

### 🟣 `webhook.py` — Recebimento de Mensagens

Este script implementa um **servidor FastAPI** capaz de **receber mensagens e eventos** enviados pela WhatsApp Cloud API:

| Função / Endpoint | Descrição |
| :--- | :--- |
| `enviar_hello_world(numero_destino: str)` | Envia um template `hello_world` para um número específico, útil para testes de webhook ou de envio de mensagens iniciadas pelo bot (requer aprovação prévia do template pela Meta). |
| `enviar_mensagem_texto(numero_destino: str, texto: str)` | Envia uma mensagem de texto livre para um número de WhatsApp. Essa função é usada **dentro de uma conversa já iniciada pelo usuário**, sem necessidade de template aprovado. |
| `enviar_pergunta_com_botoes(numero_destino: str)` | Envia uma **mensagem interativa com botões** para o usuário, permitindo respostas rápidas como "Ótima", "Boa" ou "Regular". A função trata o envio do payload correto para o WhatsApp Cloud API e deve ser usada **após o Hello World** ou em pontos estratégicos da conversa. |
| `@app.get("/webhook")` | Endpoint de **verificação do webhook**. O Meta envia uma requisição GET com `hub.challenge` para validar a URL e o `VERIFY_TOKEN`. |
| `@app.post("/webhook")` | Endpoint para **receber mensagens e notificações**. Processa o payload JSON enviado pelo Meta, exibindo informações como remetente e conteúdo da mensagem no terminal. Implementa também a lógica de feedback: ao receber a primeira mensagem do usuário, envia a pergunta “De 0 a 10, o que achou da oficina de Python?”, e em seguida valida e registra a nota. |

> 💡 Durante o desenvolvimento, o servidor pode ser exposto à internet com **ngrok**, permitindo que a Meta envie notificações para o seu endpoint local.

---

## 📌 Pré-requisitos

Para rodar os scripts do projeto, você precisará:

### 🟢 Para `zapsender.py` (envio de templates)
- **Python 3.12+** instalado.
- **ACCESS_TOKEN**: Token de acesso da Meta for Developers.
- **PHONE_NUMBER_ID**: O ID do número de telefone (sandbox ou oficial) usado para enviar a mensagem.
- **Biblioteca requests**: para enviar requisições HTTP.

Instalação:
```bash
pip install requests
```

---

### 🟣 Para `webhook.py` (recebimento de mensagens)
- **Python 3.12+** instalado.
- **ACCESS_TOKEN** e **PHONE_NUMBER_ID** (opcional, se quiser testar envio de hello_world).
- **VERIFY_TOKEN**: token para validação do webhook no Meta.
- **Bibliotecas FastAPI e uvicorn**: para rodar o servidor web.
- **requests**: para enviar mensagens de teste, se necessário.
- **ngrok**: para expor o servidor local à internet e obter a URL HTTPS de callback.

Instalação:
```bash
pip install fastapi uvicorn requests
```

Instalação do ngrok:
- Baixe e instale o ngrok via [site oficial](https://ngrok.com/download)
- Configure seu token pessoal (somente na primeira execução):
ngrok config add-authtoken SEU_TOKEN_AQUI

---

## 🐍 Ambiente virtual (recomendado)
1. **Crie o ambiente virtual:**
```bash
python -m venv .venv
```

2. **Ative o ambiente virtual:**

- **Windows:**
```bash
.venv\Scripts\activate
```

- **Linux/macOS:**
```bash
source .venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install requests # zapsender.py
pip install fastapi uvicorn requests # webhook.py
```

---

## ⚡ Execução

### 🟢 1. Configuração do `zapsender.py`

No arquivo `zapsender.py`, substitua os *placeholders* na seção `CONFIGURAÇÕES` pelos valores obtidos na plataforma Meta Developers:

- **`ACCESS_TOKEN`**: Seu token de acesso de usuário (deve ser tratado com segurança em produção).
- **`PHONE_NUMBER_ID`**: O ID do número de telefone de teste/produção.

### 🟢 2. Executando o `zapsender.py`

Execute o script principal para enviar um template de teste:

python zapsender.py

---

### 🟣 3. Configuração do `webhook.py`

No arquivo `webhook.py`, verifique:

- **`VERIFY_TOKEN`**: Token que será usado para validar o webhook na Meta.
- **`ACCESS_TOKEN`**: Necessário se quiser testar o envio de `hello_world` diretamente do webhook.
- **`PHONE_NUMBER_ID`**: Necessário se quiser testar o envio de `hello_world` diretamente do webhook.

---

### 🟣 4. Expondo o servidor com ngrok

1. Configure seu token pessoal do ngrok (somente na primeira execução):

ngrok config add-authtoken SEU_TOKEN_AQUI

2. Inicie o túnel HTTPS para expor a porta local 8000:

ngrok http 8000

3. Copie a URL HTTPS gerada e adicione `/webhook` ao final.  
   Exemplo: `https://1234abcd.ngrok.io/webhook`

4. Use essa URL como **Callback URL** no painel da Meta, junto com o **Verify Token** configurado.

---

### 🟣 5. Executando o `webhook.py`

Execute o servidor localmente:

python webhook.py

Agora, quando alguém enviar uma mensagem para o número configurado no WhatsApp Business, você verá o payload JSON aparecer no terminal.

> 💡 O webhook está pronto para receber notificações, e você pode combinar o envio de `hello_world` para testar a comunicação bidirecional.

---

### 6. Exemplo de Saída no Terminal

zapsender.py

```bash
(.venv) (base) joaopauloaramuni@MacBook-Pro-de-Joao Projeto ZapSender % python zapsender.py
✅ Template 'hello_world' enviado com sucesso!
```

webhook.py

```bash
(.venv) (base) joaopauloaramuni@MacBook-Pro-de-Joao Projeto ZapSender % python webhook.py
Servidor iniciado!
✅ Hello World enviado para 5531980402103
✅ Pergunta com botões enviada para 5531980402103
INFO:     Started server process [82605]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

# Recebimento de payloads de status de mensagens
📩 Payload recebido: {... 'status': 'read', ...}
Status de mensagem recebido (entregue, lido, etc.). Ignorando.

# Recebimento de interação com botão
📩 Payload recebido: {... 'button_reply': {'id': 'opcao_otima', 'title': 'Ótima'}}...
📌 553180402103 clicou na opção: Ótima
✅ Mensagem de texto enviada para 553180402103

# Recebimento de mensagem de texto
📩 Payload recebido: {... 'text': {'body': 'Oi'}}...
Mensagem recebida de 553180402103: Oi
✅ Mensagem de texto enviada para 553180402103

# Recebimento de nota do usuário
📩 Payload recebido: {... 'text': {'body': '10'}}...
⭐️ Nota recebida de 553180402103: 10
✅ Mensagem de texto enviada para 553180402103
```

### Exemplo de requisição cURL (Formato E.164)

Esta é a requisição HTTP pura que o código Python está executando (com placeholders):

```bash
curl -i -X POST \
  https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'Content-Type: application/json' \
  -d '{ "messaging_product": "whatsapp", "to": "{numero_destino}", "type": "template", "template": { "name": "hello_world", "language": { "code": "en_US" } } }'
```

---

## 📚 Documentação e Links Úteis

| Recurso | Descrição | Link |
| :--- | :--- | :--- |
| **Meta Apps** | Portal para gerenciar seus aplicativos e configurações. | https://developers.facebook.com/apps/ |
| **Gerenciador de Templates** | Onde você cria e gerencia todos os seus modelos de mensagem. | https://business.facebook.com/latest/whatsapp_manager/message_templates |
| **Guia de Introdução** | Documentação oficial para configurar a Cloud API. | https://developers.facebook.com/docs/whatsapp/cloud-api/get-started |
| **Guia de Envio** | Detalhes sobre o envio de diferentes tipos de mensagens. | https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages |
| **Webhooks** | Documentação oficial sobre como configurar Webhooks para receber mensagens e eventos. | https://developers.facebook.com/docs/whatsapp/cloud-api/guides/webhooks |
| **ngrok** | Ferramenta para expor o servidor local à internet via URL HTTPS, usada para testes de webhook. | https://ngrok.com/ |
| **ngrok Auth Token** | Página para obter o token de autenticação necessário para configurar ngrok. | https://dashboard.ngrok.com/get-started/your-authtoken |
| **FastAPI Docs** | Documentação oficial do FastAPI, usada para criar servidores web e acessar a interface `/docs`. | https://fastapi.tiangolo.com/ |

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests. 

Agradecimentos especiais pelas contribuições

- :octocat: GitHub: [João Vitor Santana](https://github.com/JoaoSantanaLopes)  
- ☁️ Portfólio: [joao-santana.vercel.app](https://joao-santana.vercel.app/)  

Projeto desenvolvido durante as **Oficinas do DevLabs** para o curso de **Engenharia de Software** da **PUC Minas**.

---

## 🧾 Licença

Este projeto é disponibilizado sob a licença **MIT**.
