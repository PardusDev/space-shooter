import pygame as pg
from Spaceship import *

class Player:
	def __init__(self):
		self.health = 100
		self.spaceship = Spaceship(0)
		self.speed = 120

	def update(self, game):
		self.spaceship.move(self, game.dt_seconds)
		self.spaceship.fire(self)

		self.spaceship.update()

		

	def draw(self, screen):
		self.spaceship.draw(screen)