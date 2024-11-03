# Compressor de Imagens

Este é um programa simples de compressão de imagens desenvolvido em Python. Ele permite que o usuário ajuste a qualidade de compressão diretamente no código e salva a imagem comprimida no mesmo diretório da original.

## Funcionalidades

- **Upload de Imagem**: Seleção de uma imagem no formato `.jpg`, `.jpeg` ou `.png` (definido diretamente no código).
- **Ajuste de Qualidade**: Controle de qualidade da compressão configurável de 1 a 100.
- **Execução Simples**: Código editável e executável diretamente pelo terminal.

## Compressão

No exemplo apresentado, o arquivo original `image.jpg`, com um tamanho de 3.2 MB, foi comprimido para `comprimido_image.jpg`, que agora ocupa apenas 893 KB. Essa compressão foi realizada utilizando um parâmetro de qualidade de 0.5, demonstrando uma redução significativa no tamanho do arquivo, mantendo uma qualidade aceitável da imagem.

## Dependências

Para executar este projeto, você precisará das seguintes bibliotecas Python:

- `Pillow`: Para manipulação de imagens.

Você pode instalar as dependências necessárias utilizando o seguinte comando:

```bash
pip3 install Pillow
```

## Uso

1. **Edite o código**:
   - Abra o arquivo `app.py` e defina o caminho da imagem (`caminho_imagem`) e o nível de qualidade desejado (1-100).

2. **Execute o programa**:
   
    ```console
    python app.py
    ```

3. **Saída**:
   - A imagem comprimida será salva no mesmo diretório da imagem original com o prefixo `comprimido_`.

## Ambiente Virtual

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

## Licença

Este projeto é livre para uso pessoal. Para uso comercial, consulte o autor.
