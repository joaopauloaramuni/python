# ASCII Art Generator

Este é um gerador de arte ASCII que converte uma imagem em uma representação textual usando caracteres ASCII. 

## Dependências

Para executar este código, você precisará da biblioteca Pillow. Você pode instalá-la usando o seguinte comando:

```bash
pip3 install Pillow
```

### Pillow

**Pillow** é uma biblioteca Python que facilita a manipulação e o processamento de imagens. Com ela, é possível abrir, salvar e converter imagens em diversos formatos, além de realizar operações como redimensionamento, recorte e rotação. A biblioteca também oferece a aplicação de filtros e efeitos, bem como a capacidade de adicionar texto e formas às imagens. Pillow é uma ferramenta poderosa e versátil, amplamente utilizada em projetos que envolvem tratamento de imagens.

## Estrutura de diretórios

1. Certifique-se de que a imagem que deseja converter está localizada na pasta especificada. Neste exemplo, `Documents` no macOS.
   - **Observação**: No Windows, o caminho seria algo como `C:\Users\SeuUsuario\Documents`, e no Linux, poderia ser `/home/SeuUsuario/Documents`. Adapte o caminho conforme o sistema operacional que você está utilizando.

## Como usar

1. Certifique-se de que a imagem que deseja converter está localizada na pasta especificada. 
2. Atualize a variável `image_path` com o caminho correto da sua imagem.
3. Execute o script.

## Modos de saída

O script oferece duas opções de saída para a representação da arte ASCII:

- **`multi`**: Este modo usa uma variedade de caracteres ASCII para representar diferentes níveis de brilho. A lista de caracteres é `['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']`, onde caracteres mais à esquerda representam áreas mais escuras e os caracteres à direita representam áreas mais claras.

- **`single`**: Neste modo, todos os pixels escuros são representados pelo caractere `#`, enquanto os pixels claros não são representados (deixando um espaço vazio). Isso resulta em uma representação mais simples da imagem.

## Threshold

O `threshold` é um valor que determina a intensidade do pixel a partir da qual um pixel é considerado "escuro". No modo `single`, pixels com intensidade abaixo do `threshold` são representados como `#`, enquanto pixels acima são deixados como espaços vazios. O valor padrão é **128**, que é o ponto médio na escala de 0 a 255. Você pode ajustar esse valor para ver como ele afeta a saída da arte ASCII.

## Resolução da imagem

O parâmetro `new_width` define a largura da imagem redimensionada antes de convertê-la para arte ASCII. Ele desempenha um papel importante na resolução da imagem ASCII resultante. A altura da imagem é ajustada automaticamente para manter a proporção com base na largura especificada.

- **Considerações sobre a resolução**:
    - **Valor de new_width**: Um valor menor para `new_width` resultará em uma arte ASCII mais compacta, mas pode perder detalhes importantes da imagem original. 
    - **Valor maior de new_width**: Um valor maior proporcionará mais detalhes na arte ASCII, mas também pode tornar a saída muito longa para ser exibida em uma única tela, exigindo rolagem.

A escolha do `new_width` deve ser feita com base no equilíbrio desejado entre detalhes e legibilidade da saída ASCII.

## Melhoria de contraste

O contraste na arte ASCII gerada depende da escolha do modo de saída e dos caracteres utilizados para representar os pixels da imagem. Aqui estão algumas dicas para melhorar o contraste da sua arte ASCII:

- **Escolha de caracteres**: No modo `multi`, você pode observar que caracteres mais escuros, como `@` e `#`, são usados para representar áreas escuras, enquanto caracteres mais claros, como `.` e `,`, são usados para áreas mais claras. Usar uma gama mais ampla de caracteres pode melhorar o contraste visual.

- **Ajuste do Threshold**: O parâmetro `threshold` determina a intensidade do pixel a partir da qual um pixel é considerado "escuro". Ajustar este valor pode ajudar a realçar o contraste. Por exemplo, um `threshold` menor resultará em mais pixels escuros representados como caracteres, aumentando a densidade visual da arte.

- **Tamanho da imagem**: Reduzir o `new_width` pode resultar em uma arte ASCII mais compacta, o que pode ajudar a aumentar a percepção de contraste, já que a densidade de caracteres será maior. Contudo, isso também pode causar a perda de detalhes, então é importante encontrar um equilíbrio.

- **Experimentos**: Não hesite em experimentar diferentes combinações de caracteres, valores de `threshold` e `new_width` para encontrar a configuração que melhor se adapta à sua imagem e ao efeito desejado.

Ajustar esses fatores pode levar a uma arte ASCII mais impactante e visualmente atraente.

## Exemplo de uso

Para usar o script, basta definir o caminho da imagem e escolher o modo de saída (multi ou single):

```python
output_mode = 'multi'  # ou 'single'
```

Depois, execute o script para ver a arte ASCII gerada.

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

Após ativar o ambiente virtual, você pode instalar a dependência do Pillow conforme mencionado anteriormente.
