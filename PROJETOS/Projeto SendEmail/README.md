# Projeto SendEmail

Este é um projeto simples em Python para enviar e-mails utilizando o protocolo SMTP. Ele demonstra como carregar credenciais de um arquivo `.env`, criar mensagens de e-mail, e enviá-las utilizando um servidor de e-mail.

## Dependências

- **python-dotenv**: Usado para carregar variáveis de ambiente armazenadas em um arquivo `.env` de forma segura e prática.
- **smtplib**: Biblioteca padrão do Python para comunicação com servidores de e-mail via protocolo SMTP.
- **email.mime**: Utilizado para construir mensagens de e-mail com múltiplas partes, como corpo de texto e anexos.

### Arquivo `.env`

O arquivo `.env` armazena credenciais sensíveis de forma segura. Para este projeto, o arquivo deve conter:

```
EMAIL=seu_email@gmail.com
SENHA=sua_senha_de_app
```

O uso do `.env` evita expor credenciais diretamente no código.

## Ambiente Virtual (venv)

### Passo 1: Criar e ativar o ambiente virtual

É recomendado criar um ambiente virtual para isolar as dependências do projeto. Para configurar o ambiente virtual:

1. **Criar o ambiente virtual**:
   ```bash
   python -m venv venv
   ```

2. **Ativar o ambiente virtual**:
   - No Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Passo 2: Instalar as dependências

Após ativar o ambiente virtual, instale as dependências:
```bash
pip install python-dotenv
```

### Passo 3: Executar o script

Após ativar o ambiente virtual, e instalar as dependências, execute o script principal:
```bash
python main.py
```

## Funções do Código

### `carregar_credenciais()`

Carrega o e-mail e a senha armazenados no arquivo `.env`. Retorna essas informações para uso posterior.

### `criar_mensagem(remetente, destinatario, assunto, corpo)`

Constrói uma mensagem de e-mail utilizando o formato MIME, que permite adicionar texto, anexos e outros elementos no corpo do e-mail.

### `enviar_email(smtp_host, smtp_port, email, senha, mensagem)`

Envia a mensagem criada para o destinatário utilizando o servidor SMTP especificado. Inclui autenticação e comunicação segura via TLS.

### `main()`

Função principal que orquestra o processo de carregar credenciais, criar a mensagem e enviá-la.

## Documentação e Links Úteis

- [Documentação do módulo email.mime](https://docs.python.org/3/library/email.mime.html)
- [Configuração de Senhas de Aplicativos Google](https://myaccount.google.com/apppasswords)

## Licença

Este projeto está licenciado sob a Licença MIT.
