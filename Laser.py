import pygame as pg
from settings import *

class Laser:
	def __init__(self, x, y, damage):
		self.width = 3
		self.height = 10
		self.x = x - (self.width / 2)
		self.y = y - (self.height / 2)
		self.damage = damage

	def move(self):
		self.y -= 5

	def draw(self, screen):
		pg.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
		

