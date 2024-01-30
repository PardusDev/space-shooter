from Enemy import *
from settings import *
from utilities import *

class Wave:
	def __init__(self, game):
		self.wave = 0
		self.start = False

	def create_enemy(self, game):
		if (self.wave == 1):
			for i in range (5):
				x, y = get_random_pos_for_enemies()
				game.enemies.append(Marauder(x, y, 0, 0, 500))

	def next_wave_start(self, game):
		self.wave += 1
		self.start = True
		self.create_enemy(game)