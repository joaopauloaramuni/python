import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from yt_dlp import YoutubeDL
import threading  # Importa o módulo threading

# Cores do YouTube
bg_color = "#282828"  # Fundo preto
fg_color = "#FFFFFF"  # Texto branco
button_color = "#FF0000"  # Botão vermelho


def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Aviso", "Por favor, insira uma URL.")
        return

    # Muda o texto do botão e desabilita enquanto baixa
    download_button.config(text="Baixando...", state=tk.DISABLED)
    status_label.config(text="Baixando...")

    threading.Thread(target=run_downloader, args=(url,)).start()


def run_downloader(url):
    ydl_opts = {
        "format": "bestvideo[height<=1080]+bestaudio/best",  # Prioriza 1080p, caindo para a melhor disponível
        "outtmpl": "videos/%(title)s.%(ext)s",  # Salva o vídeo com o título original
        "merge_output_format": "mp4",  # Garante que o vídeo e áudio estejam em MP4
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            window.after(100, lambda: update_progress(100, "100%"))
            messagebox.showinfo(
                "Sucesso", f"Download concluído!\nTítulo: {info.get('title')}"
            )
    except Exception as ex:
        window.after(
            100,
            lambda ex=ex: messagebox.showerror(
                "Erro", f"Ocorreu um erro ao baixar o vídeo: {ex}"
            ),
        )
    finally:
        # Reinicia o botão e o rótulo de status após completar o download
        window.after(100, reset_ui)


def progress_hook(d):
    if d["status"] == "downloading":
        p = d["_percent_str"].strip().strip("%")
        try:
            percent = float(p)
            window.after(100, lambda: update_progress(percent, f"{percent:.2f}%"))
        except ValueError:
            print(f"Erro ao converter {p} para float")
    elif d["status"] == "finished":
        window.after(100, lambda: update_progress(100, "100%"))


def animate_progress(value):
    current_value = progress_bar["value"]
    if current_value < value:
        progress_bar["value"] = current_value + 1
        progress_label.config(text=f"{current_value + 1:.2f}%")
        window.after(10, lambda: animate_progress(value))
    else:
        progress_label.config(text=f"{value:.2f}%")


def update_progress(value, text):
    progress_bar["value"] = value
    progress_label.config(text=text)


def reset_ui():
    download_button.config(text="Baixar Vídeo", state=tk.NORMAL)
    status_label.config(text="")
    progress_bar["value"] = 0
    progress_label.config(text="0%")


# Configuração da janela
window = tk.Tk()
window.title("YouTube Video Downloader")
window.geometry("400x250")
window.configure(bg=bg_color)  # Cor de fundo

# Rótulo e entrada de URL
tk.Label(
    window, text="Insira a URL do vídeo do YouTube:", bg=bg_color, fg=fg_color
).pack(pady=10)
url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=5)

# Barra de progresso
progress_bar = Progressbar(window, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

# Rótulo da porcentagem
progress_label = tk.Label(window, text="0%", bg=bg_color, fg=fg_color)
progress_label.pack(pady=5)

# Rótulo de status
status_label = tk.Label(window, text="", bg=bg_color, fg=fg_color)
status_label.pack(pady=5)

# Botão de download
download_button = tk.Button(
    window, text="Baixar Vídeo", command=download_video, bg=button_color, fg=fg_color
)
download_button.pack(pady=20)

# Execução da interface
window.mainloop()