import pygame as pg
from utilities import *
from settings import *

class Enemy:
	def __init__(self, x, y, speed, damage, health, image):
		self.x = x
		self.y = y
		self.speed = speed
		self.damage = damage
		self.health = health
		self.image = scale_image(image, 100, 80)
		self.width, self.height = self.image.get_size()
	
	def move(self, game):
		self.y += self.speed * game.dt_seconds

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))

class Marauder(Enemy):
	def __init__(self, x, y , speed, damage, health):
		asset = pg.image.load("assets/enemy_ships/marauder.png")

		super().__init__(x, y , speed, damage, health, asset)
		
	def move(self, game):
		super().move(game)

	def draw(self, screen):
		super().draw(screen)
