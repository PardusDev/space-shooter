import pygame as pg
from utilities import *
from settings import *

class Button:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.image = scale_image(pg.image.load(BUTTON_BACKGROUND), width, height)
		self.width, self.height = self.image.get_size()
		
	def check_pressed(self):
		for event in pg.event.get():
			if event.type == pg.MOUSEBUTTONDOWN:
				return pg.Rect(self.x, self.y, self.width, self.height).collidepoint(pg.mouse.get_pos())
					

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))
		