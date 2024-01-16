class ChessBoard:
    def __init__(self):
        self.board = self.initial_board()

    def initial_board(self):
        # Create an 8x8 chess board with pieces in their initial positions
        board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        return board

    def display(self):
        # Display the current state of the chess board
        for row in self.board:
            print(' '.join(row))

if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.display()
