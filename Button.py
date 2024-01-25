import pygame as pg
from utilities import *
from settings import *

class Button:
	def __init__(self, x, y, width, height, onClick, asset, text = None, font_size = 24):
		self.x = x
		self.y = y
		self.image = scale_image(pg.image.load(asset), width, height)
		self.width, self.height = self.image.get_size()
		self.onClick = onClick
		
		self.text = text

		if self.text != None:	
			self.font_size = font_size
			self.font = pg.font.SysFont(None, self.font_size)
			self.img = self.font.render(self.text, True, (255, 255, 255))
			self.text_width, self.text_height = self.img.get_size()
			

		
	def update(self):
		for event in pg.event.get():
			if event.type == pg.MOUSEBUTTONDOWN:		
				if pg.Rect(self.x, self.y, self.width, self.height).collidepoint(pg.mouse.get_pos()):
					self.onClick()
					

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))

		if self.text != None:
			screen.blit(self.img, (self.x + self.width / 2 - self.img.get_width() / 2, self.y + self.height / 2 - self.img.get_height() / 2))
		