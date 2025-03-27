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
        'cookie': '_ga_H2EHN44B05=GS1.1.1721773819.4.1.1721773850.29.0.0; _ga_KWPYPZ923E=GS1.1.1721773819.4.1.1721773850.0.0.0; _ga_ZFLF1RN8MD=GS1.1.1721773819.2.1.1721773850.0.0.0; _ga_VWP0B7W5MB=GS1.1.1721773819.2.1.1721773850.29.0.1827824156; _ga=GA1.2.1052199836.1700858459; JSESSIONID=e75de7eedd9085b378bc320db5a1a6f9; _gid=GA1.2.1439983255.1733969187; AlteonSession=AqzQRDIBAgqvHCtCMB5rWQ$$; OptanonAlertBoxClosed=2024-12-12T20:32:06.595Z; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Dec+12+2024+17%3A44%3A22+GMT-0300+(Hor%C3%A1rio+Padr%C3%A3o+de+Bras%C3%ADlia)&version=202409.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=64dea044-d25b-48c3-a976-a246c1a2214f&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0005%3A0&AwaitingReconsent=false&intType=3&geolocation=BR%3BMG; _gat=1',
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
            'cookie': '_ga_H2EHN44B05=GS1.1.1721773819.4.1.1721773850.29.0.0; _ga_KWPYPZ923E=GS1.1.1721773819.4.1.1721773850.0.0.0; _ga_ZFLF1RN8MD=GS1.1.1721773819.2.1.1721773850.0.0.0; _ga_VWP0B7W5MB=GS1.1.1721773819.2.1.1721773850.29.0.1827824156; _ga=GA1.2.1052199836.1700858459; JSESSIONID=e75de7eedd9085b378bc320db5a1a6f9; _gid=GA1.2.1439983255.1733969187; AlteonSession=AqzQRDIBAgqvHCtCMB5rWQ$$; OptanonAlertBoxClosed=2024-12-12T20:32:06.595Z; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Dec+12+2024+17%3A44%3A22+GMT-0300+(Hor%C3%A1rio+Padr%C3%A3o+de+Bras%C3%ADlia)&version=202409.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=64dea044-d25b-48c3-a976-a246c1a2214f&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0005%3A0&AwaitingReconsent=false&intType=3&geolocation=BR%3BMG; _gat=1',
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
        self.parse(get_response, session)
 
    def parse(self, response, session):
        # Exemplo de parsing com BeautifulSoup
        soup = BeautifulSoup(response.text, 'lxml')
        # Adicione seu código de parsing aqui
        self.create_json(soup)
        pass
   
    def create_json(self, soup):
        materias = []
       
        # Encontrando o elemento com a classe "class1"
        classe_pai = soup.find('span', class_='class1')
   
        # Encontrando todas as tabelas com a classe "smc" dentro do elemento "class1"
        tabelas = classe_pai.find_all('table', class_='smc-sgagrad-agrupamento-primario') if classe_pai else []
        print(len(tabelas))
   
        # Exibindo as tabelas encontradas e pegando o texto do primeiro <td> da primeira <tr>
        for idx, tabela in enumerate(tabelas, start=1):
            primeira_tr = tabela.find('tr')
            if primeira_tr:
                tds = primeira_tr.find_all('td')
                valores = [td.get_text(strip=True).replace('\n', ' ') for td in tds]
                print(f"Tabela {idx} - Valores encontrados na primeira linha: {valores}")
                materias.append(valores)
 
        with open('faltas.json', 'w', encoding='utf-8') as f:
            json.dump(materias, f, ensure_ascii=False, indent=4)
 
if __name__ == "__main__":
    spider = FaltasSpider()
    spider.start_requests()
