class Piece:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def symbol(self):
        symbols = {
            'P': '♙' if self.color == 'w' else '♟',
            'R': '♖' if self.color == 'w' else '♜',
            'N': '♘' if self.color == 'w' else '♞',
            'B': '♗' if self.color == 'w' else '♝',
            'Q': '♕' if self.color == 'w' else '♛',
            'K': '♔' if self.color == 'w' else '♚'
        }
        return symbols[self.name]

class ChessBoard:
    def __init__(self):
        self.board = self.create_board()
        self.turn = 'w'

    def create_board(self):
        empty = [[None]*8 for _ in range(8)]
        for i in range(8):
            empty[1][i] = Piece('P', 'b')
            empty[6][i] = Piece('P', 'w')
        layout = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for i in range(8):
            empty[0][i] = Piece(layout[i], 'b')
            empty[7][i] = Piece(layout[i], 'w')
        return empty

    def display(self):
        print("  a b c d e f g h")
        for i in range(8):
            row = str(8 - i) + " "
            for j in range(8):
                piece = self.board[i][j]
                row += piece.symbol() if piece else "."
                row += " "
            print(row + str(8 - i))
        print("  a b c d e f g h\n")

    def parse_move(self, move_str):
        try:
            start, end = move_str.split()
            sx, sy = 8 - int(start[1]), ord(start[0]) - ord('a')
            ex, ey = 8 - int(end[1]), ord(end[0]) - ord('a')
            return (sx, sy, ex, ey)
        except:
            return None

    def is_valid(self, sx, sy, ex, ey):
        piece = self.board[sx][sy]
        if not piece or piece.color != self.turn:
            return False

        dx, dy = ex - sx, ey - sy
        abs_dx, abs_dy = abs(dx), abs(dy)

        if piece.name == 'P':
            dir = -1 if piece.color == 'w' else 1
            if dy == 0 and dx == dir and not self.board[ex][ey]:
                return True
            if dy == 0 and dx == 2*dir and sx == (6 if piece.color == 'w' else 1) and not self.board[ex][ey]:
                return True
            if abs_dy == 1 and dx == dir and self.board[ex][ey] and self.board[ex][ey].color != piece.color:
                return True
        elif piece.name == 'R':
            if sx == ex or sy == ey:
                return self.clear_path(sx, sy, ex, ey)
        elif piece.name == 'N':
            return (abs_dx, abs_dy) in [(2, 1), (1, 2)]
        elif piece.name == 'B':
            if abs_dx == abs_dy:
                return self.clear_path(sx, sy, ex, ey)
        elif piece.name == 'Q':
            if sx == ex or sy == ey or abs_dx == abs_dy:
                return self.clear_path(sx, sy, ex, ey)
        elif piece.name == 'K':
            return max(abs_dx, abs_dy) == 1
        return False

    def clear_path(self, sx, sy, ex, ey):
        dx = (ex - sx) and (1 if ex > sx else -1)
        dy = (ey - sy) and (1 if ey > sy else -1)
        x, y = sx + dx, sy + dy
        while (x, y) != (ex, ey):
            if self.board[x][y]:
                return False
            x += dx
            y += dy
        dest = self.board[ex][ey]
        return not dest or dest.color != self.board[sx][sy].color

    def move(self, sx, sy, ex, ey):
        self.board[ex][ey] = self.board[sx][sy]
        self.board[sx][sy] = None
        self.turn = 'b' if self.turn == 'w' else 'w'

def main():
    game = ChessBoard()
    while True:
        game.display()
        move = input(f"{'White' if game.turn == 'w' else 'Black'} move (e.g. e2 e4): ")
        parsed = game.parse_move(move)
        if parsed:
            sx, sy, ex, ey = parsed
            if game.is_valid(sx, sy, ex, ey):
                game.move(sx, sy, ex, ey)
            else:
                print("Invalid move. Try again.")
        else:
            print("Invalid input format. Use e.g. e2 e4.")

if __name__ == "__main__":
    main()
