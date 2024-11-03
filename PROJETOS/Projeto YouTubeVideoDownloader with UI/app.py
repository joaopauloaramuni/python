# app.py
from yt_dlp import YoutubeDL
from tkinter import messagebox
import threading
from interface import create_interface

# Configuração de opções de download do YouTube
ydl_opts = {
    "format": "bestvideo[height<=1080]+bestaudio/best",
    "outtmpl": "YoutubeVideoDownloader/videos/%(title)s.%(ext)s",
    "merge_output_format": "mp4",
}


def download_video(url, update_progress, reset_ui):
    """Função para fazer o download do vídeo em uma thread."""
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            update_progress(100, "100%")
            messagebox.showinfo(
                "Sucesso", f"Download concluído!\nTítulo: {info.get('title')}"
            )
    except Exception as ex:
        messagebox.showerror("Erro", f"Ocorreu um erro ao baixar o vídeo: {ex}")
    finally:
        reset_ui()


def start_download(url, update_progress, reset_ui):
    """Inicia o download em uma nova thread."""
    threading.Thread(
        target=download_video, args=(url, update_progress, reset_ui)
    ).start()


if __name__ == "__main__":
    create_interface(start_download)
