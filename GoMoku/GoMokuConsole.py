from Game import game_engine

class GoMokuConsole(object):
    """Console UI to interact with gomoku Game() engine object"""

    def __init__(self, game):
        self.game = game


    def draw_board(self):
        """Draw the game board."""      
        board = self.game.game_board()
        (w, h) = (self.game.width, self.game.height)
        print()
        for j in range(h):
            for i in range(w):
                p = board[j][i]
                c = "?"
                if p == 1:
                    c ="○"
                elif p == 2:
                    c= "●"
                elif p == 0:
                    if i == 0:
                        if j == 0:
                            c = "┌"
                        elif j == h-1:
                            c = "└"
                        else:
                            c = "├"
                    elif i == w-1:
                        if j == 0:
                            c = "┐"
                        elif j == h-1:
                            c = "┘"
                        else:
                            c = "┤"
                    elif j == 0:
                        c = "┬"
                    elif j == h-1:
                        c = "┴"
                    else:
                        c = "┼"
                print(c, end="")
            print()

    def place_piece(self, x, y):
        """Place piece of current player in column x of row y"""
        return self.game.place_piece(x, y)


    def get_move(self):
        """Prompt current player for x and y coordinate to place a piece"""
            
        print(self.game.game_status())
        x = input("X: ")
        y = input("Y: ")
        print(self.place_piece(x,y))


    def run(self):
        while not self.game.game_over:
            self.draw_board()
            self.get_move()
        self.draw_board()
        print(self.game.game_status())


if __name__ == "__main__":
    game = game_engine(win_length=3, player_labels=["Black"])
    UI = GoMokuConsole(game)
    UI.run()
    








