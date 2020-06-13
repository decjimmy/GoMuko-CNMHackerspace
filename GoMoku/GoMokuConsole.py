import Game
class GoMokuConsole(object):
    """description of class"""
    def __init__(self):
        self.game = Game.Game()
    def drawBoard(self):
        board = self.game.board
        for x in range(len(board)):
            for y in range(len(board[x])):
                
                print (board[x][y], end=' ')
            print()

    def placePiece(self, player, x,y):
        self.game.place_piece(player, x, y)
        
    def calc(self):
        pass

g = GoMokuConsole()
g.placePiece(1, 3,4)
g.placePiece(1, 4,4)
g.placePiece(1, 5,4)
g.placePiece(1, 6,4)
g.placePiece(1, 7,4)

g.drawBoard()




