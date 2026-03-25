import os
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import json
 
#--- NOVO PIP INSTALL NECESSÁRIO : pip install requests beautifulsoup4 lxml pdfplumber ---#
 
## LÓGICA DO CÓDGIO
# Faz login no sistema da Puc(sga)
# Navega nas páginas autenticadas (extrai faltas, notas, credenciais e um PDF do histórico de matérias para puxar as horas complementares)
# Salva tudo em arquivos JSON
# Forma a interface gráfica com os dados
class FaltasSpider:
    login_url = 'https://www.sistemas.pucminas.br/sgaaluno4/SilverStream/Pages/pgAln_LoginSSL.html' #esse é o link que redireciona para home do sga
    formdata = {
        'AgEvtSrc': 'S124_',
        'AgStateCode': '7',
        'S50_': 'SUA_MATRICULA',
        'S64_': 'SUA_SENHA',
        'S78_': '9',
        'S219_': ''
    }
 
    #var global cookies
    cookies= '_fbp=fb.1.1749245621327.769442003777369661; _ga_26QEFB1Y29=GS2.1.s1752357264$o4$g1$t1752357264$j60$l0$h0; tt.u=0100007FF4F30468E106FA2402B6480B; _ttuu.s=1753041858657; _ga_9BNXXTFE8X=GS2.1.s1754086319$o1$g1$t1754087141$j60$l0$h0; _ga_3GKZKNZYJR=GS2.1.s1755288595$o2$g1$t1755288620$j35$l0$h0; _hjSessionUser_1550884=eyJpZCI6Ijk2OTBiODRhLWQ3MmMtNTE0MC1iODc2LTk2YWZhOWU4NjlkMiIsImNyZWF0ZWQiOjE3NjM2NTIyMTI0NDcsImV4aXN0aW5nIjp0cnVlfQ==; _ga_X68HE3G4D0=GS2.1.s1764451210$o5$g0$t1764451210$j60$l0$h0; _ga_LJ2M29EH7V=GS2.1.s1766544677$o7$g0$t1766544677$j60$l0$h0; _gcl_au=1.1.512152484.1771199003; _hjSessionUser_1470092=eyJpZCI6IjM5MDczZThlLWMyNjctNWVmNS05MGFjLWIyNzg3YzFkZDJhOCIsImNyZWF0ZWQiOjE3NzE1NDkyOTY5MTIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_1463114=eyJpZCI6IjA1YjQwZTM0LTZhNzgtNThjOS04ZDI0LWRjMDA0YmRkNzNjOSIsImNyZWF0ZWQiOjE3NzE1NDkzMzkyMTMsImV4aXN0aW5nIjp0cnVlfQ==; _ga_MDLGHK92DJ=GS2.1.s1771549339$o1$g1$t1771549368$j31$l0$h0; _ga_RHR2WB3W1P=GS2.1.s1771549310$o1$g1$t1771549404$j60$l0$h0; _ga_FXXCB7KT02=GS2.1.s1771549313$o1$g1$t1771549682$j59$l0$h0; _ga_MLDZ7J98DX=GS2.1.s1771549426$o1$g1$t1771549953$j60$l0$h0; _ga_HYC7HRYVNL=GS2.1.s1773870947$o7$g1$t1773870947$j60$l0$h0; _ga_N6FD3Q0PJD=GS2.1.s1773870947$o13$g1$t1773870947$j60$l0$h0; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Mar+23+2026+12%3A30%3A34+GMT-0300+(Hora+padr%C3%A3o+de+Bras%C3%ADlia)&version=202602.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=b038d45a-6dda-4a8c-89bf-bd29cab0722c&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0005%3A0&intType=3&geolocation=BR%3BMG&AwaitingReconsent=false&prevHadToken=0; _ga_H2EHN44B05=GS2.1.s1774279835$o37$g0$t1774279835$j60$l0$h0; _ga_D37LF6BXDH=GS2.1.s1774279835$o32$g0$t1774279835$j60$l0$h0; _ga_E6D4Q6Q9YH=GS2.1.s1774279835$o1$g0$t1774279835$j60$l0$h0; _ga_ZFLF1RN8MD=GS2.1.s1774279835$o36$g0$t1774279835$j60$l0$h0; _ga_VWP0B7W5MB=GS2.1.s1774279835$o36$g0$t1774279835$j60$l0$h131516227; _ga_KWPYPZ923E=GS2.1.s1774279835$o43$g0$t1774279835$j60$l0$h0; _clck=1fy8krw%5E2%5Eg4l%5E0%5E1743; _ga=GA1.2.341103122.1713384278; AlteonSession=AY6gRjIBAgqqbew8DrdoYw$$; JSESSIONID=e5cdcab5755381f44bd9573d29dd5a2a; _gid=GA1.2.1959339055.1774469042; _gat=1; _dd_s=rum=0&expire=1774469957457'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'connection': 'keep-alive',
        'content-length': '74',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookies,
        'host': 'www.sistemas.pucminas.br',
        'origin': 'https://www.sistemas.pucminas.br',
        'referer': 'https://www.sistemas.pucminas.br/sgaaluno4/SilverStream/Pages/pgAln_LoginSSL.html',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0'
    }
 
    def start_requests(self):
        #Cria uma sessão HTTP que mantém os cookies  automaticamente entre as requisições
        with requests.Session() as session:
            # Faz um POST na URL de login com os dados do formulário (matrícula e senha)
            # É exatamente o que acontece quando você clica em "Entrar" no site
            response = session.post(self.login_url, data=self.formdata, headers=self.headers)
            # Verifica se o login falhou checando o texto da resposta
            if "authentication failed" in response.text:
                print("Login failed")
                return
            self.after_login(response, session)
 
    def after_login(self, response, session):
        # Adiciona a requisição GET aqui
        # Define headers básicos para as requisições GET, na intenção de simular um ato humano para não ser ser bloqueado
        basic_headers = {
            'accept': 'text/htmlextraapplication/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'connection': 'keep-alive',
            'cookie': self.cookies,
            'host': 'www.sistemas.pucminas.br',
            'referer': 'https://www.sistemas.pucminas.br/sgaaluno4/SilverStream/Pages/pgAln_Noticias.html',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0'
        }
       
        ##### REQUISIÇÃO 1: Página de Notas e Frequência ######
        get_url = "https://www.sistemas.pucminas.br/sgaaluno4/SilverStream/Pages/pgAln_NotaFrequencia2.html"
        get_response = session.get(get_url, headers=basic_headers)
       
        # Salvar o HTML para debug
        with open('debug.html', 'w', encoding='utf-8') as f:
            f.write(get_response.text)
 
        # Converte o HTML em um objeto BeautifulSoup navegável
        soup = self.parse(get_response, session)
        self.extract_attendance_and_grades(soup)
 
        ##### REQUISIÇÃO 2: Página de credênciais ######
        get_url = "https://www.sistemas.pucminas.br/sga4/SilverStream/Pages/pg_Credenciais.html"
        get_response = session.get(get_url, headers=basic_headers)
 
        ##### # Converte o HTML em um objeto BeautifulSoup navegável #####
        soup = self.parse(get_response, session)
        self.extract_credentials(soup)
        ##### REQUISIÇÃO 3: Baixa o PDF de atividades complementares ####
        self.baixar_relatorio_pdf(session)
   
    def extrair_dados_historico_pdf(self):
        import pdfplumber
        import re
 
        with pdfplumber.open("historico.pdf") as pdf:
            # Pega só a primeira página
            pagina = pdf.pages[0]
            texto = pagina.extract_text()
 
        print("=== TEXTO EXTRAÍDO DA PRIMEIRA PÁGINA ===")
        print(texto)
        print("=========================================")
 
        # Extrai os valores com regex
        resultado = {}
 
        ##BUSCANDO OS DADOS DA APLICAÇÃO
        match_minimo = re.search(r'[Mm]ínimo de horas exigidas[:\s]+([\d:]+)', texto)
        match_cumpridas = re.search(r'[Tt]otal de horas cumpridas[:\s]+([\d:]+)', texto)
        match_cumprir = re.search(r'[Hh]oras a cumprir[:\s]+([\d:]+)', texto)
        match_data = re.search(r'[Dd]ata do [úu]ltimo lan[çc]amento[:\s]+([\d/]+)', texto)
 
        resultado['minimo_horas_exigidas'] = match_minimo.group(1) if match_minimo else None
        resultado['total_horas_cumpridas'] = match_cumpridas.group(1) if match_cumpridas else None
        resultado['horas_a_cumprir'] = match_cumprir.group(1) if match_cumprir else None
        resultado['data_ultimo_lancamento'] = match_data.group(1) if match_data else None
 
        print("=== DADOS EXTRAÍDOS ===")
        for chave, valor in resultado.items():
            print(f"  {chave}: {valor}")
       
 
        ##ESCREVENDO DADOS NO DOC JSON
        with open('atividades_complementares.json', 'w', encoding='utf-8') as f:
            json.dump(resultado, f, ensure_ascii=False, indent=4)
 
        print("Dados salvos em atividades_complementares.json")
        return resultado
   
## TIRAR A DÚVIDA SE EU AINDA PRECISO PASSAR PELA ABA DE EMISSÃO DE DOCUMENTOS PARA PUXAR O PDF SENDO QUE É POSSIVEL FAZER UM POST DIRETO NA URL DO PDF
    def baixar_relatorio_pdf(self, session):
            import time
 
            # --- PASSO 1: POST na página de emissão de documentos ---
            headers_sga = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-encoding': 'gzip, deflate, br, zstd',
                'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6',
                'cache-control': 'max-age=0',
                'connection': 'keep-alive',
                'content-type': 'application/x-www-form-urlencoded',
                'host': 'www.sistemas.pucminas.br',
                'origin': 'https://www.sistemas.pucminas.br',
                'referer': 'https://www.sistemas.pucminas.br/sga4/SilverStream/Pages/pgAln_EmissaoDocumentos.html',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
            }
 
            # ── PASSO 1: Acessa a página de emissão de documentos ─────────────
            # Simula clicar em "Histórico(consulta)" no sistema
            # O parâmetro S16_=5 provavelmente identifica qual documento gerar
            payload_emissao = {
                'AgEvtSrc': 'undefined',
                'AgStateCode': '8',
                'S16_': '5', # código do tipo de documento
                'S68_': 'selDocumento'
            }
 
            time.sleep(1)
 
            # --- PASSO 2: POST direto no gerador do PDF, nesse momento vamos extrair diretamente da página que é gerada o pdf---
            # PARA FINS DE DEBUG , headers e também o payload é obtido no momento que o pdf é gerado.
            headers_was = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-encoding': 'gzip, deflate, br, zstd',
                'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6',
                'cache-control': 'max-age=0',
                'connection': 'keep-alive',
                'content-type': 'application/x-www-form-urlencoded',
                'host': 'was.sistemas.pucminas.br',
                'origin': 'https://www.sistemas.pucminas.br',
                'referer': 'https://www.sistemas.pucminas.br/',
                'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-site',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
            }
 
            # pParam6 é a matrícula do aluno — já está no seu formdata como S50_
            matricula = self.formdata.get('S50_', '834809')
 
            payload_pdf = {
                'pNomeRPT': 'SGA/Rel_HE_Externo_2Col.rpt',
                'pUsuario': 'rel_SGA',
                'pQtdParam': '7',
                'pTipo1': 'Null',
                'pTipo2': 'Null',
                'pTipo3': 'Integer',
                'pParam3': '0',
                'pTipo4': 'Boolean',
                'pParam4': 'false',
                'pTipo5': 'Integer',
                'pParam5': '0',
                'pTipo6': 'Integer',
                'pParam6': matricula, #passa a matrícula do aluno
                'pTipo7': 'Null'
            }
 
            print("Passo 2: POST em RelatorioGenerico.jsp...")
            #respota 02
            r2 = session.post(
                'https://was.sistemas.pucminas.br/Generico/RelatorioGenerico.jsp', #url de post para obter o pdf do histórico escolar
                data=payload_pdf,
                headers=headers_was,
                allow_redirects=True
            )
 
            print(f"  Status: {r2.status_code}")
            print(f"  Content-Type: {r2.headers.get('Content-Type', '')}")
 
            content_type = r2.headers.get('Content-Type', '')
            # Verifica se a resposta é realmente um PDF
            # PDFs sempre começam com os bytes %PDF
            if 'pdf' in content_type.lower() or r2.content[:4] == b'%PDF':
                with open("historico.pdf", "wb") as f:
                    f.write(r2.content)
                print("PDF salvo com sucesso em historico.pdf!")
                self.extrair_dados_historico_pdf()  # AQUI EXTRAIMOS OS DADOS DO PDF PARA USAR NO TKINTER
            else:
                print("Resposta não é PDF. Salvando debug em debug_relatorio.html")
                with open("debug_relatorio.html", "w", encoding="utf-8") as f:
                    f.write(r2.text)
                print(f"  Primeiros 500 chars: {r2.text[:500]}")
 
    def parse(self, response, session):
    # Parsing com BeautifulSoup
        soup = BeautifulSoup(response.text, 'lxml')
        return soup
 
    def extract_attendance_and_grades(self, soup):
        # Encontrando o elemento com a classe "class1"
        classe_pai = soup.find('span', class_='class1')
   
        # Encontrando todas as tabelas com a classe "smc" dentro do elemento "class1"
        tabelas = classe_pai.find_all('table', class_='smc-sgagrad-agrupamento-primario') if classe_pai else []
       
        # Listas para armazenar faltas e notas
        materias_faltas = []
        notas = []
        titulos = []
        i = 0
        # Extraindo faltas
        for idx, tabela in enumerate(tabelas, start=1):
            primeira_tr = tabela.find('tr')
            if primeira_tr:
                tds = primeira_tr.find_all('td')
                valores = [td.get_text(strip=True).replace('\n', ' ') for td in tds]
                materias_faltas.append(valores)
                primeira_td = tds[0] if tds else None
                titulo = primeira_td.find('p').get_text(strip=True) if primeira_td else None
                titulos.append(titulo)
                i+= 1
       
        # NOVA ABORDAGEM PARA EXTRAIR NOTAS
        # Vamos usar o mesmo método original, mas com um controle para evitar duplicações
       
        # Conjunto para armazenar notas já processadas
        notas_processadas = set()
       
        # Encontrando todas as células com a classe "smc-grid-totalizador"
        total_cells = soup.find_all('td', class_='smc-grid-totalizador')
       
        # Vamos processar em grupos de 4 (assumindo que cada nota tem 4 colunas)
        # Isso ajuda a agrupar as células corretamente mesmo se houver várias tabelas
        i = 0
        j = 0
        while i + 3 < len(total_cells):
            # Extrair os 4 valores da nota
            data = total_cells[i].get_text(strip=True).replace('\n', ' ')
            descricao = total_cells[i+1].get_text(strip=True).replace('\n', ' ')
            valor_max = total_cells[i+2].get_text(strip=True).replace('\n', ' ')
            valor_obtido = total_cells[i+3].get_text(strip=True).replace('\n', ' ').replace('\t', ' ')
           
            # Criar identificador único para esta nota
            nota_key = f"{data}|{descricao}|{valor_max}|{valor_obtido}"
           
            # Verificar se já processamos esta nota
            if nota_key not in notas_processadas:
                # Adicionar à lista em formato estruturado
                nota = {
                    "titulo": titulos[j],
                    "data": data,
                    "descricao": descricao,
                    "valor_maximo": valor_max,
                    "valor_obtido": valor_obtido
                }
                notas.append(nota)
                notas_processadas.add(nota_key)
            j += 1
            # Avançar para o próximo grupo de 4 células
            i += 4
       
        # Salvando faltas em faltas.json
        with open('faltas.json', 'w', encoding='utf-8') as f:
            json.dump(materias_faltas, f, ensure_ascii=False, indent=4)
       
        # Salvando notas em notas.json
        with open('notas.json', 'w', encoding='utf-8') as f:
            json.dump(notas, f, ensure_ascii=False, indent=4)
       
        # Debug: imprimir notas encontradas
        print(f"Número de notas encontradas: {len(notas)}")
        if notas:
            print("Exemplo da primeira nota:", notas[0])
        print("Dados extraídos e salvos em faltas.json e notas.json")
 
    def extract_credentials(self, soup):
 
        credenciasArray = []
 
        tables = soup.find_all('table', class_='smc-sgagrad-credenciaisacesso-item')
 
        for table_index, table in enumerate(tables):
            print(f"Tabela {table_index + 1}:")
            # Pega todas as linhas (tr) dentro da tabela
            rows = table.find_all("tr")
           
            if len(rows) >= 2:
                primeira_linha = rows[0].get_text(strip=True).replace('\n', ' ')
                segunda_linha = rows[1].get_text(strip=True).replace('\n', ' ')  
           
                print("Primeira linha:", primeira_linha)
                print("Segunda linha:", segunda_linha)
 
                credencias = {
                "Titulo" : primeira_linha,
                "Credencial" : segunda_linha
                }
                credenciasArray.append(credencias)
 
 
        with open('credenciais.json', 'w', encoding='utf-8') as f:
            json.dump(credenciasArray, f, ensure_ascii=False, indent=4)
       
    def criar_interface_tkinter(self):
        # ----------------- CARREGAR JSONs -----------------
        with open("notas.json", "r", encoding="utf-8") as f:
            notas = json.load(f)
 
        with open("faltas.json", "r", encoding="utf-8") as f:
            materias_faltas = json.load(f)
 
        with open("credenciais.json", "r", encoding="utf-8") as f:
            credenciais = json.load(f)
 
        # Carrega atividades se existir
        atividades = {}
        try:
            with open("atividades_complementares.json", "r", encoding="utf-8") as f:
                atividades = json.load(f)
        except FileNotFoundError:
            pass
 
        # ----------------- INTERFACE -----------------
        root = tk.Tk()
        style = ttk.Style()
        style.theme_use("default")
 
        root.title("SGA - Faltas, Notas, Credenciais e Horas Complementares")
        root.geometry("1000x400")
 
        notebook = ttk.Notebook(root)
        notebook.pack(fill="both", expand=True)
 
        # ----------------- ABA FALTAS -----------------
        frame_faltas = ttk.Frame(notebook)
        notebook.add(frame_faltas, text="Faltas")
 
        tree_faltas = ttk.Treeview(frame_faltas, columns=("Disciplina", "Carga Horária", "Faltas"), show="headings")
        tree_faltas.heading("Disciplina", text="Disciplina")
        tree_faltas.heading("Carga Horária", text="Carga Horária")
        tree_faltas.heading("Faltas", text="Faltas")
        tree_faltas.pack(fill="both", expand=True)
 
        for f in materias_faltas:
            if len(f) >= 3:
                tree_faltas.insert("", "end", values=(f[0], f[1], f[2]))
 
        # ----------------- ABA NOTAS -----------------
        frame_notas = ttk.Frame(notebook)
        notebook.add(frame_notas, text="Notas")
 
        tree_notas = ttk.Treeview(frame_notas, columns=("Disciplina", "Data", "Descrição", "Máximo", "Obtido"), show="headings")
        tree_notas.heading("Disciplina", text="Disciplina")
        tree_notas.heading("Data", text="Data")
        tree_notas.heading("Descrição", text="Descrição")
        tree_notas.heading("Máximo", text="Máximo")
        tree_notas.heading("Obtido", text="Obtido")
        tree_notas.pack(fill="both", expand=True)
 
        for n in notas:
            tree_notas.insert("", "end", values=(n["titulo"], n["data"], n["descricao"], n["valor_maximo"], n["valor_obtido"]))
 
        # ----------------- ABA CREDENCIAIS -----------------
        frame_cred = ttk.Frame(notebook)
        notebook.add(frame_cred, text="Credenciais")
 
        tree_cred = ttk.Treeview(frame_cred, columns=("Titulo", "Credencial"), show="headings")
        tree_cred.heading("Titulo", text="Título")
        tree_cred.heading("Credencial", text="Credencial")
        tree_cred.pack(fill="both", expand=True)
 
        for c in credenciais:
            tree_cred.insert("", "end", values=(c["Titulo"], c["Credencial"]))
 
        # ----------------- ABA ATIVIDADES COMPLEMENTARES -----------------
        frame_ativ = ttk.Frame(notebook)
        notebook.add(frame_ativ, text="Horas Complementares")
 
        tree_ativ = ttk.Treeview(frame_ativ, columns=("Campo", "Valor"), show="headings")
        tree_ativ.heading("Campo", text="Campo")
        tree_ativ.heading("Valor", text="Valor")
        tree_ativ.column("Campo", width=300)
        tree_ativ.column("Valor", width=200)
        tree_ativ.pack(fill="both", expand=True)
 
        labels = {
            "minimo_horas_exigidas": "Mínimo de horas exigidas",
            "total_horas_cumpridas": "Total de horas cumpridas",
            "horas_a_cumprir": "Horas a cumprir",
            "data_ultimo_lancamento": "Data do último lançamento"
        }
 
        for chave, label in labels.items():
            valor = atividades.get(chave) or "Não encontrado"
            tree_ativ.insert("", "end", values=(label, valor))
 
        root.mainloop()
 
if __name__ == "__main__":
    spider = FaltasSpider()
    spider.start_requests()
    spider.criar_interface_tkinter()