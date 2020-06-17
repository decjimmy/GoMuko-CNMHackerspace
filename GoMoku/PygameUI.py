import pygame
from Game import game_engine


class PygameUI(object):
	"""Pygame GUI interface for GoMoku"""


	def __init__(self, game, tile_size=24):
		"""Start Pygame and initialize a GoMoku UI."""
		self.game = game
		self.tile_size = tile_size
		self.width = tile_size * (game.width + 2)
		self.height = tile_size * (game.height + 2)
		pygame.init()
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.font = pygame.font.Font('freesansbold.ttf', tile_size // 2) 
		self.board_color = (200, 170, 30)
		self.running = False
	

	def draw_board(self):
		"""Draw the GoMoku game board"""
		self.screen.fill(self.board_color)

		# Draw column labels and lines
		for x in range(self.game.width):
			column_label = self.font.render(str(x+1), True, (0,0,0), self.board_color)
			label_rect = column_label.get_rect()
			label_rect.center = (int((x+1.5)*self.tile_size), self.tile_size//2)
			self.screen.blit(column_label, label_rect)
			label_rect.center = (int((x+1.5)*self.tile_size), self.height - self.tile_size//2)
			self.screen.blit(column_label, label_rect)
			pygame.draw.line(self.screen, (0,0,0), 
					(int((x+1.5)*self.tile_size), int(1.5*self.tile_size)),
					(int((x+1.5)*self.tile_size), int(self.height - 1.5*self.tile_size)))

		# Draw row labels and lines
		for y in range(self.game.height):
			row_label = self.font.render(str(y+1), True, (0,0,0), self.board_color)
			label_rect = row_label.get_rect()
			label_rect.center = (self.tile_size//2, int((y+1.5)*self.tile_size)) 
			self.screen.blit(row_label, label_rect)
			label_rect.center = (self.height - self.tile_size//2, int((y+1.5)*self.tile_size))
			self.screen.blit(row_label, label_rect)
			pygame.draw.line(self.screen, (0,0,0), 
					(int(1.5*self.tile_size), int((y+1.5)*self.tile_size)),
					(int(self.width - 1.5*self.tile_size), int((y+1.5)*self.tile_size)))

		board = self.game.game_board()
		for x in range(self.game.width):
			for y in range(self.game.height):
				if(board[x][y] == 0):
					continue
				else:
					if board[x][y] == 1:
						piece_color = (0,0,0,)
					else:
						piece_color = (255,255,255)
					pygame.draw.circle(self.screen, piece_color,
						(int((x + 1.5)*self.tile_size), int((y + 1.5)*self.tile_size)), self.tile_size // 2)


		pygame.display.set_caption(self.game.game_status()) 
		pygame.display.flip()


	def run(self):
		"""Run the Pygame GoMoku UI"""
		self.running = True
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
			if not self.game.game_over:
				self.game.place_rational()
				self.draw_board()
		pygame.quit()


if __name__ == "__main__":
	game = game_engine()
	UI = PygameUI(game)
	UI.run()