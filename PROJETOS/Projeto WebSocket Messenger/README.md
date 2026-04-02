# Projeto WebSocket Messenger 💬

Projeto em Python para comunicação em tempo real utilizando **WebSockets** com interface gráfica em **Tkinter**.

---

## 🔎 O que é WebSocket?

WebSocket é um protocolo de comunicação que permite **conexão bidirecional persistente** entre cliente e servidor.

### 🧠 Conceito principal

Diferente do HTTP tradicional: - Comunicação contínua (sem múltiplas requisições) - Baixa latência - Ideal para aplicações em tempo real (chat, jogos, dashboards)

---

## 🖼️ Capturas de Tela

| <img src="https://joaopauloaramuni.github.io/python-imgs/WebSocketMessenger/imgs/ChatWebSocket.png" alt="ChatWebSocket" width="800"/> |
|:-----------------:|
| ChatWebSocket.png |

---

## ⚙️ Como funciona?

O projeto possui três partes:

-   **Servidor (`chat_server.py`)**
    -   Gerencia conexões
    -   Faz broadcast das mensagens
    -   Controla entrada/saída de usuários
-   **Cliente (`client.py`)**
    -   Conecta ao servidor via WebSocket
    -   Envia e recebe mensagens
-   **Interface (`gui.py`)**
    -   Interface gráfica com Tkinter
    -   Interação do usuário

---

## 🚀 Funcionalidades

-   Chat em tempo real
-   Múltiplos usuários na mesma rede
-   Identificação por nickname
-   Notificação de entrada e saída
-   Interface gráfica simples
-   Tratamento de erro de conexão

---

## 🧰 Dependências

``` bash
pip install websockets
```

Tkinter já vem instalado por padrão no Python (na maioria dos sistemas).

---

## 🐍 Ambiente Virtual

### Criar ambiente:

``` bash
python3 -m venv .venv
```

### Ativar ambiente:

**macOS/Linux**

``` bash
source .venv/bin/activate
```

**Windows**

``` bash
.venv\Scripts\activate
```

---

## ▶️ Execução

### 1. Iniciar o servidor

``` bash
python chat_server.py
```

Saída esperada:

    Servidor rodando em ws://0.0.0.0:8765

---

### 2. Iniciar os clientes

Abra **dois terminais diferentes** e execute:

``` bash
python gui.py
```

Digite o Nickname: João  
Digite o IP do servidor: (ex: 192.168.0.13)

---

## 🌐 Como descobrir o IP local

Para conectar os clientes ao servidor, você precisa do **IP local da máquina que está rodando o servidor**.

---

### 🪟 Windows

Abra o Prompt de Comando e execute:

```bash
ipconfig
```

Procure por:

```bash
IPv4 Address . . . . . . . . . . : 192.168.x.x
```

---

### 🐧 Linux

Abra o terminal e execute:

```bash
ip a
```

ou:

```bash
ifconfig
```

Procure por:

```bash
inet 192.168.x.x
```

---

### 🍎 macOS

Abra o terminal e execute:

```bash
ipconfig getifaddr en0
```

Se não funcionar, tente:

```bash
ifconfig
```

Procure por:

```bash
inet 192.168.x.x
```

---

### ⚠️ Importante

- Use um IP no formato:
  ```bash
  192.168.x.x ou 10.x.x.x
  ```

- **Não use:**
  - `127.0.0.1` (localhost)
  - `169.x.x.x` (problema de rede)

- Todos os dispositivos devem estar na **mesma rede (Wi-Fi ou cabo)**.

---

## 💬 Simulação de chat

Para simular:

1.  Abra **1 terminal para o servidor**
2.  Abra **2 terminais para clientes**
3.  Conecte ambos ao mesmo IP
4.  Envie mensagens entre eles

---

## 📊 Exemplo de uso

    🔵 Henrique entrou no chat
    🔵 João entrou no chat
    
    Henrique: Oi João!
    João: Olá Henrique!
    
    🔴 João saiu do chat
    🔴 Henrique saiu do chat

---

## 🔗 Documentação e links úteis

-   https://docs.python.org/3/library/tkinter.html
-   https://websockets.readthedocs.io/
-   https://github.com/python-websockets/websockets

---

## 📜 Licença

Este projeto está licenciado sob a MIT License.
