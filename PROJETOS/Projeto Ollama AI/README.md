# Projeto Ollama AI

Este projeto demonstra o uso da biblioteca ollama para interagir com modelos de linguagem avançados, como o llama3.1. Ele utiliza streaming de respostas para melhorar a experiência em consultas longas e complexas.

## Dependências

- Python 3.8 ou superior
- Biblioteca ollama
- Homebrew (para gerenciar o Ollama)

## Como criar o ambiente virtual Python

1. Crie e ative um ambiente virtual:
   - No Linux/MacOS:
     python -m venv venv  
     source venv/bin/activate
   - No Windows:
     python -m venv venv  
     venv\Scripts\activate

2. Instale a biblioteca ollama no ambiente virtual:
     pip install ollama

3. Instale e configure o Ollama:
     brew install ollama  
     brew services start ollama

## Baixando o modelo

Antes de usar, você precisa baixar o modelo llama3.1, que ocupa aproximadamente **4.7 GB**. Para isso, execute o comando abaixo com o serviço do Ollama já em execução:

     ollama pull llama3.1

Certifique-se de que o modelo foi baixado e está pronto para uso.

## Integração com o Llama

O serviço Ollama precisa estar rodando localmente para que você consiga interagir com os modelos. Para iniciar o serviço, use o seguinte comando:

     ollama start

Verifique se o serviço está ativo antes de iniciar o script.

## Sobre o Streaming

O parâmetro `stream=True` no método `ollama.chat` permite que as respostas sejam enviadas em partes, ao invés de esperar pelo resultado completo. Isso pode ser útil em casos de consultas mais longas ou complexas, pois permite que você comece a receber e processar as respostas enquanto o modelo ainda está gerando o conteúdo.

## Documentação e links úteis:

- [Ollama](https://ollama.com/)
- [GitHub ollama-python](https://github.com/ollama/ollama-python)
- [Llama API](https://www.llama-api.com/)

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
