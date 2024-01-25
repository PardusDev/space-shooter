import pygame as pg
from Button import *
from settings import *

class MainMenu:
	def __init__(self):
		self.buttons = []

		self.buttons.append(Button("Play", (WIDTH / 2) - 100, (HEIGHT / 2) - 50, 200, 50, (0, 0, 0), (255, 255, 255), 30))