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
        'cookie': 'JSESSIONID=da0ca35df886b6c0889cf9af58b44e44; _ga_0TJQPCZ48T=GS1.1.1725372738.1.1.1725373330.0.0.0; _ga_DN8V9JG2C4=GS1.1.1725373656.1.0.1725373658.0.0.0; _ga_WVMD6PTDMQ=GS1.1.1725373512.3.1.1725375790.0.0.0; _ga_SCEMZGCYKZ=GS1.1.1725373512.3.1.1725375790.0.0.0; _ga_26QEFB1Y29=GS1.1.1731332633.2.1.1731332715.0.0.0; _hjSessionUser_1550884=eyJpZCI6IjZlZDNkZDVlLTk4NzEtNTM0ZC1iYWU4LWQ3N2E1MDA3OWJiNiIsImNyZWF0ZWQiOjE3MzE1OTQyNDUzNzcsImV4aXN0aW5nIjp0cnVlfQ==; _ga_D37LF6BXDH=GS1.1.1732026485.7.0.1732026485.0.0.0; _ga_LRYPTM2EJ3=GS1.1.1732026485.5.0.1732026485.0.0.0; _ga_LJ2M29EH7V=GS1.1.1739205996.8.0.1739205998.0.0.0; _ga_X68HE3G4D0=GS1.1.1740436938.8.1.1740437068.0.0.0; _ga_J83V3696B9=GS1.1.1740519740.13.0.1740519740.0.0.0; _ga_N6FD3Q0PJD=GS1.1.1740519740.19.0.1740519740.0.0.0; _gcl_au=1.1.1359516055.1741700610; _clck=1qsiu3j%7C2%7Cfu4%7C0%7C1702; tt.u=0100007F043ED067CC06C21B027B8707; _ttuu.s=1741700623526; _ga_H2EHN44B05=GS1.1.1741700610.8.1.1741700642.28.0.0; _ga_KWPYPZ923E=GS1.1.1741700610.8.1.1741700642.0.0.0; _ga_ZFLF1RN8MD=GS1.1.1741700610.6.1.1741700642.0.0.0; _ga_VWP0B7W5MB=GS1.1.1741700610.6.1.1741700642.28.0.1817347834; _ga=GA1.2.460504609.1691065328; _gid=GA1.2.1475727565.1743108935; AlteonSession=AZzaQTIBAgrzTWFztIFSKA$$; _gat=1; _dd_s=rum=2&id=ab09acee-772a-4778-8bc7-7e0425d55553&created=1743160137982&expire=1743161548267',
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
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'connection': 'keep-alive',
            'cookie': 'JSESSIONID=da0ca35df886b6c0889cf9af58b44e44; _ga_0TJQPCZ48T=GS1.1.1725372738.1.1.1725373330.0.0.0; _ga_DN8V9JG2C4=GS1.1.1725373656.1.0.1725373658.0.0.0; _ga_WVMD6PTDMQ=GS1.1.1725373512.3.1.1725375790.0.0.0; _ga_SCEMZGCYKZ=GS1.1.1725373512.3.1.1725375790.0.0.0; _ga_26QEFB1Y29=GS1.1.1731332633.2.1.1731332715.0.0.0; _hjSessionUser_1550884=eyJpZCI6IjZlZDNkZDVlLTk4NzEtNTM0ZC1iYWU4LWQ3N2E1MDA3OWJiNiIsImNyZWF0ZWQiOjE3MzE1OTQyNDUzNzcsImV4aXN0aW5nIjp0cnVlfQ==; _ga_D37LF6BXDH=GS1.1.1732026485.7.0.1732026485.0.0.0; _ga_LRYPTM2EJ3=GS1.1.1732026485.5.0.1732026485.0.0.0; _ga_LJ2M29EH7V=GS1.1.1739205996.8.0.1739205998.0.0.0; _ga_X68HE3G4D0=GS1.1.1740436938.8.1.1740437068.0.0.0; _ga_J83V3696B9=GS1.1.1740519740.13.0.1740519740.0.0.0; _ga_N6FD3Q0PJD=GS1.1.1740519740.19.0.1740519740.0.0.0; _gcl_au=1.1.1359516055.1741700610; _clck=1qsiu3j%7C2%7Cfu4%7C0%7C1702; tt.u=0100007F043ED067CC06C21B027B8707; _ttuu.s=1741700623526; _ga_H2EHN44B05=GS1.1.1741700610.8.1.1741700642.28.0.0; _ga_KWPYPZ923E=GS1.1.1741700610.8.1.1741700642.0.0.0; _ga_ZFLF1RN8MD=GS1.1.1741700610.6.1.1741700642.0.0.0; _ga_VWP0B7W5MB=GS1.1.1741700610.6.1.1741700642.28.0.1817347834; AlteonSession=AXbnQjIBAgrhT4sx/8kUPg$$; _ga=GA1.2.460504609.1691065328; _gid=GA1.2.1475727565.1743108935; _dd_s=rum=0&expire=1743110091624',
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
        
        self.parse(get_response, session)
 
    def parse(self, response, session):
        # Parsing com BeautifulSoup
        soup = BeautifulSoup(response.text, 'lxml')
        self.extract_attendance_and_grades(soup)
   
    def extract_attendance_and_grades(self, soup):
        # Encontrando o elemento com a classe "class1"
        classe_pai = soup.find('span', class_='class1')
   
        # Encontrando todas as tabelas com a classe "smc" dentro do elemento "class1"
        tabelas = classe_pai.find_all('table', class_='smc-sgagrad-agrupamento-primario') if classe_pai else []
        
        # Listas para armazenar faltas e notas
        materias_faltas = []
        notas = []
        
        # Extraindo faltas
        for idx, tabela in enumerate(tabelas, start=1):
            primeira_tr = tabela.find('tr')
            if primeira_tr:
                tds = primeira_tr.find_all('td')
                valores = [td.get_text(strip=True).replace('\n', ' ') for td in tds]
                materias_faltas.append(valores)
        
        # NOVA ABORDAGEM PARA EXTRAIR NOTAS
        # Vamos usar o mesmo método original, mas com um controle para evitar duplicações
        
        # Conjunto para armazenar notas já processadas
        notas_processadas = set()
        
        # Encontrando todas as células com a classe "smc-grid-totalizador"
        total_cells = soup.find_all('td', class_='smc-grid-totalizador')
        
        # Vamos processar em grupos de 4 (assumindo que cada nota tem 4 colunas)
        # Isso ajuda a agrupar as células corretamente mesmo se houver várias tabelas
        i = 0
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
                    "data": data,
                    "descricao": descricao,
                    "valor_maximo": valor_max,
                    "valor_obtido": valor_obtido
                }
                notas.append(nota)
                notas_processadas.add(nota_key)
            
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
 
if __name__ == "__main__":
    spider = FaltasSpider()
    spider.start_requests()
