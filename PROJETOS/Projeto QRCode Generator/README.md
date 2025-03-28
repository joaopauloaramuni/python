# Gerador de QR Code Personalizado

Este projeto é uma aplicação GUI desenvolvida em Python utilizando Tkinter para gerar QR Codes personalizados. O usuário pode inserir um texto ou URL, escolher cores personalizadas, ajustar o tamanho do QR Code e até adicionar uma imagem central.

## 📌 Funcionalidades
- Gerar QR Codes com dados personalizados (texto/URL)
- Personalização de cores do QR Code e do fundo
- Ajuste do tamanho do QR Code
- Adicionar uma imagem central ao QR Code
- Visualizar uma prévia do QR Code gerado
- Salvar o QR Code como imagem

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **Tkinter** (Interface gráfica)
- **Pillow** (Manipulação de imagens)
- **qrcode** (Geração de QR Codes)

## 📂 Estrutura do Projeto
```
📂 qr_code_generator
├── 📄 main.py          # Arquivo principal para iniciar a aplicação
├── 📄 qr_gui.py        # Interface gráfica da aplicação
├── 📄 qr_logic.py      # Lógica de geração e salvamento do QR Code
└── 📄 README.md        # Documentação do projeto
```

## 🚀 Como Executar
### Pré-requisitos
Antes de executar o projeto, certifique-se de ter o **Python 3** instalado.

### Instalação das Dependências
Instale as bibliotecas necessárias executando:
```sh
pip install pillow qrcode[pil] tkinter
```

### Executando a Aplicação
No terminal, navegue até a pasta do projeto e execute:
```sh
python main.py
```

## 🎨 Como Usar
1. Insira o texto ou URL no campo correspondente.
2. Escolha a cor do QR Code e do fundo.
3. Ajuste o tamanho do QR Code (entre 1 e 40).
4. Opcionalmente, adicione uma imagem central.
5. Clique em **Gerar QR Code** para visualizar o resultado.
6. Para salvar, clique em **Salvar QR Code** e escolha um local no seu computador.

## 📜 Licença
Este projeto é de código aberto e está licenciado sob a **MIT License**.
