import pygame as pg

from Player import *
from settings import *

class Interface:
	def __init__(self):
		self.screen = pg.display.set_mode(RES)
		pg.display.set_caption("Space Shooter")

	def draw_health_bar(self, player):
		pg.draw.rect(self.screen, "red", (10, 10, 200, 20))
		pg.draw.rect(self.screen, "green", (10, 10, player.health * 2, 20))

	def update(self, game):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				game.running = False
			elif event.type == pg.KEYDOWN:
				game.running = True


	def draw(self, player):
		self.draw_health_bar(player)

	
		
