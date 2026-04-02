## 💻 Exercício: Implementar “Usuário está digitando...” em tempo real

### 🎯 Objetivo

Modificar o projeto **WebSocket Messenger** para exibir, em tempo real, quando um usuário está digitando:

```
João está digitando...
```

---

## 📋 Descrição

Atualmente, o chat apenas envia mensagens completas.  
Sua tarefa é implementar um sistema de **evento de digitação** que:

- Detecta quando o usuário começa a digitar
- Notifica os outros clientes conectados
- Exibe um indicador visual na interface
- Remove o indicador após alguns segundos de inatividade

---

## 🧩 Requisitos

- Não quebrar o funcionamento atual do chat
- Implementar comunicação em tempo real
- Não exibir “você está digitando...” para o próprio usuário
- Evitar envio excessivo de eventos (spam)

---

## 💡 Dicas importantes

### 🔹 1. Detectar digitação no Tkinter

Você pode usar eventos do teclado:

```
self.msg_entry.bind("<Key>", callback)
```

👉 Isso dispara sempre que o usuário pressiona uma tecla.

---

### 🔹 2. Criar um tipo especial de mensagem

Diferencie mensagens normais de eventos:

Exemplo:

```
__typing__:João
```

👉 Assim o servidor consegue identificar facilmente.

---

### 🔹 3. Alterar o cliente (envio)

Ao detectar digitação:

- Envie um evento ao servidor
- Não envie mensagem vazia
- Considere usar um “controle” para não enviar a cada tecla

💡 Dica: use uma variável para controlar tempo:

```
if not self.typing:
    enviar_evento()
    self.typing = True
```

---

### 🔹 4. Usar debounce (evitar spam)

Evite enviar eventos a cada tecla pressionada.

💡 Estratégia:

- Envie o evento apenas se passou um tempo desde o último envio
- Use `after()` do Tkinter

Exemplo de ideia:

```
self.root.after(1000, parar_de_digitar)
```

---

### 🔹 5. Alterar o servidor

No servidor:

- Detecte mensagens de digitação
- Faça broadcast para outros usuários
- Não tratar como mensagem normal

💡 Dica:

```
if mensagem.startswith("__typing__"):
    broadcast(...)
```

---

### 🔹 6. Alterar a interface (GUI)

Adicione um indicador visual:

- Um `Label` abaixo do chat

Exemplo:

```
self.typing_label = tk.Label(root, text="", fg="gray")
```

---

### 🔹 7. Atualizar a UI ao receber evento

Quando receber:

```
__typing__:João
```

Você deve:

- Mostrar “João está digitando...”
- Limpar após alguns segundos

💡 Dica:

```
self.root.after(2000, limpar_label)
```

---

### 🔹 8. Evitar mostrar para si mesmo

Você pode:

- Comparar o nickname recebido com o seu
- Ignorar se for o mesmo

---

## ⭐ Desafios extras (opcional)

- Mostrar múltiplos usuários digitando ao mesmo tempo
- Criar animação (ex: “digitando...” com pontos)
- Melhorar UX (ex: desaparecer suavemente)
- Usar JSON ao invés de string simples

---

## 🧠 Resultado esperado

Quando um usuário começa a digitar:

```
Maria está digitando...
```

E após parar:

- O texto desaparece automaticamente

---

## 🚀 Entrega

- Código funcional
- Explicação breve da solução
- (Opcional) melhorias implementadas

---

## 🏁 Boa prática

Separe responsabilidades:

- Cliente → envia eventos
- Servidor → distribui eventos
- GUI → exibe estado

---

Boa implementação! 👨‍🏫🔥