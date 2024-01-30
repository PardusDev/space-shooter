import random

from BackgroundAsset import *
from settings import *

class Background:
	def __init__(self, game):
		self.background_assets = []
		self.game = game
		for i in range(WIDTH // 2):
			self.background_assets.append(BackgroundAsset(random.randint(0, WIDTH), random.randint(0, HEIGHT), self.game.space_assets["white_dot"], random.uniform(0, 0.02), random.randint(50, 175)))

		for i in range(WIDTH // 8):
				self.background_assets.append(BackgroundAsset(random.randint(0, WIDTH), random.randint(0, HEIGHT), self.game.space_assets["white_dot"], random.uniform(0, 0.04), random.randint(50, 125)))
				
				if (i % 2 == 0):
					self.background_assets.append(BackgroundAsset(random.randint(0, WIDTH), random.randint(0, HEIGHT), self.game.space_assets["star"], random.uniform(0, 0.03), random.randint(50, 125)))
					

	def update(self):
		for asset in self.background_assets:
			asset.update(self.game.dt_seconds)

	def draw(self):
		for asset in self.background_assets:
			asset.draw(self.game.interface.screen)