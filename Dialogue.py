import pygame as pg
from settings import *

class Dialogue:
	def __init__(self, game, header, text):
		self.game = game
		self.header = header
		self.text = text

		self.width, self.height = self.game.ui["dialogue_bg"].get_size()
		self.bg = self.game.ui["dialogue_bg"]

		self.font = pg.font.SysFont(None, 24)
		self.header = self.font.render(self.text, True, (255, 255, 255))
		self.bg.blit(self.header, (100, 100))

	def update(self, game):
		pass

	def draw(self, game):
		# Button.. etc.
		game.interface.screen.blit(self.bg, (WIDTH / 2 - self.width / 2, HEIGHT / 2 - self.height / 2))