import pygame
import sys
import random
import time

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (10, 10, 10)
WIN_LINE_COLOR = (255, 0, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 300, 360  # Extra space for score
SQUARE_SIZE = WIDTH // 3
LINE_WIDTH = 5
WIN_LINE_WIDTH = 8

# Game state variables
board = [["" for _ in range(3)] for _ in range(3)]
game_over = False
winner = None
win_line = None
player_turn = True
last_game_end_time = None
score = {"X": 0, "O": 0, "Draw": 0}


def draw_lines(screen):
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE + 60), (WIDTH, i * SQUARE_SIZE + 60), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 60), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_figures(screen):
    for row in range(3):
        for col in range(3):
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE + 60
            if board[row][col] == "X":
                pygame.draw.line(screen, BLACK, (x + 20, y + 20), (x + SQUARE_SIZE - 20, y + SQUARE_SIZE - 20), LINE_WIDTH)
                pygame.draw.line(screen, BLACK, (x + SQUARE_SIZE - 20, y + 20), (x + 20, y + SQUARE_SIZE - 20), LINE_WIDTH)
            elif board[row][col] == "O":
                center = (x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2)
                pygame.draw.circle(screen, BLACK, center, SQUARE_SIZE // 2 - 20, LINE_WIDTH)


def check_winner():
    global winner, game_over, win_line

    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            winner = board[row][0]
            y = row * SQUARE_SIZE + SQUARE_SIZE // 2 + 60
            win_line = ((0, y), (WIDTH, y))
            game_over = True
            return

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            winner = board[0][col]
            x = col * SQUARE_SIZE + SQUARE_SIZE // 2
            win_line = ((x, 60), (x, HEIGHT))
            game_over = True
            return

    if board[0][0] == board[1][1] == board[2][2] != "":
        winner = board[0][0]
        win_line = ((0, 60), (WIDTH, HEIGHT))
        game_over = True
        return

    if board[0][2] == board[1][1] == board[2][0] != "":
        winner = board[0][2]
        win_line = ((WIDTH, 60), (0, HEIGHT))
        game_over = True
        return

    if all(board[r][c] != "" for r in range(3) for c in range(3)):
        winner = "Draw"
        game_over = True


def draw_winner_line(screen):
    if win_line:
        pygame.draw.line(screen, WIN_LINE_COLOR, win_line[0], win_line[1], WIN_LINE_WIDTH)


def ai_move():
    empty = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
    if empty:
        r, c = random.choice(empty)
        board[r][c] = "O"


def reset_game():
    global board, game_over, winner, win_line, player_turn, last_game_end_time
    board = [["" for _ in range(3)] for _ in range(3)]
    game_over = False
    winner = None
    win_line = None
    player_turn = True
    last_game_end_time = None


def draw_score(screen, font):
    text = font.render(f"X: {score['X']}   O: {score['O']}   Draws: {score['Draw']}", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))


def main():
    global player_turn, last_game_end_time

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic-Tac-Toe")
    font = pygame.font.SysFont(None, 24)
    big_font = pygame.font.SysFont(None, 40)
    clock = pygame.time.Clock()

    reset_game()

    while True:
        screen.fill(WHITE)
        draw_score(screen, font)
        draw_lines(screen)
        draw_figures(screen)

        if game_over:
            draw_winner_line(screen)
            msg = f"{winner} wins!" if winner != "Draw" else "It's a draw!"
            text = big_font.render(msg, True, BLUE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
            if last_game_end_time is None:
                score[winner] += 1
                last_game_end_time = time.time()
            elif time.time() - last_game_end_time > 3:
                reset_game()

        pygame.display.update()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()

            if not game_over and event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                x, y = event.pos
                if y > 60:
                    row = (y - 60) // SQUARE_SIZE
                    col = x // SQUARE_SIZE
                    if board[row][col] == "":
                        board[row][col] = "X"
                        player_turn = False
                        check_winner()
                        if not game_over:
                            pygame.time.delay(400)
                            ai_move()
                            check_winner()
                        player_turn = True


if __name__ == "__main__":
    main()

# pip install pygame
# python tictactoe.py