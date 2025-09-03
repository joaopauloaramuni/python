import os
import requests
from bs4 import BeautifulSoup
import json
 
class FaltasSpider:
    login_url = 'https://www.sistemas.pucminas.br/sgaaluno4/SilverStream/Pages/pgAln_LoginSSL.html'
    formdata = {
        'AgEvtSrc': 'S124_',
        'AgStateCode': '7',
        'S50_': 'SUA MATRICULA',
        'S64_': 'SUA SENHA',
        'S78_': '9',
        'S219_': ''
    }
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'connection': 'keep-alive',
        'content-length': '74',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': '_gcl_au=1.1.566669173.1756326589; _fbp=fb.1.1756326589203.5074139852899606; _gid=GA1.2.612709533.1756895976; _clck=1b2cqbc%5E2%5Efz0%5E0%5E2065; JSESSIONID=0b5655b79c4b1dba1621cdfcc7868162; AlteonSession=ArKwQDIBAgqtY+xxOEmkEA$$; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Sep+03+2025+18%3A12%3A53+GMT-0300+(Hor%C3%A1rio+Padr%C3%A3o+de+Bras%C3%ADlia)&version=202507.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=393ebcdd-6437-4948-b522-05908c5801a3&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0005%3A0&AwaitingReconsent=false; _hjSessionUser_1550884=eyJpZCI6IjhmM2IzNmI4LTVkY2MtNWQ2Ni05NWY5LWY2NWUxN2U1MmZkMyIsImNyZWF0ZWQiOjE3NTY5MzM5NzQyNzQsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1550884=eyJpZCI6IjM1MzIzMzVjLTdmMzYtNDVjYS1iMGZhLTJhYzY0NjU4YmMyMSIsImMiOjE3NTY5MzM5NzQyNzUsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _ga_KWPYPZ923E=GS2.1.s1756933974$o5$g0$t1756933974$j60$l0$h0; _ga_D37LF6BXDH=GS2.1.s1756933974$o5$g0$t1756933974$j60$l0$h0; _ga_H2EHN44B05=GS2.1.s1756933974$o5$g0$t1756933974$j60$l0$h0; _ga_VWP0B7W5MB=GS2.1.s1756933974$o5$g0$t1756933974$j60$l0$h1603008975; _ga_ZFLF1RN8MD=GS2.1.s1756933974$o5$g0$t1756933974$j60$l0$h0; _clsk=ocvifs%5E1756933975619%5E1%5E1%5Ef.clarity.ms%2Fcollect; _ga=GA1.2.1474928918.1756326589; _gat=1; _dd_s=rum=0&expire=1756934974481',
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
        with requests.Session() as session:
            response = session.post(self.login_url, data=self.formdata, headers=self.headers)
            if "authentication failed" in response.text:
                print("Login failed")
                return
            self.after_login(response, session)
 
    def after_login(self, response, session):
        # Adiciona a requisição GET aqui
        basic_headers = {
            'accept': 'text/htmlextraapplication/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'connection': 'keep-alive',
            'cookie': '_gcl_au=1.1.566669173.1756326589; _fbp=fb.1.1756326589203.5074139852899606; _gid=GA1.2.612709533.1756895976; _clck=1b2cqbc%5E2%5Efz0%5E0%5E2065; JSESSIONID=0b5655b79c4b1dba1621cdfcc7868162; AlteonSession=ArKwQDIBAgqtY+xxOEmkEA$$; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Sep+03+2025+18%3A12%3A53+GMT-0300+(Hor%C3%A1rio+Padr%C3%A3o+de+Bras%C3%ADlia)&version=202507.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=393ebcdd-6437-4948-b522-05908c5801a3&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0005%3A0&AwaitingReconsent=false; _hjSessionUser_1550884=eyJpZCI6IjhmM2IzNmI4LTVkY2MtNWQ2Ni05NWY5LWY2NWUxN2U1MmZkMyIsImNyZWF0ZWQiOjE3NTY5MzM5NzQyNzQsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1550884=eyJpZCI6IjM1MzIzMzVjLTdmMzYtNDVjYS1iMGZhLTJhYzY0NjU4YmMyMSIsImMiOjE3NTY5MzM5NzQyNzUsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _ga_KWPYPZ923E=GS2.1.s1756933974$o5$g0$t1756933974$j60$l0$h0; _ga_D37LF6BXDH=GS2.1.s1756933974$o5$g0$t1756933974$j60$l0$h0; _ga_H2EHN44B05=GS2.1.s1756933974$o5$g0$t1756933974$j60$l0$h0; _ga_VWP0B7W5MB=GS2.1.s1756933974$o5$g0$t1756933974$j60$l0$h1603008975; _ga_ZFLF1RN8MD=GS2.1.s1756933974$o5$g0$t1756933974$j60$l0$h0; _clsk=ocvifs%5E1756933975619%5E1%5E1%5Ef.clarity.ms%2Fcollect; _ga=GA1.2.1474928918.1756326589; _gat=1; _dd_s=rum=0&expire=1756934974481',
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
        get_url = "https://www.sistemas.pucminas.br/sgaaluno4/SilverStream/Pages/pgAln_NotaFrequencia2.html"
        get_response = session.get(get_url, headers=basic_headers)
        
        # Salvar o HTML para debug
        with open('debug.html', 'w', encoding='utf-8') as f:
            f.write(get_response.text)
        
        soup = self.parse(get_response, session)
        self.extract_attendance_and_grades(soup)

        get_url = "https://www.sistemas.pucminas.br/sga4/SilverStream/Pages/pg_Credenciais.html"
        get_response = session.get(get_url, headers=basic_headers)

        soup = self.parse(get_response, session)
        self.extract_credentials(soup)
 
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
        

if __name__ == "__main__":
    spider = FaltasSpider()
    spider.start_requests()