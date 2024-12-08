from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def carregar_credenciais():
    """
    Carrega as credenciais do arquivo .env.
    Retorna o e-mail e a senha.
    """
    load_dotenv()
    email = os.getenv("EMAIL")
    senha = os.getenv("SENHA")
    return email, senha


def criar_mensagem(remetente, destinatario, assunto, corpo):
    """
    Cria uma mensagem de e-mail.
    """
    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = assunto
    mensagem.attach(MIMEText(corpo, "plain"))
    return mensagem


def enviar_email(smtp_host, smtp_port, email, senha, mensagem):
    """
    Envia um e-mail usando o servidor SMTP.
    """
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(email, senha)
            server.sendmail(mensagem["From"], mensagem["To"], mensagem.as_string())
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")


def main():
    """
    Função principal para carregar credenciais, criar a mensagem e enviar o e-mail.
    """
    # Carregar credenciais do arquivo .env
    email, senha = carregar_credenciais()

    # Configurações do e-mail
    destinatario = "destinatario@gmail.com"
    assunto = "Teste de envio de e-mail."
    corpo = "Olá, este é um e-mail enviado usando Python."

    # Criar a mensagem
    mensagem = criar_mensagem(email, destinatario, assunto, corpo)

    # Enviar o e-mail
    smtp_host = "smtp.gmail.com"
    smtp_port = 587
    enviar_email(smtp_host, smtp_port, email, senha, mensagem)


if __name__ == "__main__":
    main()

# pip install python-dotenv
