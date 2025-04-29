# Importando as bibliotecas necessárias
from canvasapi import Canvas  # Biblioteca para interagir com a API do Canvas
from datetime import datetime  # Para manipulação de datas e horas
from datetime import timedelta
import pytz  # Para lidar com fusos horários
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os.path

# Definir a URL da API e o token de autenticação
API_URL = "https://pucminas.instructure.com"  # URL do Canvas da PUC Minas
API_KEY = "11748~3QtRew2BRuThCaBZcJDem8Mn24rh9yDXJcKMaDrxMxTEEa6DUYHByN**********"  # Token gerado no Canvas para autenticação
# https://pucminas.instructure.com/profile/settings 
# Configurações > Integrações aprovadas > Novo token de acesso

# Inicializar o objeto Canvas com a URL e o token
canvas = Canvas(API_URL, API_KEY)  # Criando a instância do Canvas com as credenciais fornecidas

# Definir o fuso horário de São Paulo (UTC-3)
saopaulo_tz = pytz.timezone('America/Sao_Paulo')  # Definindo o fuso horário de São Paulo usando a biblioteca pytz

# Permissões que vamos solicitar
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Função para listar cursos e tarefas
def listar_cursos_e_tarefas():
    """
    Função para listar os cursos e tarefas do usuário autenticado no Canvas.
    """
    # Obter o usuário autenticado e listar os cursos
    try:
        user = canvas.get_user('self')  # Obtendo o usuário logado, 'self' refere-se ao usuário autenticado
        courses = user.get_courses()  # Obtendo os cursos em que o usuário está matriculado
        
        # Iterando sobre os cursos do usuário
        for course in courses:
            # Exibindo o nome e o ID de cada curso
            print(f"***** Curso: {course.name} | ID do curso: {course.id} *****")
            
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
                        
                        # Criar lembrete no Google Calendar usando o formato ISO 8601, mantendo a data como datetime
                        due_date_local_iso = due_date_local.isoformat()  # Formato ISO 8601 (2025-04-06T23:59:59-03:00)
                        
                        # Criar lembrete
                        criar_lembrete(service, assignment.name, due_date_local_iso)
                    else:
                        # Caso não haja data de entrega definida, exibe uma mensagem
                        print(f"Tarefa: {assignment.name} | ID da Tarefa: {assignment.id} | Data de Entrega: Não especificada")
            else:
                # Caso não haja tarefas no curso
                print("Nenhuma tarefa encontrada neste curso.")
            
            # Separador visual entre cursos
            print("*" * 150)
    except Exception as e:
        # Caso ocorra algum erro na execução do código, será exibida a mensagem de erro
        print(f"Ocorreu um erro: {e}")

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

def criar_lembrete(service, nome_tarefa, data_entrega):
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

# Função principal
def main():
    listar_cursos_e_tarefas()

if __name__ == "__main__":
    main()

# Links úteis para referência da documentação e para mais exemplos de uso da biblioteca
# https://github.com/ucfopen/canvasapi
# https://pypi.org/project/canvasapi/
# https://pypi.org/project/pytz/
# https://canvasapi.readthedocs.io/en/stable/
# https://canvasapi.readthedocs.io/en/stable/examples.html#courses
# https://canvasapi.readthedocs.io/en/stable/examples.html#assignments
# https://canvas.instructure.com/doc/api/index.html
# https://developers.google.com/workspace/calendar?hl=pt-br
# https://pypi.org/project/google-auth/
# https://pypi.org/project/google-auth-oauthlib/
# https://pypi.org/project/google-auth-httplib2/
# https://pypi.org/project/google-api-python-client/
