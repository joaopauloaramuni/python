# interface.py
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar

# Cores do YouTube
bg_color = "#282828"
fg_color = "#FFFFFF"
button_color = "#FF0000"


def create_interface(start_download):
    """Cria e exibe a interface da aplicação."""

    def download_handler():
        url = url_entry.get()
        if not url:
            messagebox.showwarning("Aviso", "Por favor, insira uma URL.")
            return
        download_button.config(text="Baixando...", state=tk.DISABLED)
        status_label.config(text="Baixando...")
        start_download(url, update_progress, reset_ui)

    def update_progress(value, text):
        """Atualiza a barra e o texto de progresso."""
        progress_bar["value"] = value
        progress_label.config(text=text)

    def reset_ui():
        """Reinicia a interface após o download."""
        download_button.config(text="Baixar Vídeo", state=tk.NORMAL)
        status_label.config(text="")
        progress_bar["value"] = 0
        progress_label.config(text="0%")

    # Configuração da janela
    window = tk.Tk()
    window.title("YouTube Video Downloader")
    window.geometry("400x250")
    window.configure(bg=bg_color)

    # Interface
    tk.Label(
        window, text="Insira a URL do vídeo do YouTube:", bg=bg_color, fg=fg_color
    ).pack(pady=10)
    url_entry = tk.Entry(window, width=50)
    url_entry.pack(pady=5)

    progress_bar = Progressbar(
        window, orient="horizontal", length=300, mode="determinate"
    )
    progress_bar.pack(pady=10)

    progress_label = tk.Label(window, text="0%", bg=bg_color, fg=fg_color)
    progress_label.pack(pady=5)

    status_label = tk.Label(window, text="", bg=bg_color, fg=fg_color)
    status_label.pack(pady=5)

    download_button = tk.Button(
        window,
        text="Baixar Vídeo",
        command=download_handler,
        bg=button_color,
        fg=fg_color,
    )
    download_button.pack(pady=20)

    # Execução da interfaces
    window.mainloop()


# Executa a interface se este arquivo for chamado diretamente
if __name__ == "__main__":
    from app import start_download

    create_interface(start_download)
