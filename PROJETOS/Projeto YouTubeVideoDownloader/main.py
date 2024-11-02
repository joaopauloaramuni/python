from yt_dlp import YoutubeDL

# URL do vídeo
url = 'https://www.youtube.com/watch?v=LXb3EKWsInQ'

# Configurações de download
ydl_opts = {
    "format": "bestvideo[height<=1080]+bestaudio/best",  # Prioriza 1080p, caindo para a melhor disponível
    "outtmpl": "videos/%(title)s.%(ext)s",  # Salva o vídeo com o título original
    "merge_output_format": "mp4",  # Garante que o vídeo e áudio estejam em MP4
}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)  # Baixa o vídeo
    print("Título do vídeo:", info.get('title'))
    print("Download concluído!")
