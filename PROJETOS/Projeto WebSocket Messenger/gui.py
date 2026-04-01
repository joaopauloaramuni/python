import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox
import threading
from client import ChatClient

class ChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Projeto WebSocket Messenger")
        self.root.geometry("600x430")
        
        self.chat_area = scrolledtext.ScrolledText(root, state='disabled')
        self.chat_area.pack(padx=10, pady=10)

        self.msg_entry = tk.Entry(root)
        self.msg_entry.pack(padx=10, pady=5, fill="x")
        self.msg_entry.bind("<Return>", self.send_msg)

        self.send_button = tk.Button(root, text="Enviar", command=self.send_msg)
        self.send_button.pack(padx=10, pady=5, fill="x")

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
            initialvalue="192.168.0.13",
            parent=self.root
        )

        uri = f"ws://{server_ip}:8765"

        # cria client
        self.client = ChatClient(uri, nickname, self.on_message, self.on_error)

        # roda client em thread separada
        threading.Thread(target=self.client.start, daemon=True).start()

    def on_message(self, msg):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, msg + "\n")
        self.chat_area.configure(state='disabled')
        self.chat_area.yview(tk.END)

    def on_error(self, error_msg):
        def show():
            messagebox.showerror(
                "Erro de conexão",
                "Não foi possível conectar ao servidor.\n\n"
                "Verifique se:\n"
                "- O servidor está rodando\n"
                "- O IP está correto\n"
                "- Estão na mesma rede"
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