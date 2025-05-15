# Internet Velocity Test

Este aplicativo, desenvolvido com [Streamlit](https://streamlit.io/) e [speedtest-cli](https://pypi.org/project/speedtest-cli/), realiza um teste de velocidade da internet, medindo as velocidades de download, upload e o ping.

## Dependências do Projeto

Antes de iniciar, certifique-se de ter Python e as bibliotecas necessárias instaladas:

## Streamlit

- **Descrição**: O Streamlit é uma biblioteca de código aberto que facilita a criação de aplicativos web interativos e visualizações de dados em Python. Com uma interface simples e intuitiva, os desenvolvedores podem transformar scripts de Python em aplicações web de forma rápida e eficiente, sem a necessidade de conhecimentos profundos em front-end. O Streamlit é especialmente popular entre cientistas de dados e analistas, pois permite criar dashboards e protótipos de forma ágil.

- [Streamlit](https://streamlit.io/)

## speedtest-cli

- **Descrição**: O speedtest-cli é uma ferramenta de linha de comando que permite realizar testes de velocidade de internet usando o serviço Speedtest.net. Ele fornece informações sobre a velocidade de download, upload e o ping da conexão de internet. É uma biblioteca útil para desenvolvedores que desejam integrar testes de velocidade em seus aplicativos, oferecendo uma maneira fácil de medir e exibir o desempenho da conexão de internet de um usuário.

- [Speedtest-cli](https://github.com/sivel/speedtest-cli)

### Instalando as Dependências

Execute o comando abaixo para instalar as bibliotecas:

```bash
pip3 install streamlit speedtest-cli
```

## Estrutura do Código

O código possui três funções principais:

1. `run_speedtest()`: Executa o teste de velocidade e retorna as velocidades de download e upload (em Mbps) e o ping.
2. `display_results(download_speed, upload_speed, ping)`: Exibe os resultados no aplicativo, incluindo as barras de progresso para download e upload.
3. `main()`: Interface principal do Streamlit, com um botão para iniciar o teste.

## Executando o Aplicativo

Para iniciar o aplicativo, execute o seguinte comando no terminal:

```bash
streamlit run internetvelocity.py
```
## Interface Gráfica

A interface gráfica permite que o usuário clique no botão Iniciar para começar o teste de velocidade. Para usar, basta clicar em iniciar e aguardar os resultados de Velocidade de Download, Velocidade de Upload e Ping.

### Capturas de Tela

- **Tela Inicial: Teste de Velocidade da Internet**: Botão para iniciar o teste.
- **Tela de Resultados:**: Apresenta os resultados do teste de velocidade.

| ![Tela Inicial](https://joaopauloaramuni.github.io/python-imgs/InternetVelocityTest/imgs/home1.png) | ![Tela de Resultados](https://joaopauloaramuni.github.io/python-imgs/InternetVelocityTest/imgs/home2.png) |
|:--:|:--:|
| Tela Inicial | Tela de Resultados |

## Exemplo de Uso

1. Clique no botão **Iniciar** para começar o teste.
2. Aguarde o cálculo da velocidade.
3. Veja os resultados:
   - **Velocidade de Download**: Em Mbps com uma barra de progresso (máximo de 100 Mbps).
   - **Velocidade de Upload**: Em Mbps com uma barra de progresso (máximo de 100 Mbps).
   - **Ping**: Tempo de resposta em milissegundos.

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

Após ativar o ambiente virtual, você pode instalar a dependência do streamlit conforme mencionado anteriormente.

## Licença

Este projeto é de código aberto e está licenciado sob a MIT License. Sinta-se livre para usá-lo e modificá-lo conforme necessário.
