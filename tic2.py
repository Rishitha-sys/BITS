import pygame
import sys
import random

def tic_tac():
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 300, 300
    LINE_COLOR = (0, 0, 0)
    BG_COLOR = (255, 255, 255)
    X_COLOR = (66, 66, 66)
    O_COLOR = (200, 0, 0)
    LINE_WIDTH = 5

    # Board setup
    board = [" "] * 9
    current_player = "X"

    # Pygame window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe (You vs Computer)")

    # Font
    font = pygame.font.SysFont(None, 80)

    # Functions
    def draw_board():
        screen.fill(BG_COLOR)
        # Draw grid
        pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 300), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 300), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, 100), (300, 100), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), LINE_WIDTH)
        
        # Draw X and O
        for i in range(9):
            x = (i % 3) * 100 + 50
            y = (i // 3) * 100 + 50
            if board[i] == "X":
                text = font.render("X", True, X_COLOR)
                text_rect = text.get_rect(center=(x, y))
                screen.blit(text, text_rect)
            elif board[i] == "O":
                text = font.render("O", True, O_COLOR)
                text_rect = text.get_rect(center=(x, y))
                screen.blit(text, text_rect)
        pygame.display.update()

    def check_winner(player):
        win_conditions = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        return any(all(board[i] == player for i in condition) for condition in win_conditions)

    def is_draw():
        return all(cell != " " for cell in board)

    def computer_move():
        available = [i for i, cell in enumerate(board) if cell == " "]
        if available:
            move = random.choice(available)
            board[move] = "O"

    def reset_game():
        global board, current_player
        board = [" "] * 9
        current_player = "X"

    # Game loop
    running = True
    while running:
        draw_board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and current_player == "X":
                x, y = pygame.mouse.get_pos()
                row = y // 100
                col = x // 100
                idx = row * 3 + col
                if board[idx] == " ":
                    board[idx] = "X"
                    if check_winner("X"):
                        draw_board()
                        pygame.time.delay(500)
                        pygame.display.set_caption("You Win! Click to play again.")
                        current_player = "None"
                    elif is_draw():
                        draw_board()
                        pygame.time.delay(500)
                        pygame.display.set_caption("Draw! Click to play again.")
                        current_player = "None"
                    else:
                        current_player = "O"
        
        # Computer's turn
        if current_player == "O":
            pygame.time.delay(500)
            computer_move()
            if check_winner("O"):
                draw_board()
                pygame.time.delay(500)
                pygame.display.set_caption("Computer Wins! Click to play again.")
                current_player = "None"
            elif is_draw():
                draw_board()
                pygame.time.delay(500)
                pygame.display.set_caption("Draw! Click to play again.")
                current_player = "None"
            else:
                current_player = "X"

        # Restart game on mouse click after game ends
        if event.type == pygame.MOUSEBUTTONDOWN and current_player == "None":
            reset_game()
            pygame.display.set_caption("Tic Tac Toe")

        pygame.display.update()


tic_tac()
