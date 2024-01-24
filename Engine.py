import pygame as pg
from settings import *


class Engine:
	def __init__(self, ship, x, y, engine_path):
		self.x = x
		self.y = y
		self.asset = pg.image.load(engine_path)
		self.frames = [pg.image.load(engine_path)]
		self.index = 0

	def draw(self, screen):
		pg.draw.rect(screen, (255, 255, 255), (self.x, self.y, 8, 15))
