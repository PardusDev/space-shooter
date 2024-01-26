import pygame as pg
from Spaceship import *

class Player:
	def __init__(self, interface):
		self.interface = interface
		self.max_health = 100
		self.health = 100
		self.spaceship = Sentinel()
		self.speed = 120

		self.interface.update_manual(self)


	def update(self, game):
		self.spaceship.move(self, game.dt_seconds)
		self.spaceship.fire(self)

		self.spaceship.update(game.dt_seconds)

	def player_lost_health(self, damage):
		self.health -= damage
		self.interface.update_manual(self)

	def draw(self, screen):
		self.spaceship.draw(screen)