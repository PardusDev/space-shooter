import pygame as pg
import copy
from Button import *
from settings import *

class Dialogue:
	def __init__(self, game, header, text , onClick):
		self.game = game
		self.header_text = header
		self.text = text

		
		self.bg, self.ratio = scale_image_and_get_ratio(self.game.ui["dialogue_bg"], 500, 300)
		self.width, self.height = self.bg.get_size()
		self.x, self.y = WIDTH / 2 - self.width / 2, HEIGHT / 2 - self.height / 2

		# Header
		self.header = scale_and_rot_image(game.ui["dialogue_header"], self.ratio, 0)
		self.header_width, self.header_height = self.header.get_size()
		self.bg.blit(self.header, (self.width / 2 - self.header_width / 2, -(self.header_height/2)))
		
		self.header_text = game.fonts["sys-24"].render(self.header_text, True, (255, 255, 255))
		self.header_text_width, self.header_text_height = self.header_text.get_size()
		self.bg.blit(self.header_text, (self.width / 2 - self.header_text_width / 2, 15  * self.ratio))

		# Text
		blit_text(self.bg, self.text, (20, 30 + self.header_text_height), game.fonts["sys-20"], (255, 255, 255), self.width - 20, self.height - 20)

		self.button_bg = self.game.ui["dialogue_button"]
		self.button = Button(self.x + self.width - 120, self.y + self.height - 40, 100, 80, onClick, game.ui["dialogue_button"],"OK")

	def update(self, game):
		for event in pg.event.get():
				if event.type == pg.MOUSEBUTTONDOWN:	
					if (self.button.isCollide(pg.mouse.get_pos())):
						self.button.onClick()

	def draw(self, game):
		game.interface.screen.blit(self.bg, (self.x, self.y))

		self.button.draw(game.interface.screen)