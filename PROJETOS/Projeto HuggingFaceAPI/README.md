# Projeto de Geração de Imagens com Hugging Face

Este projeto utiliza a API de inferência da Hugging Face, que é uma ferramenta baseada em inteligência artificial (IA), para gerar imagens a partir de descrições de texto.

## Como Funciona

O código envia uma solicitação POST para a API de inferência da Hugging Face, que utiliza modelos de IA treinados para gerar uma imagem com base na descrição fornecida. Esse processo demonstra como a IA pode ser aplicada para transformar texto em representações visuais, facilitando a criação de conteúdo visual a partir de descrições verbais.

### Código

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer hf_seutoken"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
    # "inputs": "Astronaut riding a horse",
	"inputs": "Bearded software engineering professor",
})

import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

if image_bytes:
    print("Recebido conteúdo da imagem.")
    image = Image.open(io.BytesIO(image_bytes))
    image.show()  # Para exibir a imagem
    
    # Salvar a imagem na pasta raiz do projeto como 'imagem_gerada2.png'
    image.save("imagem_gerada2.png")
    print("Imagem salva como 'imagem_gerada2.png'.")
```

### Exibição e Salvamento da Imagem

Após receber os dados da imagem gerados pela API, o código executa as seguintes ações:

1. **Verificação dos Dados da Imagem**: 
   O bloco `if image_bytes:` verifica se a variável `image_bytes` contém dados da imagem recebidos da API.

2. **Exibição da Imagem**:
   Se os dados da imagem estiverem presentes, a linha `image = Image.open(io.BytesIO(image_bytes))` converte os bytes da imagem em um objeto de imagem utilizável pela biblioteca PIL. A seguir, `image.show()` exibe a imagem em uma janela separada.

3. **Salvamento da Imagem**:
   A imagem é salva na pasta raiz do projeto usando `image.save("imagem_gerada2.png")`. Isso cria um arquivo PNG com o nome `imagem_gerada2.png`, permitindo que você acesse a imagem gerada a qualquer momento.

4. **Confirmação do Salvamento**:
   Por fim, uma mensagem é impressa no console informando que a imagem foi salva com sucesso: `print("Imagem salva como 'imagem_gerada2.png'.")`.

Para este exemplo, foram escolhidas as imagens:
- Astronaut riding a horse (Astronauta andando a cavalo)
- Bearded software engineering professor (Professor barbudo de engenharia de software)

## Documentação
- [Hugging Face Website](https://huggingface.co/)
- [Link da documentação da API](https://huggingface.co/docs/api-inference/tasks/text-to-image?code=python#text-to-image)

## Token
Para gerar seu próprio token, visite: [Configurações de Token](https://huggingface.co/settings/tokens)

## Dependências

Este projeto requer as seguintes bibliotecas:
- requests: Para fazer requisições HTTP à API do Hugging Face.
- Pillow: Para manipulação de imagens.

Você pode instalá-las usando o seguinte comando:

```bash
pip3 install requests pillow
```

## Execução do código

Para executar o código e gerar a imagem a partir do texto especificado, basta utilizar o seguinte comando no terminal:

```bash
python3 main.py
```

Certifique-se de que você esteja no diretório onde o arquivo main.py está localizado e que o ambiente virtual esteja ativado, caso você esteja usando um. Assim, o script irá rodar e você verá a imagem gerada, de acordo com o texto passado como parâmetro.

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

Este projeto é de código aberto e está licenciado sob a MIT License. Sinta-se livre para usá-lo e modificá-lo conforme necessário.
