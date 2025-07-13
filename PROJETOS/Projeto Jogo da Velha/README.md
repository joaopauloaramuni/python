# 🎮 Projeto Jogo da Velha (Tic-tac-toe)

Este é um projeto simples de **Jogo da Velha (Tic-tac-toe)** desenvolvido em **Python** utilizando a biblioteca **Pygame**. Ele permite que o jogador humano jogue contra a máquina, com placar, reinício automático da partida e uma linha indicando a vitória.

---

## 🎮 O que é o Pygame?

**Pygame** é uma biblioteca popular para desenvolvimento de jogos em Python que fornece funcionalidades para manipular gráficos, sons e eventos de entrada, permitindo criar jogos 2D de forma simples e eficiente. Com Pygame, é possível desenvolver desde jogos simples até projetos mais complexos com animações e interatividade.

---

## 📜 História do Jogo da Velha (Tic-tac-toe)

O **Jogo da Velha**, conhecido como **Tic-tac-toe** em inglês, é um jogo de estratégia simples geralmente jogado em papel. Suas origens remontam ao Império Romano, onde já era praticado de forma rudimentar. É um jogo de dois jogadores onde cada um marca uma célula de uma grade 3x3 com seu símbolo (X ou O), tentando formar uma linha reta horizontal, vertical ou diagonal.

### 🎯 Dinâmica do jogo

Neste projeto:

- O jogador humano joga com **X**.
- A máquina joga com **O**.
- Quando uma vitória acontece, uma **linha vermelha** aparece sobre a combinação vencedora.
- O placar é atualizado a cada partida.
- O jogo reinicia automaticamente após **3 segundos**, ou manualmente com a tecla **R**.

### 🤖 Inteligência da Máquina

A inteligência artificial da máquina utiliza uma **estratégia aleatória**: ela escolhe aleatoriamente uma célula vazia do tabuleiro para jogar. Isso significa que a IA não é invencível e pode ser derrotada facilmente. Você pode aprimorá-la com algoritmos como **Minimax** (sugestão para a versão 2.0).

---

## 📷 Capturas de Tela

| ![Tela Inicial](https://joaopauloaramuni.github.io/python-imgs/JogodaVelha/imgs/home.png) | ![Tela do Jogo](https://joaopauloaramuni.github.io/python-imgs/JogodaVelha/imgs/game.png) | ![Tela do Vencedor](https://joaopauloaramuni.github.io/python-imgs/JogodaVelha/imgs/game_winner.png) |
|:--:|:--:|:--:|
| 🏠 Tela Inicial | 🕹️ Tela do Jogo | 🏁 Tela do Vencedor |

---

## 📦 Dependências

Para rodar o jogo, você precisa instalar a biblioteca **Pygame**:

```bash
pip install pygame
```

---

## ⚙️ Ambiente virtual

É recomendado criar um ambiente virtual para isolar as dependências do projeto.

1. **Crie o ambiente virtual:**

```bash
python -m venv .venv
```

2. **Ative o ambiente virtual:**

- **Windows:**

```bash
.venv\Scripts\activate
```

- **Linux/macOS:**

```bash
source .venv/bin/activate
```

---

## 💻 Como executar o jogo

Após ativar o ambiente virtual e instalar o Pygame:

```bash
python jogo_da_velha.py
```

---

## 📚 Documentação e links úteis

- 📘 [Pygame Documentation](https://www.pygame.org/docs/)
- 📦 [Pygame no PyPI](https://pypi.org/project/pygame/)
- 🐍 [Python Documentation](https://docs.python.org/3/)

---

## 📄 Licença

Este projeto está sob a Licença **MIT** — sinta-se à vontade para usá-lo, modificá-lo e distribuí-lo.

---
