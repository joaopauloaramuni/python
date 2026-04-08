# 💻 Exercício: Implementar “Usuário está digitando...” em tempo real

## 🎯 Objetivo

Modificar o projeto **WebSocket Messenger** para exibir, em tempo real, quando um usuário está digitando:

```
João está digitando...
```

---

## 📋 Descrição

Atualmente, o chat apenas envia mensagens completas.  
Sua tarefa é implementar um sistema de **evento de digitação** que:

- Detecta quando o usuário está digitando  
- Notifica os outros clientes conectados  
- Exibe um indicador visual na interface  
- Remove automaticamente o indicador após alguns segundos  

---

## 🧩 Requisitos

- Não quebrar o funcionamento atual do chat  
- Implementar comunicação em tempo real  
- Não exibir “você está digitando...” para o próprio usuário  
- Evitar envio excessivo de eventos (spam)  
- Suportar múltiplos usuários digitando ao mesmo tempo  

---

## 💡 Dicas importantes

### 🔹 1. Detectar digitação no Tkinter

Use eventos de teclado no campo de entrada:

```
self.msg_entry.bind("<Key>", self.on_typing)
```

👉 Isso dispara sempre que o usuário pressiona uma tecla.

---

### 🔹 2. Criar um tipo especial de mensagem

Utilize uma mensagem simples para representar o evento de digitação:

```
__typing__
```

E no servidor, associe ao nome do usuário:

```
__typing__:João
```

---

### 🔹 3. Alterar o cliente (envio)

Ao detectar digitação:

- Envie o evento `__typing__`
- Use o evento de teclado para disparar o envio

Exemplo:

```
self.msg_entry.bind("<Key>", self.on_typing)
```

E na função:

```
def on_typing(self, event=None):
    self.client.send_typing()
```

👉 Isso envia um evento sempre que o usuário pressiona uma tecla.

💡 Observação:

- O controle de tempo (para evitar spam e remover o status)  
- É feito no **lado da interface (recebimento)** usando `time.time()`  

---

### 🔹 4. Evitar spam (debounce)

Não envie eventos continuamente.

Use uma variável de controle de tempo:

- Envie no máximo 1 evento por segundo
- Isso reduz carga no servidor e melhora desempenho

---

### 🔹 5. Alterar o servidor

No servidor:

- Detecte mensagens `__typing__`
- Faça broadcast para os outros clientes

Exemplo:

```
if mensagem == "__typing__":
    await broadcast(f"__typing__:{nome}")
else:
    await broadcast(f"{nome}: {mensagem}")
```

---

### 🔹 6. Alterar a interface (GUI)

Adicione um indicador visual:

```
self.typing_label = tk.Label(root, text="", fg="gray")
```

👉 Esse label exibirá quem está digitando.

---

### 🔹 7. Atualizar a UI ao receber evento

Quando receber:

```
__typing__:João
```

Armazene o tempo do evento:

```
self.typing_users[nome] = time.time()
```

---

### 🔹 8. Remover automaticamente (timeout)

Crie uma função que roda continuamente usando `after`:

```
self.root.after(500, self.update_typing_label)
```

Nela:

- Remova usuários que não digitam há alguns segundos (ex: 3s)
- Atualize o texto do label

Exemplo:

```
ativos = [
    nome for nome, t in self.typing_users.items()
    if time.time() - t < 3
]
```

---

### 🔹 9. Atualizar texto dinamicamente

Trate singular e plural:

```
if len(ativos) == 1:
    texto = f"{ativos[0]} está digitando..."
elif len(ativos) > 1:
    texto = f"{', '.join(ativos)} estão digitando..."
else:
    texto = ""
```

---

### 🔹 10. Evitar mostrar para si mesmo

Você pode ignorar o próprio usuário:

```
if nome == self.nickname:
    return
```

---

## ⭐ Desafios extras (opcional)

- Mostrar múltiplos usuários digitando simultaneamente  
- Criar animação (ex: “digitando...”)  
- Melhorar UX (ex: fade out)  
- Usar JSON ao invés de string simples  
- Implementar evento “parou de digitar”  

---

## 🧠 Resultado esperado

Quando um usuário começa a digitar:

```
Maria está digitando...
```

Após alguns segundos sem digitar:

- O indicador desaparece automaticamente  

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
