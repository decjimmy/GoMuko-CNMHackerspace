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
        
        

    


    

g = GoMokuConsole()
gameloop = True
#if you subtract alternator - player you will always get next player so easy way to switch back and forth between 1 and 2
alternator = 3
activeplayer = 1
while gameloop:
    g.drawBoard()
    win = g.place_move(2 - (activeplayer %2)) #wonky math that allows you to alternate between 1 and 2
    #g.drawBoard()
    #win = g.placeMove(2)
    if win:
        print("Player " + str(activeplayer) + "Has won the game")
        again = input("Would you like to play again? y/n")
        if again != 'y':
            gameloop = False
    activeplayer = alternator - activeplayer
print ("Thank you for playing. I hope you return")







