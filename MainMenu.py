import pygame as pg
from Button import *
from settings import *

class MainMenu:
	def __init__(self):
		self.background = pg.image.load(MAIN_MENU_BACKGROUND)
		self.buttons = []
							#     x: WIDTH / 2 - BUTTON_WIDTH / 2
		self.buttons.append(Button(280, 120, 240, 120))

	def update(self):
		for button in self.buttons:
			if button.check_pressed():
				print("Button pressed")
			
	def draw(self, screen):
		screen.blit(self.background, (0, 0))

		for button in self.buttons:
			button.draw(screen)