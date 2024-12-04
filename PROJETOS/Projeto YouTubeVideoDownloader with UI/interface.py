import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar, Style

# Cores
bg_color = "#FFFFFF"  # Fundo branco
button_color = "#FF0000"  # Cor do botão
fg_color = "#333333"  # Cor do texto
highlight_color = "#007ACC"  # Cor para destaque (ex: status)
entry_bg_color = "#F9F9F9"  # Fundo mais sutil para o campo de entrada
entry_border_color = "#DDDDDD"  # Borda bem suave para o campo de entrada


def create_interface(start_download):
    """
    Cria a interface gráfica.

    :param start_download: Função para iniciar o download.
    """
    def download_handler():
        url = url_entry.get()
        if not url:
            messagebox.showwarning("Aviso", "Por favor, insira uma URL.")
            return
        download_button.config(text="Baixando...", state=tk.DISABLED)
        status_label.config(text="Status: Baixando...", fg=highlight_color)
        video_label.config(text=f"URL: {url}", fg=highlight_color)
        start_download(url, update_progress, reset_ui)

    def update_progress(value, text):
        progress_bar["value"] = value
        progress_label.config(text=text)

    def reset_ui():
        download_button.config(text="Baixar Vídeo", state=tk.NORMAL)
        status_label.config(
            text="Status: Aguardando...",
            fg=fg_color,
        )
        video_label.config(text="Aguardando URL...", fg="#666666")
        progress_bar["value"] = 0
        progress_label.config(text="0%")

    # Janela principal
    window = tk.Tk()
    window.title("YouTube Video Downloader")
    window.geometry("600x450")
    window.configure(bg=bg_color)

    # Estilo para a barra de progresso
    style = Style()
    style.theme_use("clam")
    style.configure(
        "Custom.Horizontal.TProgressbar",
        thickness=20,
        background=button_color,
        troughcolor=bg_color,
    )

    # Cabeçalho
    header_label = tk.Label(
        window,
        text="Baixe vídeos do YouTube",
        bg=bg_color,
        fg=fg_color,
        font=("Arial", 16, "bold"),
    )
    header_label.pack(pady=20)

    # Caixa para a URL
    url_entry_frame = tk.Frame(window, bg=bg_color)
    url_entry_frame.pack(pady=15)

    url_entry = tk.Entry(
        url_entry_frame,
        width=50,
        font=("Arial", 12),
        justify="center",
        bg=entry_bg_color,
        relief="solid",
        bd=1,
        highlightthickness=0,
    )
    url_entry.pack(padx=10, pady=10)

    # Borda bem sutil para o campo de entrada
    url_entry.config(
        borderwidth=1,
        highlightcolor=entry_border_color,
        highlightbackground=entry_border_color,
        relief="solid",
        fg="#666666",  # Texto de cor mais suave
    )

    # Status e progresso
    status_label = tk.Label(
        window,
        text="Status: Aguardando...",
        bg=bg_color,
        fg=fg_color,
        font=("Arial", 12),
    )
    status_label.pack(pady=10)

    video_label = tk.Label(
        window,
        text="Aguardando URL...",
        bg=bg_color,
        fg="#666666",
        font=("Arial", 10, "italic"),
        wraplength=450,
        justify="center",
    )
    video_label.pack(pady=10)

    # Botão de download
    download_button = tk.Button(
        window,
        text="Baixar Vídeo",
        command=download_handler,
        bg=button_color,
        fg=bg_color,
        font=("Arial", 12, "bold"),
        relief="flat",
        padx=50,
        pady=10,
    )
    download_button.pack(pady=15)

    # Barra de progresso
    progress_bar = Progressbar(
        window,
        orient="horizontal",
        length=500,
        mode="determinate",
        style="Custom.Horizontal.TProgressbar",
    )
    progress_bar.pack(pady=15)

    # Texto da barra de progresso
    progress_label = tk.Label(
        window,
        text="0%",
        bg=bg_color,
        fg=fg_color,
        font=("Arial", 12, "bold"),
    )
    progress_label.pack(pady=10)

    # Iniciar a interface
    window.mainloop()


if __name__ == "__main__":
    from app import start_download

    create_interface(start_download)
