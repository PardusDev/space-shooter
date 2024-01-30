import pygame as pg

from Wave import *
from MainMenuScreen import *
from Enemy import *
from Interface import *
from Player import *

class Game:
	def __init__(self):
		pg.init()
		# It is created in the button class
		# self.iconFont = pg.font.Font("assets/fonts/icons.ttf", 18)
		self.sound_effects = {
			"enemy_laser": pg.mixer.Sound("assets/sounds/basic_laser/enemy_laser_effect.ogg"),
			"ally_laser": pg.mixer.Sound("assets/sounds/basic_laser/ally_laser_effect.ogg"),
		}

		self.ui = {
			
			"dialogue_bg": scale_image(pg.image.load(DIALOG_SPLASH), 500, 300),
			"dialogue_button": scale_image(pg.image.load(DIALOG_SPLASH_BUTTON), 100, 80)
		}
		self.mainmenu = MainMenuScreen(self)

		# Because it has an interface screen, we are creating it from the beginning. Even if it's in the main menu, the interface will have been formed in the background.
		self.interface = Interface()
		self.clock = pg.time.Clock()
		self.running = True

		self.enemies = []

	def run(self):
		while self.running:
			if self.mainmenu is not None:
				self.mainmenu.draw(self.interface.screen)
				self.mainmenu.update()

			self.dt = game.clock.tick(60)
			self.dt_seconds = self.dt / 1000.0
				
			'''
			self.dt = game.clock.tick(60)
			self.dt_seconds = self.dt / 1000.0

			self.interface.draw(self.player)
			self.interface.update(self)

			self.player.update(self)
			self.player.draw(self.interface.screen)

			for enemy in self.enemies:
				enemy.update(self)
				enemy.draw(self.interface.screen)

				for laser in self.player.spaceship.lasers:
					if laser.collide(enemy):
						# Damage enemy
						enemy.health -= laser.damage
						
						# Remove enemy if health is 0
						if (enemy.health <= 0):
							self.enemies.remove(enemy)
						
						# Remove laser
						self.player.spaceship.lasers.remove(laser)
			'''
			pg.display.update()


	def play(self):
		print("Clicked play")
		self.mainmenu = None
		self.player = Player(self.interface)
		self.wave = Wave(self)
		
		

		# Like wave-based enemies
		
		# Countdown code
		
		# Start wave
		self.wave.next_wave_start()

		while self.running:
			# Attention! For debug
			print(len(self.enemies))

			self.dt = game.clock.tick(60)
			self.dt_seconds = self.dt / 1000.0
			self.interface.screen.fill((11, 11, 11))

			# For dialogue or merchant window
			self.wave.draw()
			self.wave.update()
			
			self.player.draw(self.interface.screen)
			self.player.update(self)
			

			for enemy in self.enemies:
				enemy.draw(self.interface.screen)
				enemy.update(self)
				
				# Enemy's laser to player collision
				for laser in enemy.lasers:
					if laser.collide(self.player.spaceship):
						# Damage player
						self.player.player_lost_health(laser.damage)
						
						# Remove laser
						enemy.lasers.remove(laser)

				# Player's laser to enemy collision
				for laser in self.player.spaceship.lasers:
					if laser.collide(enemy):
						# Damage enemy
						enemy.health -= laser.damage
						
						# Remove enemy if health is 0
						if (enemy.health <= 0):
							self.enemies.remove(enemy)

							if (len(self.enemies) <= 0):
								self.wave.current_wave_end()
						
						# Remove laser
						self.player.spaceship.lasers.remove(laser)

			self.interface.draw(self.player)
			self.interface.update(self)
			pg.display.update()


	def quit(self):
		print("Clicked quit")
		self.running = False

			

game = Game()
game.run()