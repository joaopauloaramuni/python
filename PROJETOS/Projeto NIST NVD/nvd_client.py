import requests
import pandas as pd
from typing import Dict, Any, List, Optional

# URLs base da API NVD
BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
HISTORY_URL = "https://services.nvd.nist.gov/rest/json/cvehistory/2.0"


# ---------------------------
# Funções de busca na API
# ---------------------------

def fetch_cves(params: Dict[str, Any]) -> Dict[str, Any]:
    """Função genérica para buscar CVEs usando parâmetros."""
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()


def fetch_cve_by_id(cve_id: str) -> Dict[str, Any]:
    """Retorna detalhes de um CVE específico."""
    return fetch_cves({"cveId": cve_id})


def fetch_cves_by_cpe(cpe_name: str, is_vulnerable: bool = False) -> Dict[str, Any]:
    """Retorna CVEs associados a um CPE específico."""
    params = {"cpeName": cpe_name}
    if is_vulnerable:
        params["isVulnerable"] = ""
    return fetch_cves(params)


def fetch_cves_by_keyword(keyword: str, exact_match: bool = False) -> Dict[str, Any]:
    """Retorna CVEs que contenham uma palavra-chave na descrição."""
    params = {"keywordSearch": keyword}
    if exact_match:
        params["keywordExactMatch"] = ""
    return fetch_cves(params)


def fetch_cves_by_date(pub_start: str, pub_end: str) -> Dict[str, Any]:
    """Retorna CVEs publicados em um intervalo de datas."""
    params = {"pubStartDate": pub_start, "pubEndDate": pub_end}
    return fetch_cves(params)


def fetch_paginated_cves(results_per_page: int = 20, max_pages: int = 1) -> List[Dict[str, Any]]:
    """Busca CVEs de forma paginada."""
    all_cves = []
    start_index = 0

    for _ in range(max_pages):
        params = {"resultsPerPage": results_per_page, "startIndex": start_index}
        data = fetch_cves(params)

        if "vulnerabilities" not in data:
            break

        all_cves.extend(data["vulnerabilities"])
        start_index += results_per_page

        if start_index >= data.get("totalResults", 0):
            break

    return all_cves


def fetch_cve_history(cve_id: Optional[str] = None,
                      change_start: Optional[str] = None,
                      change_end: Optional[str] = None) -> Dict[str, Any]:
    """Retorna histórico de mudanças de um CVE ou dentro de um intervalo de datas."""
    params = {}
    if cve_id:
        params["cveId"] = cve_id
    if change_start and change_end:
        params["changeStartDate"] = change_start
        params["changeEndDate"] = change_end

    response = requests.get(HISTORY_URL, params=params)
    response.raise_for_status()
    return response.json()


# ---------------------------
# Funções de parsing e análise
# ---------------------------

def parse_cve(cve: Dict[str, Any]) -> Dict[str, Any]:
    """Extrai informações úteis de um CVE bruto da NVD."""
    cve_id = cve.get("cve", {}).get("id", "")
    published = cve.get("cve", {}).get("published", "")
    last_modified = cve.get("cve", {}).get("lastModified", "")

    # Descrição (primeira em inglês, se existir)
    descriptions = cve.get("cve", {}).get("descriptions", [])
    description = ""
    for d in descriptions:
        if d.get("lang") == "en":
            description = d.get("value")
            break

    # Métricas CVSS
    metrics = cve.get("cve", {}).get("metrics", {})
    cvss_score = None
    severity = None

    if "cvssMetricV31" in metrics:
        metric = metrics["cvssMetricV31"][0]["cvssData"]
        cvss_score = metric.get("baseScore")
        severity = metric.get("baseSeverity")
    elif "cvssMetricV2" in metrics:
        metric = metrics["cvssMetricV2"][0]["cvssData"]
        cvss_score = metric.get("baseScore")
        severity = metric.get("baseSeverity")

    # CWE
    weaknesses = cve.get("cve", {}).get("weaknesses", [])
    cwe_ids = [w["description"][0]["value"] for w in weaknesses if "description" in w]

    # Referências
    refs = cve.get("cve", {}).get("references", [])
    ref_urls = [r["url"] for r in refs]

    return {
        "id": cve_id,
        "published": published,
        "last_modified": last_modified,
        "description": description,
        "cvss_score": cvss_score,
        "severity": severity,
        "cwe_ids": cwe_ids,
        "references": ref_urls
    }


def cves_to_dataframe(cves: List[Dict[str, Any]]) -> pd.DataFrame:
    """Converte uma lista de CVEs simplificados em DataFrame para análise."""
    simplified = [parse_cve(v) for v in cves]
    return pd.DataFrame(simplified)


# ---------------------------
# Exemplo de uso
# ---------------------------
if __name__ == "__main__":
    # Buscar CVEs por palavra-chave
    raw_data = fetch_cves_by_keyword("Microsoft", exact_match=False)

    if "vulnerabilities" in raw_data:
        cves = raw_data["vulnerabilities"]

        # Converter para DataFrame
        df = cves_to_dataframe(cves)

        # Mostrar primeiras linhas
        print(df.head())

        # Exportar para Excel
        df.to_excel("cves_microsoft.xlsx", index=False)
        print("Arquivo 'cves_microsoft.xlsx' gerado com sucesso!")
