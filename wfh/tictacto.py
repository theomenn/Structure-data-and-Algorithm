import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Pengaturan layar
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic-Tac-Toe")

# Warna
white = (255, 255, 255)
black = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 55)

# Fungsi untuk menggambar papan
def draw_board(board):
    screen.fill(white)

    # Garis vertikal
    pygame.draw.line(screen, black, (screen_width // 3, 0), (screen_width // 3, screen_height), 5)
    pygame.draw.line(screen, black, (2 * screen_width // 3, 0), (2 * screen_width // 3, screen_height), 5)

    # Garis horizontal
    pygame.draw.line(screen, black, (0, screen_height // 3), (screen_width, screen_height // 3), 5)
    pygame.draw.line(screen, black, (0, 2 * screen_height // 3), (screen_width, 2 * screen_height // 3), 5)

    # Menampilkan simbol X dan O pada papan
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                text = font.render('X', True, black)
            elif board[row][col] == 'O':
                text = font.render('O', True, black)
            else:
                continue

            text_rect = text.get_rect(center=(col * (screen_width // 3) + screen_width // 6,
                                              row * (screen_height // 3) + screen_height // 6))
            screen.blit(text, text_rect)

# Fungsi untuk mengecek kemenangan
def check_winner(board):
    # Cek baris dan kolom
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Cek diagonal
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

# Fungsi utama
# Fungsi utama
def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // (screen_height // 3)
                clicked_col = mouseX // (screen_width // 3)

                if board[clicked_row][clicked_col] == ' ':
                    board[clicked_row][clicked_col] = current_player
                    winner = check_winner(board)

                    if winner:
                        print(f'Player {winner} wins!')
                        game_over = True

                        # Tampilkan pesan selamat kepada pemenang
                        font_winner = pygame.font.SysFont(None, 70)
                        text_winner = font_winner.render(f'Congratulations Player {winner}!', True, (255, 0, 0))
                        screen.blit(text_winner, (screen_width // 2 - text_winner.get_width() // 2,
                                                  screen_height // 2 - text_winner.get_height() // 2))
                    elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                        print('It\'s a draw!')
                        game_over = True
                    else:
                        current_player = 'O' if current_player == 'X' else 'X'

            draw_board(board)
            pygame.display.flip()

# Menjalankan permainan
if __name__ == "__main__":
    main()
