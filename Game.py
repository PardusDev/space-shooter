import pygame as pg
from Interface import *
from Player import *

class Game:
	def __init__(self):
		self.player = Player()
		self.interface = Interface()
		self.clock = pg.time.Clock()
		self.running = True

	def run(self):
		while self.running:
			self.dt = game.clock.tick(60)
			self.dt_seconds = self.dt / 1000.0
			
			self.interface.draw(self.player)
			self.interface.update(self)

			self.player.update(self)
			self.player.draw(self.interface.screen)

			pg.display.update()

game = Game()
game.run()