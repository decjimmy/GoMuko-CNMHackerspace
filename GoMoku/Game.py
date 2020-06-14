import numpy as np

class Game(object):
    """Gomoku game engine object"""
    
    def __init__(self):

        self.BLACK = 0
        self.WHITE = 1
        self.NO_WINNER = -1
        self.DRAW = -2
        self.HEIGHT = 6
        self.WIDTH = 6
        self.WIN_LENGTH = 3
        self.player = self.BLACK  # black makes the first move
        self.move = 0
        self.BBoard = np.zeros((self.WIDTH, self.HEIGHT))
        self.WBoard = np.zeros((self.WIDTH, self.HEIGHT))
 
 
    def place_piece(self, x, y):
        """x: x coord to place piece of current player
           y: y coord to place piece of current player """
        try:
            assert x in range(self.WIDTH) and y in range(self.HEIGHT), \
                "Coordinate ({0}, {1}) out of range (0, 0)..({2}, {3})".format(x, y, self.WIDTH-1, self.HEIGHT-1)
            assert self.BBoard[x][y] == 0 and self.WBoard[x][y] == 0, \
                "Coordinate ({0}, {1}) already occupied".format(x, y)
        except AssertionError as msg:
            print("place_piece:", msg)
        else:
            self.move += 1
            if self.player == self.BLACK:
                self.BBoard[x][y] = 1
                self.player = self.WHITE
            else:
                self.WBoard[x][y] = 1
                self.player = self.BLACK

    def check_win(self):
        """Return BLACK or WHITE if one player has WIN_LENGTH pieces in a row or column, otherwise
           Return DRAW if there are no more empty spaces on the board
           Return NO_WINNER if there are still empty spaces"""
        result = self.NO_WINNER
        for (board, player) in [(self.BBoard, self.BLACK), (self.WBoard, self.WHITE)]:
            for board in [board, np.rot90(board)]:
                for row in board:
                    if "1. "*self.WIN_LENGTH in np.array2string(row):
                       result = player
 
                # Check diagonals by reshaping 2D array into 1D and taking slices
                # that correspond to all possible diagonals of length WIN_LENGTH
                (h, w) = board.shape # Can't use WIDTH and HEIGHT because board may be transposed
                board = board.reshape((w*h,)) # Make array 1D
                step = w + 1 # next element in diagonal is one more ahead than the width
                for j in range(h-self.WIN_LENGTH+1):
                    for i in range(w-self.WIN_LENGTH+1):
                        start = j*w+i
                        dSlice = board[start:start+step*self.WIN_LENGTH:step]
                        if np.array_equal(dSlice, np.ones((self.WIN_LENGTH,))):
                            result = player
            
        if result == self.NO_WINNER:
            if np.array_equal(self.WBoard+self.BBoard, np.ones((self.WIDTH, self.HEIGHT))):
                result = self.DRAW
            else:
                result = self.NO_WINNER

        # TODO DR These descriptions of result should come from a separate method
        #         that the UI could call if it needs to.
        if result == self.BLACK:
            print("Black wins on move", self.move)
        elif result == self.WHITE:
            print("White wins on move", self.move)
        elif result == self.DRAW:
            print("Game is a draw on move", self.move)
        else:
            print("No winner yet on move", self.move)
        return result


if __name__ == "__main__":
    #testing placement of pieces
    g = Game()

    print("width: ", g.WIDTH)
    print("height:", g.HEIGHT)
    print("Playing to", g.WIN_LENGTH, "in a row")

    # Test placing a piece off the board
    g.place_piece(-1, 0)
    g.place_piece(0, -1)
    g.place_piece(0, g.HEIGHT)
    g.place_piece(g.WIDTH, 0)

    # Test that black wins after placing 3 in a diagonal
    for x in range(g.WIN_LENGTH):
        g.place_piece(x, (x+1)*2-1)
        g.check_win()
        g.place_piece(x, x)
        g.check_win()

  

    # TODO DR Make more comprehensive tests:
    #   Test row, column and upward diagonal wins
    #   Force a draw by filling board with alternating pieces


    

  




