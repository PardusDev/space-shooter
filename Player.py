import pygame as pg
from Spaceship import *

class Player:
	def __init__(self, interface, game):
		self.interface = interface
		self.game = game
		self.max_health = 100
		self.health = 100
		self.spaceship = Sentinel(game)
		self.speed = 120


	def update(self, game):
		self.spaceship.move(self, game.dt_seconds)
		self.spaceship.fire(self, game)

		self.spaceship.update(game.dt_seconds)

	def player_lost_health(self, damage):
		if (self.health - damage <= 0):
			self.health = 0
			self.game.end_game()
		else:
			self.health -= damage

	def player_get_health(self, regen_amount):
		if (self.health + regen_amount >= self.max_health):
			self.health = self.max_health
		else:
			self.health += regen_amount

	def draw(self, screen):
		self.spaceship.draw(screen)