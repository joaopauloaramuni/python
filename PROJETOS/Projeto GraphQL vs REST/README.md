# 🚀 Projeto GraphQL vs REST

Este projeto tem como objetivo **comparar o tempo de resposta** entre duas requisições feitas para a API do GitHub: uma usando **GraphQL** e outra usando **REST**.  
Ele mede e calcula o tempo médio de execução para identificar qual abordagem é mais rápida.

---

## 📖 O que é GraphQL?
**GraphQL** é uma linguagem de consulta para APIs desenvolvida pelo Facebook.  
Ela permite que o cliente **especifique exatamente** quais dados deseja receber, reduzindo sobrecarga e evitando dados desnecessários.  
- 📌 Vantagem: Reduz chamadas à API e diminui transferência de dados.  
- 📌 Desvantagem: Pode ser mais complexo de implementar no backend.  

## 📖 O que é REST?
**REST** (Representational State Transfer) é um estilo de arquitetura que usa requisições HTTP para acessar e manipular recursos.  
Cada endpoint geralmente retorna **dados fixos**, podendo incluir informações que o cliente não precisa.  
- 📌 Vantagem: Simples e amplamente suportado.  
- 📌 Desvantagem: Pode gerar excesso de dados em uma única chamada.

---

## 🆚 Quando usar GraphQL ou REST?

✅ **Use GraphQL quando:**  
- O cliente precisa de **dados personalizados**.  
- Há necessidade de reduzir a quantidade de chamadas à API.  
- O sistema consome dados de múltiplas fontes que precisam ser agregados.  

✅ **Use REST quando:**  
- O consumo de dados é **simples** e previsível.  
- A API já está estruturada e otimizada.  
- Deseja maior **compatibilidade** com bibliotecas e ferramentas existentes.

---

## 📦 Dependências

- `requests`

Para instalar:  
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

```text
Executando 10 requisições REST...
Executando 10 requisições GraphQL...

--- RESULTADOS ---
Tempo médio REST: 0.3830 segundos
Tempo médio GraphQL: 0.3011 segundos
✅ GraphQL foi mais rápido.
```

---

## 📚 Documentação e links úteis

- [📌 GitHub API (REST)](https://docs.github.com/en/rest)
- [📌 GitHub Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [📌 GitHub GraphQL API](https://docs.github.com/en/graphql)

---

## 📜 Licença

Este projeto está licenciado sob a licença **MIT**.
