import subprocess
import whisper
from deep_translator import GoogleTranslator


# Função para extrair áudio do arquivo de vídeo
def extract_audio(video_file):
    audio_file = "audio.wav"
    command = [
        "ffmpeg",
        "-i", video_file,
        "-vn",  # Sem vídeo
        "-acodec", "pcm_s16le",  # Codec de áudio sem perdas
        "-ar", "22050",  # Taxa de amostragem de 22.05 kHz
        "-ac", "1",  # Canal mono
        audio_file
    ]
    subprocess.run(command)
    return audio_file

# Função para gerar o arquivo .srt
def generate_srt(transcription_result, srt_filename, translate=False):
    subtitle_counter = 1
    with open(srt_filename, "w") as srt_file:
        for segment in transcription_result["segments"]:
            start_time = segment["start"]
            end_time = segment["end"]
            start_time_str = format_time(start_time)
            end_time_str = format_time(end_time)
            text = segment["text"]
            
            # Se a tradução for necessária, traduz o texto
            if translate:
                text = GoogleTranslator(source='en', target='pt').translate(text)
            
            # Escreve o texto e os tempos no arquivo .srt
            srt_file.write(f"{subtitle_counter}\n")
            srt_file.write(f"{start_time_str} --> {end_time_str}\n")
            srt_file.write(f"{text}\n\n")
            subtitle_counter += 1

# Função para formatar o tempo em segundos para o formato hh:mm:ss,SSS
def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    milliseconds = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{int(seconds):02},{milliseconds:03}"

# Usando Whisper para transcrever o áudio e gerar os arquivos .srt
def transcribe_audio(video_file):
    print(f"Iniciando a transcrição do vídeo: {video_file}")
    
    audio_file = extract_audio(video_file)
    print(f"Áudio extraído com sucesso para: {audio_file}")
    
    model = whisper.load_model("small")
    print("Modelo Whisper carregado com sucesso!")
    
    # Realizar a transcrição para o inglês
    print("Iniciando a transcrição do áudio para o inglês...")
    result = model.transcribe(audio_file, task="transcribe", language="en")
    print("Transcrição concluída!")

    # Gerar a legenda em inglês
    print("Gerando legenda em inglês...")
    generate_srt(result, srt_filename="english.srt", translate=False)
    print("Legenda em inglês gerada com sucesso!")

    # Gerar a legenda traduzida para o português
    print("Gerando legenda traduzida para o português...")
    generate_srt(result, srt_filename="portuguese.srt", translate=True)
    print("Legenda em português gerada com sucesso!")

# Transcrever o arquivo de vídeo e gerar as legendas em inglês e português
transcribe_audio("teste.mp4")
