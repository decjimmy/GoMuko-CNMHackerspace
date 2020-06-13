import Game
class GoMokuConsole(object):
    """allows you to play GoMoku in a text base format"""
    def __init__(self):
        self.game = Game.Game()
    def drawBoard(self):
        """draws the board with 1's representing player one and 2s representing player 2"""
        board = self.game.board
        for x in range(len(board)):
            for y in range(len(board[x])):
                
                print (board[x][y], end=' ')
            print()

    def place_piece(self, player, x,y):
        """calls main GoMoku game to place piece and returns true if it is a winning move"""
        return self.game.place_piece(player, x, y)
    def place_move(self, player):
        """asks player to choose where they want to place their piece and places it"""
        P = ""
        if player == 1:
            P = "white"
        else:
            P = "black"
        x = int(input(P + " player, what is the x coord of your move?"))
        y = int(input(P + " player, what is the y coord of your move?"))
        win = self.place_piece(player, x,y)
        print( win)

    


    

g = GoMokuConsole()
gameloop = True
while gameloop:
    g.drawBoard()
    g.place_move(1)
    #g.drawBoard()
    #g.placeMove(2)







