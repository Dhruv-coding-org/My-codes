import pygame, sys

# === Initialize ===
pygame.init()
WIDTH, HEIGHT = 420, 550
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
FONT = pygame.font.SysFont("Arial", 80)
SMALL_FONT = pygame.font.SysFont("Arial", 24)
CLOCK = pygame.time.Clock()

# === Colors ===
BG = (17, 17, 17)
GRID = (255, 255, 255)
X_COLOR = (255, 76, 76)
O_COLOR = (76, 175, 255)
WIN_LINE = (0, 255, 136)
TEXT_COLOR = (220, 220, 220)

# === Game state ===
board = [["" for _ in range(3)] for _ in range(3)]
turn = "X"
game_over = False
winner = None
scores = {"X": 0, "O": 0}
player_names = {"X": "Player X", "O": "Player O"}

# === Drawing functions ===
def draw_grid():
    SCREEN.fill(BG)
    for x in range(1, 3):
        pygame.draw.line(SCREEN, GRID, (x * 140, 0), (x * 140, 420), 4)
        pygame.draw.line(SCREEN, GRID, (0, x * 140), (420, x * 140), 4)

def draw_marks():
    for r in range(3):
        for c in range(3):
            mark = board[r][c]
            if mark:
                x, y = c * 140 + 70, r * 140 + 70
                mark_surface = FONT.render(mark, True, X_COLOR if mark == "X" else O_COLOR)
                rect = mark_surface.get_rect(center=(x, y))
                SCREEN.blit(mark_surface, rect)

def draw_hover():
    if game_over:
        return
    mouse_x, mouse_y = pygame.mouse.get_pos()
    row, col = mouse_y // 140, mouse_x // 140
    if row < 3 and col < 3 and board[row][col] == "":
        ghost = FONT.render(turn, True, X_COLOR if turn == "X" else O_COLOR)
        ghost.set_alpha(100)  # translucent
        rect = ghost.get_rect(center=(col * 140 + 70, row * 140 + 70))
        SCREEN.blit(ghost, rect)

def draw_scoreboard():
    name_text = f"{player_names['X']} (X): {scores['X']}     {player_names['O']} (O): {scores['O']}"
    text = SMALL_FONT.render(name_text, True, TEXT_COLOR)
    SCREEN.blit(text, (20, 430))

    if game_over:
        msg = f"{player_names[winner]} wins!" if winner else "Draw!"
        m = SMALL_FONT.render(msg + " - Click to restart", True, TEXT_COLOR)
        SCREEN.blit(m, (60, 480))

def draw_win_line(cells):
    x1 = cells[0][1] * 140 + 70
    y1 = cells[0][0] * 140 + 70
    x2 = cells[2][1] * 140 + 70
    y2 = cells[2][0] * 140 + 70
    pygame.draw.line(SCREEN, WIN_LINE, (x1, y1), (x2, y2), 6)

# === Game logic ===
def get_win_cells():
    lines = []
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != "":
            lines.append([(r, 0), (r, 1), (r, 2)])
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != "":
            lines.append([(0, c), (1, c), (2, c)])
    if board[0][0] == board[1][1] == board[2][2] != "":
        lines.append([(0, 0), (1, 1), (2, 2)])
    if board[0][2] == board[1][1] == board[2][0] != "":
        lines.append([(0, 2), (1, 1), (2, 0)])
    return lines[0] if lines else []

def reset_game():
    global board, turn, game_over, winner
    board = [["" for _ in range(3)] for _ in range(3)]
    turn = "X"
    game_over = False
    winner = None

def handle_click(pos):
    global turn, game_over, winner
    if game_over:
        reset_game()
        return
    x, y = pos
    row, col = y // 140, x // 140
    if row < 3 and board[row][col] == "":
        board[row][col] = turn
        win_cells = get_win_cells()
        if win_cells:
            game_over = True
            winner = turn
            scores[turn] += 1
        elif all(board[r][c] != "" for r in range(3) for c in range(3)):
            game_over = True
            winner = None
        else:
            turn = "O" if turn == "X" else "X"

# === Main game loop ===
while True:
    CLOCK.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(pygame.mouse.get_pos())

    draw_grid()
    draw_marks()
    draw_hover()
    draw_scoreboard()
    if game_over and (cells := get_win_cells()):
        draw_win_line(cells)
    pygame.display.update()
