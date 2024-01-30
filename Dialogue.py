import pygame as pg
import copy
from Button import *
from settings import *

class Dialogue:
	def __init__(self, game, header, text , onClick):
		self.game = game
		self.header = header
		self.text = text

		self.width, self.height = self.game.ui["dialogue_bg"].get_size()
		self.bg = self.game.ui["dialogue_bg"].copy()

		self.font = pg.font.SysFont(None, 24)
		self.header = self.font.render(self.text, True, (255, 255, 255))
		self.bg.blit(self.header, (100, 100))

		self.button_bg = self.game.ui["dialogue_button"]
		self.button = Button(100, 100, 100, 80, onClick, DIALOG_SPLASH_BUTTON,"OK")

	def update(self, game):
		# It's not work
		# self.button.update()
		for event in pg.event.get():
				if event.type == pg.MOUSEBUTTONDOWN:	
					if (self.button.isCollide(pg.mouse.get_pos())):
						self.button.onClick()
						game.wave.dialogue = None

	def draw(self, game):
		# Button.. etc.
		game.interface.screen.blit(self.bg, (WIDTH / 2 - self.width / 2, HEIGHT / 2 - self.height / 2))

		self.button.draw(game.interface.screen)