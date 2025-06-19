from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from bs4 import BeautifulSoup
import re

# Função de log: imprime no console e salva em log.txt
def log(msg):
    # print(msg)
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def fechar_banner_cookies(driver):
    try:
        log("[COOKIES] Tentando aceitar cookies...")
        botao_aceitar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        botao_aceitar.click()
        log("[COOKIES] Cookies aceitos")
    except:
        log("[COOKIES] Banner de cookies não encontrado ou já fechado.")

def extrair_nome_disciplina(td_element):
    try:
        log("[DISCIPLINA] Extraindo nome da disciplina...")
        html = td_element.get_attribute("innerHTML")
        soup = BeautifulSoup(html, "html.parser")
        h5 = soup.find("h5", class_="modal-title")
        if h5:
            nome = h5.text.strip()
            log(f"[DISCIPLINA] Nome extraído: {nome}")
            return nome
        a_tags = soup.find_all("a")
        for a in a_tags:
            texto = a.get_text(strip=True)
            if texto and texto != "Requisito(s)":
                log(f"[DISCIPLINA] Nome extraído via <a>: {texto}")
                return texto
    except:
        log("[DISCIPLINA] Erro ao extrair nome da disciplina")
    return "Não informado"

def extrair_ementa(td_element):
    try:
        log("[EMENTA] Extraindo ementa...")
        ementa = td_element.find_element(By.TAG_NAME, "input").get_attribute("value").strip()
        log(f"[EMENTA] Ementa extraída: {ementa[:100]}")  # Limita para 100 caracteres no log
        return ementa
    except:
        log("[EMENTA] Ementa não disponível")
        return "Ementa não disponível"

def extrair_carga_horaria(td_element):
    try:
        log("[CARGA HORÁRIA] Extraindo carga horária...")
        carga = td_element.get_attribute("innerText").strip()
        log(f"[CARGA HORÁRIA] Carga horária extraída: {carga}")
        return carga if carga else "Não informada"
    except:
        log("[CARGA HORÁRIA] Erro ao extrair carga horária")
        return "Não informada"

def extrair_requisitos(td_element):
    try:
        log("[REQUISITOS] Buscando input dentro do td...")
        inputs = td_element.find_elements(By.TAG_NAME, "input")
        if not inputs:
            log("[REQUISITOS] Nenhum input encontrado. Buscando texto direto...")
            texto = td_element.text.strip()
            if texto:
                log(f"[REQUISITOS] Texto direto encontrado: {texto}")
                return texto
            else:
                log("[REQUISITOS] Nenhum texto direto também.")
                return "Nenhum requisito"

        requisito_html = inputs[0].get_attribute("value")
        log(f"[REQUISITOS] HTML dentro do input: {requisito_html[:200]} ...")

        soup = BeautifulSoup(requisito_html, "html.parser")
        requisitos_li = soup.find_all("li")
        textos = [
            li.get_text(strip=True)
            for li in requisitos_li
            if li.get_text(strip=True) and li.get_text(strip=True) != "--"
        ]
        log(f"[REQUISITOS] Textos extraídos: {textos}")

        return "; ".join(textos) if textos else "Nenhum requisito"
    except Exception as e:
        log(f"[REQUISITOS] Erro ao extrair requisitos: {e}")
        return "Nenhum requisito"

def limpar_texto(texto):
    texto = re.sub(r"\s+", " ", texto)        # múltiplos espaços para um só
    texto = re.sub(r"\s*/\s*", "/", texto)    # remove espaço antes/depois da barra
    texto = texto.strip()
    return texto

def extrair_docentes(td_element):
    try:
        log("[DOCENTES] Iniciando extração de docentes...")
        html = td_element.get_attribute("innerHTML")
        soup = BeautifulSoup(html, "html.parser")
        resultado = []

        secao_atual = None
        for el in soup.find_all(["strong", "li"]):
            if el.name == "strong":
                texto_raw = el.get_text()
                texto_limpo = re.sub(r"\s+", " ", texto_raw).strip()
                texto_sem_espacos_antes_dos_pontos = re.sub(r"\s+:", ":", texto_limpo)
                secao_atual = texto_sem_espacos_antes_dos_pontos.upper()
                resultado.append(f"{secao_atual}")
            elif el.name == "li":
                input_tag = el.find("input", type="hidden")
                if input_tag and input_tag.has_attr("value"):
                    detalhes_html = input_tag["value"]
                    detalhes_soup = BeautifulSoup(detalhes_html, "html.parser")
                    paragrafos = [
                        limpar_texto(p.get_text(strip=True))
                        for p in detalhes_soup.find_all("p")
                        if p.get_text(strip=True).lower() not in ["fechar", "enviar"]
                    ]
                    if paragrafos:
                        resultado.append("\n".join(paragrafos))
                else:
                    texto = el.get_text(strip=True)
                    texto = limpar_texto(texto)
                    if texto and texto.lower() not in ["fechar", "enviar", "×"]:
                        resultado.append(texto)

        log("[DOCENTES] Extração concluída.")
        return "\n\n".join(resultado) if resultado else "Docente não informado"
    except Exception as e:
        log(f"[DOCENTES] Erro ao extrair docentes: {e}")
        return f"Erro ao extrair docentes: {e}"

def expandir_painel_noite(driver):
    log("[PAINEL NOITE] Tentando localizar painel 'NOITE'...")

    headers = driver.find_elements(By.ID, "ui-id-3")
    if headers:
        header_noite = headers[0]
        log("[PAINEL NOITE] Painel 'NOITE' localizado com ID 'ui-id-3'.")

        aria_expanded = header_noite.get_attribute("aria-expanded")
        log(f"[PAINEL NOITE] Valor inicial de aria-expanded: {aria_expanded}")

        if aria_expanded == "false":
            log("[PAINEL NOITE] Painel 'NOITE' está colapsado. Tentando expandir...")
            header_noite.click()
            try:
                WebDriverWait(driver, 5).until(
                    lambda d: header_noite.get_attribute("aria-expanded") == "true"
                )
                log("[PAINEL NOITE] Painel 'NOITE' expandido com sucesso.")
            except:
                log("[PAINEL NOITE] Timeout esperando painel expandir, mas continuando execução.")
        else:
            log("[PAINEL NOITE] Painel 'NOITE' já está expandido ou sem atributo esperado. Continuando.")
    else:
        log("[PAINEL NOITE] Painel 'NOITE' com ID 'ui-id-3' não encontrado. Assumindo modo estático e continuando execução normalmente.")

def log_inicio_execucao():
    data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log(f"{'=' * 60} {data_atual} {'=' * 60}\n")
    log("[EXECUÇÃO] Iniciando a execução...")

def abrir_navegador_com_user_agent():
    options = Options()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    )
    return webdriver.Chrome(options=options)

def abrir_navegador():
    log("[EXECUÇÃO] Abrindo navegador...")
    driver = abrir_navegador_com_user_agent()
    log("[EXECUÇÃO] Navegador aberto.")
    return driver

def acessar_pagina(driver):
    url = "https://www.pucminas.br/campus/coracao-eucaristico/ensino/graduacao/Paginas/Engenharia-de-Software.aspx?curso=267"
    log(f"[EXECUÇÃO] Acessando página: {url}")
    driver.get(url)

def localizar_painel_noite(driver):
    log("[EXECUÇÃO] Tentando localizar conteúdo do painel NOITE...")
    painel_elements = driver.find_elements(By.ID, "ui-id-4")
    if painel_elements:
        log("[EXECUÇÃO] Painel 'ui-id-4' encontrado via ID.")
        return painel_elements[0]

    log("[EXECUÇÃO] Painel 'ui-id-4' não encontrado. Tentando localizar por <h3>NOITE</h3>...")
    headers = driver.find_elements(By.XPATH, "//h3[normalize-space()='NOITE']")
    if headers:
        try:
            painel = headers[0].find_element(By.XPATH, "following-sibling::div[1]")
            log("[EXECUÇÃO] Painel localizado após <h3>NOITE</h3>.")
            return painel
        except:
            log("[ERRO] <div> após <h3>NOITE</h3> não encontrado.")
            return None
    else:
        log("[ERRO] Nenhum cabeçalho <h3>NOITE</h3> encontrado.")
        return None

def processar_painel(painel):
    tabelas = painel.find_elements(By.CSS_SELECTOR, "table.tab_listagem_maiuscula_curso")
    periodos = painel.find_elements(By.CSS_SELECTOR, "h4.puc-pl-graduacao-periodo")
    log(f"[EXECUÇÃO] Encontrados {len(periodos)} períodos no painel NOITE.")

    for i in range(min(len(periodos), len(tabelas))):
        periodo = periodos[i].text.strip()
        tabela = tabelas[i]
        print(f"\n\n{'=' * 60} {periodo} {'=' * 60}")

        linhas = tabela.find_elements(By.TAG_NAME, "tr")[1:]
        log(f"[EXECUÇÃO] Encontradas {len(linhas)} disciplinas no período {periodo}.")

        for linha in linhas:
            processar_linha_disciplina(linha)

def processar_linha_disciplina(linha):
    colunas = linha.find_elements(By.TAG_NAME, "td")
    if len(colunas) < 4:
        log("[EXECUÇÃO] Linha com menos de 4 colunas. Ignorando.")
        return

    disciplina = extrair_nome_disciplina(colunas[0])
    ementa = extrair_ementa(colunas[0])
    carga_horaria = extrair_carga_horaria(colunas[1])
    requisitos = extrair_requisitos(colunas[2])
    docentes = extrair_docentes(colunas[3])

    print(f"\nDisciplina: {disciplina}")
    print(f"Ementa: {ementa}")
    print(f"Carga Horária: {carga_horaria}")
    print(f"Requisitos: {requisitos}")
    print(f"Corpo Docente:\n{docentes}")
    print("-" * 130)

def abrir_pagina():
    log_inicio_execucao()
    driver = abrir_navegador()
    acessar_pagina(driver)
    fechar_banner_cookies(driver)
    expandir_painel_noite(driver)

    painel = localizar_painel_noite(driver)
    if painel is None:
        driver.quit()
        return

    processar_painel(painel)
    # print(driver.page_source)
    input("Pressione Enter para fechar o navegador...")
    driver.quit()
    log("[EXECUÇÃO] Navegador fechado.")

if __name__ == "__main__":
    abrir_pagina()

# pip install selenium
# brew install chromedriver