# Projeto Subs Generator with AI

O projeto **Subs Generator with AI** tem como objetivo utilizar inteligência artificial para transcrever e traduzir arquivos de áudio extraídos de vídeos em formato `.MKV` ou `.MP4` para legendas no formato `.srt` em inglês e em português. A transcrição e a tradução são realizadas utilizando, respectivamente, o modelo **Whisper** da OpenAI e a API **GoogleTranslator** do pacote `deep-translator`.

## Dependências

Este projeto foi desenvolvido utilizando Python 3.9.9 e PyTorch 1.10.1 para treinar e testar os modelos, mas o código base é compatível com versões do Python de 3.8 a 3.11 e versões recentes do PyTorch.

As dependências essenciais do projeto incluem:

1. **openai-whisper**: Para transcrição e tradução de áudio com o modelo Whisper da OpenAI.
2. **deep-translator**: Para tradução de texto com o Google Translator (para o português).
3. **ffmpeg**: Para extrair o áudio dos vídeos.

### Instalação das dependências

Para instalar as dependências necessárias, siga os passos abaixo:

1. **Instale o pacote `openai-whisper`** com o seguinte comando:

    ```bash
    pip install -U openai-whisper
    ```

    Alternativamente, você pode instalar a versão mais recente do repositório diretamente do GitHub:

    ```bash
    pip install git+https://github.com/openai/whisper.git
    ```

    Para atualizar o pacote para a versão mais recente, execute:

    ```bash
    pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
    ```

2. **Instale o pacote `deep-translator`** para utilizar o Google Translator na tradução das legendas:

    ```bash
    pip install deep-translator
    ```

3. **Instale o `ffmpeg`** no seu sistema para extrair o áudio dos vídeos. Você pode instalá-lo utilizando o gerenciador de pacotes correspondente ao seu sistema operacional:

    - No Ubuntu ou Debian:

    ```bash
    sudo apt update && sudo apt install ffmpeg
    ```

    - No Arch Linux:

    ```bash
    sudo pacman -S ffmpeg
    ```

    - No MacOS usando o Homebrew:

    ```bash
    brew install ffmpeg
    ```

    - No Windows com o Chocolatey:

    ```bash
    choco install ffmpeg
    ```

    - No Windows com o Scoop:

    ```bash
    scoop install ffmpeg
    ```

## Criando o Ambiente Virtual com `pyenv`

Para garantir que o seu projeto utilize a versão correta do Python, siga os passos abaixo:

1. **Instale a versão desejada do Python com o `pyenv`:**

Se você ainda não tiver a versão do Python instalada, use o comando abaixo para instalar a versão 3.9.9:

```bash
pyenv install 3.9.9
```

2. **Defina a versão global ou local do Python:**

Se você deseja usar o Python 3.9.9 globalmente em seu sistema:

```bash
pyenv global 3.9.9
```

Ou, para configurar a versão específica para o seu projeto (no diretório onde o código está):

```bash
pyenv local 3.9.9
```

3. **Crie o ambiente virtual usando o `python -m venv`:**

Agora, com o `pyenv` configurado para usar a versão do Python correta, crie o ambiente virtual:

```bash
python -m venv venv
```

4. **Ative o ambiente virtual:**

- **No macOS/Linux:**

```bash
source venv/bin/activate
```

- **No Windows:**

```bash
venv\Scripts\activate
```

5. **Atualize o `pip` e instale as dependências do projeto:**

Para garantir que você tenha a versão mais recente do `pip`, execute:

```bash
pip install --upgrade pip
```

Em seguida, instale todas as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Com isso, o ambiente estará configurado com a versão correta do Python e as dependências necessárias para rodar o projeto.

## Código

### extract_audio(video_file) 

Função para extrair áudio do arquivo MKV ou MP4.

### generate_srt(transcription_result, srt_filename, translate=False)

Função para gerar o arquivo `.srt` (primeiro em inglês, depois em português).

### format_time(seconds)

Função para formatar o tempo em segundos para o formato `hh:mm:ss,SSS`.

### transcribe_audio(video_file)

Função para transcrever o áudio e gerar o arquivo `.srt` da legenda.

### Explicação sobre os modelos Whisper: "tiny", "base", "small", "medium", "large" e "turbo"

O Whisper oferece diferentes modelos de transcrição e tradução de áudio, variando em tamanho, desempenho e precisão. Abaixo estão as principais características de cada modelo, para que você possa escolher o mais adequado às suas necessidades:

- **tiny**: O modelo mais leve e rápido, com apenas 39 milhões de parâmetros. Ele é adequado para tarefas simples e rápidas, quando a precisão não é crítica. Ele é ~10 vezes mais rápido que o modelo `large`, mas com menor capacidade de reconhecimento.

- **base**: Um modelo pequeno, com 74 milhões de parâmetros, que oferece um bom equilíbrio entre velocidade e precisão. É ideal quando você precisa de mais precisão do que o modelo `tiny`, mas sem comprometer muito o tempo de execução. Ele é ~7 vezes mais rápido que o modelo `large`.

- **small**: Com 244 milhões de parâmetros, este modelo é mais preciso que os anteriores, mas ainda assim relativamente rápido. Ele é ideal para transcrições rápidas e precisas. Ele é ~4 vezes mais rápido que o modelo `large`.

- **medium**: Com 769 milhões de parâmetros, esse modelo oferece um bom equilíbrio entre precisão e velocidade, sendo ideal para tarefas que exigem maior exatidão, mas ainda com desempenho razoável. Ele é ~2 vezes mais rápido que o modelo `large`.

- **large**: O modelo mais preciso, com 1550 milhões de parâmetros, é o mais lento, mas o mais eficaz em termos de transcrição, especialmente em tarefas mais complexas. Ele é recomendado quando a precisão é a principal preocupação.

- **turbo**: Com 809 milhões de parâmetros, esse modelo é uma versão otimizada do modelo `large`, oferecendo um bom equilíbrio entre precisão e velocidade. Ele é ~8 vezes mais rápido que o modelo `large`, mas com um desempenho de precisão ligeiramente inferior.

### Explicação sobre a Taxa de Amostragem `-ar`

A taxa de amostragem, representada pelo parâmetro `-ar`, define o número de amostras de áudio capturadas por segundo. No caso de uma taxa de 22.05 kHz (22050 Hz), significa que 22.050 amostras são capturadas a cada segundo. Essa taxa é um bom compromisso entre a qualidade do áudio e o tamanho do arquivo, oferecendo boa qualidade para transcrições sem gerar arquivos excessivamente grandes.

### Como Funciona o processo de transcrição

1. **Extração do áudio**: Primeiramente, é necessário extrair o áudio do arquivo de vídeo. Isso é feito utilizando o `ffmpeg`, que converte o áudio em um arquivo WAV com uma taxa de amostragem de 22.05 kHz, o que ajuda a reduzir o tamanho do arquivo sem perder qualidade.
   
2. **Transcrição com Whisper**: Depois de extrair o áudio, o modelo Whisper é utilizado para transcrever o conteúdo. O modelo pode ser escolhido com base nas necessidades de desempenho e precisão. O Whisper pode também traduzir o áudio de uma língua para outra durante a transcrição, o que é útil para legendas multilíngues.

3. **Geração de legendas**: Após a transcrição, o texto é formatado em um arquivo `.srt` com os tempos de início e fim para cada segmento de áudio. Isso resulta em um arquivo de legenda que pode ser utilizado para exibir o texto junto com o vídeo.

Esses passos permitem automatizar a criação de legendas para vídeos de forma eficiente, com a flexibilidade de escolher o modelo que melhor atende ao seu caso de uso, seja para precisão máxima ou processamento rápido.

### Exemplo de uso

```python
# Transcrever o arquivo MP4 e gerar a legenda traduzida
transcribe_audio("teste.mp4")

# Transcrever o arquivo MKV e gerar a legenda traduzida
transcribe_audio("teste.mkv")
```

## Executando o Código

Para rodar o código, basta executar o seguinte comando no terminal:

```python
python main.py
```

## Resultados:

1. Os arquivos `audio.wav`, `english.srt` e `portuguese.srt` serão gerados na pasta raiz do projeto.
2. Dois arquivos de exemplo, `english.srt` e `portuguese.srt`, foram incluídos na pasta do projeto, mas os arquivos de áudio e vídeo não estão presentes devido ao seu tamanho.
3. Para que a legenda seja reconhecida automaticamente por players de vídeo, como o VLC ou KM Player, é importante que o arquivo de vídeo e o arquivo de legenda possuam o mesmo nome.
   Exemplo: `teste.mp4` e `teste.srt`.

## Links Úteis

- [Whisper no GitHub](https://github.com/openai/whisper)
- [Artigo: Introducing Whisper](https://openai.com/index/whisper/)
- [Deep Translator](https://pypi.org/project/deep-translator/)

## Licença

Este projeto está licenciado sob a Licença MIT.
