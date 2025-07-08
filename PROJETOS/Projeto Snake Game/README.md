# Projeto Snake Game - Ara Snake

## O que é o projeto?

Este é um jogo da cobrinha (Snake Game) desenvolvido em Python utilizando a biblioteca Pygame. O objetivo é controlar a cobrinha para que ela coma a comida vermelha, cresça, e acumule pontos sem colidir com as paredes ou com o próprio corpo. O jogo oferece três níveis de dificuldade (Easy, Medium e Hard), influenciando a velocidade da cobrinha.

## O que é o Pygame?

Pygame é uma biblioteca popular para desenvolvimento de jogos em Python que fornece funcionalidades para manipular gráficos, sons e eventos de entrada, permitindo criar jogos 2D de forma simples e eficiente. Com Pygame, é possível desenvolver desde jogos simples até projetos mais complexos com animações e interatividade.

## História do Jogo da Cobrinha (Snake Game)

O jogo da cobrinha é um clássico dos videogames, surgido na década de 1970 e popularizado principalmente em celulares Nokia nos anos 1990. Sua simplicidade e desafio conquistaram jogadores ao redor do mundo, fazendo dele um dos jogos mais reconhecidos da história. O objetivo sempre foi crescer a cobra coletando itens e evitar colisões que causam o fim do jogo.

## Capturas de Tela

| ![Tela Inicial](https://joaopauloaramuni.github.io/python-imgs/SnakeGame/imgs/home.png) | ![Tela do Jogo](https://joaopauloaramuni.github.io/python-imgs/SnakeGame/imgs/game.png) |
|:--:|:--:|
| Tela Inicial | Tela do Jogo |

## Como Jogar

- Use as **setas do teclado** para mover a cobrinha:
  - ↑ (Seta para cima): Move para cima
  - ↓ (Seta para baixo): Move para baixo
  - ← (Seta para esquerda): Move para esquerda
  - → (Seta para direita): Move para direita

- **Objetivo**: Coma a comida vermelha para crescer e ganhar pontos
- **Cuidado**: Não bata nas paredes ou no próprio corpo da cobra!
- **Pontuação**: Cada comida vale 10 pontos

## Game Over

Quando o jogo terminar:
- Pressione **R** para reiniciar
- Pressione **Q** para sair

## Características do Jogo

- Cobrinha verde
- Comida vermelha que aparece aleatoriamente
- Sistema de pontuação
- Detecção de colisões
- Tela de game over com opção de reiniciar
- Velocidade alternável (easy, medium e hard)

Divirta-se jogando!

## Dependências

Para rodar o jogo, instale a biblioteca Pygame:

```bash
pip install pygame
```

---

## ⚙️ Ambiente virtual

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

## Documentação e links úteis

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Documentation](https://docs.python.org/3/)

---

## Licença

Este projeto está sob a Licença MIT.
