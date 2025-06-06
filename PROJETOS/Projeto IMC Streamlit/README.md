# 🧮 Calculadora de IMC com Streamlit

Este projeto é uma **Calculadora de IMC (Índice de Massa Corporal)** construída com [Streamlit](https://streamlit.io/), uma biblioteca Python voltada para a criação rápida de aplicações web interativas com foco em ciência de dados e protótipos.

---

## 🚀 O que é Streamlit?

[Streamlit](https://streamlit.io) é uma **ferramenta de front-end para Python** que permite criar **interfaces web de forma simples e rápida**, sem precisar mexer com HTML, CSS ou JavaScript.

Com poucos comandos, você transforma scripts Python em aplicações interativas acessíveis via navegador.

---

## 🔍 Diferença entre Streamlit e Tkinter

| Característica     | Streamlit 🌐                 | Tkinter 🖥️                 |
|--------------------|------------------------------|----------------------------|
| Interface          | Web (navegador)              | Desktop (aplicativo local) |
| Estilo visual      | Moderno, responsivo          | Mais simples e datado      |
| Instalação do usuário final | Nenhuma (roda no navegador) | Necessário instalar app    |
| Facilidade de uso  | Muito simples (foco em dados)| Mais trabalhoso            |
| Melhor para        | Protótipos, dashboards       | Interfaces locais simples  |

---

## Captura de tela:

| <img src="https://joaopauloaramuni.github.io/python-imgs/IMC_Streamlit/imgs/Home.png" alt="Home" width="800"/> |
|:--------------------:|
|         Home         |

---

## ✅ Funcionalidades

- Entrada de peso (kg) e altura (m)
- Cálculo automático do IMC
- Classificação do resultado:
  - Abaixo do peso
  - Peso normal
  - Sobrepeso
  - Obesidade
- Barra de progresso como feedback visual

---

## 📦 Dependências

- Python 3.7+
- [Streamlit](https://pypi.org/project/streamlit/)

### Instalação:

```bash
pip install streamlit
```

---

## 🧪 Ambiente Virtual (Recomendado)

### Passo 1: Criar e ativar o ambiente virtual

É recomendado criar um ambiente virtual para isolar as dependências do projeto. Para configurar o ambiente virtual:

1. **Criar o ambiente virtual**:
   ```bash
   python -m venv venv
   ```

2. **Ativar o ambiente virtual**:
   - No Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Passo 2: Executar o script

Após ativar o ambiente virtual, execute o script principal:
```bash
streamlit run imc_streamlit.py
```

---

## ▶️ Como executar

```bash
streamlit run imc_streamlit.py
```

Acesse no navegador: [http://localhost:8501](http://localhost:8501)

### 🧠 Por que não usar `python imc_streamlit.py`?

Executar diretamente com o comando:

```bash
python imc_streamlit.py
```

faz com que o código seja rodado como um script Python tradicional, **fora do ambiente interativo do Streamlit**. Isso pode causar mensagens de aviso como:

`missing ScriptRunContext! This warning can be ignored when running in bare mode.`

Ou até mesmo impedir o correto funcionamento da interface gráfica.

---

### ⚙️ O que acontece com `streamlit run imc_streamlit.py`

- 🧩 Um servidor local é iniciado automaticamente.
- 🌐 A aplicação é exibida no navegador, geralmente em `http://localhost:8501`.
- 🔁 A interface se atualiza automaticamente sempre que você salva o código.
- ✅ Toda a infraestrutura interativa do Streamlit (inputs, botões, visualização de dados) funciona corretamente.

---

## 📚 Documentação e links úteis

- [Documentação oficial do Streamlit](https://docs.streamlit.io/)
- [Guia rápido de Streamlit](https://docs.streamlit.io/streamlit-tutorial)
- [Calculadora de IMC - Wikipedia](https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal)

---

📘 Leia sobre o protocolo do Ministério da Saúde:

- [**PCDT Resumido de Sobrepeso e Obesidade**](PCDT_MS/PCDTResumidodeSobrepesoObesidade.pdf)

---

## ✨ Exemplo de uso

Digite seu peso e altura na interface e clique em **Calcular IMC**. Você verá o resultado e uma barra de progresso correspondente ao valor.

---

## 👨‍💻 Autor

Feito com ❤️ para fins educacionais.

---

## 🪪 Licença

Este projeto está licenciado sob a **Licença MIT**.
