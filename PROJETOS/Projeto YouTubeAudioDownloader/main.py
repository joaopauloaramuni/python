from yt_dlp import YoutubeDL

# URL do vídeo
url = 'https://www.youtube.com/watch?v=LXb3EKWsInQ'

# Configurações de download
ydl_opts = {
    "format": "bestaudio/best",  # Escolhe o melhor áudio disponível
    "outtmpl": "audios/%(title)s.%(ext)s",  # Salva o áudio com o título original
    "postprocessors": [{  
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",  # Converte para MP3
    }],
    "postprocessor_args": [
        "-q:a", "0"  # Preserva a qualidade original ao máximo
    ],
    "prefer_ffmpeg": True,  # Garante que o FFmpeg será usado
}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)  # Baixa somente o áudio
    print("Título do áudio:", info.get('title'))
    print("Download concluído!")