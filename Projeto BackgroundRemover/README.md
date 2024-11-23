# Projeto BackgroundRemover

Este é um projeto que utiliza a biblioteca `rembg` para remover o fundo de uma imagem. O exemplo fornecido utiliza uma imagem do Guido van Rossum, o criador do Python, e ao final do processo a imagem com o fundo removido será salva na pasta `imgs` com o nome `fundoremovido.png`.

O `rembg` funciona com versões do Python 3.7 a 3.10.

## Como Funciona

1. O script irá remover o fundo de uma imagem fornecida.
2. Ao final do processo, a imagem resultante será salva na pasta `imgs`.
3. A imagem será exibida automaticamente após a remoção do fundo.

Foi utilizado como exemplo a imagem `Guido_van_Rossum.jpeg`, que está localizada na pasta `imgs`. 

## Captura de Tela

| <img src="imgs/Guido_van_Rossum.jpeg" alt="Guido_van_Rossum" width="600"/> | <img src="imgs/fundoremovido.png" alt="fundoremovido" width="600"/> |
|:---------------------:|:-----------------:|
| Guido_van_Rossum.jpeg | fundoremovido.png | 

## Links úteis

- [GitHub rembg](https://github.com/danielgatis/rembg/)
- [GitHub Microsoft onnxruntime](https://github.com/microsoft/onnxruntime)
- [GitHub Pillow](https://github.com/python-pillow/Pillow)

- [pip rembg](https://pypi.org/project/rembg/)
- [pip onnxruntime](https://pypi.org/project/onnxruntime/)
- [pip pillow](https://pypi.org/project/pillow/)

## Como Rodar

### Passo 1: Instalar as dependências

É recomendável instalar as dependências em um ambiente virtual. Para isso, siga os passos abaixo:

1. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

2. Caso não tenha o arquivo `requirements.txt`, instale as bibliotecas manualmente:

    ```bash
    pip install rembg onnxruntime pillow
    ```

### Passo 2: Criar e ativar o ambiente virtual

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

### Passo 3: Executar o script

1. Certifique-se de que a imagem `Guido_van_Rossum.jpeg` esteja na pasta `imgs`.
2. Execute o script:

    ```bash
    python main.py
    ```

### Requisitos de versão

Este projeto foi testado com Python 3.9.9. O `rembg` é compatível com versões do Python 3.7 até 3.10.

## Licença

Este projeto está licenciado sob a **Licença MIT**.
