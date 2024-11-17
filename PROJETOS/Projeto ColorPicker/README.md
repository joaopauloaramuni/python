# ColorPicker

O **ColorPicker** é um utilitário simples em Python que permite capturar cores RGB e Hexadecimais do pixel sob o ponteiro do mouse em tempo real. É ideal para designers, desenvolvedores e entusiastas que precisam identificar cores diretamente da tela.

## Requisitos

- Python 3.6 ou superior

## Pillow e PyAutoGUI

### Pillow
Pillow é uma biblioteca Python para manipulação de imagens, oferecendo ferramentas para abrir, editar, salvar e processar imagens em diversos formatos. Em um projeto **Color Picker**, Pillow pode ser usada para analisar e manipular cores de imagens, permitindo, por exemplo, identificar a cor de um pixel em uma imagem ou realizar ajustes nas cores antes de exibir os resultados ao usuário.

### PyAutoGUI
PyAutoGUI é uma biblioteca Python voltada para automação de interfaces gráficas, possibilitando o controle do teclado e do mouse por meio de código. Em um projeto **Color Picker**, PyAutoGUI pode ser usada para capturar a posição atual do cursor e tirar screenshots da tela, permitindo obter a cor de um pixel específico diretamente da tela em tempo real.

### Como se relacionam
No contexto de um **Color Picker**, PyAutoGUI captura a posição e a tela onde o cursor está localizado, enquanto Pillow pode processar a imagem capturada para identificar e manipular a cor do pixel desejado. Juntas, essas bibliotecas permitem criar uma ferramenta eficiente para selecionar e exibir cores do monitor.

## Instalação

1. Clone este repositório ou copie o arquivo do projeto.
2. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install Pillow pyautogui
   ```

## Uso

1. Execute o script no terminal:
   ```bash
   python main.py
   ```
2. Mova o mouse para capturar as cores dos pixels na tela.
3. Pressione `Ctrl+C` para encerrar o programa.

## Exemplo de saída

```text
Movimente o mouse para capturar as cores. Pressione Ctrl+C para sair.
Posição: Point(x=996, y=927) | RGB: RGB(red=96, green=43, blue=23) | Hex: #602b17
```

## Documentação

- [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/en/latest/)
- [PyAutoGUI Screenshot](https://pyautogui.readthedocs.io/en/latest/screenshot.html)
- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)

## Licença

Este projeto é licenciado sob os termos da MIT License.
