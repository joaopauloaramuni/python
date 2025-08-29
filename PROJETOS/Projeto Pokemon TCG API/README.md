# 🃏 Projeto Pokémon TCG API

## 🚀 Sobre o projeto

Este projeto em Python permite buscar e exibir cartas de Pokémon diretamente da API oficial da Pokémon TCG. Ele cria uma interface gráfica simples com  **Tkinter** , baixa imagens de cartas usando **Pillow** e obtém informações detalhadas das cartas por meio da biblioteca  **requests** . É ideal para fãs de Pokémon e desenvolvedores que querem experimentar dados reais do TCG.

---

### 🔥 Capturas de Tela

| <img src="https://joaopauloaramuni.github.io/python-imgs/PokemonTCG/imgs/Charizard.png" alt="Charizard" width="250"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/PokemonTCG/imgs/Pikachu.png" alt="Pikachu" width="250"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/PokemonTCG/imgs/Mewtwo.png" alt="Mewtwo" width="250"/> | <img src="https://joaopauloaramuni.github.io/python-imgs/PokemonTCG/imgs/Bulbasaur.png" alt="Bulbasaur" width="250"/> |
|:---:|:---:|:---:|:---:|
| 🔥 **Charizard - swsh4-25** | ⚡ **Pikachu - smp-SM109** | 🧠 **Mewtwo - basep-3** | 🌱 **Bulbasaur - ex4-39** |

---

### 📦 Pokémon TCG API 

A Pokémon TCG API é uma API oficial que fornece informações detalhadas sobre cartas do Pokémon Trading Card Game. Com ela, é possível obter dados como:

* Nome e tipo da carta
* HP (pontos de vida)
* Ataques e habilidades
* Fraquezas e resistências
* Artista e raridade
* Imagens das cartas (pequenas ou grandes)

---

### 🛠️ Bibliotecas utilizadas

* **requests** : Permite fazer requisições HTTP para obter dados da API.
* **Pillow (PIL)** : Permite abrir, manipular e exibir imagens das cartas.
* **Tkinter** : Biblioteca padrão do Python para criar interfaces gráficas de maneira simples.

---

### 🔑 Criando uma API_KEY

Para acessar a Pokémon TCG API, você precisa de uma API_KEY:

1. Acesse o [Dashboard da Pokémon TCG API](https://dev.pokemontcg.io/dashboard).
2. Cadastre-se e confirme seu e-mail.
3. Deslogue e faça login novamente.
4. Copie a sua **API_KEY** e substitua no código do projeto.

---

### 🌐 URL da API

```python
API_URL = "https://api.pokemontcg.io/v2/cards/{}"
```

---

### 🕵️‍♂️ Como buscar um Pokémon

Você pode buscar cartas pelo ID ou pelo nome. Exemplo de busca pelo nome:

* [Charizard](https://api.pokemontcg.io/v2/cards?q=name:Charizard)

Exemplo de IDs de cartas para testar:

* swsh4-25 — Charizard 🔥
* smp-SM109 — Pikachu ⚡
* basep-3 — Mewtwo 🧠
* xy8-64 - Mewtwo-EX 🧠
* ex4-39 — Bulbasaur 🌱
* dp5-62 — Eevee ✨

---

### 📥 Dependências

Instale as bibliotecas necessárias com o pip:

```bash
pip install requests pillow
```

> O Tkinter já faz parte do Python padrão, então não precisa instalar.

---

## ⚙️ Ambiente virtual

É recomendado criar um ambiente virtual para isolar as dependências do projeto.

1. **Crie o ambiente virtual:**

```bash
python -m venv .venv
```

2. **Ative o ambiente virtual:**

* **Windows:**

```bash
.venv\Scripts\activate
```

* **Linux/macOS:**

```bash
source .venv/bin/activate
```

---

## 📚 Documentação e links úteis

* [GitHub Pokémon TCG](https://github.com/PokemonTCG)
* [Pokémon TCG](https://pokemontcg.io/)
* [Documentação da API](https://docs.pokemontcg.io/getting-started/authentication)
* [Dashboard da API](https://dev.pokemontcg.io/dashboard)
* [API Developers](https://dev.pokemontcg.io/)
* [Pokemon Card](https://pokemoncard.io/)

---

## 🪪 Licença

Este projeto está licenciado sob a **Licença MIT**.
