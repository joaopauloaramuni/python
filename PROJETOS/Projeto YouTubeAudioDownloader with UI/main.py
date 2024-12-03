from yt_dlp import YoutubeDL
from tkinter import messagebox
import threading
from interface import create_interface

# Configuração de opções de download do YouTube
ydl_opts = {
    "format": "bestaudio/best",  # Escolhe o melhor áudio disponível
    "outtmpl": "audios/%(title)s.%(ext)s",  # Salva o áudio com o título original
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",  # Converte para MP3
        },
    ],
    "postprocessor_args": ["-q:a", "0"],  # Preserva a qualidade original ao máximo
    "prefer_ffmpeg": True,  # Garante que o FFmpeg será usado
}


def download_audio(url, update_status, reset_ui):
    """Função para fazer o download do áudio."""
    try:
        update_status("Iniciando o download...", "green")
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            update_status(f"Download concluído: {info.get('title', 'Desconhecido')}", "green")
            messagebox.showinfo("Sucesso", f"Download concluído!\nTítulo: {info.get('title')}")
    except Exception as ex:
        update_status(f"Erro: {str(ex)}", "red")
        messagebox.showerror("Erro", f"Ocorreu um erro ao baixar o áudio: {ex}")
    finally:
        reset_ui()


def start_download(url, update_status, reset_ui):
    """Inicia o download em uma nova thread."""
    threading.Thread(
        target=download_audio, args=(url, update_status, reset_ui), daemon=True
    ).start()


if __name__ == "__main__":
    create_interface(start_download)
