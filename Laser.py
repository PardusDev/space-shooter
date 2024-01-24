import pygame as pg
from settings import *

class Laser:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move(self):
		self.y -= 5

	def draw(self, screen):
		pg.draw.rect(screen, (255, 0, 0), (self.x, self.y, 5, 10))
		

