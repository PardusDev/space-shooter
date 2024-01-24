import pygame as pg
from Spaceship import *

class Player:
	def __init__(self):
		self.health = 100
		self.spaceship = Spaceship(1)
		self.speed = 120

	def update(self, game):
		self.spaceship.move(self, game.dt_seconds)
		self.spaceship.fire(self)

		self.spaceship.update()

		for laser in self.spaceship.lasers:
			if (laser.y < 0):
				self.spaceship.lasers.remove(laser)
			else:
				laser.move()

	def draw(self, screen):
		self.spaceship.draw(screen)