import pygame as pg
from settings import *

class Laser:
	def __init__(self, x, y, damage):
		self.width = 3
		self.height = 10
		self.x = x - (self.width / 2)
		self.y = y - (self.height / 2)
		self.damage = damage

	def collide(self, enemy):
		return pg.Rect(self.x, self.y, self.width, self.height).colliderect(pg.Rect(enemy.x, enemy.y, enemy.width, enemy.height))

	def move(self):
		self.y -= 5

	def update(self):
		self.move()

	def draw(self, screen):
		pg.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
		

