
# ColorPicker

O **ColorPicker** é um utilitário simples em Python que permite capturar cores RGB e Hexadecimais do pixel sob o ponteiro do mouse em tempo real. É ideal para designers, desenvolvedores e entusiastas que precisam identificar cores diretamente da tela.

## Requisitos

- Python 3.6 ou superior

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
   python color_picker.py
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

Este projeto é licenciado sob os termos da licença MIT. Consulte o arquivo LICENSE para mais detalhes.
