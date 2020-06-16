import numpy as np
from random import choice as random_choice

class game_engine(object):
	"""Generalized GoMoku game engine."""
	
	game_over = False
	winner = False	# label of winner, e.g. "Black" or "White"
	player = 0		# game starts with the first player's move
	move_num = 0

	def __init__(self, width=15, height=15, win_length=5, player_labels=["Black", "White"]):
		"""Initialize a generalized GoMoku game for number of players in player_labels.
		   Play area has dimensions of width by height.
		   The first player to create a completion of at least win_length wins.
		   Game is a draw if a completion becomes impossible for any player."""

		self.num_players = len(player_labels)
		try:
			assert type(width) is int and type(height) is int, \
				"Board dimensions must be integers. Given ({0}, {1})".format(width, height)
			assert width > 0 and height > 0 , \
				"Board dimensions must be > 0. Given ({0}, {1}).".format(width, height)
			assert win_length <= width or win_length <= height, \
				"Board dimensions ({0}, {1}) too small for {2} in a row.".format(width, height, win_length)
			assert self.num_players == len(set(player_labels)), \
				"Player labels must be unique. Given {0}.".format(player_labels)
			assert self.num_players > 0, \
				"Game requires at least one player label."
		except AssertionError as msg:
			raise ValueError(msg)
		else:
			self.width = width
			self.height = height
			self.win_length = win_length
			self.player_labels = player_labels
			self.pieces = [np.zeros((height, width)) for label in player_labels]


	def game_board(self):
		"""Returns a game board array with all pieces on one board.
		   Empty spaces are 0, player_label[0] pieces are 1, player_label[1] pieces are 2, etc."""
		result = np.zeros((self.height, self.width))
		for p in range(self.num_players):
			result += (p+1)*self.pieces[p]
		return result


	def empty_spaces(self):
		"""Returns a list of tuples with coordinates of all empty spaces on the game board."""
		board = self.game_board()
		return [(i, j) 
		  for j in range(self.height) 
		  for i in range(self.width) 
		  if board[j][i] == 0]


	def win_length_slices(self, board):
		"""Returns a list of all win_length slices of a board along rows, columns and diagonals."""
		result = []

		# rot90 rotates rows into columns and downward diagonals into upward diagonals	
		for b in [board, np.rot90(board)]: 
			(h, w) = b.shape

			# Rows
			for row in b:
				for i in range(w-self.win_length+1):
					result.append(row[i:i+self.win_length])

			# Downward diagonals
			# Flatten array to 1D
			b = b.reshape((w*h,)) 

			# Elements of downward diagonal are separated by one more than the 2D width
			step = w + 1
			for j in range(h-self.win_length+1):
				for i in range(w-self.win_length+1):
					start = j*w+i
					result.append(b[start:start+step*self.win_length:step])
		return np.array(result)


	def sanity_check(self):
		"""Returns True if game state passes sanity checks.  False otherwise.
		   Prints results of all failed checks."""
		errors = []

		# currently only tests for multiple pieces at the same point
		for j in range(self.height):
			for i in range(self.width):
				occupants = 0
				for p in range(self.num_players):
					occupants += self.pieces[p][j][i]
				if occupants > 1:
					errors.append("{0} pieces at position ({1},{2})".format(occupants, i, j))
		for error in errors:
			print(error)
		return not errors


	def update_status(self):
		"""Determine if game is over and why."""

		# A slice that contains more than one non-zero label can never contain a win
		possible_wins = [s for s in self.win_length_slices(self.game_board()) 
				   if len(set(s)) == 1 or (len(set(s)) == 2 and 0 in s)]

		# Game is a draw if there are no possible ways for any player to win
		if not possible_wins:
			self.game_over = True
			return
		else:
			for s in possible_wins:
				if len(set(s)) == 1:
					if 0 in s: # a slice of all zeros isn't a win
						continue
					self.winner = self.player_labels[int(s[0])-1]
					self.game_over = True
					break	


	def game_status(self):
		"""Returns a string describing the status of the game."""
		if(self.game_over):
			if(self.winner):
				return "{0} wins on move {1}".format(self.winner, self.move_num)
			else:
				return "Game is a draw on move {0}".format(self.move_num + 1)
		else:
			return "Move {0}: {1}".format(self.move_num+1, self.player_labels[self.player])


	def player_pass(self):
		"""Advances game to next player."""
		self.move_num += 1
		self.player = (self.player + 1) % self.num_players


	def place_piece(self, x, y):
		"""Place current player's piece at coordinates x, y
		   Returns a string describing the move."""
		try:
			assert not self.game_over, \
				"after game has ended."
			assert type(x) == int and type(y) == int, \
				"but coordinates must be integers."
			assert x in range(self.width) and y in range(self.height), \
				"out of range (0, 0)..({0}, {1})".format(self.width-1, self.height-1)
			assert 1 not in [p[y][x] for p in self.pieces], \
				"which is already occupied."
		except AssertionError as msg:
			return "{0} attempted to play at ({1}, {2}) {3}".format( \
				self.player_labels[self.player], x, y, msg)
		else:
			self.pieces[self.player][y][x] = 1
			self.update_status()
			msg = "{0} plays ({1}, {2})".format(self.player_labels[self.player], x, y)
			if not self.game_over:
				self.player_pass()
			return msg


	def place_random(self):
		"""Place current player's piece randomly.
		   Returns a string describing the move."""
		(x, y) = random_choice(self.empty_spaces())
		return self.place_piece(x, y)


	def playout_random(self):
		"""Play randomly until game is over."""
		while not self.game_over:
			print(self.game_status())
			print(self.place_random())
		print(self.game_board())
		print(self.game_status())
		

if __name__ == "__main__":

	# Test invalid constructions
	try:
		game_engine(7.6, 15, 3) # only int dimensions
	except ValueError as msg:
		print(msg)

	try:
		game_engine(0, 15, 3) # only positive width
	except ValueError as msg:
		print(msg)

	try:
		game_engine(5, -1, 3) # only positive height	
	except ValueError as msg:
		print(msg)

	try:
		game_engine(5, 5, 15) # board must be big enough for a win_length slice
	except ValueError as msg:
		print(msg)

	try:
		game_engine(player_labels=["Daryl", "Daryl"]) # player labels must be unique
	except ValueError as msg:
		print(msg)

	try:
		game_engine(player_labels=[]) # at least one player needed
	except ValueError as msg:
		print(msg)
	

	game = game_engine(5, 5, 4, player_labels=["Larry", "Moe", "Curly"])
	print(game.game_status())
	print(game.place_piece(-1, 0)) # play off board
	print(game.game_status())
	print(game.place_piece(3, 3))
	print(game.game_status())
	print(game.place_piece(3, 3)) # play on occupied space
	game.playout_random()
	print(game.place_piece(3, 3)) # play after game has ended
	
