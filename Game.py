import pygame as pg

from MainMenuScreen import *
from Enemy import *
from Interface import *
from Player import *

class Game:
	def __init__(self):
		pg.init()
		self.mainmenu = MainMenuScreen(self)

		# Because it has an interface screen, we are creating it from the beginning. Even if it's in the main menu, the interface will have been formed in the background.
		self.interface = Interface()
		self.clock = pg.time.Clock()
		self.running = True

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
		
		

		# Like wave-based enemies
		self.enemies = []
		for i in range(10):
			self.enemies.append(Marauder(random.randrange(10, WIDTH - 100), random.randrange(-1000, -10), 0, 0, 500))

		while self.running:
			self.dt = game.clock.tick(60)
			self.dt_seconds = self.dt / 1000.0
			self.interface.screen.fill((11, 11, 11))

			
			
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