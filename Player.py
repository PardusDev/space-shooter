import pygame as pg
from Spaceship import *

class Player:
	def __init__(self, interface, game):
		self.interface = interface
		self.max_health = 100
		self.health = 100
		self.spaceship = Sentinel(game)
		self.speed = 120

		self.interface.update_manual(self)


	def update(self, game):
		self.spaceship.move(self, game.dt_seconds)
		self.spaceship.fire(self, game)

		self.spaceship.update(game.dt_seconds)

	def player_lost_health(self, damage):
		if (self.health - damage <= 0):
			self.health = 0
			self.interface.update_manual(self)
			#self.interface.game_over()
		else:
			self.health -= damage
			self.interface.update_manual(self)

	def player_get_health(self, regen_amount):
		if (self.health + regen_amount >= self.max_health):
			self.health = self.max_health
			self.interface.update_manual(self)
		else:
			self.health += regen_amount
			self.interface.update_manual(self)

	def draw(self, screen):
		self.spaceship.draw(screen)