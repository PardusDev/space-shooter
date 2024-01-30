from Enemy import *
from settings import *
from utilities import *

class Wave:
	def __init__(self, game):
		self.wave = 0
		self.game = game
		self.start = False

	def create_enemy(self):
		if (self.wave == 1):
			for i in range (5):
				x, y = get_random_pos_for_enemies()
				self.game.enemies.append(Marauder(x, y, 0, 0, 500))
		elif (self.wave == 2):
			for i in range (7):
				x, y = get_random_pos_for_enemies()
				self.game.enemies.append(Marauder(x, y, 0, 0, 500))

	def next_wave_start(self):
		self.wave += 1
		self.start = True
		self.create_enemy(self.game)

	def current_wave_end(self):
		# If there is a dialog menu or a merchant, write the code here.
		self.start = False
	
