import pygame as pg

from Enemy import *
from Interface import *
from Player import *

class Game:
	def __init__(self):
		self.player = Player()
		self.interface = Interface()
		self.clock = pg.time.Clock()
		self.running = True

		self.enemies = []
		for i in range(10):
			self.enemies.append(Marauder(random.randrange(10, WIDTH - 100), random.randrange(-1000, -10), 0, 0, 500))

	def run(self):
		while self.running:
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

			pg.display.update()

game = Game()
game.run()