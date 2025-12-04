# 🪄 Projeto Magic: The Gathering — Scryfall API Viewer

## 🚀 Sobre o projeto

Este projeto em Python permite buscar e exibir cartas de **Magic: The Gathering** diretamente da **Scryfall API**, a base de dados mais completa do jogo.  
Ele cria uma interface gráfica usando **Tkinter**, baixa imagens com **Pillow** e busca dados reais das cartas usando **requests**.  
É ideal para jogadores, colecionadores e desenvolvedores que desejam visualizar cartas rapidamente.

---

### 🔥 Capturas de Tela

| <img src="https://joaopauloaramuni.github.io/python-imgs/Scryfall/imgs/Ring.png" alt="Ring" width="250"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/Scryfall/imgs/Sauron.png" alt="Sauron" width="250"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/Scryfall/imgs/Sauron2.png" alt="Sauron2" width="250"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/Scryfall/imgs/Deadpool.png" alt="Deadpool" width="250"/> |
|:---:|:---:|:---:|:---:|
| 💍 **The One Ring - ltr/A-246** | 👁️‍🗨️ **Sauron - ltc/4** | 🗡️ **Sauron 2 - ltr/224** | 😜 **Deadpool - sld/1753** |

---

### 📦 Scryfall API

A **Scryfall API** é uma API gratuita e extremamente completa, oferecendo:

- Nome da carta  
- Tipo e subtipos  
- Raridade  
- Artista  
- Custo de mana  
- Texto Oracle  
- Poder e resistência  
- Imagens em alta resolução  
- Suporte a cartas dupla-face, transform, meld, etc.

---

### 🛠️ Bibliotecas utilizadas

- **requests** — Para realizar requisições HTTP ao Scryfall  
- **Pillow (PIL)** — Para abrir e exibir as imagens das cartas  
- **Tkinter** — Interface gráfica nativa do Python  

---

### 🌐 URL da API

A Scryfall permite duas formas principais de buscar cartas:

#### 🔹 Por UUID
```
https://api.scryfall.com/cards/{uuid}
```

#### 🔹 Por set + collector number (forma usada no projeto)
```
https://api.scryfall.com/cards/{set}/{collector_number}
```

Exemplo real usado no projeto:
```
https://api.scryfall.com/cards/ltr/A-246
```

---

### 🧙 Como buscar uma carta

O programa suporta referências no formato:

```python
show_card("ltr/A-246")   # Carta 'The One Ring'
```

Ou qualquer combinação válida de:

- **Código do set** (ex.: ltr, mh2, bro, neo, 2xm, khm…)  
- **Collector number** (com ou sem prefixos como A-, JP-, G-, etc.)  

---

### 📥 Dependências

Instale as dependências com:

```bash
pip install requests pillow
```

> Tkinter já vem instalado com o Python oficial.

---

## ⚙️ Ambiente virtual

Recomendado para manter dependências organizadas:

```bash
python -m venv .venv
```

### Ativar

**Windows**
```bash
.venv\Scripts\activate
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

---

## 📚 Documentação e links úteis

- 🌐 Scryfall — https://scryfall.com  
- 📘 Documentação da API — https://scryfall.com/docs/api  
- 🔍 Pesquisas avançadas — https://scryfall.com/docs/syntax  
- 🧪 Testar endpoints — https://api.scryfall.com/cards  

---

## 🪪 Licença

Este projeto está licenciado sob a **Licença MIT**.
