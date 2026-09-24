# Projeto ASCII WebCam

Este é um espelho ASCII em tempo real: o script captura a imagem da webcam e a converte, quadro a quadro, em uma representação textual exibida diretamente no terminal. É como se ver "virar Matrix"!

## Captura de Tela

| <img src="https://joaopauloaramuni.github.io/java-imgs/ASCII_WebCam/imgs/print.png" alt="Print" width="1000"/> |
|:--------------------------------------------------------------:|
|                        Captura de Tela                         |

## Dependências

Para executar este código, você precisará das bibliotecas OpenCV e NumPy. Você pode instalá-las usando o seguinte comando:

```bash
pip3 install opencv-python numpy
```

### OpenCV

**OpenCV** (Open Source Computer Vision Library) é uma das bibliotecas de visão computacional mais utilizadas no mundo. Com ela, é possível capturar vídeo de câmeras, ler e salvar imagens e vídeos, redimensionar, recortar, espelhar e converter imagens entre diferentes espaços de cor, além de realizar tarefas mais avançadas, como detecção de rostos e objetos. Neste projeto, o OpenCV é responsável por acessar a webcam, espelhar a imagem, redimensioná-la e convertê-la para tons de cinza.

### NumPy

**NumPy** é a biblioteca fundamental para computação numérica em Python. Ela oferece arrays multidimensionais e operações vetorizadas extremamente rápidas. Como toda imagem capturada pelo OpenCV é, na prática, um array NumPy, podemos converter o brilho de todos os pixels em caracteres de uma só vez, sem precisar percorrer pixel por pixel. Isso é essencial para manter uma boa taxa de quadros por segundo (FPS).

> **Observação**: o NumPy já é instalado automaticamente junto com o `opencv-python`, mas deixá-lo explícito no comando não causa nenhum problema.

## Como usar

1. Certifique-se de que o computador possui uma webcam conectada e que nenhum outro programa (Zoom, Teams, Meet etc.) está utilizando a câmera.
2. Abra o terminal no diretório onde o arquivo `ascii_webcam.py` está localizado.
3. Execute o script, escolhendo (opcionalmente) o modo de cor e o estilo de caracteres.
4. Pressione **S** para salvar um retrato ASCII e **Q** (ou **Ctrl+C**) para sair.

## Modos de cor

O script oferece três modos de exibição, escolhidos com o argumento `--modo`:

- **`matrix`** (padrão): os caracteres são exibidos em tons de verde. Quanto mais claro o pixel, mais intenso o verde, criando o visual clássico do filme Matrix.

- **`mono`**: todos os caracteres são exibidos na cor padrão do terminal. É o visual clássico da arte ASCII.

- **`cor`**: cada caractere recebe a cor RGB real do pixel correspondente (truecolor). É o modo mais impressionante, mas também o mais pesado, pois cada caractere carrega seu próprio código de cor.

## Estilos de caracteres

O argumento `--estilo` define quais caracteres serão usados para representar os diferentes níveis de brilho. Os caracteres são ordenados do mais escuro (menos "tinta") para o mais claro (mais "tinta"):

| Estilo | Caracteres | Efeito |
|---|---|---|
| `classico` (padrão) | ` .:-=+*#%@` | Arte ASCII tradicional |
| `blocos` | ` ░▒▓█` | Visual de vídeo pixelado, bem nítido |
| `katakana` | ` ･ｰｱｲｳｴｵｶｷｸｹｺ` | O "Matrix de verdade" |
| `detalhado` | sequência longa de ~70 caracteres | Mais níveis de brilho e detalhes |

Também é possível criar a sua própria sequência com o argumento `--caracteres`, que tem prioridade sobre o `--estilo`:

```bash
python3 ascii_webcam.py --caracteres " .oO@"
```

- **Katakanas de meia largura**: o estilo `katakana` utiliza caracteres de *meia largura* (ｱ, ｲ, ｳ), que ocupam apenas uma coluna no terminal, assim como uma letra comum. Os katakanas de largura cheia (ア, イ, ウ) ocupariam duas colunas e deixariam a imagem distorcida.

## Retratos ASCII

Durante a execução, ao pressionar a tecla **S**, o frame atual é salvo como um arquivo de texto na pasta `retratos/`, criada automaticamente no diretório onde o script está sendo executado. Cada arquivo recebe a data e a hora (com milissegundos) no nome, por exemplo:

```
retratos/retrato_20260924_143015_482.txt
```

Os retratos são salvos em **texto puro**, sem os códigos de cor ANSI, para que possam ser abertos normalmente em qualquer editor, como o Bloco de Notas ou o VS Code. Para visualizá-los corretamente, utilize uma fonte monoespaçada e diminua o zoom do editor.

## Argumentos

| Argumento | Descrição | Padrão |
|---|---|---|
| `--modo` | Modo de cor: `mono`, `matrix` ou `cor` | `matrix` |
| `--estilo` | Conjunto de caracteres: `classico`, `blocos`, `katakana` ou `detalhado` | `classico` |
| `--caracteres` | Sequência personalizada (do mais escuro ao mais claro) | — |
| `--camera` | Índice da webcam (útil quando há mais de uma câmera) | `0` |
| `--fps` | Limite de quadros por segundo | `24` |
| `--inverter` | Inverte o brilho (útil em terminais de fundo branco) | desativado |
| `--sem-espelho` | Desativa o efeito espelho | desativado |

## Como funciona

A cada quadro capturado, o script executa as seguintes etapas:

1. **Captura**: o OpenCV lê um frame da webcam.
2. **Espelhamento**: a imagem é invertida horizontalmente, para que o movimento na tela acompanhe o seu, como em um espelho.
3. **Redimensionamento**: a imagem é reduzida para o número de colunas e linhas que cabem no terminal.
4. **Tons de cinza**: a imagem é convertida para tons de cinza, em que cada pixel passa a ter um valor de brilho de 0 (preto) a 255 (branco).
5. **Mapeamento**: cada valor de brilho é convertido em um índice da sequência de caracteres, usando operações vetorizadas do NumPy.
6. **Desenho**: o texto gerado é exibido no terminal, sobrescrevendo o quadro anterior.

## Proporção da fonte

Um caractere no terminal é aproximadamente **duas vezes mais alto do que largo**. Se cada pixel virasse um caractere sem nenhuma correção, a imagem sairia esticada verticalmente. Por isso, o script utiliza a constante `PROPORCAO_FONTE = 0.5`, que reduz a altura da imagem pela metade no momento do redimensionamento, mantendo a proporção correta do rosto.

Além disso, o tamanho da imagem é recalculado automaticamente a cada quadro com base no tamanho atual do terminal. Assim, se você redimensionar a janela durante a execução, a imagem se adapta sozinha.

## Códigos ANSI

Os **códigos ANSI** são sequências especiais de caracteres que o terminal interpreta como comandos, e não como texto. O script os utiliza para:

- **Mover o cursor para o início da tela** (`\033[H`): em vez de limpar a tela a cada quadro, o que causaria "piscadas", o script apenas volta o cursor ao topo e sobrescreve o quadro anterior.
- **Esconder e mostrar o cursor** (`\033[?25l` e `\033[?25h`): evita que o cursor fique piscando no meio da imagem.
- **Colorir os caracteres** (`\033[38;2;R;G;Bm`): define a cor RGB de cada caractere nos modos `matrix` e `cor`.

- **Otimização**: nos modos `mono` e `matrix`, a string de cada caractere (já com seu código de cor) é pré-calculada uma única vez na função `construir_tabela`. No loop principal, basta consultar essa tabela pelo índice, o que deixa a geração dos quadros muito mais rápida.

## Leitura do teclado

Para que as teclas **S** e **Q** funcionem sem pausar a câmera, o script verifica se alguma tecla foi pressionada **sem esperar** por ela:

- **No Windows**: utiliza o módulo `msvcrt`, que permite verificar e ler teclas diretamente.
- **No macOS e Linux**: utiliza os módulos `termios`, `tty` e `select`. O terminal é colocado temporariamente no modo *cbreak*, no qual as teclas são lidas na hora, sem precisar apertar Enter. Ao final da execução, a configuração original do terminal é sempre restaurada.

## Melhor visualização

Aqui estão algumas dicas para obter o melhor resultado:

- **Diminua a fonte do terminal** (Ctrl + `-` ou Cmd + `-`) antes de executar o script. Quanto mais caracteres couberem na tela, maior será a resolução da imagem.
- **Use um terminal com suporte a truecolor**, como o Windows Terminal, o terminal integrado do VS Code, o iTerm2 ou a maioria dos terminais Linux. O `cmd.exe` antigo não exibe bem as cores.
- **Iluminação**: um ambiente bem iluminado, com luz de frente para o rosto, gera muito mais contraste e detalhes.
- **Quadradinhos ou `?` no lugar dos caracteres**: significa que a fonte do terminal não possui os caracteres do estilo escolhido (`blocos` ou `katakana`). Experimente outra fonte ou outro terminal.
- **Experimentos**: combine diferentes modos, estilos e sequências personalizadas para encontrar o visual de que você mais gosta.

## Exemplos de uso

```bash
# Padrão: modo matrix com o estilo clássico
python3 ascii_webcam.py

# Matrix de verdade
python3 ascii_webcam.py --estilo katakana --modo matrix

# Vídeo pixelado colorido
python3 ascii_webcam.py --estilo blocos --modo cor

# Mais detalhes, limitado a 20 FPS
python3 ascii_webcam.py --estilo detalhado --fps 20

# Terminal de fundo branco, usando uma segunda câmera
python3 ascii_webcam.py --inverter --camera 1
```

## Execução do código

Para executar o código e ver o espelho ASCII, basta utilizar o seguinte comando no terminal:

```bash
python3 ascii_webcam.py
```

Certifique-se de que você esteja no diretório onde o arquivo `ascii_webcam.py` está localizado e que o ambiente virtual esteja ativado, caso você esteja usando um. Assim, o script irá abrir a webcam e você verá a sua imagem em ASCII, em tempo real, no seu terminal.

- **Permissão de câmera no macOS**: na primeira execução, o macOS pode solicitar permissão para que o terminal acesse a câmera. Caso a permissão tenha sido negada, habilite-a em **Ajustes do Sistema > Privacidade e Segurança > Câmera**.

## Ambiente virtual

É recomendável usar um ambiente virtual para gerenciar suas dependências. Siga os passos abaixo para configurar um ambiente virtual:

1. Crie um ambiente virtual usando o seguinte comando:

    ```bash
    python3 -m venv .venv
    ```

2. Ative o ambiente virtual:
   - No macOS e Linux:

    ```bash
    source .venv/bin/activate
    ```
   - No Windows:

    ```bash
    .venv\Scripts\activate
    ```

Após ativar o ambiente virtual, você pode instalar as dependências do OpenCV e do NumPy conforme mencionado anteriormente.

## Licença

Este projeto está licenciado sob a MIT License.