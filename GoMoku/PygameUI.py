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
	

	def draw_board(self, move_numbers=False):
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
			label_rect.center = (self.width - self.tile_size//2, int((y+1.5)*self.tile_size))
			self.screen.blit(row_label, label_rect)
			pygame.draw.line(self.screen, (0,0,0), 
					(int(1.5*self.tile_size), int((y+1.5)*self.tile_size)),
					(int(self.width - 1.5*self.tile_size), int((y+1.5)*self.tile_size)))

		for (move, player, x, y) in self.game.move_list:
			if player == 0:
				color = 0
			else:
				color = 255*player//(self.game.num_players-1)
			center_x = int((x + 1.5)*self.tile_size)
			center_y = int((y + 1.5)*self.tile_size)
			pygame.draw.circle(self.screen, (color, color, color), (center_x, center_y), self.tile_size // 2)
			if move_numbers:
				piece_label = self.font.render(str(move+1), True, self.board_color, (color, color, color))
				piece_label_rect = piece_label.get_rect()
				piece_label_rect.center = (center_x, center_y)
				self.screen.blit(piece_label, piece_label_rect)


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
				self.draw_board(move_numbers=True)
		pygame.quit()


if __name__ == "__main__":
	game = game_engine()
	UI = PygameUI(game)
	UI.run()