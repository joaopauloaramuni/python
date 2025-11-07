# 📍 Projeto IBGE Locations

Este projeto é um script Python que permite consultar as APIs públicas do IBGE.

---

## 📦 Sobre as versões do projeto

### 🧩 Versão 1 (v1)

Na primeira versão, o projeto utilizava apenas a **API de Localidades**, oferecendo as seguintes funcionalidades:

1. Listar todos os estados (UFs) do Brasil.  
2. Listar todos os municípios de um estado específico, informando a sigla da UF.  

Essa versão era voltada principalmente para **análises geográficas** e **aplicações de geolocalização**.

---

### 🚀 Versão 2 (v2)

Na segunda versão, o projeto foi expandido para incluir também a **API de Agregados (v3)** do IBGE, adicionando uma nova funcionalidade:

3. Consultar a **população residente estimada (senso 2025)** de qualquer estado (UF) do Brasil.  

Com isso, o projeto passou a ser útil não apenas para geolocalização, mas também para **análises populacionais**, **integrações com dashboards** e **sistemas baseados em dados oficiais do IBGE**.

---

## 🔗 APIs utilizadas

- **API de Localidades (versão 1):**
  - [https://servicodados.ibge.gov.br/api/v1/localidades](https://servicodados.ibge.gov.br/api/v1/localidades)  
- **API de Agregados (versão 2):**
  - [https://servicodados.ibge.gov.br/api/v3/agregados](https://servicodados.ibge.gov.br/api/v3/agregados)

### 🌐 Exemplos de uso:

- **API de Localidades (versão 1):**
  - [https://servicodados.ibge.gov.br/api/v1/localidades/estados/MG/municipios](https://servicodados.ibge.gov.br/api/v1/localidades/estados/MG/municipios)
- **API de Agregados (versão 2):**
  - População estimada por UF: [https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2025/variaveis/9324?localidades=N3[31]](https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2025/variaveis/9324?localidades=N3[31])
  - PIB Nominal por UF: [https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/2021/variaveis/37?localidades=N3[31]](https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/2021/variaveis/37?localidades=N3[31])

---

## 📦 Instalação das Dependências

Para rodar este projeto, instale as bibliotecas necessárias usando o comando:

```bash
pip install requests
```

---

## ⚙️ Ambiente virtual

Para usar este projeto, recomendamos criar e ativar um ambiente virtual Python:

```bash
# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente virtual

# Windows:
.venv\Scripts\activate

# Linux/macOS:
source .venv/bin/activate
```

---

## 🖥️ Exemplo de saída no terminal

### v1

```bash
(.venv) (base) joaopauloaramuni@MacBook-Pro-de-Joao Projeto IBGE Locations % python ibge.py
Buscando todos os estados...
RO - Rondônia
AC - Acre
AM - Amazonas
RR - Roraima
PA - Pará
AP - Amapá
TO - Tocantins
MA - Maranhão
PI - Piauí
CE - Ceará
RN - Rio Grande do Norte
PB - Paraíba
PE - Pernambuco
AL - Alagoas
SE - Sergipe
BA - Bahia
MG - Minas Gerais
ES - Espírito Santo
RJ - Rio de Janeiro
SP - São Paulo
PR - Paraná
SC - Santa Catarina
RS - Rio Grande do Sul
MS - Mato Grosso do Sul
MT - Mato Grosso
GO - Goiás
DF - Distrito Federal

Digite a sigla do estado para listar seus municípios: MG

Municípios de MG:
Abadia dos Dourados
Abaeté
Abre Campo
Acaiaca
Açucena
Água Boa
Água Comprida
Aguanil
...
```

### v2

```bash
(.venv) (base) joaopauloaramuni@MacBook-Pro-de-Joao Projeto IBGE Locations % python ibge.py
Buscando todos os estados...
RO - Rondônia
AC - Acre
AM - Amazonas
RR - Roraima
PA - Pará
AP - Amapá
TO - Tocantins
MA - Maranhão
PI - Piauí
CE - Ceará
RN - Rio Grande do Norte
PB - Paraíba
PE - Pernambuco
AL - Alagoas
SE - Sergipe
BA - Bahia
MG - Minas Gerais
ES - Espírito Santo
RJ - Rio de Janeiro
SP - São Paulo
PR - Paraná
SC - Santa Catarina
RS - Rio Grande do Sul
MS - Mato Grosso do Sul
MT - Mato Grosso
GO - Goiás
DF - Distrito Federal

Digite a sigla do estado para listar seus municípios: MG

Municípios de MG:
Abadia dos Dourados
Abaeté
Abre Campo
Acaiaca
Açucena
Água Boa
Água Comprida
Aguanil

População residente estimada de Minas Gerais (2025): 21,393,441 pessoas
...
```

Para SP:
```
População residente estimada de São Paulo (2025): 46,081,801 pessoas
```

---

## 📄 Documentação e Links úteis

### v1 - 🌎 API de Localidades do IBGE
- **Documentação:** [https://servicodados.ibge.gov.br/api/docs/localidades](https://servicodados.ibge.gov.br/api/docs/localidades)
- **Base URL:** [https://servicodados.ibge.gov.br/api/v1/localidades](https://servicodados.ibge.gov.br/api/v1/localidades)

### v2 - 📊 API de Agregados do IBGE
- **Documentação:** [https://servicodados.ibge.gov.br/api/docs/agregados?versao=3](https://servicodados.ibge.gov.br/api/docs/agregados?versao=3)
- **Base URL:** [https://servicodados.ibge.gov.br/api/v3/agregados](https://servicodados.ibge.gov.br/api/v3/agregados)

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests. 

Agradecimentos especiais pelas contribuições

* v2 -> Aramuni, Diogo Brunoro - [https://github.com/DiogoBrunoro](https://github.com/DiogoBrunoro) e Filipe Faria Melo - [https://github.com/ffmelo-coder](https://github.com/ffmelo-coder)

Projeto desenvolvido durante as **Oficinas do DevLabs** para o curso de **Engenharia de Software** da **PUC Minas**.

---

## 📝 Licença

Este projeto está licenciado sob a Licença MIT.
