class Game(object):
    """The game object of Gomoku.
       0 represents empty spot
       1 represents white piece
       2 represents black piece"""
    def __init__(self):
        self.board = []
        self.generate_board()
    def generate_board(self):
        """Creates a 15 by 15 grid in the form of an array where the game will be played"""
        self.board = []
        for x in range(0,15):
            self.board.append([])
            for y in range(0,15):
                self.board[x].append(0)
    def place_piece(self,player, x, y):
        """player: the player playing 1 is white, 2 is black
           x: x coord of place to place piece
           y: y coord of place to place piece """
        
        if player == 1 or player == 2:
            self.board[x][y] = player
            self.check_win(player, x, y)
        else:
            """TODO: add error protection"""
            print('invalid player')
    def check_win(self, player, x, y):
        """checks if play is a winning move"""
        pass

if __name__ == "__main__":
    g = Game()
    g.generate_board()
    g.place_piece(1,2,3)
    print (g.board)



