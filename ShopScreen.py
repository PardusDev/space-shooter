import pygame as pg
from Button import *
from settings import *

class ShopScreen:
	def __init__(self, game, previous_screen):
		self.game = game
		self.background = pg.image.load(SETTINGS_MENU_BACKGROUND)
		self.previous_screen = previous_screen
		self.buttons = []
		self.font = pg.font.Font("assets/fonts/icons.ttf", 18)
		self.buttons.append(Button(30, 30, 64, 64, self.back, BACK_BUTTON, "", 0, self.font))

	def update(self):
		for event in pg.event.get():
			if event.type == pg.MOUSEBUTTONDOWN:	
				for button in self.buttons:
					if button.isCollide(pg.mouse.get_pos()):
						button.onClick()
	
	def draw(self, screen):
		screen.blit(self.background, (0, 0))

		for button in self.buttons:
			button.draw(screen)

	def back(self):
		self.game.mainmenu.currentScreen = self.previous_screen