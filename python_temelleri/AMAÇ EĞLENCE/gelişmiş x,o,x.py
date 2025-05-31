import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(board):
    print("\n   1   2   3")
    for idx, row in enumerate(board):
        print(f"{idx + 1}  {' | '.join(row)}")
        if idx < 2:
            print("  ---+---+---")
    print("\n")


def check_winner(board, symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def get_move(player_name):
    while True:
        try:
            row = int(input(f"{player_name}, satır girin (1-3): "))
            col = int(input(f"{player_name}, sütun girin (1-3): "))
            if 1 <= row <= 3 and 1 <= col <= 3:
                return row - 1, col - 1
            else:
                print("1 ile 3 arasında bir sayı girin.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")



def main():
    clear_screen()
    print("🎮 X-O-X Oyununa Hoş Geldiniz!")
    player1 = input("1. Oyuncunun adını girin (X): ")
    player2 = input("2. Oyuncunun adını girin (O): ")
    players = { "X": player1, "O": player2 }

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_symbol = "X"

    while True:
        clear_screen()
        print_board(board)
        print(f"Sıra: {players[current_symbol]} ({current_symbol})")

        row, col = get_move(players[current_symbol])

        if board[row][col] != " ":
            print("❗ Bu hücre dolu! Devam etmek için Enter'a bas.")
            input()
            continue

        board[row][col] = current_symbol

        if check_winner(board, current_symbol):
            clear_screen()
            print_board(board)
            print(f"🏆 Tebrikler {players[current_symbol]}! Kazandınız!")
            break
        elif is_full(board):
            clear_screen()
            print_board(board)
            print("🤝 Oyun berabere!")
            break

        current_symbol = "O" if current_symbol == "X" else "X"

if __name__ == "__main__":
    main()
