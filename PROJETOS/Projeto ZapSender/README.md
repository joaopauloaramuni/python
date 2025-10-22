# 🤖 ZapSender: Envio de Mensagens via WhatsApp Cloud API

Este projeto em Python demonstra como enviar mensagens de template do WhatsApp utilizando a **Cloud API da Meta**, a maneira oficial e escalável de automatizar a comunicação.

---

## 💡 O que é este Projeto?

O **ZapSender** é um script Python (`zapsender.py`) simples, mas funcional, projetado para interagir com a API de Nuvem do WhatsApp (Meta for Developers). Ele encapsula a lógica necessária para construir o payload JSON e enviar requisições HTTP POST para o endpoint da Meta, permitindo o envio programático de mensagens pré-aprovadas (Templates) para números específicos.

---

## 📘 Meta for Developers e a Cloud API

### O que é Meta for Developers?
É a plataforma que fornece as ferramentas, APIs e documentação necessárias para desenvolvedores criarem aplicativos que se integram aos produtos da Meta (Facebook, Instagram, WhatsApp). Para usar a API do WhatsApp, é necessário criar um aplicativo aqui.

## 🚀 Passo a passo para criar o App no Meta for Developers

Antes de enviar mensagens com a **Cloud API do WhatsApp**, é necessário **criar um aplicativo** no **Meta for Developers** e vinculá-lo a uma **Conta Comercial (Business Portfolio)**.  
Esse vínculo é essencial para que o produto **WhatsApp** esteja disponível no seu app.

---

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
Templates (ou Modelos de Mensagem) são mensagens pré-aprovadas que devem ser usadas para iniciar conversas ou enviar notificações fora da janela de 24 horas de atendimento. Para usar a Cloud API, a primeira mensagem para um novo contato deve ser um Template, como o `hello_world` usado neste projeto.

### Passo a passo para criar um Template
1.  Acesse o **Gerenciador do WhatsApp** através do link: [Gerenciador de Templates](https://business.facebook.com/latest/whatsapp_manager/message_templates).
2.  Certifique-se de que está na conta de Negócios correta.
3.  Clique em **"Criar Modelo de Mensagem"**.
4.  Defina o **Nome** (ex.: `hello_world`), **Categoria** (ex.: Utilidade) e **Idioma**.
5.  Crie o corpo da mensagem.
6.  Envie o template para aprovação (em ambientes de teste, templates básicos são aprovados instantaneamente).

---

## ⚙️ Explicação do Código Python

O script `zapsender.py` é dividido em funções claras para gerenciamento do envio:

| Assinatura da Função | Descrição |
| :--- | :--- |
| `criar_payload_template(nome_template: str, codigo_idioma: str, numero_destino: str) -> dict` | Responsável por montar o corpo JSON da requisição, garantindo que o nome do template, o código de idioma e o número de destino estejam no formato exigido pela API da Meta. |
| `enviar_requisicao(payload: dict) -> dict` | Cuida da comunicação HTTP. Esta função realiza a chamada `POST` para a API da Meta, incluindo o **ACCESS_TOKEN** nos *headers* de autorização e o payload JSON no corpo da requisição. |
| `enviar_template(numero_destino: str, nome_template: str, codigo_idioma: str)` | É a função de orquestração. Ela chama `criar_payload_template` e `enviar_requisicao`, e então verifica a resposta da API, exibindo uma mensagem de sucesso ou um erro no terminal. |

---

## 🛠️ Pré-requisitos

- **Python 3.7+** instalado.
- **ACCESS_TOKEN**: Token de acesso da Meta for Developers.
- **PHONE_NUMBER_ID**: O ID do número de telefone (sandbox ou oficial) usado para enviar a mensagem.

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
pip install requests
```

---

## ⚙️ Execução

### 1. Configuração

No arquivo `zapsender.py`, substitua os *placeholders* na seção `CONFIGURAÇÕES` pelos seus valores obtidos na plataforma Meta Developers:

- **`ACCESS_TOKEN`**: Seu token de acesso de usuário (deve ser tratado com segurança em produção).
- **`PHONE_NUMBER_ID`**: O ID do número de telefone de teste/produção.

### 2. Comando Principal

Execute o script principal:

```bash
python zapsender.py
```

### 3. Exemplo de Saída no Terminal

```bash
(.venv) (base) joaopauloaramuni@MacBook-Pro-de-Joao Projeto ZapSender % python zapsender.py
✅ Template 'hello_world' enviado com sucesso!
```

### Exemplo de requisição cURL (Formato E.164)

Esta é a requisição HTTP pura que o código Python está executando (com placeholders):

```bash
curl -i -X POST \
  https://graph.facebook.com/v24.0/{PHONE_NUMBER_ID}/messages \
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

---

## 🧾 Licença

Este projeto é disponibilizado sob a licença **MIT**.
