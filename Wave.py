from Dialogue import *
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

			# Wave enemies =>
			def spawn_enemies():
				for i in range (5):
					x, y = get_random_pos_for_enemies()
					self.game.enemies.append(Marauder(x, y, 0, 0, 500))

			self.dialogue = Dialogue(self.game, "Test", "This is just a test text. The first wave will begin once this window closes.", spawn_enemies )
			# When dialogue screen closed, spawn enemies.
			
		elif (self.wave == 2):

			def spawn_enemies():
				for i in range (7):
					x, y = get_random_pos_for_enemies()
					self.game.enemies.append(Marauder(x, y, 0, 0, 500))

			self.dialogue = Dialogue(self.game, "Test", "This is a test text. The second wave will start when this window closes.", spawn_enemies )

	def next_wave_start(self):
		self.wave += 1
		self.start = True
		self.create_enemy()

	def current_wave_end(self):
		# If there is a dialog menu or a merchant, write the code here.
		self.start = False

		# Next wave start
		self.next_wave_start()

	def update(self):
		if (self.dialogue is not None):
			self.dialogue.update(self.game)

	def draw(self):
		if (self.dialogue is not None):
			self.dialogue.draw(self.game)
	
