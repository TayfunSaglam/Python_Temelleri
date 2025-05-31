import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    clear()
    print("\n    1   2   3")
    for i, row in enumerate(board):
        print(f" {i+1}  " + " | ".join(row))
        if i < 2:
            print("   ---+---+---")
    print()

def check_winner(board, player):
    win_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_states

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def get_move(name):
    while True:
        try:
            move = input(f"{name}, hamleni yap (satır sütun): ").split()
            if len(move) != 2:
                raise ValueError
            x, y = int(move[0])-1, int(move[1])-1
            if 0 <= x <= 2 and 0 <= y <= 2:
                return x, y
        except ValueError:
            pass
        print("Geçersiz giriş. Lütfen 1-3 arası iki sayı gir.")

def play_game(p1, p2):
    board = [[' ']*3 for _ in range(3)]
    current_player, name = 'X', p1

    while True:
        print_board(board)
        x, y = get_move(name)
        if board[x][y] != ' ':
            print("Bu hücre zaten dolu!")
            continue
        board[x][y] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Tebrikler {name}! Kazandın!")
            break
        if is_draw(board):
            print_board(board)
            print("Oyun berabere!")
            break
        current_player, name = ('O', p2) if current_player == 'X' else ('X', p1)

def main_menu():
    while True:
        clear()
        print("===== XOX Oyunu =====")
        print("1. Oyuna Başla")
        print("2. Hakkında")
        print("3. Çıkış")
        choice = input("Seçiminiz: ")
        if choice == '1':
            p1 = input("1. Oyuncu adı (X): ")
            p2 = input("2. Oyuncu adı (O): ")
            play_game(p1, p2)
            input("Ana menüye dönmek için Enter'a basın...")
        elif choice == '2':
            print("\nBu oyun Python ile geliştirilmiştir. İki oyunculu klasik XOX oyunudur.")
            input("Ana menüye dönmek için Enter'a basın...")
        elif choice == '3':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")

main_menu()
