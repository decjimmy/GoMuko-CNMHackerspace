class Game(object):
    """The game object of Gomoku."""
    def __init__(self):
        self.board = []
        self.generate_board()
    def generate_board(self):
        """Creates a 15 by 15 grid in the form of an array where the game will be played"""
        """zeros represent no placed gamepiece"""
        self.board = []
        for x in range(0,15):
            self.board.append([])
            for y in range(0,15):
                self.board[x].append(0)

g = Game()
g.generate_board()
print (g.board)



