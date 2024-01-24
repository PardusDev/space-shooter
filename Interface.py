import pygame as pg

from Player import *
from settings import *

class Interface:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode(RES)
		pg.display.set_caption("Space Shooter")

	def update(self, game):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				game.running = False
			elif event.type == pg.KEYDOWN:
				game.running = True
				# The word guess logic is here...

	def draw(self, player):
		self.screen.fill("black")
