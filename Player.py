import pygame as pg
from Spaceship import *

class Player:
	def __init__(self):
		self.health = 100
		self.spaceship = Spaceship(0)
		self.speed = 120

	def update(self, game):
		dt = game.clock.tick(60)
		dt_seconds = dt / 1000.0
		
		keys = pg.key.get_pressed()
		self.spaceship.move(self, keys, dt_seconds)
		#if keys[pg.K_LEFT]:
		#	self.spaceship.x -= (self.speed * self.spaceship.speedMultiplier) * dt_seconds
		#if keys[pg.K_RIGHT]:
		#	self.spaceship.x += (self.speed * self.spaceship.speedMultiplier) * dt_seconds

	def draw(self, screen):
		self.spaceship.draw(screen)