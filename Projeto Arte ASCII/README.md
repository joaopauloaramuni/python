# ASCII Art Generator

Este é um gerador de arte ASCII que converte uma imagem em uma representação textual usando caracteres ASCII. 

## Dependências

Para executar este código, você precisará da biblioteca Pillow. Você pode instalá-la usando o seguinte comando:

```bash
pip3 install Pillow
```

## Estrutura de Diretórios

1. Certifique-se de que a imagem que deseja converter está localizada na pasta especificada. Neste exemplo, `Documents` no macOS.
   - **Observação**: No Windows, o caminho seria algo como `C:\Users\SeuUsuario\Documents`, e no Linux, poderia ser `/home/SeuUsuario/Documents`. Adapte o caminho conforme o sistema operacional que você está utilizando.

## Como Usar

1. Certifique-se de que a imagem que deseja converter está localizada na pasta especificada. 
2. Atualize a variável `image_path` com o caminho correto da sua imagem.
3. Execute o script.

## Modos de Saída

O script oferece duas opções de saída para a representação da arte ASCII:

- **`multi`**: Este modo usa uma variedade de caracteres ASCII para representar diferentes níveis de brilho. A lista de caracteres é `['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']`, onde caracteres mais à esquerda representam áreas mais escuras e os caracteres à direita representam áreas mais claras.

- **`single`**: Neste modo, todos os pixels escuros são representados pelo caractere `#`, enquanto os pixels claros não são representados (deixando um espaço vazio). Isso resulta em uma representação mais simples da imagem.

## Threshold

O `threshold` é um valor que determina a intensidade do pixel a partir da qual um pixel é considerado "escuro". No modo `single`, pixels com intensidade abaixo do `threshold` são representados como `#`, enquanto pixels acima são deixados como espaços vazios. O valor padrão é **128**, que é o ponto médio na escala de 0 a 255. Você pode ajustar esse valor para ver como ele afeta a saída da arte ASCII.

## Exemplo de Uso

Para usar o script, basta definir o caminho da imagem e escolher o modo de saída (multi ou single):

```python
output_mode = 'multi'  # ou 'single'
```

Depois, execute o script para ver a arte ASCII gerada.

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

Após ativar o ambiente virtual, você pode instalar a dependência do Pillow conforme mencionado anteriormente.
