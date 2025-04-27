# Importando as bibliotecas necessárias
from canvasapi import Canvas  # Biblioteca para interagir com a API do Canvas
from datetime import datetime  # Para manipulação de datas e horas
import pytz  # Para lidar com fusos horários

# Definir a URL da API e o token de autenticação
API_URL = "https://pucminas.instructure.com"  # URL do Canvas da PUC Minas
API_KEY = "11748~U646vcwetXcJRXwhPMvZwNym9PKYLUhCZuRWmPBD4Yv2t4YnnkH2FG**********"  # Token gerado no Canvas para autenticação
# https://pucminas.instructure.com/profile/settings 
# Configurações > Integrações aprovadas > Novo token de acesso

# Inicializar o objeto Canvas com a URL e o token
canvas = Canvas(API_URL, API_KEY)  # Criando a instância do Canvas com as credenciais fornecidas

# Definir o fuso horário de São Paulo (UTC-3)
saopaulo_tz = pytz.timezone('America/Sao_Paulo')  # Definindo o fuso horário de São Paulo usando a biblioteca pytz

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
            for assignment in assignments:
                # Verificando se a tarefa tem data de entrega
                due_date = assignment.due_at  # A data de entrega da tarefa
                if due_date:
                    # Convertendo a data de entrega de UTC para o horário de São Paulo
                    due_date_utc = datetime.strptime(due_date, "%Y-%m-%dT%H:%M:%SZ")  # Convertendo a string da data para datetime
                    due_date_utc = pytz.utc.localize(due_date_utc)  # Convertendo a data para o fuso horário UTC
                    due_date_local = due_date_utc.astimezone(saopaulo_tz)  # Convertendo para o fuso horário de São Paulo
                    
                    # Formatando a data para o formato desejado
                    due_date_local = due_date_local.strftime("%d/%m/%Y %H:%M:%S")  # Formato de exibição: DD/MM/AAAA HH:MM:SS
                    print(f"Tarefa: {assignment.name} | ID da Tarefa: {assignment.id} | Data de Entrega: {due_date_local}")  # Exibindo a tarefa com a data formatada
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

# Links úteis para referência da documentação e para mais exemplos de uso da biblioteca
# https://github.com/ucfopen/canvasapi
# https://pypi.org/project/canvasapi/
# https://pypi.org/project/pytz/
# https://canvasapi.readthedocs.io/en/stable/
# https://canvasapi.readthedocs.io/en/stable/examples.html#courses
# https://canvasapi.readthedocs.io/en/stable/examples.html#assignments
# https://canvas.instructure.com/doc/api/index.html
