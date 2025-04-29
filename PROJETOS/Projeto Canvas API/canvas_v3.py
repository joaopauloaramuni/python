import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from canvasapi import Canvas
from datetime import datetime
from datetime import timedelta
import pytz
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os.path
import threading

# Definir a URL da API e o token de autenticação
API_URL = "https://pucminas.instructure.com"  # URL do Canvas da PUC Minas
API_KEY = "11748~XWMKCJrPYXCQzBVLZWBQHACkFmwRcZ94RcCm4nXrhhEz9ZUWGKBU7Y**********"  # Token gerado no Canvas para autenticação

# Inicializar o objeto Canvas com a URL e o token
canvas = Canvas(API_URL, API_KEY)

# Definir o fuso horário de São Paulo (UTC-3)
saopaulo_tz = pytz.timezone('America/Sao_Paulo')  # Definindo o fuso horário de São Paulo usando a biblioteca pytz

# Permissões que vamos solicitar
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Função para listar cursos e tarefas
def listar_cursos_e_tarefas(text_area):
    """
    Função para listar os cursos e tarefas do usuário autenticado no Canvas.
    """
    try:
        user = canvas.get_user('self')  # Obtendo o usuário logado, 'self' refere-se ao usuário autenticado
        courses = user.get_courses()  # Obtendo os cursos em que o usuário está matriculado
        
        # Iterando sobre os cursos do usuário
        for course in courses:
            # Exibindo o nome e o ID de cada curso
            print(f"***** Curso: {course.name} | ID do curso: {course.id} *****")
            text_area.insert(tk.END, f"***** Curso: {course.name} | ID do curso: {course.id} *****\n")
            text_area.yview(tk.END)
            
            # Listar as tarefas (assignments) de cada curso
            assignments = course.get_assignments()  # Obtendo as tarefas do curso
            
            # Verificando se existem tarefas no curso
            if assignments:
                service = autenticar_google_calendar()  # Autenticar uma vez fora do loop!
                for assignment in assignments:
                    # Verificando se a tarefa tem data de entrega
                    due_date = assignment.due_at  # A data de entrega da tarefa
                    if due_date:
                        # Convertendo a data de entrega de UTC para o horário de São Paulo
                        due_date_utc = datetime.strptime(due_date, "%Y-%m-%dT%H:%M:%SZ")  # Convertendo a string da data para datetime
                        due_date_utc = pytz.utc.localize(due_date_utc)  # Convertendo a data para o fuso horário UTC
                        due_date_local = due_date_utc.astimezone(saopaulo_tz)  # Convertendo para o fuso horário de São Paulo
                        
                        # Formatando a data para o formato desejado para o print
                        due_date_local_print = due_date_local.strftime("%d/%m/%Y %H:%M:%S")  # Formato para print (DD/MM/AAAA HH:MM:SS)
                        print(f"Tarefa: {assignment.name} | ID da Tarefa: {assignment.id} | Data de Entrega: {due_date_local_print}")  # Exibindo a tarefa com a data formatada
                        text_area.insert(tk.END, f"Tarefa: {assignment.name} | ID da Tarefa: {assignment.id} | Data de Entrega: {due_date_local_print}\n")
                        text_area.yview(tk.END)
                        
                        # Criar lembrete no Google Calendar usando o formato ISO 8601, mantendo a data como datetime
                        due_date_local_iso = due_date_local.isoformat()  # Formato ISO 8601 (2025-04-06T23:59:59-03:00)
                        
                        # Criar lembrete
                        criar_lembrete(service, assignment.name, due_date_local_iso, text_area)
                    else:
                        # Caso não haja data de entrega definida, exibe uma mensagem
                        print(f"Tarefa: {assignment.name} | ID da Tarefa: {assignment.id} | Data de Entrega: Não especificada")
                        text_area.insert(tk.END, f"Tarefa: {assignment.name} | ID da Tarefa: {assignment.id} | Data de Entrega: Não especificada\n")
                        text_area.yview(tk.END)
            else:
                # Caso não haja tarefas no curso
                print("Nenhuma tarefa encontrada neste curso.")
                text_area.insert(tk.END, "Nenhuma tarefa encontrada neste curso.\n")
                text_area.yview(tk.END)
            
            # Separador visual entre cursos
            print("*" * 150)
            text_area.insert(tk.END, "*" * 120 + "\n")
            text_area.yview(tk.END)
    except Exception as e:
        # Caso ocorra algum erro na execução do código, será exibida a mensagem de erro
        print(f"Ocorreu um erro: {e}")
        text_area.insert(tk.END, f"Ocorreu um erro: {e}\n")
        text_area.yview(tk.END)

# Função para autenticação no Google
def autenticar_google_calendar():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    return service

def criar_lembrete(service, nome_tarefa, data_entrega, text_area):
    # data_entrega já está no formato ISO (ex: 2025-04-28T14:00:00-03:00)
    start_datetime = datetime.fromisoformat(data_entrega)
    end_datetime = start_datetime + timedelta(minutes=30)  # <<< 30 minutos de duração
    
    evento = {
        'summary': nome_tarefa,
        'description': f'Lembrete da entrega: {nome_tarefa}',
        'start': {
            'dateTime': start_datetime.isoformat(),
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': end_datetime.isoformat(),
            'timeZone': 'America/Sao_Paulo',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 60},   # 1h antes
                {'method': 'email', 'minutes': 1440}, # 1 dia antes
            ],
        },
        'colorId': '10',  # Verde
    }
    event = service.events().insert(calendarId='primary', body=evento).execute()
    print(f"Evento criado: {event.get('htmlLink')}")
    text_area.insert(tk.END, f"Evento criado: {event.get('htmlLink')}\n")
    text_area.yview(tk.END)

# Função para rodar o processo em outra thread
def gerar_lembretes(text_area):
    # Limpar o conteúdo da TextArea antes de começar
    text_area.delete(1.0, tk.END)  # Limpa o conteúdo anterior
    
    # Desabilitar o botão enquanto o processo estiver em execução
    btn_gerar.config(state=tk.DISABLED)
    
    # Chama a função de listar cursos e tarefas
    listar_cursos_e_tarefas(text_area)
    
    # Habilitar o botão novamente quando o processo terminar
    btn_gerar.config(state=tk.NORMAL)

# Função principal
def main():
    root = tk.Tk()
    root.title("Gerador de lembretes")
    root.geometry("900x600")  # Aumenta a largura da janela

    # Criando o TextArea para exibição de logs
    text_area = scrolledtext.ScrolledText(root, width=100, height=25)
    text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  # Garantir que o TextArea ocupe toda a área disponível
    
    # Função do botão
    def gerar():
        # Rodando o processo de geração de lembretes em uma thread separada
        threading.Thread(target=gerar_lembretes, args=(text_area,), daemon=True).start()
    
    # Criando o botão para gerar lembretes
    global btn_gerar
    btn_gerar = tk.Button(root, text="Gerar lembretes no Google Calendar", command=gerar)
    btn_gerar.pack(padx=10, pady=10)

    # Adicionando o rodapé
    rodape = tk.Label(root, text="PUC Minas - Integração Canvas", font=("Helvetica", 9), fg="gray")
    rodape.pack(side="bottom", pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
