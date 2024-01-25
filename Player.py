import pygame as pg
from Spaceship import *

class Player:
	def __init__(self):
		self.max_health = 100
		self.health = 90
		self.spaceship = Sentinel()
		self.speed = 120

	def update(self, game):
		self.spaceship.move(self, game.dt_seconds)
		self.spaceship.fire(self)

		self.spaceship.update()

		

	def draw(self, screen):
		self.spaceship.draw(screen)