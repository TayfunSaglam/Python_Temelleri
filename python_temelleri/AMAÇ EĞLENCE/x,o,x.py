def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def check_winner(board, player):
    # Satırlar, sütunlar ve çaprazlar
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Sıra oyuncu {current_player}'de.")
        try:
            row = int(input("Satır (0-2): "))
            col = int(input("Sütun (0-2): "))
        except ValueError:
            print("Geçerli bir sayı girin.")
            continue

        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == " ":
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Tebrikler! Oyuncu {current_player} kazandı!")
                    break
                elif is_full(board):
                    print_board(board)
                    print("Oyun berabere!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Bu hücre dolu! Başka bir yer seçin.")
        else:
            print("Geçersiz koordinatlar! 0-2 arasında bir değer girin.")

if __name__ == "__main__":
    main()
