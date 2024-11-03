# Compressor de Imagens

Este é um programa de compressão de imagens com uma interface gráfica construída em Python usando a biblioteca `Tkinter`. Ele permite que o usuário selecione uma imagem, ajuste a qualidade de compressão e salve a versão comprimida. Este README inclui instruções para gerar o executável (.exe) do projeto.

## Funcionalidades

- **Upload de Imagem**: Seleção de uma imagem no formato `.jpg`, `.jpeg` ou `.png`.
- **Ajuste de Qualidade**: Controle de qualidade da compressão, de 1 a 100.
- **Interface Gráfica**: Interface amigável e intuitiva para facilitar o uso.
- **Versão Executável (.exe)**: Pode ser gerado para uso direto no Windows, sem necessidade de instalar Python.

## Compressão

No exemplo apresentado, o arquivo original `image.jpg`, com um tamanho de 3.2 MB, foi comprimido para `comprimido_image.jpg`, que agora ocupa apenas 893 KB. Essa compressão foi realizada utilizando um parâmetro de qualidade de 0.5, demonstrando uma redução significativa no tamanho do arquivo, mantendo uma qualidade aceitável da imagem.

## Dependências

Para executar este projeto, você precisará das seguintes bibliotecas Python:

- `Pillow`: Para manipulação de imagens.

Você pode instalar as dependências necessárias utilizando o seguinte comando:

```bash
pip3 install Pillow
```
## Execução do código

Para executar o código e gerar a imagem a partir do texto especificado, basta utilizar o seguinte comando no terminal:

```bash
python3 app.py
```

Certifique-se de que você esteja no diretório onde o arquivo app.py está localizado e que o ambiente virtual esteja ativado, caso você esteja usando um. Assim, o script irá rodar e você verá a imagem gerada, de acordo com o texto passado como parâmetro.

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
