# Projeto Melodia Algorítmica

Este projeto gera uma melodia simples utilizando uma cadeia de Markov para criar variações de notas musicais. A melodia gerada é salva em formato MIDI e convertida para o formato WAV utilizando um soundfont. O código utiliza a biblioteca `MIDIUtil` para criação de arquivos MIDI e `midi2audio` para conversão de MIDI para WAV. O soundfont é essencial para gerar a sonoridade da melodia.

## Como funciona

O projeto utiliza uma cadeia de Markov para gerar sequências de notas musicais. A cadeia de Markov é um modelo probabilístico em que o estado futuro depende apenas do estado atual. Neste projeto, as notas musicais representam os estados e a probabilidade de transição entre elas é determinada por uma matriz de transições predefinida.

- **Cadeia de Markov**: A cadeia de Markov utilizada aqui é uma sequência de notas musicais, onde a cada nova nota, a probabilidade de transição é determinada por uma nota atual. Por exemplo, se a última nota for "C4", a próxima nota pode ser "D4", "E4", "G4" ou "A4", com uma probabilidade definida.

## Dependências

Este projeto utiliza as seguintes dependências:

### 1. `MIDIUtil`
- **O que é**: A biblioteca `MIDIUtil` é uma ferramenta simples para criar arquivos MIDI a partir de dados programáticos. Ela é utilizada neste projeto para gerar a melodia no formato MIDI.
- **Instalação**: 
  ```
  pip install MIDIUtil
  ```

### 2. `midi2audio`
- **O que é**: `midi2audio` é uma biblioteca que permite a conversão de arquivos MIDI para áudio (como WAV), utilizando o software `FluidSynth`. É usada neste projeto para transformar a melodia gerada em um arquivo de áudio.
- **Instalação**: 
  ```
  pip install midi2audio
  ```

### 3. `FluidSynth`
- **O que é**: `FluidSynth` é um software que gera áudio a partir de arquivos MIDI utilizando soundfonts. Neste projeto, ele é utilizado para transformar o arquivo MIDI em um arquivo WAV.
- **Instalação**: 
  ```
  brew install fluid-synth
  ```

## Soundfont

Para gerar o áudio a partir do arquivo MIDI, é necessário um arquivo **soundfont**. O soundfont usado neste projeto é o "Essential Keys-sforzando-v9.6", que pode ser baixado a partir do seguinte link:

- [Soundfont Essential Keys-sforzando-v9.6](https://sites.google.com/site/soundfonts4u/)
  (Tamanho: 968MB)

Este arquivo contém os samples necessários para a renderização do áudio a partir do MIDI, garantindo que a melodia gerada tenha uma sonoridade de piano realista.

## Formatos de arquivo

### 1. **MIDI (.mid)**
- O formato MIDI é um padrão para representar dados musicais. Ele contém informações sobre as notas musicais, tempos e outras informações necessárias para reproduzir a música. O arquivo MIDI gerado neste projeto pode ser aberto e manipulado por qualquer software que suporte o formato MIDI.

### 2. **WAV (.wav)**
- O formato WAV é um formato de áudio sem compressão, utilizado para armazenar áudio digitalizado. O arquivo WAV gerado neste projeto contém a música em formato de áudio e pode ser reproduzido em qualquer dispositivo de áudio.

## Como usar

1. **Instale as dependências**:
   - `pip install MIDIUtil midi2audio`
   - `brew install fluid-synth`
2. **Baixe o soundfont** a partir do link fornecido acima e coloque o arquivo `sforzando-v9.6.sf2` no diretório do seu projeto.
3. **Execute o código** para gerar a melodia e salvar os arquivos MIDI e WAV.

## Licença

Este projeto está licenciado sob a Licença MIT.
