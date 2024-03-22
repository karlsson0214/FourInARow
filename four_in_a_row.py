"""Object Oriented Programming: Four in a Row Game.

Complete the game."""

class Board:
    """A board for playing Four in a Row.

    index 0 is the bottom of the board
    
    5
    4
    3
    2
    1
    0 1 2 3 4 5 6 7
    """

    def __init__(self):
        """Call constructor to create a new board."""
        self.board = [[], [], [], [], [], [], []]

    def __str__(self):
        """Return a string representation of the board."""
        answer = ''
        for row in range(6):
            this_row = ''
            for column in range(7):
                if row >= len(self.board[column]):
                    # empty
                    this_row += '. '
                else:
                    this_row += self.board[column][row] + ' '
            answer = '\n' + this_row + answer
        answer +='\n0 1 2 3 4 5 6 column index\n'
        return answer
        
    def add_piece(self, column, piece):
        """Add a piece to the board at the given column.
        
        Keyword arguments:
        column -- the column to add the piece to 1-7
        piece -- the piece to add to the board 'X' or 'O'
        """
        self.board[column].append(piece)
    
class Game:
    """A game of Four in a Row."""
    
    def __init__(self):
        """Call constructor to create a new game."""
        self.board = Board()
        self.current_player = 'X'
    
    def play(self):
        """Play a game of Four in a Row."""
        while True:
            print(self.board)
            column = int(input('Player ' + self.current_player + ' enter column: '))
            self.board.add_piece(column, self.current_player)
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'


class Test:
    """Test the Board class."""
    def __init__(self):
        """Call constructor to create a new test."""
        self.board = Board()
        self.run()
    def test_print_board(self):
        """Test print(board)."""
        self.board.add_piece(0, '0')
        self.board.add_piece(0, '0')
        self.board.add_piece(1, '1')
        self.board.add_piece(1, '1')
        self.board.add_piece(1, '1')
        self.board.add_piece(1, '1')
        self.board.add_piece(1, '1')
        self.board.add_piece(1, '1')
        self.board.add_piece(2, '2')
        self.board.add_piece(3, '3')
        self.board.add_piece(4, '4')
        self.board.add_piece(5, '5')
        self.board.add_piece(6, '6')
        print(self.board)

#test = Test()
#test.run()

game = Game()
game.play()