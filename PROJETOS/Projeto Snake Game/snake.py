import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# --- Cores RGB ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
CYAN = (0, 200, 200) 

# --- Tamanho da grade e da tela ---
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
WIDTH = GRID_WIDTH * CELL_SIZE
HEIGHT = GRID_HEIGHT * CELL_SIZE

# --- Criação da janela e do relógio do jogo ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Ara Snake")
clock = pygame.time.Clock()


# Representa a cobra (posição, movimento e crescimento)
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)  # Inicia indo para a direita
        self.grow = False        # Indica se a cobra deve crescer

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        # Verifica colisão com as bordas
        if new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
            return False

        # Verifica colisão com o próprio corpo
        if new_head in self.body:
            return False

        # Adiciona nova cabeça
        self.body.insert(0, new_head)

        # Remove a cauda se não estiver crescendo
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

        return True

    def change_direction(self, new_direction):
        # Impede a cobra de inverter a direção
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def grow_snake(self):
        self.grow = True

    def draw(self, surface):
        for segment in self.body:
            x, y = segment
            pygame.draw.rect(surface, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


# Representa a comida que aparece aleatoriamente no mapa
class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        return (
            random.randint(0, GRID_WIDTH - 1),
            random.randint(0, GRID_HEIGHT - 1)
        )

    def draw(self, surface):
        x, y = self.position
        pygame.draw.rect(surface, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


# Exibe a tela de seleção de dificuldade e retorna a velocidade do jogo
def selecionar_dificuldade():
    font_titulo = pygame.font.SysFont(None, 60)
    font_subtitulo = pygame.font.SysFont(None, 40)
    font_opcao = pygame.font.SysFont(None, 30)

    while True:
        screen.fill(BLACK)

        # Título do jogo
        titulo = font_titulo.render("Ara Snake", True, WHITE)

        # Subtítulo de dificuldade
        subtitulo = font_subtitulo.render("Selecione a dificuldade:", True, WHITE)

        # Opções
        facil = font_opcao.render("1 - Easy (Lento)", True, GREEN)
        medio = font_opcao.render("2 - Medium (Normal)", True, CYAN)
        dificil = font_opcao.render("3 - Hard (Rápido)", True, RED)

        # Posicionamento
        screen.blit(titulo, titulo.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120)))
        screen.blit(subtitulo, subtitulo.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60)))
        screen.blit(facil, facil.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        screen.blit(medio, medio.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40)))
        screen.blit(dificil, dificil.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 5
                elif event.key == pygame.K_2:
                    return 10
                elif event.key == pygame.K_3:
                    return 15

# Processa os eventos do teclado e retorna se o jogo deve continuar
def processar_eventos(snake, game_over):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Sai do jogo ao pressionar Q
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))
            elif game_over and event.key == pygame.K_r:
                return "restart"
    return "continue"


# Atualiza o estado do jogo (movimento, colisões e comida)
def atualizar_jogo(snake, food, score):
    if not snake.move():
        return True, score  # game_over = True

    # Verifica se a cobra comeu a comida
    if snake.body[0] == food.position:
        snake.grow_snake()
        score += 10
        while True:
            food.position = food.generate_position()
            if food.position not in snake.body:
                break

    return False, score


# Desenha todos os elementos na tela (cobra, comida, pontuação e mensagens)
def desenhar_tela(snake, food, score, game_over):
    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)

    font = pygame.font.SysFont(None, 36)
    texto_pontuacao = font.render(f"Pontuação: {score}", True, WHITE)
    screen.blit(texto_pontuacao, (10, 10))

    if game_over:
        msg1 = font.render("GAME OVER - Pressione R para reiniciar", True, WHITE)
        msg2 = font.render("Pressione Q para sair", True, WHITE)
        screen.blit(msg1, msg1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
        screen.blit(msg2, msg2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))

    pygame.display.flip()


# Função principal do jogo (organiza o loop principal e lógica)
def main():
    velocidade = selecionar_dificuldade()

    snake = Snake()
    food = Food()
    score = 0
    game_over = False

    while True:
        clock.tick(velocidade)

        acao = processar_eventos(snake, game_over)
        if acao == "restart":
            return main()

        if not game_over:
            game_over, score = atualizar_jogo(snake, food, score)

        desenhar_tela(snake, food, score, game_over)


# Inicia o jogo
if __name__ == "__main__":
    main()

# pip install pygame
# python snake.py