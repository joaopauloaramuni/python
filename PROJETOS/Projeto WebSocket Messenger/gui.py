import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox
import threading
import time
from client import ChatClient

class ChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Projeto WebSocket Messenger")
        self.root.geometry("600x450")
        
        self.chat_area = scrolledtext.ScrolledText(root, state='disabled')
        self.chat_area.pack(padx=10, pady=10)

        self.typing_label = tk.Label(root, text="", fg="gray")
        self.typing_label.pack()
        
        self.msg_entry = tk.Entry(root)
        self.msg_entry.pack(padx=10, pady=5, fill="x")
        self.msg_entry.bind("<Return>", self.send_msg)
        self.msg_entry.bind("<Key>", self.on_typing)
        
        self.send_button = tk.Button(root, text="Enviar", command=self.send_msg)
        self.send_button.pack(padx=10, pady=5, fill="x")

        self.last_typing = 0
        self.typing_users = {}
        
        # inputs iniciais
        nickname = simpledialog.askstring(
            "Nickname",
            "Digite seu nome:",
            initialvalue="",
            parent=self.root
        )
        server_ip = simpledialog.askstring(
            "Servidor", 
            "IP do servidor:", 
            initialvalue="10.250.32.133",
            parent=self.root
        )

        uri = f"ws://{server_ip}:8765"

        # cria client
        self.client = ChatClient(uri, nickname, self.on_message, self.on_error)

        # roda client em thread separada
        threading.Thread(target=self.client.start, daemon=True).start()
        
        self.update_typing_label()

    def on_message(self, msg):
        if msg.startswith("__typing__:"):
            nome = msg.split(":")[1]
            self.typing_users[nome] = time.time()
            return

        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, msg + "\n")
        self.chat_area.configure(state='disabled')
        self.chat_area.yview(tk.END)

    def update_typing_label(self):
        now = time.time()

        self.typing_users = {
            nome: t for nome, t in self.typing_users.items()
            if now - t < 2
        }

        ativos = list(self.typing_users.keys())

        if len(ativos) == 1:
            texto = f"{ativos[0]} está digitando..."
        elif len(ativos) > 1:
            texto = f"{', '.join(ativos)} estão digitando..."
        else:
            texto = ""

        self.typing_label.config(text=texto)

        self.root.after(500, self.update_typing_label)
    
    def on_typing(self, event=None):
        now = time.time()
        if now - self.last_typing > 1:
            self.client.send_typing()
            self.last_typing = now

    def on_error(self, error_msg):
        def show():
            messagebox.showerror(
                "Erro",
                "Não foi possível conectar ao servidor."
            )
            self.root.quit()

        self.root.after(0, show)

    def send_msg(self, event=None):
        msg = self.msg_entry.get()
        self.msg_entry.delete(0, tk.END)
        self.client.send(msg)

# Execução
root = tk.Tk()
app = ChatGUI(root)
root.mainloop()
