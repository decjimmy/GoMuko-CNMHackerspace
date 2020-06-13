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
    def placeMove(self, player):
        P = ""
        if player == 1:
            P = "white"
        else:
            P = "black"
        x = int(input(P + " player, what is the x coord of your move?"))
        y = int(input(P + " player, what is the y coord of your move?"))
        self.placePiece(x,y)



    def calc(self):
        pass

g = GoMokuConsole()
gameloop = True
while gameloop:
    g.drawBoard()
    g.placeMove(1)
    g.drawBoard()
    g.placeMove(2)







