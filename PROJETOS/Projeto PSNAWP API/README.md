# Projeto PSNAWP API

Este projeto utiliza a biblioteca `PSNAWP` para acessar e interagir com a PlayStation Network, permitindo obter informações sobre sua conta, amigos, dispositivos registrados, troféus e muito mais.

## Funcionalidades

- **Informações da Conta**: Exibe o ID Online, ID da Conta e perfil.
- **Dispositivos Registrados**: Lista os dispositivos conectados à sua conta.
- **Lista de Amigos**: Mostra seus amigos e permite verificar sua lista de amigos bloqueados.
- **Troféus**: Acessa seus troféus, suportando plataformas como PS4.
- **Grupos de Chat**: Obtém informações de grupos e interage com eles, como enviar mensagens.
- **Tempo de Jogo**: Exibe o tempo de jogo em títulos específicos (suporta PS4 e PS5).
- **Busca de Jogos**: Realiza buscas por títulos de jogos na PSN.

## Pré-requisitos

- Instalar a dependência `PSNAWP`:
  ```bash
  pip3 install PSNAWP
  ```

- Criar um código `npsso` (64 caracteres) seguindo as instruções:
  1. Acesse sua conta no [My PlayStation](https://my.playstation.com).
  2. Em outra aba, vá para: https://ca.account.sony.com/api/v1/ssocookie
  3. O código `npsso` será gerado e utilizado para autenticação na API. O token de atualização dura cerca de 2 meses.

## Links Úteis

- [PSNAWP na PyPI](https://pypi.org/project/PSNAWP/)
- [Documentação Oficial](https://psnawp.readthedocs.io/en/latest/)

## Executando o Código

Para rodar o código, basta executar o seguinte comando no terminal:

```bash
python3 main.py
```

## Ambiente Virtual

Recomenda-se o uso de um ambiente virtual para gerenciar as dependências do projeto:

```bash
python3 -m venv .venv
```

Ative o ambiente virtual:

- **macOS e Linux**:
  ```bash
  source .venv/bin/activate
  ```
- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```

## Licença

Este projeto é de código aberto, licenciado sob a MIT License. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.
