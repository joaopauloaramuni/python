# YouTube Audio Downloader

Este é um projeto simples para baixar o áudio de vídeos do YouTube utilizando a biblioteca `yt_dlp`, uma ferramenta poderosa que facilita o download de conteúdo na melhor qualidade disponível. O áudio é extraído, convertido para MP3 e salvo com o título original do vídeo.

## Pré-requisitos

Certifique-se de ter o Python instalado (versão 3.6 ou superior é recomendada).

## Dependências

Este projeto requer a instalação das seguintes dependências:

**yt_dlp**: Para gerenciar o download de áudios.

```bash
pip install yt-dlp
```

O `yt_dlp` é uma ferramenta poderosa para baixar vídeos e áudios de várias plataformas, como YouTube, Vimeo, Twitch, entre outras. Ele é uma ramificação aprimorada do `youtube-dl`, com maior suporte e novas funcionalidades.

### Principais funcionalidades do `yt_dlp`:

- Download de alta qualidade: Escolha o melhor formato disponível para vídeo ou áudio.
- Suporte a várias plataformas: Compatível com centenas de sites de streaming e redes sociais.
- Filtragem de formatos: Permite selecionar apenas áudio, apenas vídeo ou combinações específicas.
- Customização: Oferece muitas opções de configuração para personalizar o download.
- Integração com FFmpeg: Realiza conversões e edições avançadas de áudio e vídeo.

### Exemplo de uso básico:

Baixando apenas o áudio de um vídeo:

    yt-dlp -x --audio-format mp3 https://www.youtube.com/watch?v=EXEMPLO

- `-x`: Extrai apenas o áudio.
- `--audio-format mp3`: Converte o áudio para o formato MP3.

Baixando o melhor formato de vídeo e áudio:

    yt-dlp -f best https://www.youtube.com/watch?v=EXEMPLO

- `-f best`: Seleciona o melhor formato disponível.

Para mais opções, consulte a documentação oficial: https://github.com/yt-dlp/yt-dlp.

---

**FFmpeg**: Necessário para realizar a conversão e manipulação de arquivos de áudio.

### Instalação do FFmpeg

- **macOS (usando Homebrew)**

  ```bash
  brew install ffmpeg
  ```

- **Ubuntu/Debian (Linux)**

  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

- **Windows**

  Para Windows, o processo é um pouco diferente:

  1. Acesse o [site oficial do FFmpeg](https://ffmpeg.org/download.html) e baixe a versão mais recente para Windows.
  2. Extraia o arquivo baixado em uma pasta de fácil acesso.
  3. Adicione o caminho da pasta `bin` (onde está o executável `ffmpeg.exe`) à variável de ambiente **PATH**:
     - Abra o menu Iniciar e procure por **Variáveis de Ambiente**.
     - Edite a variável **Path** e adicione o caminho completo até a pasta `bin` do `ffmpeg`.
  5. Verifique a instalação no terminal (Prompt de Comando ou PowerShell) com:

     ```bash
     ffmpeg -version
     ```

O FFmpeg é uma ferramenta robusta para processar arquivos de multimídia. Ele é amplamente utilizado para converter, editar, e manipular vídeos e áudios em diversos formatos.

### Principais funcionalidades do `FFmpeg`:

- Conversão de formatos: Transforme arquivos para praticamente qualquer formato de áudio e vídeo.
- Edição de arquivos: Corte, junte, ou aplique filtros em arquivos multimídia.
- Extração de áudio: Extraia áudio de vídeos ou remova faixas específicas.
- Configuração de qualidade: Permite ajustar taxas de bits, resolução e outros parâmetros.

### Exemplo de uso básico:

Converter um arquivo para MP3:

  ```bash
  ffmpeg -i input.mp4 -q:a 0 output.mp3
  ```

- `-i input.mp4`: Especifica o arquivo de entrada.
- `-q:a 0`: Define a qualidade do áudio (0 é a melhor qualidade).
- `output.mp3`: Especifica o nome do arquivo de saída.

Cortar um trecho de um vídeo (exemplo dos primeiros 30 segundos):

  ```bash
  ffmpeg -i input.mp4 -ss 00:00:00 -t 00:00:30 -c copy output.mp4
  ```

- `-ss 00:00:00`: Define o ponto inicial (neste caso, o início do vídeo).
- `-t 00:00:30`: Define a duração do clipe.
- `-c copy`: Copia os fluxos sem reprocessamento.

Para mais detalhes, visite o site oficial do FFmpeg: https://ffmpeg.org.

---

## Configurações de qualidade do áudio

A qualidade do áudio é configurada utilizando o parâmetro `-q:a` (ou `-aq`). Para o codec MP3, os valores variam de **0** (melhor qualidade) a **9** (qualidade mais baixa).

### Relação entre qualidade e taxa de bits aproximada:

| Valor (`q`) | Taxa de Bits Aproximada (kbps) | Qualidade       |
|-------------|--------------------------------|-----------------|
| **0**       | 240-320                       | Excelente       |
| **2**       | 170-210                       | Boa (padrão)    |
| **4**       | 140-180                       | Média           |
| **6**       | 100-130                       | Baixa           |
| **9**       | ~65                           | Muito baixa     |

## Uso

1. Clone este repositório ou copie o código para um arquivo `.py`.
2. Configure a URL do vídeo no código e execute o script para baixar o áudio.

## Código

Abaixo está o código principal do projeto:

```python
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
```

## Ambiente virtual

É recomendável usar um ambiente virtual para gerenciar as dependências. Siga os passos abaixo:

1. Crie um ambiente virtual:

    ```bash
    python3 -m venv .venv
    ```

2. Ative o ambiente virtual:
   - No macOS/Linux:

    ```bash
    source .venv/bin/activate
    ```

   - No Windows:

    ```bash
    .venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    pip install yt-dlp
    ```

## Observação

Para baixar áudios de outros vídeos, altere o valor da variável `url` no código.

## Licença

Este projeto é de código aberto e está licenciado sob a MIT License. Sinta-se livre para usá-lo e modificá-lo conforme necessário.
