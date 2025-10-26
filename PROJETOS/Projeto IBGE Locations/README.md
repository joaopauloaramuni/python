# 📍 Projeto IBGE Locations

Este projeto é um script Python que permite consultar a API de localidades do IBGE. Ele possui duas funcionalidades principais:

1. Listar todos os estados (UFs) do Brasil.
2. Listar todos os municípios de um estado específico, informando a sigla do UF.

O projeto é útil para análise de dados geográficos, aplicações de geolocalização, ou para qualquer cenário em que seja necessário ter acesso às localidades do Brasil.

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

---

## 📄 Documentação e Links úteis

* [API de Localidades do IBGE](https://servicodados.ibge.gov.br/api/docs/localidades)

---

## 📝 Licença

Este projeto está licenciado sob a Licença MIT.
