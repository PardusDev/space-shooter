import pygame as pg
from ShopScreen import *
from SettingsScreen import *
from Button import *
from settings import *

class MainMenuScreen:
	def __init__(self, game):
		self.background = game.ui["main-bg"]
		self.game = game
		self.buttons = []
							#     x: WIDTH / 2 - BUTTON_WIDTH / 2
		self.buttons.append(Button(280, 120, 240, 120, game.play, game.ui["start_button"]))

		self.buttons.append(Button(270, 250, 260, 140, self.shop, game.ui["other_main_menu_button"], "Shop", 22))

		self.buttons.append(Button(270, 300, 260, 140, self.settings, game.ui["other_main_menu_button"], "Settings", 22))

		self.buttons.append(Button(270, 350, 260, 140, game.quit, game.ui["other_main_menu_button"], "Quit Game", 22))

		self.currentScreen = None

	def update(self):
		if self.currentScreen is None:
			for event in pg.event.get():
				if event.type == pg.MOUSEBUTTONDOWN:	
					for button in self.buttons:
						if button.isCollide(pg.mouse.get_pos()):
							button.onClick()
		else:
			self.currentScreen.update()
			
	def draw(self, screen):

		if self.currentScreen is None:
			screen.blit(self.background, (0, 0))

			for button in self.buttons:
				button.draw(screen)
		else:
			self.currentScreen.draw(screen)

	def settings(self):
		self.currentScreen = SettingsScreen(self.game, None)

	def shop(self):
		self.currentScreen = ShopScreen(self.game, None)