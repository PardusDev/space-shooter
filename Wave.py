from Dialogue import *
from Enemy import *
from settings import *
from utilities import *
from time import sleep

class Wave:
	def __init__(self, game):
		self.wave = 0
		self.game = game
		self.start = False

	def create_enemy(self):
		self.game.sound_effects["radio_noise"].play()
		if (self.wave == 1):

			# Wave enemies =>
			def spawn_enemies():
				for i in range (5):
					x, y = get_random_pos_for_enemies()
					self.game.enemies.append(Marauder(x, y, 0, 0, 500, self.game))
				self.game.wave.dialogue = None

			self.dialogue = Dialogue(self.game, "Wave 1: Threat", "Our radars have detected unidentified spacecraft with unknown origin locations. We do not know whether they are friend or foe. Regardless of what they are, it's imperative that we ensure our own safety. According to the information from the radars, there are 5 unidentified ships. We believe they will enter our field of view shortly.", spawn_enemies )
			# When dialogue screen closed, spawn enemies.
			
		elif (self.wave == 2):

			def spawn_enemies():
				for i in range (7):
					x, y = get_random_pos_for_enemies()
					self.game.enemies.append(Marauder(x, y, 0, 0, 500, self.game))
				self.game.wave.dialogue = None

			self.dialogue = Dialogue(self.game, "Wave 2: More of Them", "It seems these ships are hostile! Their launch locations have been detected by our radars. There are 7 more ships coming from this location! Let's defeat them as well.", spawn_enemies )

		elif (self.wave == 3):
			def another_dialog():
				def spawn_enemies():
					for i in range (10):
						x, y = get_random_pos_for_enemies()
						self.game.enemies.append(Marauder(x, y, 0, 0, 500, self.game))
					self.game.wave.dialogue = None
				
				sleep(0.1)
				self.dialogue = Dialogue(self.game, "Test", "This is a test text. This is a ANOTHER text.", spawn_enemies)

			self.dialogue = Dialogue(self.game, "Test", "This is a test text. The third wave won't start when this window closes.", another_dialog )

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
	
