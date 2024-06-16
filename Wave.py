import pygame as pg
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

		self.MarauderQue = 0

		self.last_spawn_time = 0
		self.spawnInterval = 0.5

	def create_enemy(self):
		self.game.sound_effects["radio_noise"].play()
		if (self.wave == 1):
			# Wave enemies =>
			def spawn_enemies():
				self.MarauderQue = 5
				self.game.wave.dialogue = None

			self.dialogue = Dialogue(self.game, "Wave 1: Threat", "Our radars have detected unidentified spacecraft with unknown origin locations. We do not know whether they are friend or foe. Regardless of what they are, it's imperative that we ensure our own safety. According to the information from the radars, there are 5 unidentified ships. We believe they will enter our field of view shortly.", spawn_enemies )
			# When dialogue screen closed, spawn enemies.
			
		elif (self.wave == 2):

			def spawn_enemies():
				self.MarauderQue = 7
				self.game.wave.dialogue = None

			self.dialogue = Dialogue(self.game, "Wave 2: More of Them", "It seems these ships are hostile! Their launch locations have been detected by our radars. There are 7 more ships coming from this location! Let's defeat them as well.", spawn_enemies )

		elif (self.wave == 3):
			def another_dialog():
				def spawn_enemies():
					self.MarauderQue = 10
					self.game.wave.dialogue = None
					
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

	def spawnMarauder(self):
		x, y = get_random_pos_for_enemies()
		self.game.enemies.append(Marauder(self.game, x, y, 0, 0, 500))

	def update(self):
		current_time = pg.time.get_ticks() / 1000.0
		if (current_time - self.last_spawn_time >= self.spawnInterval):
			
			if (self.MarauderQue > 0):
				self.spawnMarauder()
				self.MarauderQue -= 1
			
			self.last_spawn_time = current_time

		if (self.dialogue is not None):
			self.dialogue.update(self.game)

	def draw(self):
		if (self.dialogue is not None):
			self.dialogue.draw(self.game)
	
