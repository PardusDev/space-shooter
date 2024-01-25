import pygame as pg
from Button import *
from settings import *

class MainMenu:
	def __init__(self, game):
		self.background = pg.image.load(MAIN_MENU_BACKGROUND)
		self.buttons = []
							#     x: WIDTH / 2 - BUTTON_WIDTH / 2
		self.buttons.append(Button(280, 120, 240, 120, game.play, START_BUTTON_BACKGROUND))

		self.buttons.append(Button(280, 280, 240, 120, game.play, START_BUTTON_BACKGROUND, "Settings"))

	def update(self):
		for button in self.buttons:
			button.update()
			
	def draw(self, screen):
		screen.blit(self.background, (0, 0))

		for button in self.buttons:
			button.draw(screen)