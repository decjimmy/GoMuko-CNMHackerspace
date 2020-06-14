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
                self.board[x].append('0')
    def place_piece(self,player, x, y):
        """player: the player playing 1 is white, 2 is black
           x: x coord of place to place piece
           y: y coord of place to place piece """
        
        if player == 1 or player == 2:
            self.board[x][y] = str(player)
            return self.check_win(player, x, y)
        else:
            """TODO: add error protection"""
            print('invalid player')
            return False
    def check_row(self, player, x, y):
        """checks to see if there are 5 matching player symbols in a row"""
        row = ''.join(self.board[x])
        if player == 1:
            if "11111" in row:
                return True
        if player == 2:
            if "22222" in row:
                return True
        return False

    def check_column(self, player, x, y):
        column = ''
        for i in range(0,15):
            column += self.board[i][y]
        if player == 1:
            if "11111" in column:
                return True
        if player == 2:
            if "22222" in column:
                return True
        return False
    def check_diagonal(self, player, x, y):
        """checks to see if there are 5 matching player symbols in a diagonal"""
        return False
    def check_win(self, player, x, y):
        """checks if play is a winning move"""
        
        if self.check_row(player, x,y):
            return True
        elif self.check_column(player, x,y):
            return True
        elif self.check_diagonal(player, x,y):
            return True


        return False
        

if __name__ == "__main__":
    #testing placement of pieces
    g = Game()
    g.generate_board()
    g.place_piece(1,2,3)
    g.place_piece(1,2,4)
    g.place_piece(1,2,5)
    g.place_piece(1,2,6)
    g.place_piece(1,2,7)
    print (g.board)



