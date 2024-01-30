import pygame as pg
import copy
from Button import *
from settings import *

class Dialogue:
	def __init__(self, game, header, text , onClick):
		self.game = game
		self.header = header
		self.text = text

		
		self.bg = scale_image(self.game.ui["dialogue_bg"], 500, 300)
		self.width, self.height = self.bg.get_size()
		self.x, self.y = WIDTH / 2 - self.width / 2, HEIGHT / 2 - self.height / 2

		# Header
		self.header = game.fonts["sys-24"].render(self.header, True, (255, 255, 255))
		self.header_width, self.header_height = self.header.get_size()
		self.bg.blit(self.header, (self.width / 2 - self.header_width / 2, 20))

		# Text
		blit_text(self.bg, self.text, (20, 30 + self.header_height), game.fonts["sys-20"], (255, 255, 255), self.width - 20, self.height - 20)

		self.button_bg = self.game.ui["dialogue_button"]
		self.button = Button(self.x + self.width - 120, self.y + self.height - 40, 100, 80, onClick, game.ui["dialogue_button"],"OK")

	def update(self, game):
		for event in pg.event.get():
				if event.type == pg.MOUSEBUTTONDOWN:	
					if (self.button.isCollide(pg.mouse.get_pos())):
						self.button.onClick()
						game.wave.dialogue = None

	def draw(self, game):
		game.interface.screen.blit(self.bg, (self.x, self.y))

		self.button.draw(game.interface.screen)